import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title('Jogo da Velha')
        self.jogador = 'X'
        self.tabuleiro = [['' for _ in range(3)] for _ in range(3)]
        self.botoes = [[None for _ in range(3)] for _ in range(3)]
        self.criar_menu()

    def criar_menu(self):
        self.menu = tk.Toplevel(self.root)
        self.menu.title('Menu')
        tk.Label(self.menu, text='Quem começa?', font=('Arial', 16)).pack(pady=10)
        tk.Button(self.menu, text='Jogador X', font=('Arial', 14), command=lambda: self.iniciar_jogo('X')).pack(pady=5)
        tk.Button(self.menu, text='Jogador O', font=('Arial', 14), command=lambda: self.iniciar_jogo('O')).pack(pady=5)

    def iniciar_jogo(self, jogador):
        self.jogador = jogador
        self.menu.destroy()
        self.criar_tabuleiro()

    def criar_tabuleiro(self):
        if hasattr(self, 'frame_tabuleiro'):
            self.frame_tabuleiro.destroy()
        self.frame_tabuleiro = tk.Frame(self.root)
        self.frame_tabuleiro.pack()
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.frame_tabuleiro, text='', font=('Arial', 32), width=3, height=1,
                                command=lambda i=i, j=j: self.jogada(i, j))
                btn.grid(row=i, column=j)
                self.botoes[i][j] = btn

    def jogada(self, i, j):
        if self.tabuleiro[i][j] == '' and not self.verificar_vitoria():
            self.tabuleiro[i][j] = self.jogador
            self.botoes[i][j]['text'] = self.jogador
            if self.verificar_vitoria():
                self.mostrar_fim(f'Jogador {self.jogador} venceu!')
            elif self.verificar_empate():
                self.mostrar_fim('Empate!')
            else:
                self.jogador = 'O' if self.jogador == 'X' else 'X'

    def verificar_vitoria(self):
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] != '':
                return True
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] != '':
                return True
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != '':
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != '':
            return True
        return False

    def verificar_empate(self):
        for linha in self.tabuleiro:
            if '' in linha:
                return False
        return True

    def mostrar_fim(self, mensagem):
        fim = tk.Toplevel(self.root)
        fim.title('Fim de Jogo')
        tk.Label(fim, text=mensagem, font=('Arial', 16)).pack(pady=10)
        tk.Button(fim, text='Jogar Novamente', font=('Arial', 14), command=lambda: self.reiniciar(fim)).pack(pady=5)
        tk.Button(fim, text='Sair', font=('Arial', 14), command=self.root.quit).pack(pady=5)

    def reiniciar(self, janela_fim):
        janela_fim.destroy()
        self.tabuleiro = [['' for _ in range(3)] for _ in range(3)]
        self.criar_tabuleiro()
        self.criar_menu()

def main():
    root = tk.Tk()
    jogo = JogoDaVelha(root)
    root.mainloop()

if __name__ == '__main__':
    main()
