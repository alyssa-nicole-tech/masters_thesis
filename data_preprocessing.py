import pandas as pd

def load_data(path):
  df = pd.read_csv(path)
  return df

def clean_text(text):
  #TODO: add linguistic preprocess
  return text.lower().strup()
 
