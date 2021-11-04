// import a greet_user method
frappe.require([
    '/assets/custom_app/js/example.js',
]);

// create a custom btn on patient appointment list
frappe.listview_settings['Patient Appointment'] = {
	onload: function(listview) {
		listview.page.add_menu_item(__("HAPPY:D "), function() {
			greet_user()
		});
	}
};


// frappe.listview_settings["Patient Appointment"] = {

// 	onload: function(listview) {
// 		this.add_button([button_name], "default", function() { /*actions*/ })
// 	},

// 	add_button(name, type, action, wrapper_class=".page-actions") {
// 		const button = document.createElement("button");
// 		button.classList.add("btn", "btn-" + type, "btn-sm", "ml-2");
// 		button.innerHTML = name;
// 		button.onclick = action;
// 		document.querySelector(wrapper_class).prepend(button);
// 	},
// };
// frappe.listview_settings['Patient Appointment'] = {
//     // add fields to fetch
//     add_fields: ['title', 'public'],
//     // set default filters
//     // filters: [
//     //     ['Hospital', '=', "B Hospital"]
//     // ],
//     hide_name_column: true, // hide the last column which shows the `name`
//     onload(listview) {
//         // triggers once before the list is loaded
//     },
//     before_render() {
//         // triggers before every render of list records
//     },
//     get_indicator(doc) {
//         // customize indicator color
//         if (doc.public) {
//             return [__("Public"), "green", "public,=,Yes"];
//         } else {
//             return [__("Private"), "darkgrey", "public,=,No"];
//         }
//     },
//     primary_action() {
//         // triggers when the primary action is clicked
//     },
//     get_form_link(doc) {
//         // override the form route for this doc
//     },
//     // add a custom button for each row
//     button: {
//         show(doc) {
//             return doc.reference_name;
//         },
//         get_label() {
//             return 'View';
//         },
//         get_description(doc) {
//             return __('View {0}', [`${doc.reference_type} ${doc.reference_name}`])
//         },
//         action(doc) {
//             frappe.set_route('Form', doc.reference_type, doc.reference_name);
//         }
//     },
//     // format how a field value is shown
//     formatters: {
//         title(val) {
//             return val.bold();
//         },
//         public(val) {
//             return val ? 'Yes' : 'No';
//         }
//     }
// }