document.addEventListener('DOMContentLoaded', function() {
    //sidenav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(elems, options);
  });


  document.addEventListener("DOMContentLoaded", function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);

    // datepicker initialization
    let datepicker = document.querySelectorAll(".datepicker");
    M.Datepicker.init(datepicker, {
        format: "dd mmmm, yyyy",
        i18n: {done: "Select"}
    });

    // select initialization
    let selects = document.querySelectorAll("select");
    M.FormSelect.init(selects);


    // collapsible initializataion
    let collapsibles = document.querySelectorAll(".collapsible");  //allows for action when down caret is clicked on task
    M.Collapsible.init(collapsibles);
});


