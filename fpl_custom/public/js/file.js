frappe.ui.form.on("File", {
    onload:function(frm){
        // frm.fields_dict['user'].get_query = function(doc) {
        //     return {
        //         query:"fpl_custom.docevents.file.get_users",
        //     }
        //   }
        frappe.call({
            method: "fpl_custom.docevents.file.get_users",
            callback:function(r){
                if (r.message){
                    frm.set_df_property('user', 'options', r.message.flat());
                    frm.refresh_field('user');
                }
            }
        })        

    }
})