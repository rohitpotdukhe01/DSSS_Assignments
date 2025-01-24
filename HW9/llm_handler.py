import torch
from transformers import pipeline

pipe = pipeline(
    "text-generation", 
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", 
    torch_dtype=torch.bfloat16, 
    device_map="auto"
)

def generate_response(user_message: str) -> str:
    """Generate a response to the user's message."""
    messages = [
    {
        "role": "user",
        "content": "You are a friendly chatbot who always responds in a fun and informative way",
    },
    {"role": "user", "content": user_message},
]
    # Apply the chat template
    prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    # Generate the response
    outputs = pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
    # Extract and return the generated text
    generated_text = outputs[0]["generated_text"]

    #return response
    return generated_text