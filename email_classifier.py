import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
# Initialize the client with your OpenAI API key (stored in .env or system env vars)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_email(email_text: str) -> str:
    """
    Classify an email into spam, promotional, or important (business/personal).
    Returns one of: 'spam', 'promotional', 'important-business', 'important-personal'
    """

    # Step 1: Ask the LLM to classify the email into spam, promotional, or important
    first_prompt = f"""
    You are an email classification model.
    Classify the following email text into one of these classes:
    - spam
    - promotional
    - important

    Only return the class name. No explanations.

    Email text:
    {email_text}
    """

    first_response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": first_prompt}],
        temperature=0
    )

    first_class = first_response.choices[0].message.content.strip().lower()

    # Step 2: If it's important, further classify it as business or personal
    if first_class == "important":
        second_prompt = f"""
        The email below is classified as important.
        Now further classify it into one of these categories:
        - business
        - personal

        Only return the class name. No explanations.

        Email text:
        {email_text}
        """

        second_response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": second_prompt}],
            temperature=0
        )

        second_class = second_response.choices[0].message.content.strip().lower()

        return f"important-{second_class}"

    # Otherwise, just return the first classification
    return first_class


if __name__ == "__main__":
    # Example usage


    email_text = input("Enter email text to classify:\n")

    result = classify_email(email_text)
    print("Email classified as:", result)

