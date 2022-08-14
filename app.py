# Importing the pipeline function from the transformers library
from transformers import pipeline
import streamlit as st

input=st.text_input("Inserisci titolo articolo")

# Creating a TextGenerationPipeline for text generation
generator = pipeline(task='text-generation', model='gpt2')

if st.button("Genera Articoli"):
  # Generating
  out = generator(input, max_length=60, num_return_sequences=5)
  st.write(out)
 
