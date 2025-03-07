from transformers import pipeline

modelo = pipeline('fill-mask')

frase = "The capital of <mask> is Brasilia."

predicoes = modelo(frase)
count = 1
for predicao in predicoes:
    resposta = predicao['token_str']
    score = predicao['score']
    frase = predicao['sequence']
    score_ajustado = score*100
    print(f"\n========= Predição {count} =========")
    print(f"Predição: {resposta}")
    print(f"Score: {score_ajustado:.2f}%")
    print(f"Frase preenchida: {frase}")
    count += 1