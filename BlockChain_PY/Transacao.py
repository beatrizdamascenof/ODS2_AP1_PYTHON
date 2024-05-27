import streamlit as st
from Blockchain import Blockchain
from Utils import Utils

class Transacao:
    # def __init__(self):
    #     blockchain = Blockchain(4)
    blockchain = Blockchain(4)

    def fazer_transacao(self):
            
            escolha = st.selectbox("Escolha o tipo de transação:", ["Saque", "Depósito", "Ver histórico"], key="transacao_select")

            if escolha == "Saque":
                st.write("Você escolheu Saque.")
                text = st.text_input("Qual o valor a ser sacado?")
                self.blockchain.add_block(self.blockchain.new_block(""+text))
            elif escolha == "Depósito":
                st.write("Você escolheu Depósito.")
                text = st.text_input("Qual o valor a ser depositado?")
                self.blockchain.add_block(self.blockchain.new_block(""+text))
            elif escolha == "Ver histórico":
                st.write("Você escolheu Ver histórico.")
                st.write(self.blockchain)
            # elif escolha == "Sair":
            #     parada = False

    def visualizar_historico(self):
        st.write("Você escolheu Ver histórico.")
        st.write(self.blockchain)

    def pesquisar_transacao(self):
        text = st.text_input("Qual transação deseja visualizar?")
        contem_transacao = Utils.contains_block(self.blockchain, text)
        if contem_transacao:
            st.write(f"A blockchain contém a transação: {text}")
        else:
            st.write(f"A blockchain não contém a transação: {text}")
