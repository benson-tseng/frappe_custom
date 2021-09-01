frappe.provide('frappe.dashboards.chart_sources');

frappe.dashboards.chart_sources["outpatient_dash_source"] = {
	method: "custom_app.outpatient.dashboard_chart_source.outpatient_dash_source.outpatient_dash_source.get",
	filters: [
		{
			colors: ['#7cd6fd']
		}
	],
	options:{
		colors: ['#7cd6fd']
	},
    colors: ['#7cd6fd']
};