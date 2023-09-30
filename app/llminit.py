from langchain.chat_models import AzureChatOpenAI

'''
This class helps to initialze the AzureChatOpenAI model.
Singleton design ensures same instance is reffered accoss context.
'''
class LLMInit:
    llm = None
    
    def __new__(cls):
        if cls.llm is None:
            cls.llm = AzureChatOpenAI(
                    deployment_name="gpt-35-turbo-0301",
                    model_name="gpt-35-turbo"
                  )
        return cls.llm
    
    def get_llm(self):
        return self.llm