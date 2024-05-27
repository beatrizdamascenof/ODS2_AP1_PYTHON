import streamlit as st
from Transacao import Transacao

class Menu:
    def __init__(self):
        self.t = Transacao()

    def abrir_menu(self):
        st.title("Caixa eletrônico")
        choice = st.radio("Escolha uma opção:", ["Fazer transação", "Visualizar histórico de transações", "Pesquisar transação"])

        if choice == "Fazer transação":
                self.t.fazer_transacao()
        elif choice == "Visualizar histórico de transações":
                self.t.visualizar_historico()
        elif choice == "Pesquisar transação":
                self.t.pesquisar_transacao()
           
