import random
import sys
import os
import tkinter as tk
from tkinter import *

def questao_aleatoria():
    perguntas = [
        "Quem pintou a famosa obra `Mona Lisa`?;Leonardo da Vinci;Pablo Picasso;Vincent van Gogh;Michelangelo",
        "Qual é a capital do Brasil?;Brasília;Rio de Janeiro;São Paulo;Belo Horizonte",
        "Quem escreveu a peça de teatro `Romeu e Julieta`?;William Shakespeare;Friedrich Nietzsche;Charles Dickens;Johann Wolfgang von Goethe",
        "Qual é o maior planeta do sistema solar?;Júpiter;Marte;Vênus;Saturno",
        "Qual é o rio mais longo do mundo?;Nilo;Amazonas;Mississippi;Yangtzé",
        "Quem foi o primeiro presidente dos Estados Unidos?;George Washington;Thomas Jefferson;John Adams;Abraham Lincoln",
        "Qual é a maior cadeia de montanhas do mundo?;Himalaias;Andes;Montanhas Rochosas;Alpes",
        "Quem é o autor do livro `Dom Quixote`?;Miguel de Cervantes;Gabriel García Márquez;Jorge Luis Borges;Pablo Neruda",
        "Qual é o maior oceano do mundo?;Pacífico;Atlântico;Índico;Ártico",
        "Em que país nasceu o famoso cientista Albert Einstein?;Alemanha;Estados Unidos;Suíça;Áustria",
        "Qual é o maior animal terrestre?;Elefante africano;Girafa;Rinoceronte;Leão",
        "Quem foi o primeiro homem a pisar na Lua?;Neil Armstrong;Buzz Aldrin;Michael Collins;Yuri Gagarin",
        "Qual é a capital da França?;Paris;Londres;Berlim;Roma",
        "Quem escreveu o romance `Cem Anos de Solidão`?;Gabriel García Márquez;Jorge Luis Borges;Pablo Neruda;Isabel Allende",
        "Qual é o país com a maior população do mundo?;China;Índia;Estados Unidos;Brasil",
        "Quem foi o inventor da lâmpada elétrica?;Thomas Edison;Nikola Tesla;Alexander Graham Bell;Albert Einstein",
        "Qual é a cidade italiana conhecida como `cidade eterna`?;Roma;Veneza;Milão;Florença",
        "Quem foi o líder da Revolução Cubana?;Fidel Castro;Che Guevara;Hugo Chávez;Augusto Pinochet",
        "Qual é o menor continente do mundo?;Oceania;Antártida;Europa;África",
        "Quem escreveu o livro `1984`?;George Orwell;Aldous Huxley;Ray Bradbury;J.R.R. Tolkien",
        "Qual é a capital do Japão?;Tóquio;Quioto;Osaka;Yokohama",
        "Quem pintou a obra `A Noite Estrelada`?;Vincent van Gogh;Pablo Picasso;Leonardo da Vinci;Salvador Dalí",
        "Qual é a cidade brasileira conhecida como `cidade maravilhosa`?;Rio de Janeiro;São Paulo;Salvador;Brasília",
        "Quem foi o fundador da Apple?;Steve Jobs;Bill Gates;Mark Zuckerberg;Jeff Bezos",
        "Qual é o maior deserto do mundo?;Deserto do Saara;Deserto de Gobi;Deserto do Atacama;Deserto da Arábia",
        "Quem foi o líder do movimento pelos direitos civis dos negros nos Estados Unidos?;Martin Luther King Jr.;Malcolm X;Rosa Parks;Barack Obama",
        "Qual é o maior produtor de café do mundo?;Brasil;Colômbia;Vietnã;Costa Rica",
        "Quem escreveu a peça de teatro `Hamlet`?;William Shakespeare;Friedrich Nietzsche;Charles Dickens;Johann Wolfgang von Goethe",
        "Qual é a capital da Argentina?;Buenos Aires;Santiago;Montevidéu;Lima",
        "Quem foi o pintor espanhol famoso pelo estilo surrealista?;Salvador Dalí;Pablo Picasso;Diego Velázquez;Francisco Goya",
        "Qual é a maior empresa de comércio eletrônico do mundo?;Amazon;Alibaba;eBay;Mercado Livre",
        "Quem foi o líder da Revolução Russa?;Vladimir Lênin;Joseph Stalin;Leon Trotsky;Nikita Khrushchev",
        "Qual é o maior produtor de petróleo do mundo?;Arábia Saudita;Rússia;Estados Unidos;Irã",
        "Quem escreveu o romance `Orgulho e Preconceito`?;Jane Austen;Emily Brontë;Charlotte Brontë;Virginia Woolf",
        "Qual é a capital da Espanha?;Madri;Barcelona;Valência;Sevilha",
        "Quem foi o líder da independência do Brasil?;Dom Pedro I;Dom Pedro II;Joaquim José da Silva Xavier (Tiradentes);Luís Alves de Lima e Silva (Duque de Caxias)",
        "Qual é a maior ilha do mundo?;Groenlândia;Nova Guiné;Bornéu;Madagascar",
        "Quem foi o cientista famoso pela teoria da relatividade?;Albert Einstein;Isaac Newton;Galileu Galilei;Stephen Hawking",
        "Qual é a capital da Itália?;Roma;Milão;Veneza;Florença",
        "Quem foi o líder nazista responsável pelo Holocausto durante a Segunda Guerra Mundial?;Adolf Hitler;Joseph Goebbels;Heinrich Himmler;Hermann Göring",
        "Qual é o país com a maior área territorial do mundo?;Rússia;Canadá;Estados Unidos;China",
        "Quem foi o pintor italiano famoso pela obra `A Última Ceia`?;Leonardo da Vinci;Michelangelo;Raffaello Sanzio;Caravaggio",
        "Qual é o maior animal marinho do mundo?;Baleia-azul;Tubarão-branco;Polvo-gigante;Cachalote",
        "Quem escreveu o livro `O Pequeno Príncipe`?;Antoine de Saint-Exupéry;J.R.R. Tolkien;C.S. Lewis;Lewis Carroll",
        "Qual é a capital da Austrália?;Camberra;Sydney;Melbourne;Brisbane",
        "Quem foi o autor da obra `A Divina Comédia`?;Dante Alighieri;Miguel de Cervantes;Johann Wolfgang von Goethe;Geoffrey Chaucer",
        "Qual é o maior produtor de vinho do mundo?;Itália;França;Espanha;Estados Unidos",
        "Quem foi o líder da independência dos Estados Unidos?;George Washington;Thomas Jefferson;John Adams;Benjamin Franklin",
        "Qual é a capital do México?;Cidade do México;Guadalajara;Monterrey;Puebla",
        "Quem foi o autor da obra `1984`?;George Orwell;Aldous Huxley;Ray Bradbury;J.R.R. Tolkien",
        "Qual é o país com a maior população do mundo?;China;Índia;Estados Unidos;Brasil",
        "Quem escreveu o livro `O Senhor dos Anéis`?;J.R.R. Tolkien;C.S. Lewis;George R.R. Martin;J.K. Rowling",
        "Qual é o maior produtor de cacau do mundo?;Costa do Marfim;Gana;Brasil;Indonésia",
        "Quem foi o líder sul-africano que lutou contra o apartheid?;Nelson Mandela;Desmond Tutu;Winnie Mandela;Thabo Mbeki",
        "Qual é a capital do Reino Unido?;Londres;Manchester;Birmingham;Liverpool",
        "Quem foi o autor da obra `Crime e Castigo`?;Fiódor Dostoiévski;Lev Tolstói;Aleksandr Soljenítsin;Anton Tchekhov",
        "Qual é o maior produtor de arroz do mundo?;China;Índia;Indonésia;Brasil",
        "Quem foi o líder religioso e político do Tibete?;Dalai Lama;Buda;Gandhi;Mao Tsé-tung",
        "Qual é a capital da Colômbia?;Bogotá;Medellín;Cali;Cartagena",
        "Quem foi o cientista que desenvolveu a teoria da evolução das espécies?;Charles Darwin;Gregor Mendel;Louis Pasteur;Marie Curie",
        "Qual é o maior produtor de milho do mundo?;Estados Unidos;China;Brasil;Índia",
        "Quem escreveu o romance `O Grande Gatsby`?;F. Scott Fitzgerald;Ernest Hemingway;Truman Capote;Harper Lee",
        "Qual é a capital do Canadá?;Ottawa;Toronto;Montreal;Vancouver",
        "Quem foi o autor da obra `Odisseia`?;Homero;Sófocles;Eurípides;Aristóteles",
        "Qual é o maior produtor de aço do mundo?;China;Estados Unidos;Índia;Japão",
        "Quem foi o líder indiano que lutou pela independência do país?;Mahatma Gandhi;Jawaharlal Nehru;Indira Gandhi;Rajiv Gandhi",
        "Qual é a capital da Rússia?;Moscou;São Petersburgo;Kazan;Vladivostok",
        "Quem escreveu o livro `A Revolução dos Bichos`?;George Orwell;Aldous Huxley;Ray Bradbury;J.R.R. Tolkien",
        "Qual é o maior produtor de soja do mundo?;Estados Unidos;Brasil;Argentina;China",
        "Quem foi o líder religioso e político da Índia que lutou pela independência do país?;Mahatma Gandhi;Jawaharlal Nehru;Indira Gandhi;Rajiv Gandhi",
        "Qual é a capital da Turquia?;Ancara;Istambul;Izmir;Bursa",
        "Quem foi o autor da obra `A Metamorfose`?;Franz Kafka;Friedrich Nietzsche;Thomas Mann;Hermann Hesse",
        "Qual é o maior produtor de diamantes do mundo?;Rússia;Botsuana;Canadá;Austrália",
        "Quem foi o líder militar francês que se tornou imperador?;Napoleão Bonaparte;Joana d'Arc;Carlos Magno;Luís XIV",
        "Quem escreveu a obra `O Leão, a Feiticeira e o Guarda-Roupa`?;C.S. Lewis;J.R.R. Tolkien;George Orwell;J.K. Rowling",
        "Qual é a capital da Alemanha?;Berlim;Munique;Hamburgo;Colônia",
        "Quem foi o pintor italiano famoso pelas obras `O Nascimento de Vênus` e `Primavera`?;Sandro Botticelli;Leonardo da Vinci;Rafael;Michelangelo",
        "Qual é o maior produtor de chá do mundo?;China;Índia;Quênia;Sri Lanka",
        "Quem foi o líder militar dos Estados Unidos durante a Segunda Guerra Mundial?;Dwight D. Eisenhower;George Patton;Douglas MacArthur;Franklin D. Roosevelt",
        "Qual é a capital da Argentina?;Buenos Aires;Santiago;Montevidéu;Lima",
        "Quem foi o autor da obra `A Guerra dos Tronos`?;George R.R. Martin;J.R.R. Tolkien;C.S. Lewis;J.K. Rowling",
        "Qual é o maior produtor de algodão do mundo?;China;Índia;Estados Unidos;Paquistão",
        "Quem foi o líder revolucionário cubano que assumiu o poder em 1959?;Fidel Castro;Che Guevara;Camilo Cienfuegos;Raul Castro",
        "Qual é a capital da Grécia?;Atenas;Salônica;Pireu;Patras",
        "Quem escreveu o livro `A Insustentável Leveza do Ser`?;Milan Kundera;Franz Kafka;Fyodor Dostoyevsky;Leo Tolstoy",
        "Qual é o maior produtor de cobre do mundo?;Chile;Peru;China;Austrália",
        "Quem foi o líder da Revolução Industrial na Inglaterra?;James Watt;Robert Fulton;Isambard Kingdom Brunel;George Stephenson",
        "Quem escreveu a peça de teatro `Macbeth`?;William Shakespeare;Friedrich Nietzsche;Charles Dickens;Johann Wolfgang von Goethe",
        "Qual é a capital do Peru?;Lima;Cusco;Arequipa;Trujillo",
        "Quem foi o líder político e religioso do Tibete que recebeu o Prêmio Nobel da Paz?;Dalai Lama;Buda;Gandhi;Mao Tsé-tung",
        "Qual é a capital da Coreia do Sul?;Seul;Busan;Incheon;Daegu",
        "Quem foi o autor da obra `Os Miseráveis`?;Victor Hugo;Gustave Flaubert;Émile Zola;Charles Baudelaire",
        "Qual é o maior produtor de ouro do mundo?;China;Rússia;Estados Unidos;Austrália",
        "Quem foi o líder militar britânico durante a Segunda Guerra Mundial?;Winston Churchill;Neville Chamberlain;Margaret Thatcher;Tony Blair",
        "Qual é a capital da Suíça?;Berna;Zurique;Genebra;Basileia",
        "Quem foi o pintor holandês famoso pelas obras `Os Girassóis` e `Noite Estrelada`?;Vincent van Gogh;Rembrandt;Johannes Vermeer;Pieter Bruegel",
        "Quem escreveu o livro `Moby Dick`?;Herman Melville;Mark Twain;Edgar Allan Poe;Emily Dickinson",
        "Qual é o maior produtor de borracha natural do mundo?;Tailândia;Indonésia;Malásia;Brasil",
        "Quem foi o líder militar espartano na Batalha das Termópilas?;Leônidas I;Alexandre, o Grande;Pericles;Sócrates",
        "Qual é a capital do Egito?;Cairo;Alexandria;Giza;Luxor",
    ];
    return perguntas[random.randint(0, 99)].split(";")

