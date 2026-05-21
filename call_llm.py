from openai import OpenAI
from config import OPENAI_API_KEY


client_openai = OpenAI(
    base_url='http://127.0.0.1:1234/v1',
    api_key=OPENAI_API_KEY
)


def call_llm_review(review):
    resposta_llm = client_openai.chat.completions.create(
        model="google/gemma-3-4b",
        messages=[
            {"role":"system",
            "content": """Você é um especialista em análise de dados e conversão de dados para JSON.
            Você receberá uma linha de texto que é uma resenha de um aplicativo em um marktplace online.
            Eu quero que você analise essa resenha, e me retorne um JSON com as seguintes chaves:
            - 'usuario': o nome do usuário que fez a resenha
            - 'resenha_original': a resenha no idioma original que você recebeu
            - 'resenha_pt': a resenha traduzida para o português, deve estar sempre na língua portuguesa
            - 'avaliacao': uma avalicao se essa resenha foi 'Positiva', 'Negativa' ou 'Neutra' (apenas uma dessas opções)

            Exemplo de entrada:
            '879485937$Pedro Silva$This is a positive review for the app'
            Exemplo de saída:
            {
                "usuario": "Pedro Silva",
                "resenha_original": "This is a positive review for the app",
                "resenha_pt": "Esta é uma resenha positiva para o aplicativo",
                "avaliacao": "Positiva"
            }
            
            Exemplo de entrada:
            '74398793$John Myers$Je n'aime pas cette application'
            Exemplo de saída:
            {
                "usuario": "John Myers",
                "resenha_original": "Je n'aime pas cette application",
                "resenha_pt": "Eu não gosto dessa aplicação",
                "avaliacao": "Negativa"
            }

            Regra importante: você deve retornar apenas o JSON, sem nenhum outro texto além do JSON.
            """},

            {"role":"user",
            "content": f"Resenha: {review}"}
        ],
        temperature=1.0
    )
    print(resposta_llm.choices[0].message.content.replace('```','').replace('json',''))
    return resposta_llm.choices[0].message.content.replace('```','').replace('json','')

## Primeira tentativa de prompt não funcionou conforme esperado, devido a limitação do modelo local conectado no LLM Studio    
 # messages=[
    #     {"role":'system', "content":'#Você é um especialista em análise de dados e conversão de dados para JSON'},
    #     {"role":'user', "content": '''
    #         ##Papel: Você é um especialista em ANÁLISE de avaliações de produtos
    #         ##Tarefa: Categorizar as avaliações que serão enviadas em formato de lista python e identificar os atributos presente em cada linha para formata-los ao padrão JSON desejado
    #         ##Ação: Para cada item da lista anexa, você deve:
    #             - Encontrar o texto da avaliação. O nome desse atributo será ***review***
    #             - Categorizar a ***review*** como 'Positiva', 'Negativa' ou 'Neutra'. Essa categorização deve ser realizada usando somente 1 palavra. O nome desse atributo será ***type_avaliation***
    #             - Traduzir a respectiva ***review*** para o português Brasil. O nome desse atributo será ***review_pt***
    #             - Encontrar o nome do usuário que fez a avliação. O nome desse atributo será ***usuario***
    #         Ao final, cada uma das linhas da lista de avaliações enviadas devem ser armazenadadas em uma NOVA LISTA JSON no seguinte formato:
    #         {user: ***usuario***, 'review':***review***,'review_pt': **review_pt***, 'type_avaliation': ***type_avaliation***}
    #         - AO final, deve se retornar uma lista JSON com os dados formatos conforme solicitado
    #         - Não anexe textos adicionais. O retorno da lista JSON deve estar pronta para ser anexo em uma nova variável.
    #         Lista de avaliações: {reviews_formatted}
    #     '''},
    # ],
# print(lines)