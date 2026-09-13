from openai import OpenAI
from main import run_algorithm
from norMAD import run_MAD
from database import questions_from_db



judge = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key = "ollama"
)


for question_id, question, difficulty in questions_from_db:
            response_3 = run_algorithm(question)
            response_5 = run_MAD(question)

            print("SYSTEMS FINISHED — NOW RUNNING JUDGE")

            response = judge.responses.create(
                model = "qwen3.5:4b",
                input = """/set nothink
                
                You are an independent evaluator.
            You will be given a question, the information available for answering it, and the final answers produced by two different reasoning systems.
            Evaluate each final answer independently. Do not favor either system and do not assume that either answer is correct.
            For each answer, assign scores from 0 to 10 for:
            ACCURACY — How correct is the final answer based on the information provided?
            REASONING — How logically sound, relevant, and well-supported is the reasoning?
            
            Base your evaluation only on the provided information and question. Do not reward an answer merely for sounding sophisticated or cautious.
            Pay particular attention to unsupported assumptions, logical errors, contradictions, failure to use relevant information, unjustified certainty, unjustified changes in conclusion, unnecessary reasoning or repetition.
            Return your evaluation in exactly and ONLY this format:
            SYSTEM A:
            Accuracy: X/10
            Reasoning: X/10
            
            SYSTEM B:
            Accuracy: X/10
            Reasoning: X/10
            
            """ + question+
            """System A final answer:"""
             + response_3 + """
            System B final answer:
            """ + response_5
            )
            print(response.output_text)