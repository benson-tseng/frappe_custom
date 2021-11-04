// Copyright (c) 2016, aaa and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Admission New"] = {
	"filters": [
		{
			fieldname: 'wardDepartment',
			label: __('Ward Department'),
			fieldtype: 'Link',
			options: 'Hospital Dept'
		}, {
			fieldname: 'years',
			label: __('Years'),
			fieldtype: 'Select',
			options: [
				{ label: __('2014'), value: '2014' },
				{ label: __('2015'), value: '2015' },
				{ label: __('2016'), value: '2016' },
				{ label: __('2017'), value: '2017' },
				{ label: __('2018'), value: '2018' },
				{ label: __('2019'), value: '2019' },
				{ label: __('2020'), value: '2020' },
				{ label: __('2021'), value: '2021' }
			]
		}
	]
};
