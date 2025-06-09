
# As bibliotecas Tkinter e Threading foram  descobertas por conversa com IA
import tkinter as tk
from tkinter import ttk
import random
import time
import threading


QUANTUM = 2 

 
PROCESSOS_BASE = [
    {"nome": "Usain Bolt", "tempo_total": random.randint(5, 10)},
    {"nome": "Jesse Owens", "tempo_total": random.randint(5, 10)},
    {"nome": "Paavo Nurmi", "tempo_total": random.randint(5, 10)},
    {"nome": "Carl Lewis", "tempo_total": random.randint(5, 10)},
    {"nome": "Mo Farah", "tempo_total": random.randint(5, 10)},
]


class CorridaGUI:

    
    def __init__(self, root):
        self.root = root
        self.root.title("Corrida dos Processos ")
        self.root.geometry("600x500")
        self.processos = []
        self.progressos = []
        self.labels = []
        self.politica = tk.StringVar(value="FIFO")
        self.criar_interface()

    
    def criar_interface(self):

        
        tk.Label(self.root, text="Escolha a política de escalonamento:", font=("Arial", 12)).pack(pady=10)
        tk.Radiobutton(self.root, text="FIFO", variable=self.politica, value="FIFO").pack()
        tk.Radiobutton(self.root, text="Round Robin", variable=self.politica, value="RR").pack()

        
        self.btn_iniciar = tk.Button(self.root, text="Iniciar Corrida", command=self.iniciar_corrida)
        self.btn_iniciar.pack(pady=10)

        
        self.frame_corrida = tk.Frame(self.root)
        self.frame_corrida.pack(pady=10)

        
        self.resultado_label = tk.Label(self.root, text="", font=("Arial", 14, "bold"))
        self.resultado_label.pack(pady=10)

        
        self.btn_reiniciar = tk.Button(self.root, text="Reiniciar", command=self.reiniciar, state="disabled")
        self.btn_reiniciar.pack(pady=5)

     
    def setup_corrida(self):

        
        self.processos.clear()
        for widget in self.frame_corrida.winfo_children():
            widget.destroy()
        self.progressos.clear()
        self.labels.clear()

        
        for p in PROCESSOS_BASE:
            processo = {
                "nome": p["nome"],
                "tempo_total": p["tempo_total"],
                "executado": 0,
                "concluido": False
            }


            # A barra de progressão foi feita com ajuda do ChatGPT
            self.processos.append(processo)

            label = tk.Label(self.frame_corrida, text=f"{p['nome']} (0/{p['tempo_total']})")
            label.pack()
            self.labels.append(label)

            pb = ttk.Progressbar(self.frame_corrida, maximum=p["tempo_total"], length=400)
            pb.pack(pady=2)
            self.progressos.append(pb)

    
    def atualizar_interface(self):
        for i, processo in enumerate(self.processos):
            self.labels[i].config(text=f"{processo['nome']} ({processo['executado']}/{processo['tempo_total']})")
            self.progressos[i]["value"] = processo["executado"]

    
    def iniciar_corrida(self):
        self.resultado_label.config(text="")
        self.btn_iniciar.config(state="disabled")
        self.btn_reiniciar.config(state="disabled")
        self.setup_corrida()
        threading.Thread(target=self.executar_corrida).start()

    
    def executar_corrida(self):
        if self.politica.get() == "FIFO":
            self.executar_fifo()
        elif self.politica.get() == "RR":
            self.executar_round_robin()

       
        vencedor = min(self.processos, key=lambda p: p["executado"])
        self.resultado_label.config(text=f"🏆 Vencedor: {vencedor['nome']} com {vencedor['executado']} unidades de CPU!")
        self.btn_reiniciar.config(state="normal")

    
    def executar_fifo(self):
        for processo in self.processos:
            while processo["executado"] < processo["tempo_total"]:
                processo["executado"] += 1
                self.atualizar_interface()
                time.sleep(0.2)
            processo["concluido"] = True

    
    def executar_round_robin(self):
        while any(not p["concluido"] for p in self.processos):
            for processo in self.processos:
                if processo["concluido"]:
                    continue
                for _ in range(QUANTUM):
                    if processo["executado"] < processo["tempo_total"]:
                        processo["executado"] += 1
                        self.atualizar_interface()
                        time.sleep(0.2)
                if processo["executado"] >= processo["tempo_total"]:
                    processo["concluido"] = True

    
    def reiniciar(self):
        
        for i, p in enumerate(PROCESSOS_BASE):
            p["tempo_total"] = random.randint(5, 10)
        self.resultado_label.config(text="")
        self.iniciar_corrida()



root = tk.Tk()

app = CorridaGUI(root)

root.mainloop()
