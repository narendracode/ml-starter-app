from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/msmarco-MiniLM-L-12-v3')

if __name__ == "__main__":
    print("hello world")

    sentences = ["This is an example sentence", "Each sentence is converted"]
    sentence = "What is the weather in Jamaica?"
    #print(sentences)
    
    embeddings = model.encode(sentence)
    print(embeddings)
