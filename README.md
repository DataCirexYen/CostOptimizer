# How much inventory should I stock?

Inventory optimization tool to maximize profits by calculating the optimal quantity and time to order.
This code is a Streamlit app that helps in optimizing inventory by calculating the net present value of the purchase of goods. The user can input various parameters like the number of periods, average demand, unit cost, unit retail price, fixed and variable holding costs, and the discount rate.

## Parameters

**NumberOfPeriods:** The number of periods (typically months) that the inventory will be held and sold.

**AverageDemand:** The average number of units sold per period.

**UCost:** The unit cost of each item in the inventory.

**URetailPrice:** The unit retail price of each item in the inventory.

**FixedHoldingCost:** The fixed cost of holding the inventory for the entire period.

**VariableHoldingCost:** The variable cost of holding the inventory, which depends on the number of units held.

**UDiscount:** The discount offered for buying the inventory in bulk or for buying it up front.

## Running the Streamlit app
Installation
To run the code, make sure that you have installed the required packages - Streamlit and numpy_financial. 

To run the app, use the following command:
```
*streamlit run STFIN.py*
```
![image](https://user-images.githubusercontent.com/98498927/235366390-55888acc-acf9-4287-bc42-9ffd3a428c32.png)



