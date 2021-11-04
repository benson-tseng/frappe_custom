# Copyright (c) 2013, aaa and contributors
# For license information, please see license.txt

import frappe

fields = ['yearmonth', 'ward_dept', 'ward_code', 'sec_ward_code', 'ward_cat_code', 'sec_ward', 'ward', 'ward_chin_name',
          'bed_qua', 'date', 'bed_people', 'total_hos_people', 'hos_people', 'other_ward_people', 'in_people', 'out_people', 'out_hos_people', 'period_people']

monthAry = ["jan", "feb", "mar", "apr", "may",
            "june", "july", "aug", "sep", "oct", "nov", "dec"]

monthUpAry = ["Jan.", "Feb.", "Mar.", "Apr.", "May.",
              "June.", "July.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]


def get_data(fltr):
    data = frappe.db.get_list('Admission New', fields=fields)
    fltr_data = data
    if 'wardDepartment' in fltr:
        tmp_data = []
        for i in data:
            if i['ward_dept'] == fltr['wardDepartment']:
                tmp_data.append(i)
        fltr_data = tmp_data
    if 'years' in fltr:
        tmp_data = []
        for i in fltr_data:
            if i['yearmonth'][0:4] == fltr['years']:
                tmp_data.append(i)
        fltr_data = tmp_data
    return_data = []
    for i in fltr_data:
        tmpobj = {}
        for k in fields:
            tmpobj[k] = i[k]
        return_data.append(tmpobj)

    return return_data


def get_columns():
    columns = []
    for i in fields:
        columns.append({
            "fieldname": i,
            "fieldtype": "Data",
            "label": i,
            "width": 100
        })
    return columns


def get_chart(data, fltr):
    chart = {}
    if 'wardDepartment' in fltr and 'years' in fltr:

        datasets = [{'name': '入院人數', 'values': [0 for i in monthAry]},
                    {'name': '出院人數', 'values': [0 for i in monthAry]}]

        for i in data:

            if i['total_hos_people'] != None:
                datasets[0]['values'][int(i['yearmonth'][4:6])-1
                                      ] += int(i['total_hos_people'])

            if i['out_hos_people'] != None:
                datasets[1]['values'][int(i['yearmonth'][4:6])-1
                                      ] += int(i['out_hos_people'])

        chart = {
            'data': {
                'labels': monthUpAry,
                'datasets': datasets,
                'chartType': 'bar',
            },
            'type': 'bar',
            'colors': ['#7cd6fd', '#743ee2']
        }
    frappe.logger().debug(chart)
    return chart


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    chart = get_chart(data, filters)
    return columns, data, ":D", chart
