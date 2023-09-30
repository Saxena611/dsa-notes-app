from llminit import LLMInit
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain,SequentialChain

'''
DsaPromptLangchainImpl - Resposible to do the integration of prompts with langchain for problem solving a DSA challenge.
The class design ensures the user to register single or multiple prompts and generate result through LLM's accordingly.
'''
class DsaPromptChain:
    __llm = None
    __chain_struct = []
    __input_var = ["problem_statement", "language"]
    __output_var = ['code', 'simplify','approach','algorithm', 'dry_run']

    def __init__(self):
        self.__llm = LLMInit()
    
    def init_all_prompts(self):
        self.init_chain_prompts()
        
    def init_chain_prompts(self):
        self.prompt_write_code()
        self.prompt_simplify_program()
        self.prompt_approach_program()
        self.prompt_algorithm_program()
        self.prompt_dry_run_algorithm()
        
    def prompt_write_code(self):
        prompt_init = "Help learn computer science students problem solving using data structures and algorithms. Write a program to {problem_statement} using {language}"
        self.__register_prompt(prompt_init, "code")

    def prompt_simplify_program(self):
        prompt_problem_simplify = "Simplify the problem statement {problem_statement}"
        self.__register_prompt(prompt_problem_simplify, "simplify")
    
    def prompt_approach_program(self):
        prompt_problem_approach = "Explain the approach to solve the problem statement {problem_statement}"
        self.__register_prompt(prompt_problem_approach, "approach")
    
    def prompt_algorithm_program(self):
        prompt_algorithm = "Explain the algorithm used to solve the problem statement {problem_statement} in the most simplistic form."
        self.__register_prompt(prompt_algorithm, "algorithm")

    def prompt_dry_run_algorithm(self):
        prompt_dry_run = "Dry run the generated code for a test-case for the problem statement {problem_statement}"
        self.__register_prompt(prompt_dry_run, "dry_run")
     
    def execute_chain(self, input_request):
        valid_request = self.__construct_and_validate_input_request(input_request)
        sequence_chain = self.__construct_chain()
        return sequence_chain(valid_request)
    
    def __register_prompt(self, prompt, output_key):
        chain_prompt_init = LLMChain(llm=self.__llm,
                     prompt=self.convert_prompt_to_prompt_template(prompt),
                     output_key=output_key)
        self.__chain_struct.append(chain_prompt_init)
    
    def __construct_chain(self):
        return SequentialChain(chains=self.__chain_struct,
                            input_variables=self.__input_var,
                            output_variables=self.__output_var,
                            verbose=True)

    def __construct_and_validate_input_request(self, input_request):
        request_dict = {}
        for each_input in self.__input_var:
            try:
                request_dict[each_input] = input_request[each_input]
            except:
                raise KeyError("input variable" + each_input + "is not registered.")
        return request_dict
    
    @staticmethod
    def convert_prompt_to_prompt_template(prompt):
        return ChatPromptTemplate.from_template(prompt)