import streamlit as st
from Blockchain import Blockchain
from Utils import Utils

def show_alert(message, alert_type='info'):
    if alert_type == 'info':
        st.info(message)
    elif alert_type == 'success':
        st.success(message)
    elif alert_type == 'warning':
        st.warning(message)
    elif alert_type == 'error':
        st.error(message)


class Transacao:
    # def __init__(self):
    #     blockchain = Blockchain(4)
    blockchain = Blockchain(4)

    def fazer_transacao(self):           
        escolha = st.selectbox("Escolha o tipo de transação:", ["Saque", "Depósito"], key="transacao_select")
        with st.form('Transaction'):
            value = ''
            if escolha == "Saque":
                st.write("Você escolheu Saque.")
                value = st.number_input("Qual o valor a ser sacado?")
            elif escolha == "Depósito":
                st.write("Você escolheu Depósito.")
                value = st.number_input("Qual o valor a ser depositado?")

            submit = st.form_submit_button('Confirmar')

        if submit:
            self.blockchain.add_block(self.blockchain.new_block(str(value)))
            show_alert("Operacão realizada.", "success")

    def visualizar_historico(self):
        st.table(self.blockchain.blockchain_to_dict())



    def pesquisar_transacao(self):
        text = st.text_input("Qual transação deseja visualizar?")
        contem_transacao = Utils.contains_block(self.blockchain, text)
        if contem_transacao:
            st.write(f"A blockchain contém a transação: {text}")
        else:
            st.write(f"A blockchain não contém a transação: {text}")
