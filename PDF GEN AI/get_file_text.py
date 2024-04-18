def get_text_file(file_doc):
    _, file_extension = os.path.splitext(file_doc)
    text = ''
    if file_extension.lower() == '.pdf':
        try:
            for pdf in file_doc:
                pdf_reader = PdfReader(pdf, strict=False)
                for page in pdf_reader.pages:
                    text += page.extract_text()
            return text
        except Exception:
            st.error("File not found. Please make sure the file path is correct.")

    # elif file_extension.lower()=='.doc':
    #     try:
    #         doc = docx.getdocumenttext(file_doc)
    #         fullText = []
    #         for para in doc.paragraphs:
    #             fullText.append(para.text)
    #         text = '\n'.join(fullText)
    #         return text
    #     except Exception:
    #         st.error("File not found. Please make sure the file path is correct.")

    elif file_extension.lower() is [".png"]:
        image_path = file_doc
        with Image.open(image_path) as img:
            text = pytesseract.image_to_string(img)
        return text


