frappe.provide('frappe.dashboards.chart_sources');

frappe.dashboards.chart_sources["ward_dash_source"] = {
	method: "custom_app.ward.dashboard_chart_source.ward_dash_source.ward_dash_source.get",
	filters: [
		{
			fieldname: "company",
			label: __("Company"),
			fieldtype: "Link",
			options: "Company",
			default: frappe.defaults.get_user_default("Company")
		}
	]
};