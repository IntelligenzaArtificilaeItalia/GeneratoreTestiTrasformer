# Importing the pipeline function from the transformers library
from transformers import pipeline

input=st.text_input("Inserisci titolo articolo")

# Creating a TextGenerationPipeline for text generation
generator = pipeline(task=input, model='gpt2')

if st.button("Genera Articoli"):
  # Generating
  out = generator("It takes time to write a good blog post.", max_length=60, num_return_sequences=5)
  st.write(out)
 
