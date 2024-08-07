# Formy - Dynamic Form Generator

Formy is a full-stack web application that allows users to generate custom forms based on natural language descriptions. It uses OpenAI's GPT model to interpret user descriptions and create corresponding JSON Forms schemas.

## Table of Contents

1. [Features](#features)
2. [Technology Stack](#technology-stack)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Running the Application](#running-the-application)
7. [Usage](#usage)
8. [API Endpoints](#api-endpoints)
9. [Contributing](#contributing)
10. [License](#license)

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

### Backend

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/formy.git
   cd formy/backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Frontend

1. Navigate to the frontend directory:
   ```
   cd ../frontend
   ```

2. Install the required npm packages:
   ```
   npm install
   ```

## Configuration

### Backend

1. Set your OpenAI API key as an environment variable:
   ```
   export OPENAI_API_KEY='your-api-key-here'
   ```

2. (Optional) Modify the `app.py` file to change the port or add additional configurations.

### Frontend

1. If your backend is running on a different URL, update the `axiosInstance` baseURL in `src/App.js`.

## Running the Application

### Backend

1. From the `backend` directory, run:
   ```
   python app.py
   ```
   The server should start running on `http://localhost:8080`.

### Frontend

1. From the `frontend` directory, run:
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