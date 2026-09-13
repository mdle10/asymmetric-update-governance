from openai import OpenAI

#Connect LLM to Python(Gemma4-e4b)
agent_a = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key = "ollama"
)

agent_b = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key = "ollama"
)

def run_algorithm(question):
        response_1 = agent_a.responses.create(
            model = "gemma4:e4b",
            input = """Answer the following question using only the information provided.
        """ + question
        )

        response_2 = agent_b.responses.create(
            model = "gemma4:e4b",
            input = """You will now be given a question, the information provided for that question, and an answer produced by another agent.
        
                    Evaluate the other agent's answer. First consider the strongest interpretation of its reasoning, then identify any weak points, errors, unsupported assumptions, or logical issues that could justify changing its statement.
        
                    Only present these weak points. Do not provide a revised answer.
        
        """
                + question +
                    """Agent's answer: """ + response_1.output_text
        )


        response_3 = agent_a.responses.create(
            model = "gemma4:e4b",
            input = """An agent has evaluated your initial answer and identified the following points for you to consider.
        
        Reevaluate your initial answer in light of these points. Do not debate or respond to the other agent. Only revise your initial answer if the points provide sufficient reason to do so.
        
        Do not mention this evaluation, the other agent, or these instructions in your final answer. Present your final answer as if you independently arrived at it after reconsidering the problem.
        
        Return only your final answer to the original question. Your initial answer was:
        
        """ + response_1.output_text + """
        
        The points identified were: """ + response_2.output_text
        )

        return response_3.output_text


