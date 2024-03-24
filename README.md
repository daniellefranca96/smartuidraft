# SmartUIDraft: AI-Powered Web UI Design

## Introduction

SmartUIDraft is an innovative web application that leverages the power of artificial intelligence (AI) to streamline the web UI design process. Users can describe their desired user interface in natural language, and SmartUIDraft will automatically generate the corresponding HTML, CSS, and JavaScript code. This tool empowers designers and developers of all skill levels to create professional-looking UIs with ease and efficiency.

## Key Features

- **AI-Driven Code Generation:** SmartUIDraft utilizes advanced AI models to understand user descriptions and translate them into functional UI code.
- **Natural Language Input:** Users can interact with the application using plain English, eliminating the need for technical expertise.
- **Interactive Design Process:** The application provides an interactive environment where users can refine their UI designs through iterative feedback.
- **Code Download:** Generated code can be easily downloaded for further customization and integration into existing projects.
- **Template Support:** Users can upload HTML/CSS/JavaScript files or text instructions as base templates to guide the AI's code generation.
- **Undo Functionality:** The application allows users to undo previous actions, providing flexibility and control over the design process.

## Demo (first version only, not updated with newest features)
https://github.com/daniellefranca96/smartuidraft/assets/134293046/e44402c4-d29b-423c-8681-a042f6bac58d

## Structure

- `app.py`: Main application entry point.
- `generator.py`: Contains the logic for converting user input into HTML.
- `prompt.py`: Contains prompts used for the LLM models.
- `static/`: Houses static assets like stylesheets, scripts, and images.
- `templates/`: Contains the HTML templates used to render the application's web pages.

## Installation and Setup

```bash
git clone [https://github.com/your-username/SmartUIDraft.git](https://github.com/your-username/SmartUIDraft.git)
pip install -r requirements.txt
# Configure environment variables in a .env file 
python app.py
```

> [!NOTE]
> There is an image docker avaliable as an alternate way to run it.

## Environment Variables

The following environment variables can be used to configure SmartUIDraft. You'll need to set these up in a `.env` file in your project's root directory.

- **LLM_PROVIDER:** (Required) Specifies the AI model provider to use. Options:
    * `openai`: Uses OpenAI models.
    * `anthropic`: Uses Anthropic models.
    * `google`: Uses Google AI models.
    * `hugginfaces`: Uses Hugging Face models (supports Hugging Face Inference API only).
    * `bedrock`: Uses Bedrock models.

- **OPENAI_API_KEY:**  Your OpenAI API key.

- **GOOGLE_API_KEY:**  Your Google API key.

- **ANTHROPIC_API_KEY:**  Your Anthropic API key.

- **HUGGINGFACEHUB_API_TOKEN:** Your Hugging Face API token.

- **AWS_KEY:** Your AWS access key.

- **AWS_SECRET:** Your AWS secret key.

- **ANTHROPIC_MODEL:** The model to use for anthropic, default is set to Claude 3 Haiku.

- **OPENAI_MODEL:** The model to use for OpenAI, default is set to GPT 3.5 Turbo.

- **GOOGLE_MODEL:** The model to use for Google, default is set to Gemini Pro 1.0.

- **BEDROCK_MODEL:** The model to use for Bedrock, default is set to Claude 3 Haiku.

- **HUGGINGFACEHUB_MODEL_MODEL:** The model to use for HugginFaces, default is set to Mistral 8x7b.

> [!NOTE]
> Currently, Cohere models are not supported on bedrock integration.

## Usage

1. **Access SmartUIDraft:** Open the application in your web browser at http://localhost:5000/.

2. **(Optional) Provide a Template:**
   * Upload an existing HTML/CSS/JavaScript file as a starting point.
   * Or, provide text instructions to guide the AI's design generation.

3. **Describe Your UI:** In the chat input field, describe your desired user interface using natural language. Be as specific as possible. 

4. **Generate Code:** Click the "Send" button. SmartUIDraft will process your description and generate the corresponding UI code.

5. **Review and Refine:** The generated UI will be displayed in an output area.
   * If needed, use the "Undo" button to revert previous changes.
   * Continue to refine your description and regenerate the code until you're satisfied with the design.

6. **Download Your Code:** Click the "Download" button to save the generated HTML, CSS, and JavaScript files for further use in your project.

**Example:**

"Create a login form with fields for username and password. Include a blue 'Submit' button and center the form on the page."
 
## Contributing

Whether you're looking to fix bugs, add new features, or improve documentation, all contributions are welcome! Fork the repository and submit your pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
