
# Text-to-Code: Simplify Software Development with Natural Language

Welcome to Text-to-Code, a transformative tool designed to empower developers by enabling the conversion of natural language descriptions into executable code. This Django-based application leverages the power of Large Language Models (LLMs) to interpret user intents and translate them into various programming languages such as Python, Java, and JavaScript.

## Live Demo
Text2Code is live at [Text2Code](https://owaismultani.pythonanywhere.com)

## Getting Started

### Prerequisites

- Python 3.11
- Django 5.x
- OpenAI API (version compatible with your OpenAI account)

### Installation

1. Clone the repository:
   ```bash
   git clone https://yourrepositoryurl.com/text2code.git
   ```
2. Install Poetry if you haven't already:
   ```bash
   pip install poetry
   ```
3. Navigate to the project directory:
   ```bash
   cd Text2Code
   ```
4. Install dependencies using Poetry:
   ```bash
   poetry install
   ```
5. Migrate the database:
   ```bash
   poetry run python manage.py migrate
   ```
6. Export the OpenAI API key:
   ```bash
    export OPENAI_API_KEY="your_openai_api_key"
    ```
7. Start the development server:
   ```bash
   poetry run python manage.py runserver
   ```

Now access the application at `http://localhost:8000`.

### Usage

Use the application by navigating to the respective endpoints:

- **Home Page**: `http://localhost:8000/`
- **Admin Dashboard**: `http://localhost:8000/admin/`
- **Accounts Login**: `http://localhost:8000/accounts/login/`

For a full list of available routes, please refer to the URL configurations in the `core/urls.py` and `accounts/urls.py` files.

## Features

- **Rapid Prototyping**: Automatically generates code snippets from natural language.
- **Educational Tools**: Assists in teaching programming by converting descriptions into code.
- **Accessibility**: Enhances software development accessibility for people with disabilities.
- **Documentation to Code**: Converts written documentation into runnable code.

## Business Value

- **Reduced Development Time**: Focus more on innovation less on routine coding.
- **Cost Efficiency**: Lowers the financial barriers to software development.
- **Enhanced Collaboration**: Facilitates contributions from non-technical team members.

## Challenges

- Accurate interpretation of natural language to code.
- Handling different programming syntaxes and optimizations.
- Ensuring generated code is error-free and optimized for performance.

## File Structure

Briefly describing the purpose of main directories and files:

- **`accounts/`**: Contains user management views and models.
- **`core/`**: Core functionality of the application, including primary views and models.
- **`static/`**: CSS and JavaScript files.
- **`templates/`**: HTML templates for the application.
- **`text2code/`**: Main project configuration including settings and URLs.

## Contributing

We welcome contributions of all forms. Please feel free to fork the repository, make changes, and submit pull requests. You can also open issues for bugs you've found or features you think would be beneficial.

## Authors

- Owais Multani - [OwaisMultani](https://github.com/OwaisMultani)
- Mohammed Swarim Khan - [Swarim](https://github.com/swarim)
- Saba - [saba](https://github.com/alisaba1451)
- Sana - [sana](ShaikhSanaAli)
- Jashandeep - [Jashandeep]()

## Acknowledgments

- Thanks to everyone who has contributed to making this project a reality!
