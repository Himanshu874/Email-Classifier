# Email Classification System

A Python-based application that uses the **OpenAI Chat Completions API** to classify email text into primary categories (`spam`, `promotional`, `important`) and further sub-classify **important** emails into secondary categories (`business`, `personal`).

## How It Works

The system employs a two-step hierarchical classification process using the `gpt-4-turbo` model:

1.  **Primary Classification**: The email is first classified as `spam`, `promotional`, or `important`.
2.  **Secondary Classification**: If the email is classified as `important`, a second API call further classifies it as `business` or `personal`.
3.  **Output**: The function returns the final class, or `important-{subcategory}` for sub-classified emails (e.g., `important-business`).

## Tech Stack & Dependencies

- **Python**: Core programming language.
- **OpenAI SDK (`openai`)**: For communication with the OpenAI API.
- **`python-dotenv`**: For loading the API key from the `.env` file.

## Installation

1.  **Clone or Download** the project files.
2.  **Install dependencies** using the provided `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

The application requires your OpenAI API key for authentication.

1.  **Get your API Key** from OpenAI.
2.  **Edit the `.env` file** in the project root to store your key:

    **.env file content**

    ```
    OPENAI_API_KEY="sk-proj-YOUR_ACTUAL_API_KEY_HERE"
    ```

    _Note: The `.gitignore` file is set up to ignore the `.env` file for security._

## Usage

Run the main script to start the interactive classifier:

```bash
python email_classifier.py
```
