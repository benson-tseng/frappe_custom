function greet_user() {
    fetch('https://pokeapi.co/api/v2/pokemon/ditto')
        .then(function (response) {
            return response.json();
        })
        .then(function (myJson) {
            console.log(myJson);
        });
    console.log(123)
    frappe.msgprint("Hello " + frappe.session.user_fullname)
}