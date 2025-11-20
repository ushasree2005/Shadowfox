from flask import Flask, request, jsonify, render_template
from transformers import AutoModelForCausalLM, AutoTokenizer, TextGenerationPipeline
from threading import Thread
import argparse
import torch

MODEL_NAME = "gpt2"
model = None
tokenizer = None
pipeline = None

def load_model():
    global model, tokenizer, pipeline
    print("Loading model... Please wait.")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
    pipeline = TextGenerationPipeline(model=model, tokenizer=tokenizer)

    print("Model loaded successfully.")
    return pipeline


def generate_text(prompt, max_length=60):
    pipe = load_model()
    output = pipe(prompt, max_length=max_length, do_sample=True, temperature=0.7)
    return output[0]["generated_text"]


app = Flask(__name__)


# ---------------------------
# FRONTEND ROUTE
# ---------------------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------------------
# API ROUTE (Correct, only once)
# ---------------------------
@app.route("/generate", methods=["POST"])
def api_generate():
    data = request.json
    prompt = data.get("prompt", "")
    max_length = int(data.get("max_length", 80))

    text = generate_text(prompt, max_length)
    return jsonify({"generated_text": text})


def run_server():
    Thread(target=load_model, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--serve", action="store_true")
    parser.add_argument("--prompt", type=str)
    parser.add_argument("--max-length", type=int, default=80)
    args = parser.parse_args()

    if args.serve:
        run_server()
    elif args.prompt:
        text = generate_text(args.prompt, args.max_length)
        print("\nGenerated Text:\n", text)


if __name__ == "__main__":
    main()
