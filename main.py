from call_llm import call_llm_review
import json

file_lines = []
final_json_reviews = []
final_string_reviews = []

with open('files/reviews.txt') as arquivo:
    for line in arquivo:
        file_lines.append(line)

for review in file_lines:
    final_json_reviews.append(json.loads(call_llm_review(review)))
    final_string_reviews.append(call_llm_review(review))

print('Final values: {final_json_reviews}')

def get_avalaitons(final_json_reviews):
    positives = len([review for review in final_json_reviews if review['avaliacao'] == 'Positiva'])
    negatives = len([review for review in final_json_reviews if review['avaliacao'] == 'Negativa'])
    neutras = len([review for review in final_json_reviews if review['avaliacao'] == 'Neutra'])
    list_separator = "#####".join(final_string_reviews)
    return positives, negatives, neutras, list_separator

positive_number, negative_number, neutras_number, list_separator = get_avalaitons(final_json_reviews)
print(f'Positives : {positive_number} \n')
print(f'Negatives : {negative_number} \n')
print(f'Neutras : {neutras_number} \n')
print(list_separator)
