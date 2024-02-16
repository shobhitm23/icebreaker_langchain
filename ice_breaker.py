from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profile

load_dotenv()

if __name__ == "__main__":
    print("hello LangChain!")

    # template for the prompt supplied to the LLM model
    summary_template = """
    given the LinkedIn information {information} about a person, I want you to create:
    1. A short summary
    2. Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url="https://gist.github.com/shobhitm23/8ef5234ad1ec0363605a23b6fab98da0"
    )

    print(chain.run(information=linkedin_data))
