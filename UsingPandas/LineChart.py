##############################################################################
#
# An example of converting a Pandas dataframe to an xlsx file with a line
# chart using Pandas and XlsxWriter.
#
# Copyright 2013-2017, John McNamara, jmcnamara@cpan.org
#

import pandas as pd
import random

# Create some sample data to plot.
max_row     = 21
categories  = ['Node 1', 'Node 2', 'Node 3', 'Node 4']
index_1     = range(0, max_row, 1)
multi_iter1 = {'index': index_1}

for category in categories:
    multi_iter1[category] = [random.randint(10, 100) for x in index_1]

# Create a Pandas dataframe from the data.
index_2 = multi_iter1.pop('index')
df      = pd.DataFrame(multi_iter1, index=index_2)
df      = df.reindex(columns=sorted(df.columns))

# Create a Pandas Excel writer using XlsxWriter as the engine.
sheet_name = 'Sheet1'
writer     = pd.ExcelWriter('pandas_chart_line.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name=sheet_name)

# Access the XlsxWriter workbook and worksheet objects from the dataframe.
workbook  = writer.book
worksheet = writer.sheets[sheet_name]

# Create a chart object.
chart = workbook.add_chart({'type': 'line'})

# Configure the series of the chart from the dataframe data.
for i in range(len(categories)):
    col = i + 1
    chart.add_series({
        'name':       ['Sheet1', 0, col],
        'categories': ['Sheet1', 1, 0,   max_row, 0],
        'values':     ['Sheet1', 1, col, max_row, col],
    })

# Configure the chart axes.
chart.set_x_axis({'name': 'Index'})
chart.set_y_axis({'name': 'Value', 'major_gridlines': {'visible': False}})

# Insert the chart into the worksheet.
worksheet.insert_chart('G2', chart)

# Close the Pandas Excel writer and output the Excel file.
writer.save()

#------------------- 2nd part experiments

import pandas as pd
import random

# Create some sample data to plot.
max_row     = 30
categories  = ['Janna', 'Mallory', 'Sasha', 'Sarah']
index_1     = range(0, max_row, 1) # there will be 50 rows
multi_iter1 = {'index': index_1} # creates a column named 'index' with 50 rows

for category in categories:
    multi_iter1[category] = [random.randint(1, 25) for x in index_1] # create a random number for each category 50 times

# Create a Pandas dataframe from the data.
index_2 = multi_iter1.pop('index')
df      = pd.DataFrame(multi_iter1, index=index_2)
df      = df.reindex(columns=sorted(df.columns))

# Create a Pandas Excel writer using XlsxWriter as the engine.
sheet_name = 'Chart1'
chart_name = 'Chart2' # name an extra sheet
writer     = pd.ExcelWriter('MyChart_lines.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name=sheet_name)
df.to_excel(writer, sheet_name=chart_name) # create an extra sheet using the dataframe

# Access the XlsxWriter workbook and worksheet objects from the dataframe.
workbook  = writer.book
worksheet = writer.sheets[sheet_name]
worksheet2 = writer.sheets[chart_name] 

# Create a chart object.
chart  = workbook.add_chart({'type': 'line'})
chart1 = workbook.add_chart({'type': 'column'}) #create another chart object


# Configure the series of the chart from the dataframe data.
for i in range(len(categories)):
    col = i + 1
    chart.add_series({
        'name':       ['Chart1', 0, col],
        'categories': ['Chart1', 1, 0,   max_row, 0],
        'values':     ['Chart1', 1, col, max_row, col],
    })

# Configure the series of the chart1 from the dataframe data.
for i in range(len(categories)):
    col = i + 1
    chart1.add_series({
        'name':       ['Chart2', 0, col],
        'categories': ['Chart2', 1, 0,   max_row, 0],
        'values':     ['Chart2', 1, col, max_row, col],
    })

# Configure the chart axes.
chart.set_x_axis({'name': 'Index'})
chart.set_y_axis({'name': 'Value', 'major_gridlines': {'visible': False}})
chart1.set_x_axis({'name': 'X-Axis'}) #configure chart1
chart1.set_y_axis({'name': 'Y-Axis'}) #configure chart1

# Insert the chart into the worksheet.
worksheet.insert_chart('G2', chart)
worksheet2.insert_chart('G2', chart1) #insert chart1 chart

# Close the Pandas Excel writer and output the Excel file.
writer.save()
