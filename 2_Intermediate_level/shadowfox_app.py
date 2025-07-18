import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="Web Scraper", layout="centered")

st.title("🌐 Website Web Scraper")

# User input for website URL
url = st.text_input("Enter website URL (include https://):", placeholder="https://shadowfox.in")

scraped_data = ""

if st.button("Scrape Website"):
    if not url:
        st.warning("⚠️ Please enter a valid website URL.")
    else:
        try:
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            # Extract page title
            title = soup.title.text.strip() if soup.title else "No title found"

            # Try to find an intro line with 'Founded on the belief' or something similar
            intro = soup.find(text=lambda t: "Founded on the belief" in t if isinstance(t, str) else False)
            intro_text = intro.strip() if intro else "Intro line not found."

            # Combine and show
            scraped_data = f"Page Title: {title}\n\nIntro: {intro_text}"

            st.success("✅ Scraped successfully!")
            st.subheader("Scraped Result:")
            st.code(scraped_data)

            # Optional download
            st.download_button(
                label="📥 Download as TXT",
                data=scraped_data,
                file_name="scraped_data.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"❌ Error: {e}")
