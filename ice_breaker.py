from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

if __name__ == "__main__":
    print("hello LangChain!")
    print(os.environ["OPENAI_API_KEY"])
