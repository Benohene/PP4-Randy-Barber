function noSundays(date) {
  return [date.getDay() != 0, ""];
}

$(document).ready(function () {
  $(".dateinput").datepicker({
    minDate: new Date(),
    maxDate: "+31D",
    daysOfWeekHighlighted: "5,6",
    beforeShowDay: noSundays,
  });
});
