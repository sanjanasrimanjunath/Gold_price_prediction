import os
import panda as pd
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open("C:/Users/sanja/OneDrive/Documents/machineLeaening/trained_model.sav", 'rb'))


def gold_prediction(input_data):
    # Get input from the user
    spx_input = float(input("Enter SPX value (between 676.53 and 2872.87): "))
    uso_input = float(input("Enter USO value (between 7.96 and 117.48): "))
    slv_input = float(input("Enter SLV value (between 8.85 and 47.26): "))
    eurusd_input = float(input("Enter EUR/USD value (between 1.04 and 1.60): "))
    
    input_data = pd.DataFrame({
        'SPX': [spx_input],
        'USO': [uso_input],
        'SLV': [slv_input],
        'EUR/USD': [eurusd_input]
    })

    # Predict the GLD price
    predicted_gld_price = loaded_model.predict(input_data)
    return predicted_gld_price

def main():
    st.tittle("Gold Prediction Web App")
    
    spx = st.text_input("SPX values")
    uso = st.text_input("USO values")
    slv = st.text_input("SLV values")
    eur_usd = st.text_input("EUR/USD values")
    
    pred = ''
    
    if st.button('Gold Prediction result'):
        pred = gold_prediction(spx,uso,slv,eur_usd)
        
    st.success(pred)
    
if __name__ == '__main__':
    main()
