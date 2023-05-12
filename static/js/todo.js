function fillform(old_task,id,old_desc,old_date) {
   
//Filling data in form
    document.getElementById('todoid').value = id;
    document.getElementById('task').value = old_task;
    document.getElementById('date').value = convert_Date(old_date);
    document.getElementById('description').value = old_desc;
    document.getElementById('submit').value = "Update";
    function convert_Date(old_date){
        var dateStr = old_date;
        var date = new Date(dateStr);
        var year = date.getFullYear();
        var month = ('0' + (date.getMonth() + 1)).slice(-2);
        var day = ('0' + date.getDate()).slice(-2);

        // Return the formatted date string
        return year + '-' + month + '-' + day;

    }
}
