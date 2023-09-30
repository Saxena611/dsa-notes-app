# DSA Notes App
#### Build for geeks not for typewriters !

### Description:
The application uses langchain along with AzureOpenAI.
The user can input the problem statement and choose the programming language. The application simply constructs sequential chain and generates a dictionary response which is
rendered through streamlit on UI.

### Vision:
Prompt chaining can serve to deliver content dynamically to web applications via REST calls.
Static content writting can be avoided instead more user focued content can be generated on the go.

### Input:
{"problem_statement": "{your_problem_statement}", "language": {"C/C++/Python/Java"}}

### Output:
{"code": "", "simply": {}, "approach": "", "dry_run": "", "algorithm": ""}