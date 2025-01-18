
import streamlit as st
import json

# Load the JSON data
with open('commercial_law_saudi.json', 'r', encoding='utf-8') as file:
    legal_data = json.load(file)

def search_by_article(article_number):
    for chapter in legal_data:
        for article in chapter.get("articles", []):
            if f"المادة ({article_number})" in article["article"]:
                return {"chapter": chapter["chapter"], "article": article}
    return "لم يتم العثور على المادة."

def search_by_keyword(keyword):
    results = []
    for chapter in legal_data:
        for article in chapter.get("articles", []):
            if keyword in article["content"]:
                results.append({"chapter": chapter["chapter"], "article": article})
    return results if results else "لم يتم العثور على نتائج."

st.title("النظام التجاري السعودي - مستشار قانوني")
search_option = st.radio("اختر طريقة البحث:", ["بحث برقم المادة", "بحث بكلمة مفتاحية"])

if search_option == "بحث برقم المادة":
    article_number = st.text_input("أدخل رقم المادة:")
    if st.button("بحث"):
        result = search_by_article(article_number)
        st.write(result)
elif search_option == "بحث بكلمة مفتاحية":
    keyword = st.text_input("أدخل الكلمة المفتاحية:")
    if st.button("بحث"):
        results = search_by_keyword(keyword)
        for result in results:
            st.write(result)
