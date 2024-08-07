from flask import Flask, request, jsonify
from flask_cors import CORS

from openai import OpenAI
import os
from functools import wraps
import logging 
import traceback
import json


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
logging.basicConfig(level=logging.DEBUG)

# CORS(app, supports_credentials=True)

# Set your OpenAI API key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

UI_FORMS_SCHEMA = {
    "type": "object",
    "properties": {
        "schema": {
            "type": "object",
            "properties": {
                "type": {"type": "string", "enum": ["object"]},
                "properties": {
                    "type": "object",
                    "additionalProperties": {
                        "type": "object",
                        "properties": {
                            "type": {"type": "string", "enum": ["string", "number", "integer", "boolean", "object", "array", "null"]},
                            "title": {"type": "string"},
                            "description": {"type": "string"},
                            "default": {},
                            "enum": {"type": "array"},
                            "const": {},
                            "format": {"type": "string"},
                            "readOnly": {"type": "boolean"},
                            "writeOnly": {"type": "boolean"},
                            "minLength": {"type": "integer", "minimum": 0},
                            "maxLength": {"type": "integer", "minimum": 0},
                            "pattern": {"type": "string"},
                            "minimum": {"type": "number"},
                            "maximum": {"type": "number"},
                            "exclusiveMinimum": {"type": "number"},
                            "exclusiveMaximum": {"type": "number"},
                            "multipleOf": {"type": "number", "exclusiveMinimum": 0},
                            "items": {"type": "object"},
                            "minItems": {"type": "integer", "minimum": 0},
                            "maxItems": {"type": "integer", "minimum": 0},
                            "uniqueItems": {"type": "boolean"},
                            "required": {"type": "array", "items": {"type": "string"}},
                            "properties": {"type": "object"}
                        },
                        "required": ["type"]
                    }
                },
                "required": {"type": "array", "items": {"type": "string"}}
            },
            "required": ["type", "properties"]
        },
        "uischema": {
            "type": "object",
            "properties": {
                "type": {"type": "string", "enum": ["VerticalLayout", "HorizontalLayout", "Group", "Categorization"]},
                "elements": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "type": {"type": "string", "enum": ["Control", "Group", "HorizontalLayout", "VerticalLayout"]},
                            "scope": {"type": "string"},
                            "label": {"type": "string"},
                            "options": {
                                "type": "object",
                                "properties": {
                                    "format": {"type": "string"},
                                    "multi": {"type": "boolean"}
                                }
                            },
                            "rule": {
                                "type": "object",
                                "properties": {
                                    "effect": {"type": "string", "enum": ["HIDE", "SHOW", "ENABLE", "DISABLE"]},
                                    "condition": {
                                        "type": "object",
                                        "properties": {
                                            "scope": {"type": "string"},
                                            "schema": {"type": "object"}
                                        },
                                        "required": ["scope", "schema"]
                                    }
                                },
                                "required": ["effect", "condition"]
                            },
                            "elements": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/properties/uischema/properties/elements/items"
                                }
                            }
                        },
                        "required": ["type", "scope"]
                    }
                }
            },
            "required": ["type", "elements"]
        }
    },
    "required": ["schema", "uischema"],
    "additionalProperties": False
}


@app.route('/test', methods=['GET', 'OPTIONS'])
def test():
    if request.method == "OPTIONS":
        return jsonify({}), 200
    return jsonify({"message": "Test successful!"})

@app.route('/generate-form', methods=['POST', 'OPTIONS'])
def generate_form():
    if request.method == "OPTIONS":
        response = jsonify({'message': 'OK'})
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response

    app.logger.debug(f"Received request: {request.method} {request.url}")
    app.logger.debug(f"Request headers: {request.headers}")
    app.logger.debug(f"Request body: {request.get_json()}")
    description = request.json['description']
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that generates extremely clear and usable JSON structures for forms based on text descriptions."
                },
                {
                    "role": "user",
                    "content": "Generate a highly robust and visually aesthetic JSON Forms schema for a " + description
                }
            ],
            model="gpt-4o-2024-08-06",  # Using a more recent model
            response_format={
                "type": "json_schema",
                "json_schema":  {
                    "name": "ui-forms",
                    "schema": UI_FORMS_SCHEMA
                }
            },  # Ensuring JSON output
            temperature=0.7
        )

        # Print the generated JSON structure
        output = chat_completion.choices[0].message.content 
        data = json.loads(output)
        pretty_json = json.dumps(data, indent=4)
        print(pretty_json)
        response = jsonify({"form_structure": output})
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response

    except Exception as e:
        app.logger.error(f"Error occurred: {str(e)}")
        app.logger.error(traceback.format_exc())
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8080)