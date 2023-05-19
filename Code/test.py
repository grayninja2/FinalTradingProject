from transformers import pipeline
import numpy

text = "I love it and hate it"
sentiment_pipeline = pipeline(model="zhayunduo/roberta-base-stocktwits-finetuned")
analysis = sentiment_pipeline(text)
print(analysis)
        