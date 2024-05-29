import streamlit as st
from Blockchain import Blockchain
from Utils import Utils

def blockchain_to_dataframe(blockchain):
    data = []
    for block in blockchain.chain:
        for transaction in block.transactions:
            tx_data = {
                "Block Index": block.index,
                "Sender": transaction["sender"],
                "Receiver": transaction["receiver"],
                "Amount": transaction["amount"],
                "Previous Hash": block.previous_hash
            }
            data.append(tx_data)
    return pd.DataFrame(data)


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
            st.write("Operacão realizada.")

    def visualizar_historico(self):
        st.write("Você escolheu Ver histórico.")
        st.table(self.blockchain.blockchain_to_dict())



    def pesquisar_transacao(self):
        text = st.text_input("Qual transação deseja visualizar?")
        contem_transacao = Utils.contains_block(self.blockchain, text)
        if contem_transacao:
            st.write(f"A blockchain contém a transação: {text}")
        else:
            st.write(f"A blockchain não contém a transação: {text}")
