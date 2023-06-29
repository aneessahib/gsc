from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import os
import pathlib
script_dir = str(pathlib.Path(__file__).parent.resolve())

model = AutoModelForSequenceClassification.from_pretrained('cross-encoder/ms-marco-TinyBERT-L-2-v2',cache_dir=script_dir)
tokenizer = AutoTokenizer.from_pretrained('cross-encoder/ms-marco-TinyBERT-L-2-v2',cache_dir=script_dir)
model.eval()

def predict(data):
    compute = data
    features = tokenizer([compute],  padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        scores = str(model(**features).logits.tolist()[0][0])
        print (scores)
        return scores
