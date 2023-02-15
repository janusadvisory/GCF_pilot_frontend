import openai as ai


ai.api_key = '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'

def generate_gpt3_response(user_text, print_output=False):

    completions = ai.Completion.create(
        engine='text-davinci-003',
        temperature=0.1,
        prompt=user_text,
        max_tokens=400,
        n=1,
        stop=None,
    )


    if print_output:
        print(completions)


    return completions.choices[0].text



def score_section(text):
    score = ''

    prompt = '''Please read the following text and answer the following questions if less than 3 questions are answered the score is Low, if 3 questions are answered the score is Medium if all questions are answered the score is High:

Text: '''+text +'''

[Does the text include an evaluation/assessment of the climate vulnerability context of the proposed project or programme?]
[Does the text consider observed (historic) climate trends (such as observed changes in mean annual temperature and rainfall) and expected future climate change (e.g. projected changes in temperature or rainfall)?]
[Are the geographic and temporal scales appropriate for the project, considering both slow-onset climate-related hazards and rapid-onset climate-related hazards?]
[Do the assessments/evaluations/studies demonstrate/quantify through literature/data how climate hazards will affect the project or programme geographical area in terms of loss of lives, value of physical assets or natural resources, and potential disruptions to social, economic and other activities?]

the answer should be like this :

The score is [Low/Medium/High] because [insert a detailed explanation here,the explanation should discuss the answred/non answered questions].'''

    

    response = generate_gpt3_response(prompt,False)
    score = response.split(' ')[3]
    response = response.replace(''.join(response.split(' ')[:5]),'')

    return {'answer':response,'score':score}
