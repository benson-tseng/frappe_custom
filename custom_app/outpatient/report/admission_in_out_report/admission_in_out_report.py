# Copyright (c) 2013, aaa and contributors
# For license information, please see license.txt

from typing import Collection
import frappe

monthAry = ["jan", "feb", "mar", "apr", "may",
            "june", "july", "aug", "sep", "oct", "nov", "dec"]

monthUpAry = ["Jan.", "Feb.", "Mar.", "Apr.", "May.",
              "June.", "July.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]

years = []

data_type = ''


def query(fltr):

    global years, data_type
    if 'in_out_date' in fltr.keys() and fltr['in_out_date'] == "in_date":
        data_type = 'in_date'
        data = frappe.db.get_list('Admission', fields=['in_date'])
        years = ['2014', '2015', '2016', '2017',
                 '2018', '2019', '2020', '2021']
    else:
        data_type = 'out_date'
        data = frappe.db.get_list('Admission', fields=['out_date'])
        years = ['2018', '2019', '2020', '2021']

    return data


def get_data(data):

    countAry = []
    for i in range(len(monthUpAry)):
        tmpAry = []
        for k in range(len(years)):
            tmpAry.append(0)
        countAry.append(tmpAry)

    for i in data:
        countAry[int(i[data_type][5:7]) -
                 1][years.index(i[data_type][0:4])] += 1

    returnData = []
    for i in range(len(years)):
        returnData.append({})
    for i in range(len(countAry)):
        for k in range(len(countAry[i])):
            returnData[k][monthAry[i]] = countAry[i][k]

    for i in range(len(years)):
        returnData[i]['year'] = years[i]

    return returnData


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


def get_chart(data):
    countAry = []
    for i in range(len(years)):
        countAry.append([])

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
    chart = get_chart(data)
    return columns, data, message, chart
