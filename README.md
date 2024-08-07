# Formy - Dynamic Form Generator

Formy is a full-stack web application that allows users to generate custom forms based on natural language descriptions. It uses OpenAI's GPT model to interpret user descriptions and create corresponding JSON Forms schemas.

## Table of Contents

- [Formy - Dynamic Form Generator](#formy---dynamic-form-generator)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Technology Stack](#technology-stack)
    - [Frontend](#frontend)
    - [Backend](#backend)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Running the Application](#running-the-application)
  - [Usage](#usage)
  - [API Endpoints](#api-endpoints)
  - [Contributing](#contributing)
  - [License](#license)

## Features

- Dynamic form generation based on natural language descriptions
- Dark mode UI with a sleek, modern design
- Real-time form preview using JSON Forms
- RESTful API for form generation
- Error handling and loading states
- Responsive design for various screen sizes

## Technology Stack

### Frontend
- React
- Material-UI (MUI)
- JSON Forms
- Axios for API calls

### Backend
- Flask (Python)
- OpenAI API
- Flask-CORS for handling Cross-Origin Resource Sharing

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Node.js (v14 or later)
- Python (v3.7 or later)
- OpenAI API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/formy.git
   cd formy
   ```
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install backend dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Install frontend dependencies:
   ```
   npm install
   ```

## Configuration

1. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

2. (Optional) If your backend is running on a different URL, update the `axiosInstance` baseURL in `src/App.js`.

3. (Optional) Modify the `app.py` file to change the port or add additional configurations.


## Running the Application

1. Start the backend:
   ```
   python app.py
   ```
   The server should start running on `http://localhost:8080`.

2. In a new terminal, start the frontend:
   ```
   npm start
   ```
   The application should open in your default browser at `http://localhost:3000`.

## Usage

1. Open the application in your web browser.
2. In the text area, describe the form you want to create. For example: "Create a contact form with fields for name, email, and message."
3. Click the "Generate Form" button.
4. The application will generate a form based on your description and display it below.
5. You can interact with the generated form and see the form data update in real-time.

## API Endpoints

- `GET /test`: Test the API connection
- `POST /generate-form`: Generate a form schema based on a description
  - Request body: `{ "description": "Your form description here" }`
  - Response: `{ "form_structure": "JSON Forms schema" }`

## Contributing

Contributions to Formy are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature-branch-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-branch-name`
5. Create a pull request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

For any additional questions or support, please open an issue in the GitHub repository.