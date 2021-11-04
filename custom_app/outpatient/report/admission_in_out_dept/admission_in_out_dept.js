// Copyright (c) 2016, aaa and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Admission In Out Dept"] = {
	"filters": [
		{
			fieldname: 'in_out_dept',
			label: __('出入院科別'),
			fieldtype: 'Select',
			options: [
				{ label: __('入院科別'), value: 'in_dept' },
				{ label: __('出院科別'), value: 'out_dept' }
			],
			default: 'in_dept'
		},
		{
			fieldname: 'dept',
			label: __('科別'),
			fieldtype: 'Link',
			options: 'Hospital Dept'
		}
	]
};