questao = questao_aleatoria()
respC = questao[1]
respostas = [questao[1], questao[2], questao[3], questao[4]]
respAL = random.sample(respostas, 4)

def reset():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def clique_botao(event):

    buttons = [button0, button1, button2, button3, button4]

    button0["bg"] = "SystemButtonFace"
    button1["bg"] = "SystemButtonFace"
    button2["bg"] = "SystemButtonFace"
    button3["bg"] = "SystemButtonFace"
    button4["bg"] = "SystemButtonFace"

    if(event == 0):
        button0.configure(bg='red')
    elif(event == 1):
        button1.configure(bg='red')
    elif(event == 2):
        button2.configure(bg='red')
    elif(event == 3):
        button3.configure(bg='red')
    elif(event == 4):
        button4.configure(bg='yellow')
        reset()
        
    if(respC == 0):
        button0.configure(bg='green')
    elif(respC == 1):
        button1.configure(bg='green')
    elif(respC == 2):
        button2.configure(bg='green')
    elif(respC == 3):
        button3.configure(bg='green')

    if(respC == respAL[event]):
        resposta["text"] = "Você acertou!"
    else:
        resposta["text"] = "Você errou!"

janela = tk.Tk(className='Jogo do Milhão')

pergunta = tk.Label(master=janela,
                    text = f"{questao[0]}",
                    height = 10,
                    width = 80)
pergunta.grid(row=0, column=0, columnspan = 2, padx=1, pady=2)

resposta = tk.Label(master=janela,
                    text = " ",
                    height = 10,
                    width = 80)
resposta.grid(row=4, column=0, columnspan = 2, padx=1, pady=2)

button0 = tk.Button(text=f"{respAL[0]}", command= lambda: clique_botao(0), height = 3, width = 30)
button0.grid(row=1, column=0, padx=5, pady=5)

button1 = tk.Button(text=f"{respAL[1]}", command= lambda: clique_botao(1), height = 3, width = 30)
button1.grid(row=1, column=1, padx=5, pady=5)

button2 = tk.Button(text=f"{respAL[2]}", command= lambda: clique_botao(2), height = 3, width = 30)
button2.grid(row=2, column=0, padx=5, pady=5)

button3 = tk.Button(text=f"{respAL[3]}", command= lambda: clique_botao(3), height = 3, width = 30)
button3.grid(row=2, column=1, padx=5, pady=5)

button4 = tk.Button(text=f"Jogar novamente", command= lambda: clique_botao(4), height = 3, width = 30)
button4.grid(row=3, column=1, padx=2, pady=2)

janela.mainloop()
