def define_promt(context, question):
    from langchain import PromptTemplate

    template = f'''
                You are a chat bot who loves to help people! 
                Given the following sections from the data lake, answer the
                question using only the given context. If you are 
                unsure and the answer is not explicitly writting in the 
                documentation, say "Sorry, I don't know how to help with that.
                

    Context sections: 
    {context}

    Question: 
    {question}
    '''

    prompt = PromptTemplate(template=template, input_variables=["context", "question"])

    prompt_text = prompt.format(context = context, question=question)

    return prompt_text