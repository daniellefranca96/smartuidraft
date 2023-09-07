
# SmartUIDraft

SmartUIDraft is an intuitive text-to-HTML application that harnesses the power of GPT-3 to transform user descriptions into tangible web interfaces. Users simply describe the interface they envision, and SmartUIDraft generates the corresponding HTML for it. Additionally, it offers a download option for users to easily obtain the generated HTML code.

## Features

- **GPT-3 Powered**: The application uses the capabilities of GPT-3 to understand and convert user descriptions into accurate HTML components.
- **Text-to-HTML Conversion**: Describe your desired interface and receive the HTML code in real-time.
- **User-Friendly Interface**: The application is designed with a straightforward UI, ensuring accessibility for both tech-savvy users and beginners.
- **Download Option**: Conveniently download the generated HTML directly from the application.

## Structure

- `app.py`: Main application entry point.
- `generator.py`: Contains the logic for converting user input into HTML.
- `static/`: Houses static assets like stylesheets, scripts, and images.
- `templates/`: Contains the HTML templates used to render the application's web pages.

## Setup

1. **Clone the Repository**

   If you have git installed:
   ```
   git clone <repository-url>
   cd smartuidraft
   ```

2. **Install Dependencies**

   It's recommended to use a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Environment Variables**

   Ensure the `.env` file is configured with the necessary environment variables.

4. **Run the Application**

   ```
   python app.py
   ```

   Once running, access the application at `http://localhost:5000` or the port specified in the `.env` file.

## Contributing

Whether you're looking to fix bugs, add new features, or improve documentation, all contributions are welcome! Fork the repository and submit your pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
