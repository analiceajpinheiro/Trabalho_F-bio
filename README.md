# 🏁 Simulador de Corrida entre Processos

Este projeto é um **minijogo interativo com interface gráfica** feito em Python, que simula uma **corrida entre processos** utilizando diferentes **algoritmos de escalonamento de CPU**.<br>

## 🎮 Como Rodar o Jogo

### Pré-requisitos

- Python 3.6 ou superior instalado.
- As bibliotecas usadas (`tkinter`, `threading`, `random`, `time`) são todas **nativas do Python** – não é necessário instalar nada com `pip`.<br>


⚙️ Algoritmos de Escalonamento Implementados
FIFO (First In, First Out):
Os processos são executados pela ordem de chegada, um de cada vez, até completarem seu tempo total.<br>

Round Robin (RR):
Cada processo recebe uma fatia fixa de tempo (quantum = 2 unidades). Se não terminar nesse tempo, volta para o fim da fila.<br>

🧠 Informações Adicionais
Os processos simulam atletas famosos (como Usain Bolt, Carl Lewis, entre outros), e cada um recebe um tempo de execução aleatório entre 5 e 10 unidades de tempo.<br>

O progresso de cada "atleta" é visualizado com uma barra de progresso animada, atualizada conforme o tempo de CPU é utilizado.<br>

A interface foi feita com Tkinter e é totalmente interativa.<br>

Ao final da corrida, o vencedor (processo que terminou mais rápido) é anunciado com uma mensagem especial 🏆.<br>

O botão "Reiniciar" permite refazer a corrida com novos tempos aleatórios.<br>


