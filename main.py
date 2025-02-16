import streamlit as st
from scraper import scrape_website, split_dom_content, clean_body_content, extract_body_content
from project.parse import parse_with_ollama
from Data import markdown_to_csv

st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL")

if st.button("Scrape Site"):
    st.write("Scraping the website")

    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")
    
    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing Content")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks,parse_description)
            st.write(result)
            
            
            # Appliquer la fonction
            tables = markdown_to_csv(result)
            for i in tables:
                st.write(i)
