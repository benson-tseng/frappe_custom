# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils.dashboard import cache_source

@frappe.whitelist()
@cache_source
def get(chart_name = None, chart = None, no_cache = None, filters = None, from_date = None,
	to_date = None, timespan = None, time_interval = None, heatmap_year = None):
	return {
		'labels': ['A診間','B診間','C診間','D診間','E診間'],
		'datasets': [
			{
				'name': 'load',
				'values': [110,22,331,81,57]
			}
		]
	}