# Project Overview

This project implements a text parsing and information extraction tool using a chat model. The main functionality is encapsulated in the `parse.py` file, which utilizes an API to process text content and extract relevant information based on specified descriptions.

## Files

- `parse.py`: Contains the implementation for parsing and extracting information from text content using a chat model. It imports necessary libraries, sets up an API key, defines a chat prompt template, and includes a function `parse_with_ollama` that processes chunks of text based on a provided description.

## Setup Instructions

1. **Clone the Repository**
   ```
   git clone <repository-url>
   cd project
   ```

2. **Install Dependencies**
   Ensure you have Python installed, then install the required libraries:
   ```
   pip install langchain_core langchain_openai
   ```

3. **Set Up API Key**
   Replace the placeholder API key in `parse.py` with your actual OpenRouter API key.

## Usage

To use the parsing functionality, call the `parse_with_ollama` function from `parse.py` with the appropriate parameters:

```python
from parse import parse_with_ollama

dom_chunks = ["Your text content here"]
parse_description = "Description of the information to extract"
results = parse_with_ollama(dom_chunks, parse_description)
print(results)
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.