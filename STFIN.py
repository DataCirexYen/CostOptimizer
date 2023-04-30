import streamlit as st
import numpy_financial as npf
import pandas as pd

def net_present_value(NumberOfPeriods, AverageDemand, UCost, URetailPrice, FixedHoldingCost, VariableHoldingCost, UDiscount):
    print("-------------------------------")
    total_value=0.0
    UHoldingCost=(FixedHoldingCost/AverageDemand+VariableHoldingCost)
    TotalCost=(AverageDemand*NumberOfPeriods)*(UCost*(1-UDiscount))+(AverageDemand*NumberOfPeriods*UHoldingCost)

    def Rate():
        UHoldingCost=(FixedHoldingCost/AverageDemand+VariableHoldingCost)
        TotalCostTIR=((AverageDemand*NumberOfPeriods)*(UCost))*(-1)
        CashflowTIR=((URetailPrice*AverageDemand)-UHoldingCost)
        CashflowsTIR=[TotalCostTIR]
        for n in range(0,NumberOfPeriods):
            CashflowsTIR.append(CashflowTIR)
        print(CashflowsTIR)
        irr=npf.irr(CashflowsTIR)
        return(irr)
       
    Rate=1+Rate()
    
    
    print(f"Rate+{Rate}")
    print(TotalCost)
    Cashflow=(URetailPrice*AverageDemand)
    Cashflows=[(TotalCost*-1)]

    for n in range(1,NumberOfPeriods+1):
        print(f"Elevate to+ {n}")
        total_value+=Cashflow/(Rate)**n
        print(total_value)
        Cashflows.append(Cashflow)
        
    irr=npf.irr(Cashflows)
    print(f"irr+{irr}")
    MoneyLeft=round(total_value-TotalCost)
    WLPct=total_value/TotalCost
    print(f"MoneyLeft {MoneyLeft}")
    print(f"WLPct {WLPct}")
    return irr,MoneyLeft

# create a Streamlit app
st.title("Inventory Optimization")

# define the input parameters
number_of_periods = st.slider("Numero de periodos", min_value=1, max_value=24, value=1, step=1)
average_demand = st.number_input("Cantidad de unidades compradas mensaules", value=4, step=1)
u_cost = st.number_input("Costo unitario", value=1940, step=100)
u_retail_price = st.number_input("Precio de venta unitario", value=2500, step=100)
fixed_holding_cost = st.number_input("Costos fijo (Almacenamiento, por ejemplo)", value=1000, step=100)
variable_holding_cost = st.number_input("Costo variable", value=0, step=10)
u_discount = st.slider("Descuento por comprar al contado", min_value=0.0, max_value=1.0, value=0.2, step=0.01)

min_return_perc = 0.04

# calculate the optimal quantity
value = 11
irr_arr = []
money_arr = []
quantity_arr = []

while value > min_return_perc:
    number_of_periods += 1
    npv = net_present_value(number_of_periods, average_demand, u_cost, u_retail_price, fixed_holding_cost, variable_holding_cost, u_discount)
    value = npv[0]
    money = npv[1]
    irr_arr.append(value)
    money_arr.append(money)
    quantity_arr.append(number_of_periods * average_demand)

# format the output data
irr_arr = [f"{i * 100:.1f}%" for i in irr_arr]
money_arr = [f"${i:.2f}" for i in money_arr]

data = {"Retorno Descontado": money_arr, "Porcentaje Retorno a valor presente": irr_arr, "Unidades a comprar": quantity_arr}
df = pd.DataFrame(data)

# display the output data in a table
st.write(df)