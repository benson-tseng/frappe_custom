# Copyright (c) 2013, aaa and contributors
# For license information, please see license.txt

from logging import debug
import frappe
from frappe.utils.data import flt

monthAry = ["jan", "feb", "mar", "apr", "may",
            "june", "july", "aug", "sep", "oct", "nov", "dec"]

monthUpAry = ["Jan.", "Feb.", "Mar.", "Apr.", "May.",
              "June.", "July.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]

years = ['2016', '2017', '2018', '2019', '2020', '2021']


def query(fltr):
    data = frappe.db.get_list('Death Doc plz', fields=[
        'indate', 'pname', 'birthday', 'age', 'diagnosisengname'])

    fltrData = data
    if 'diagnosisName' in fltr.keys():
        fltrData = []
        for i in data:
            if i['diagnosisengname'] == fltr['diagnosisName']:
                fltrData.append(i)

    return fltrData


def get_columns():
    columns = []

    columns.append({
        "fieldname": "year",
        "fieldtype": "Data",
        "label": "Year",
        "width": 100
    })

    for i in range(len(monthAry)):
        columns.append({
            "fieldname": monthAry[i],
            "fieldtype": "Data",
            "label": monthUpAry[i],
            "width": 90
        })

    return columns


def get_data(data):

    countAry = []
    for i in range(12):
        tmpAry = []
        for k in range(6):
            tmpAry.append(0)
        countAry.append(tmpAry)

    for i in data:
        if i['indate'][0:4] == '2016':
            countAry[int(i['indate'][4:6])-1][0] += 1
        if i['indate'][0:4] == '2017':
            countAry[int(i['indate'][4:6])-1][1] += 1
        if i['indate'][0:4] == '2018':
            countAry[int(i['indate'][4:6])-1][2] += 1
        if i['indate'][0:4] == '2019':
            countAry[int(i['indate'][4:6])-1][3] += 1
        if i['indate'][0:4] == '2020':
            countAry[int(i['indate'][4:6])-1][4] += 1
        if i['indate'][0:4] == '2021':
            countAry[int(i['indate'][4:6])-1][5] += 1

    returnData = [{}, {}, {}, {}, {}, {}]
    for i in range(len(countAry)):
        for k in range(len(countAry[i])):
            returnData[k][monthAry[i]] = countAry[i][k]

    for i in range(len(years)):
        returnData[i]['year'] = years[i]

    return returnData


def get_chart(data, columns, fltr, query):
    if fltr['chartType'] == 'line':
        countAry = [[], [], [], [], [], []]

        for i in range(len(data)):
            for m in range(len(monthAry)):
                countAry[i].append(data[i][monthAry[m]])

        datasets = []
        for i in range(len(years)):
            datasets.append({'name': years[i], 'values': countAry[i]})

        chart = {
            'data': {
                'labels': monthUpAry,
                'datasets': datasets,
                'chartType': 'line'
            },
            'type': 'line'
        }

    elif fltr['chartType'] == 'pie':
        chart_data = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
        for i in query:
            if i['indate'][0:4] == '2016':
                tmpNum = 0
            elif i['indate'][0:4] == '2017':
                tmpNum = 1
            elif i['indate'][0:4] == '2018':
                tmpNum = 2
            elif i['indate'][0:4] == '2019':
                tmpNum = 3
            elif i['indate'][0:4] == '2020':
                tmpNum = 4
            elif i['indate'][0:4] == '2021':
                tmpNum = 5
            if int(i['age']) <= 20:
                chart_data[tmpNum][0] += 1
            elif int(i['age']) <= 40:
                chart_data[tmpNum][1] += 1
            elif int(i['age']) <= 60:
                chart_data[tmpNum][2] += 1
            elif int(i['age']) <= 80:
                chart_data[tmpNum][3] += 1
            elif int(i['age']) <= 100:
                chart_data[tmpNum][4] += 1
            else:
                chart_data[0][5] += 1
        dataSets = []
        for i in range(len(years)):
            dataSets.append({'name': years[i], 'values': chart_data[i]})
        
        frappe.logger().debug(dataSets)

        chart = {
            'data': {
                'labels': ['0-20', '21-40', '41-60', '61-80', '81-100', '100+'],
                'datasets': dataSets,
                'chartType': 'pie'
            },
            'type': 'pie'
        }

    return chart


def execute(filters=None):
    query_result = query(filters)

    columns = get_columns()
    data = get_data(query_result)
    message = "Pneumonia & pie chart have bug"
    chart = get_chart(data, columns, filters, query_result)

    return columns, data, message, chart
