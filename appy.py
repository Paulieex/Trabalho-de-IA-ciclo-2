from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    resposta = ""
    if request.method == 'POST':
        pergunta = request.form['pergunta'].lower()
        if "horário" in pergunta:
            resposta = "As aulas começam às 19h."
        elif "frequentes" in pergunta:
            resposta = "Clique em qualquer pergunta e obtenha sua resposta!"
        elif "prova" in pergunta:
            resposta = "As provas estão na Semana 11."
        elif "horas" in pergunta:
            resposta = "As aulas começam as 19h."
        elif "quiz" in pergunta:
            resposta = "Temos quizzes disponíveis desde a semana 1! Gostaria de selecionar algum?"
        elif "onde" in pergunta:
            resposta = "As aulas são na sala H103, do bloco H"
        elif "calendário das aulas" in pergunta:
            resposta = "Segunda-feira = Cidadania, ética e espiritualidade/ Introdução à engenharia de soluções. Terça-feira = Introdução à engenharia de soluções. Quarta-feira = Fundamentos matemáticos para coputção. Quinta-feira = Fundamentos de computação e infraestrutura. Sexta-feira = Fundamentos de engenharia de dados."
        elif "trabalho" in pergunta:
            resposta = "O trabalho final vale 30% da nota."
        elif "professor" in pergunta:
            resposta = "O professor responsável é o Henrique."
        else:
            resposta = "Ainda não sei responder isso."
    return render_template('index.html', resposta=resposta )

if __name__ == '__main__':
    app.run(debug=True)
