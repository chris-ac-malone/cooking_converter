import tkinter as tk
from tkinter import *
from tkinter import ttk
'''''''''''''''''''''''''''
Author: Chris Malone
Programming with Functions
Brother Comeau
'''''''''''''''''''''''''''
'''''''''''''''''''''''''''
This program converts various measurements
between each other using a single convert
function that draws information from a
dictionary. It is all done in a tkinter 
window. There are no testing functions as
I couldn't get them to work with tkinter. 
'''''''''''''''''''''''''''

'''
This is a dictionary that contains all of the
conversion factors that are possible in the
program. The keys are based on the convert
function below that takes in the Comboboxes'
values and combines them. 
'''
conversion_factors={
    # Done
    "US Cups US Cups":1,
    "US Cups US Teaspoons":48,
    "US Cups US Tablespoons":16,
    "US Cups US Gallons":0.0625,
    "US Cups US Quarts":0.25,
    "US Cups US Pints":0.5,
    "US Cups US Fluid Oz":8,
    "US Cups Liters":0.236588,
    "US Cups Milliliters":236.588,
    "US Cups Imperial Cups":0.832674,
    "US Cups Imperial Teaspoons":39.9683,
    "US Cups Imperial Tablespoons":13.3228,
    "US Cups Imperial Gallons":0.0520421,
    "US Cups Imperial Quarts":0.208169,
    "US Cups Imperial Pints":0.416337,
    "US Cups Imperial Fluid Oz":8.32674,
    # Done
    "US Teaspoons US Cups":0.0208333,
    "US Teaspoons US Teaspoons":1,
    "US Teaspoons US Tablespoons":0.333333,
    "US Teaspoons US Gallons":0.00130208,
    "US Teaspoons US Quarts":0.00530833,
    "US Teaspoons US Pints":0.0104167,
    "US Teaspoons US Fluid Oz":0.166667,
    "US Teaspoons Liters":0.00492892,
    "US Teaspoons Milliliters":4.92892,
    "US Teaspoons Imperial Cups":0.0173474,
    "US Teaspoons Imperial Teaspoons":0.832674,
    "US Teaspoons Imperial Tablespoons":0.277558,
    "US Teaspoons Imperial Gallons":0.00108421,
    "US Teaspoons Imperial Quarts":0.00433684,
    "US Teaspoons Imperial Pints":0.00867369,
    "US Teaspoons Imperial Fluid Oz":0.173474,
    # Done
    "US Tablespoons US Cups":0.0625,
    "US Tablespoons US Teaspoons":3,
    "US Tablespoons US Tablespoons":1,
    "US Tablespoons US Gallons":0.00390625,
    "US Tablespoons US Quarts":0.015625,
    "US Tablespoons US Pints":0.03125,
    "US Tablespoons US Fluid Oz":0.5,
    "US Tablespoons Liters":0.0147868,
    "US Tablespoons Milliliters":14.7868,
    "US Tablespoons Imperial Cups":0.0520421,
    "US Tablespoons Imperial Teaspoons":2.49802,
    "US Tablespoons Imperial Tablespoons":0.832674,
    "US Tablespoons Imperial Gallons":0.00325263,
    "US Tablespoons Imperial Quarts":0.0130105,
    "US Tablespoons Imperial Pints":0.0260211,
    "US Tablespoons Imperial Fluid Oz":0.520421,
    # Done
    "US Gallons US Cups":16,
    "US Gallons US Teaspoons":768,
    "US Gallons US Tablespoons":256,
    "US Gallons US Gallons":1,
    "US Gallons US Quarts":4,
    "US Gallons US Pints":8,
    "US Gallons US Fluid Oz":128,
    "US Gallons Liters":3.78541,
    "US Gallons Milliliters":3785.41,
    "US Gallons Imperial Cups":13.3228,
    "US Gallons Imperial Teaspoons":639.494,
    "US Gallons Imperial Tablespoons":213.165,
    "US Gallons Imperial Gallons":0.832674,
    "US Gallons Imperial Quarts":3.3307,
    "US Gallons Imperial Pints":6.66139,
    "US Gallons Imperial Fluid Oz":133.228,
    # Done
    "US Quarts US Cups":4,
    "US Quarts US Teaspoons":192,
    "US Quarts US Tablespoons":64,
    "US Quarts US Gallons":0.25,
    "US Quarts US Quarts":1,
    "US Quarts US Pints":2,
    "US Quarts US Fluid Oz":32,
    "US Quarts Liters":0.946353,
    "US Quarts Milliliters":946.353,
    "US Quarts Imperial Cups":3.3307,
    "US Quarts Imperial Teaspoons":159.873,
    "US Quarts Imperial Tablespoons":53.2911,
    "US Quarts Imperial Gallons":0.208169,
    "US Quarts Imperial Quarts":0.832674,
    "US Quarts Imperial Pints":1.66535,
    "US Quarts Imperial Fluid Oz":33.307,
    # Done
    "US Pints US Cups":2,
    "US Pints US Teaspoons":96,
    "US Pints US Tablespoons":32,
    "US Pints US Gallons":0.125,
    "US Pints US Quarts":0.5,
    "US Pints US Pints":1,
    "US Pints US Fluid Oz":16,
    "US Pints Liters":0.473176,
    "US Pints Milliliters":437.176,
    "US Pints Imperial Cups":1.66535,
    "US Pints Imperial Teaspoons":79.9367,
    "US Pints Imperial Tablespoons":26.6456,
    "US Pints Imperial Gallons":0.04084,
    "US Pints Imperial Quarts":0.416337,
    "US Pints Imperial Pints":0.832674,
    "US Pints Imperial Fluid Oz":16.6535,
    # Done
    "US Fluid Oz US Cups":0.125,
    "US Fluid Oz US Teaspoons":6,
    "US Fluid Oz US Tablespoons":2,
    "US Fluid Oz US Gallons":0.0078125,
    "US Fluid Oz US Quarts":0.03125,
    "US Fluid Oz US Pints":0.0625,
    "US Fluid Oz US Fluid Oz":1,
    "US Fluid Oz Liters":0.0295735,
    "US Fluid Oz Milliliters":29.5735,
    "US Fluid Oz Imperial Cups":0.04084,
    "US Fluid Oz Imperial Teaspoons":4.99604,
    "US Fluid Oz Imperial Tablespoons":1.66535,
    "US Fluid Oz Imperial Gallons":0.00650527,
    "US Fluid Oz Imperial Quarts":0.0260211,
    "US Fluid Oz Imperial Pints":0.0520421,
    "US Fluid Oz Imperial Fluid Oz":1.04084,
    # Done
    "Liters US Cups":4.22675,
    "Liters US Teaspoons":202.884,
    "Liters US Tablespoons":67.628,
    "Liters US Gallons":0.264172,
    "Liters US Quarts":1.05669,
    "Liters US Pints":2.11338,
    "Liters US Fluid Oz":33.814,
    "Liters Liters":1,
    "Liters Milliliters":1000,
    "Liters Imperial Cups":3.51951,
    "Liters Imperial Teaspoons":168.936,
    "Liters Imperial Tablespoons":56.3121,
    "Liters Imperial Gallons":0.219969,
    "Liters Imperial Quarts":0.879877,
    "Liters Imperial Pints":1.75975,
    "Liters Imperial Fluid Oz":33.814,
    # Done
    "Milliliters US Cups":0.00422675,
    "Milliliters US Teaspoons":0.202884,
    "Milliliters US Tablespoons":0.067628,
    "Milliliters US Gallons":0.000264172,
    "Milliliters US Quarts":0.00105669,
    "Milliliters US Pints":0.00211338,
    "Milliliters US Fluid Oz":0.033814,
    "Milliliters Liters":0.001,
    "Milliliters Milliliters":1,
    "Milliliters Imperial Cups":0.00351951,
    "Milliliters Imperial Teaspoons":0.168936,
    "Milliliters Imperial Tablespoons":0.0563121,
    "Milliliters Imperial Gallons":0.000219969,
    "Milliliters Imperial Quarts":0.000879877,
    "Milliliters Imperial Pints":0.00175975,
    "Milliliters Imperial Fluid Oz":0.0351951,
    # Done
    "Imperial Cups US Cups":1.20095,
    "Imperial Cups US Teaspoons":57.6456,
    "Imperial Cups US Tablespoons":19.2152,
    "Imperial Cups US Gallons":0.0750594,
    "Imperial Cups US Quarts":0.300237,
    "Imperial Cups US Pints":0.600475,
    "Imperial Cups US Fluid Oz":9.6076,
    "Imperial Cups Liters":0.284131,
    "Imperial Cups Milliliters":284.131,
    "Imperial Cups Imperial Cups":1,
    "Imperial Cups Imperial Teaspoons":48,
    "Imperial Cups Imperial Tablespoons":16,
    "Imperial Cups Imperial Gallons":0.0625,
    "Imperial Cups Imperial Quarts":0.25,
    "Imperial Cups Imperial Pints":0.5,
    "Imperial Cups Imperial Fluid Oz":10,
    # Done
    "Imperial Teaspoons US Cups":0.0250198,
    "Imperial Teaspoons US Teaspoons":1.20095,
    "Imperial Teaspoons US Tablespoons":0.400317,
    "Imperial Teaspoons US Gallons":0.00156374,
    "Imperial Teaspoons US Quarts":0.00625495,
    "Imperial Teaspoons US Pints":0.0125099,
    "Imperial Teaspoons US Fluid Oz":0.200158,
    "Imperial Teaspoons Liters":0.00591939,
    "Imperial Teaspoons Milliliters":5.91939,
    "Imperial Teaspoons Imperial Cups":0.0208333,
    "Imperial Teaspoons Imperial Teaspoons":1,
    "Imperial Teaspoons Imperial Tablespoons":0.333333,
    "Imperial Teaspoons Imperial Gallons":0.00130208,
    "Imperial Teaspoons Imperial Quarts":0.00520834,
    "Imperial Teaspoons Imperial Pints":0.0104167,
    "Imperial Teaspoons Imperial Fluid Oz":0.208333,
    # Done
    "Imperial Tablespoons US Cups":0.0750594,
    "Imperial Tablespoons US Teaspoons":3.60285,
    "Imperial Tablespoons US Tablespoons":1.20095,
    "Imperial Tablespoons US Gallons":0.00469121,
    "Imperial Tablespoons US Quarts":0.0187649,
    "Imperial Tablespoons US Pints":0.0375297,
    "Imperial Tablespoons US Fluid Oz":0.600475,
    "Imperial Tablespoons Liters":0.0177582,
    "Imperial Tablespoons Milliliters":17.7582,
    "Imperial Tablespoons Imperial Cups":0.0625,
    "Imperial Tablespoons Imperial Teaspoons":3,
    "Imperial Tablespoons Imperial Tablespoons":1,
    "Imperial Tablespoons Imperial Gallons":0.00390625,
    "Imperial Tablespoons Imperial Quarts":0.015625,
    "Imperial Tablespoons Imperial Pints":0.03125,
    "Imperial Tablespoons Imperial Fluid Oz":0.625,
    # Done
    "Imperial Gallons US Cups":19.2152,
    "Imperial Gallons US Teaspoons":922.33,
    "Imperial Gallons US Tablespoons":307.443,
    "Imperial Gallons US Gallons":1.20095,
    "Imperial Gallons US Quarts":4.8038,
    "Imperial Gallons US Pints":9.6076,
    "Imperial Gallons US Fluid Oz":153.722,
    "Imperial Gallons Liters":4.54609,
    "Imperial Gallons Milliliters":4546.09,
    "Imperial Gallons Imperial Cups":16,
    "Imperial Gallons Imperial Teaspoons":768,
    "Imperial Gallons Imperial Tablespoons":256,
    "Imperial Gallons Imperial Gallons":1,
    "Imperial Gallons Imperial Quarts":4,
    "Imperial Gallons Imperial Pints":8,
    "Imperial Gallons Imperial Fluid Oz":160,
    # Done
    "Imperial Quarts US Cups":4.8038,
    "Imperial Quarts US Teaspoons":230.582,
    "Imperial Quarts US Tablespoons":76.8608,
    "Imperial Quarts US Gallons":0.300237,
    "Imperial Quarts US Quarts":1.20095,
    "Imperial Quarts US Pints":2.4019,
    "Imperial Quarts US Fluid Oz":38.4304,
    "Imperial Quarts Liters":1.13652,
    "Imperial Quarts Milliliters":1136.52,
    "Imperial Quarts Imperial Cups":4,
    "Imperial Quarts Imperial Teaspoons":192,
    "Imperial Quarts Imperial Tablespoons":64,
    "Imperial Quarts Imperial Gallons":0.25,
    "Imperial Quarts Imperial Quarts":1,
    "Imperial Quarts Imperial Pints":2,
    "Imperial Quarts Imperial Fluid Oz":40,
    # Done
    "Imperial Pints US Cups":2.409,
    "Imperial Pints US Teaspoons":115.291,
    "Imperial Pints US Tablespoons":38.4304,
    "Imperial Pints US Gallons":0.150119,
    "Imperial Pints US Quarts":0.600475,
    "Imperial Pints US Pints":1.20095,
    "Imperial Pints US Fluid Oz":19.2152,
    "Imperial Pints Liters":0.568261,
    "Imperial Pints Milliliters":568.261,
    "Imperial Pints Imperial Cups":2,
    "Imperial Pints Imperial Teaspoons":96,
    "Imperial Pints Imperial Tablespoons":32,
    "Imperial Pints Imperial Gallons":0.125,
    "Imperial Pints Imperial Quarts":0.5,
    "Imperial Pints Imperial Pints":1,
    "Imperial Pints Imperial Fluid Oz":20,
    # FREAKING DONE
    "Imperial Fluid Oz US Cups":0.120095,
    "Imperial Fluid Oz US Teaspoons":5.76456,
    "Imperial Fluid Oz US Tablespoons":1.92152,
    "Imperial Fluid Oz US Gallons":0.00750594,
    "Imperial Fluid Oz US Quarts":0.0300237,
    "Imperial Fluid Oz US Pints":0.0600475,
    "Imperial Fluid Oz US Fluid Oz":0.96076,
    "Imperial Fluid Oz Liters":0.0284131,
    "Imperial Fluid Oz Milliliters":28.4131,
    "Imperial Fluid Oz Imperial Cups":0.1,
    "Imperial Fluid Oz Imperial Teaspoons":4.8,
    "Imperial Fluid Oz Imperial Tablespoons":1.6,
    "Imperial Fluid Oz Imperial Gallons":0.00625,
    "Imperial Fluid Oz Imperial Quarts":0.025,
    "Imperial Fluid Oz Imperial Pints":0.05,
    "Imperial Fluid Oz Imperial Fluid Oz":1
}

