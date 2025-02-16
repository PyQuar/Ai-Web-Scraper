from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os

# Load OpenRouter API Key
openrouter_api_key = "<Your_API_Key>"

model = ChatOpenAI(
    openai_api_key=openrouter_api_key,  # Use OpenRouter API key
    model="qwen/qwen-vl-plus:free",  # Specify Qwen VL Plus model
    base_url="https://openrouter.ai/api/v1"  # OpenRouter API URL
)

# Create a chat prompt template
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
    "5. **Type:** The output should always be a table, and if there's more than one table, return every table separately. Use Markdown table format.\n"
    "6. **Standardized Table Format:** Ensure each table is formatted as a Markdown table with clear headers and consistent column alignment.\n"
    "7. **Accuracy:** The output should be as accurate as possible.\n"
    "8. **Column Separators:** Use the pipe symbol (|) to clearly separate columns in the Markdown table.\n"
    "9. **Header Row:** The first row of each table should be the header row, clearly labeling each column.\n"
    "10. **Alignment Row:** The second row should contain hyphens (-) to indicate column alignment (e.g., --- for left alignment, :---: for center alignment, ---: for right alignment).\n"
    "11. **Data Rows:** Subsequent rows should contain the data, with each cell aligned according to the alignment row.\n"
)

# Function to parse and extract information from the chunks
def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []

    # Loop through the chunks and parse
    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke({"dom_content": chunk, "parse_description": parse_description})

        # Extract the content from AIMessage and add it to the results
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        parsed_results.append(response.content)  # Ensure content is extracted properly

    # Return the parsed results as a single string
    return "\n".join(parsed_results)
