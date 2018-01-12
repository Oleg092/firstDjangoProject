function show(selector) {//function can replace tables and buttons
	if (selector == 1) {
		$("#tableDepartment").css("display", "none");
		$("#tablePeople").css("display", "table");
		$("#buttonAddDepartment").css("display", "none");
		$("#buttonAddPeople").css("display", "table");

	}
	if (selector == 2) {
		$("#tablePeople").css("display", "none");
		$("#tableDepartment").css("display", "table");
		$("#buttonAddPeople").css("display", "none");
		$("#buttonAddDepartment").css("display", "table");
	}
}
function sleep(millis) {
    var t = (new Date()).getTime();
    var i = 0;
    while (((new Date()).getTime() - t) < millis) {
        i++;
    }
}
function cleanForm(){
	//написать функцию очистки форм, шоб после отправки они были пустыми
}