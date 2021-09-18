# # Copyright (c) 2013, aaa and contributors
# # For license information, please see license.txt

import frappe

monthAry = ["jan", "feb", "mar", "apr", "may",
            "june", "july", "aug", "sep", "oct", "nov", "dec"]

monthUpAry = ["Jan.", "Feb.", "Mar.", "Apr.", "May.",
              "June.", "July.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]

hospital = ["A Hospital", "B Hospital", "C Hospital", "D Hospital"]


def query():
    data = frappe.db.get_list('Patient Appointment', fields=[
        'patient', 'hospital', 'department', 'date'])

    return data


def get_columns():
    columns = []

    columns.append({
        "fieldname": "hospital",
        "fieldtype": "Data",
        "label": "Hospital",
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


def get_data(data, fltr):
    fltrData = data
    if 'department' in fltr.keys():
        fltrData = []
        for i in data:
            if i['department'] == fltr['department']:
                fltrData.append(i)

    countAry = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [
        0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in fltrData:
        if i['hospital'] == "A Hospital":
            countAry[i['date'].month-1][0] += 1
        elif i['hospital'] == "B Hospital":
            countAry[i['date'].month-1][1] += 1
        elif i['hospital'] == 'C Hospital':
            countAry[i['date'].month-1][2] += 1
        elif i['hospital'] == "D Hospital":
            countAry[i['date'].month-1][3] += 1

    returnData = [{}, {}, {}, {}]

    for i in range(len(countAry)):
        for k in range(len(countAry[i])):
            returnData[k][monthAry[i]] = countAry[i][k]

    for i in range(len(hospital)):
        returnData[i]['hospital'] = hospital[i]

    return returnData


def get_chart(data, columns, fltr):

    if fltr['chartType'] == 'pie':
        countAry = []
        for i in monthAry:
            sum = []
            for k in range(4):
                sum.append(data[k][i])
            countAry.append({'name': i, 'values': sum})

        chart = {
            'data': {
                'labels': hospital,
                'datasets': countAry,
                'chartType': 'pie'
            },
            'type': 'pie'
        }

    elif fltr['chartType'] == 'line':

        countAry = [[], [], [], []]

        for i in range(len(data)):
            for m in range(len(monthAry)):
                countAry[i].append(data[i][monthAry[m]])

        datasets = []
        for i in range(len(hospital)):
            datasets.append({'name': hospital[i], 'values': countAry[i]})

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
    query_result = query()

    columns = get_columns()
    data = get_data(query_result, filters)
    message = "pie chart have bug"
    chart = get_chart(data, columns, filters)

    return columns, data, message, chart
