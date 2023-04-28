frappe.ui.form.on("Purchase Invoice", {
    before_save:function(frm){
            var start_date = moment(frm.doc.service_start_date).format("DD-MM-YYYY");
            var end_date = moment(frm.doc.service_end_date).format("DD-MM-YYYY");

            var msg = "Being Invoice Number " + frm.doc.bill_no+ " of " + frm.doc.supplier + " booked for period " +start_date+ ' to ' +end_date;
            frm.set_value("narration",msg);
    }
})