'''
The create_application function is where the window
and widgets are created. The Comboboxes' values are
where the convert function's keys come from. 
'''
def create_application():
    root = tk.Tk()

    root.winfo_toplevel().title("Kitchen Conversions")

    root.resizable(height=0, width=0)

    root.title = tk.Label(text="Kitchen Conversions")

    root.convert_from = ttk.Combobox(root, values=[
        "US Cups",
        "US Teaspoons",
        "US Tablespoons",
        "US Gallons",
        "US Quarts",
        "US Pints",
        "US Fluid Oz",
        "Liters",
        "Milliliters",
        "Imperial Cups",
        "Imperial Teaspoons",
        "Imperial Tablespoons",
        "Imperial Gallons",
        "Imperial Quarts",
        "Imperial Pints",
        "Imperial Fluid Oz",
    ])

    root.lblTo = ttk.Label(text="To")

    root.convert_to = ttk.Combobox(root, values=[
        "US Cups",
        "US Teaspoons",
        "US Tablespoons",
        "US Gallons",
        "US Quarts",
        "US Pints",
        "US Fluid Oz",
        "Liters",
        "Milliliters",
        "Imperial Cups",
        "Imperial Teaspoons",
        "Imperial Tablespoons",
        "Imperial Gallons",
        "Imperial Quarts",
        "Imperial Pints",
        "Imperial Fluid Oz",
    ])

    root.amount = tk.Entry(root)

    root.answer = tk.StringVar()
    root.answer.set("Result")
    root.converted = ttk.Label(textvariable=root.answer)

    root.title.grid(row=0, column=1, sticky="n", padx=10, pady=10)

    root.convert_from.grid(row=2, column=0, padx=15)
    root.lblTo.grid(row=2, column=1, padx=20)
    root.convert_to.grid(row=2, column=2, padx=15)

    root.amount.grid(row=3, column=1, padx=10, pady=10)

    root.converted.grid(row=4, column=1, pady=30)

    return root

'''
The convert function is activated when the Comboboxes
or the Entry are changed. It gets the values from the three
fields, creates a key for the conversion_factors dict,
and multiplies the amount with the conversion factor. 
It then sets the answer label's text to the answer. 
'''
def convert(event):
    try:
        key = root.convert_from.get() + " " + root.convert_to.get()
        print(key)
        result = int(root.amount.get())*conversion_factors[key]
        if (result > 10000):
            root.answer.set("Holy crap, that's a lot of flour")
        elif (result < 0):
            root.answer.set("You must be making void muffins")
        else:
            root.answer.set(result)
        
    except ValueError:
        print("Value Error")
        root.answer.set("Invalid")

    except KeyError:
        print(f"Key Error: {key}")
        root.answer.set("Please refrain from creating new units of measurement. Thanks you.")

'''
This is where the input is caught for each input area,
and each one calls the convert function.
'''
def handle_input():
    root.convert_from.bind("<<ComboboxSelected>>", convert)
    root.convert_to.bind("<<ComboboxSelected>>", convert)
    root.amount.bind("<KeyRelease>", convert)

root = create_application()
handle_input()
root.mainloop()