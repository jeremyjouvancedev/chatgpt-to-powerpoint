import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.openai_functions import (
    create_openai_fn_chain,
    create_structured_output_chain,
)
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from chatgpt_to_powerpoint.jsonSchema import json_schema


class LangChainHandler:
    def __init__(self, model_type="ChatOpenAI", model_name="gpt-3.5-turbo", open_api_key=None):
        self.model_type = model_type
        self.model_name = model_name
        self.openai_api_key = os.getenv('OPENAI_API_KEY', open_api_key)

    def generate_chain(self, nb_of_slides=10):
        if self.model_type == "ChatOpenAI":
            chat_model = ChatOpenAI(model_name=self.model_name, openai_api_key=self.openai_api_key, verbose=True)
            prompt = ChatPromptTemplate.from_messages(
                [
                    ("system", "You are a world class Powerpoint generator. think like a senior CPG brand manager and market researcher. "),
                    (
                        "human",
                        f"Use your knowledge to create a {nb_of_slides} slide Powerpoint presentation for the topic: {{input}}",
                    ),
                    ("human", "Tip: Make sure to answer in the correct format"),
                ]
            )
            return create_structured_output_chain(
                json_schema, chat_model, prompt, verbose=True
            )
        else:
            print(f"Model Type {self.model_type} not implemented")
            return None
