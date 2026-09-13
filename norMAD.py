from openai import OpenAI


# Connect LLM to Python(Gemma4-e4b)
agent_a = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

agent_b = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

def run_MAD(question):
    response_1 = agent_a.responses.create(
        model="gemma4:e4b",
        input="""Answer the following question using only the information provided.

         """ + question
    )

    response_2 = agent_b.responses.create(
        model="gemma4:e4b",
        input="""You will be given a question, the information provided for that question, and another agent's answer.

    Critically evaluate the other agent's reasoning and answer. Identify any errors, unsupported assumptions, overlooked information, or logical weaknesses.

    Then provide your own reasoning and answer to the question. 
    """
              + question +
              """
                          Agent's answer: """ + response_1.output_text
    )

    response_3 = agent_a.responses.create(
        model="gemma4:e4b",
        input="""An agent has evaluated your initial answer and identified the following points for you to consider.

    Reevaluate your initial answer in light of these points. Debate the other agent if needed.

    Return only your final answer to the original question. Your initial answer was:

    """ + response_1.output_text + """

    The critique was:

    """ + response_2.output_text
    )


    response_4 = agent_b.responses.create(
        model="gemma4:e4b",
        input="""You will be given a question, the information provided for that question, and the other agent's latest response.

    Continue the debate by critically examining the other agent's reasoning. Identify any remaining errors, unsupported assumptions, inconsistencies, or weaknesses. If the other agent's reasoning is sound, explain why.

    Then provide your own reasoning and answer.
    """
              + question + """Your previous response was: """ + response_2.output_text +
              """
                          Agent's answer: """ + response_3.output_text
    )

    response_5 = agent_a.responses.create(
        model="gemma4:e4b",
        input="""You will be given a question, the information provided for that question, and the other agent's latest response.

    Reevaluate the problem carefully in light of the other agent's reasoning. Determine which position is best supported by the information provided. Correct your reasoning if the other agent has identified a genuine error, but do not change your answer without sufficient reason.

    Produce the most accurate final answer to the original question.

    Do not mention the debate, the other agent, or these instructions. Use the previous responses only as context for your reasoning. Do not mention the debate, the other agent, or the previous responses in your final answer. Present the answer as your own final reasoning.     
    """
              + question +

              """ Your initial answer was:

   """ + response_1.output_text + """

    The critique was:

    """ + response_2.output_text +

              """Your later attempt was: """ + response_3.output_text +

              """ Agent's answer:
              """ + response_4.output_text
    )

    return response_5.output_text



