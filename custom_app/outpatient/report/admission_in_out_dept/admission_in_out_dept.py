# Copyright (c) 2013, aaa and contributors
# For license information, please see license.txt

from custom_app.outpatient.report.admission_in_out_report.admission_in_out_report import get_chart
import frappe

data_type = ''

monthAry = ["jan", "feb", "mar", "apr", "may",
            "june", "july", "aug", "sep", "oct", "nov", "dec"]

monthUpAry = ["Jan.", "Feb.", "Mar.", "Apr.", "May.",
              "June.", "July.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]


def query(fltr):

    global years, data_type
    if 'in_out_dept' in fltr.keys() and fltr['in_out_dept'] == "in_dept":
        data_type = 'in_dept'
        data = frappe.db.get_list(
            'Admission', fields=['in_dept', 'instructions_code'])
    else:
        data_type = 'out_dept'
        data = frappe.db.get_list(
            'Admission', fields=['out_dept', 'instructions_code'])

    return data


def get_columns(fltr):
    columns = []

    columns.append({
        "fieldname": "dept",
        "fieldtype": "Data",
        "label": "Department",
        "width": 100
    })
    columns.append({
        "fieldname": "val",
        "fieldtype": "Data",
        "label": "Value",
        "width": 100
    })

    return columns


def get_data(fltr, query):
    return_data = []
    if 'dept' in fltr:
        fltr_data = []
        instructions_code = []
        instructions_val = []
        for i in query:
            if i[data_type] == fltr['dept']:
                fltr_data.append(i)
        for i in fltr_data:
            if i['instructions_code'] in instructions_code:
                instructions_val[instructions_code.index(
                    i['instructions_code'])] += 1
            else:
                instructions_code.append(i['instructions_code'])
                instructions_val.append(1)
        for i in range(len(instructions_code)):
            return_data.append(
                {'dept': instructions_code[i], 'val': instructions_val[i]})
    else:
        dept_name_data = frappe.db.get_list('Hospital Dept')
        dept_ary = []
        dept_data = []
        for i in dept_name_data:
            dept_ary.append(i['name'])
            dept_data.append(0)
        for i in query:
            if i[data_type] != None:
                dept_data[dept_ary.index(i[data_type])] += 1
        for i in range(len(dept_data)):
            return_data.append({'dept': dept_ary[i], 'val': dept_data[i]})

    return return_data


def get_chart(fltr, query):
    dept_name_data = frappe.db.get_list('Hospital Dept')
    dept_ary = []
    dept_data = []
    for i in dept_name_data:
        dept_ary.append(i['name'])
        dept_data.append(0)
    if 'dept' in fltr:
        fltr_data = []
        instructions_code = []
        instructions_val = []
        for i in query:
            if i[data_type] == fltr['dept']:
                fltr_data.append(i)
        for i in fltr_data:
            if i['instructions_code'] in instructions_code:
                instructions_val[instructions_code.index(
                    i['instructions_code'])] += 1
            else:
                instructions_code.append(i['instructions_code'])
                instructions_val.append(1)
        datasets = [{'name': 'name', 'values': instructions_val}]
        chart = {
            'data': {
                'labels': instructions_code,
                'datasets': datasets,
                'chartType': 'bar'
            },
            'type': 'bar'
        }
    else:
        for i in query:
            if i[data_type] != None:
                dept_data[dept_ary.index(i[data_type])] += 1
        datasets = [{'name': 'test', 'values': dept_data}]
        frappe.logger().debug(datasets)
        chart = {
            'data': {
                'labels': dept_ary,
                'datasets': datasets,
                'chartType': 'pie'
            },
            'type': 'pie'
        }
    return chart


def execute(filters=None):
    query_result = query(filters)
    chart = get_chart(filters, query_result)
    message = "HDEN:d"
    columns = get_columns(filters)
    data = get_data(filters, query_result)
    return columns, data, message, chart
