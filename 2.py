from dotenv import load_dotenv
from colorama import Fore
import os

from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate


load_dotenv()

llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
prompt_template = PromptTemplate.from_template("What is a good name for a company that makes {product}?Only give name.")



def generate(product):
    """ generate text based on the input """
    prompt = prompt_template.format(product=product)
    print(prompt)
    # return llm.invoke(prompt)
    return 'good'

def start():
    instructions = (
        "Type your question and press ENTER. Type 'x' to go back to the MAIN menu.\n"
    )
    print(Fore.BLUE + "\n\x1B[3m" + instructions + "\x1B[0m" + Fore.RESET)

    print("MENU")
    print("====")
    print("[1]- Enter a Product")
    print("[2]- Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        ask()
    elif choice == "2":
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice")
        start()


def ask():
    while True:
        user_input = input("Q: ")
        # Exit
        if user_input == "x":
            start()
        else:
            response = generate(user_input)
            print(Fore.BLUE + f"A: " + response + Fore.RESET)
            print(Fore.WHITE + "\n-------------------------------------------------")


if __name__ == "__main__":
    start()