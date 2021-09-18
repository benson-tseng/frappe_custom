# Copyright (c) 2013, aaa and contributors
# For license information, please see license.txt

from logging import debug
import frappe
from frappe.utils.data import flt

monthAry = ["jan", "feb", "mar", "apr", "may",
            "june", "july", "aug", "sep", "oct", "nov", "dec"]

monthUpAry = ["Jan.", "Feb.", "Mar.", "Apr.", "May.",
              "June.", "July.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]

years = ['2018', '2019', '2020', '2021']


def query(fltr):
    data = frappe.db.get_list('Outpatient Record', fields=[
        'yearmonth', 'notifymainpurpose', 'drvs', 'drvsdept'])

    fltrData = data
    if 'hospitalDepartment' in fltr.keys():
        fltrData = []
        for i in data:
            if i['drvsdept'] == fltr['hospitalDepartment']:
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
        for k in range(4):
            tmpAry.append(0)
        countAry.append(tmpAry)

    for i in data:
        if i['yearmonth'][0:4] == '2018':
            countAry[int(i['yearmonth'][4:6])-1][0] += 1
        if i['yearmonth'][0:4] == '2019':
            countAry[int(i['yearmonth'][4:6])-1][1] += 1
        if i['yearmonth'][0:4] == '2020':
            countAry[int(i['yearmonth'][4:6])-1][2] += 1
        if i['yearmonth'][0:4] == '2021':
            countAry[int(i['yearmonth'][4:6])-1][3] += 1

    returnData = [{}, {}, {}, {}]
    for i in range(len(countAry)):
        for k in range(len(countAry[i])):
            returnData[k][monthAry[i]] = countAry[i][k]

    for i in range(len(years)):
        returnData[i]['year'] = years[i]

    return returnData


def get_chart(data, columns, fltr, query):
    countAry = [[], [], [], []]

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

    return chart


def execute(filters=None):
    query_result = query(filters)

    columns = get_columns()
    data = get_data(query_result)
    message = ":D"
    chart = get_chart(data, columns, filters, query_result)

    return columns, data, message, chart
