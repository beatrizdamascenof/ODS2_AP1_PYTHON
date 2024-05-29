import streamlit as st
from Transacao import Transacao

class Menu:
    def __init__(self):
        self.t = Transacao()

    def abrir_menu(self):
        st.title("Caixa eletrônico")

        tabs = st.tabs(["Fazer Transação", "Histórico", "Pesquisar"])
        with tabs[0]:
                st.header("Fazer transação")
                self.t.fazer_transacao()
        with tabs[1]:
                st.header("Visualizar histórico de transações")
                self.t.visualizar_historico()
        with tabs[2]:
                st.header("Pesquisar transação")
                self.t.pesquisar_transacao()

           
