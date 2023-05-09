from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import openai
from decouple import config

openai.api_key = config('KEY')
app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_engine = "gpt-3.5-turbo"

@app.post("/generate")
async def generate_text(prompt: str):
    completions = openai.ChatCompletion.create(
      model= model_engine,
      temperature=.2,
      top_p=0.3,
      messages=[
        {"role": "user", "content": prompt}
      ]
    )
    # Print the generated text
    message = completions.choices[0]['message']['content']
    return (message)
