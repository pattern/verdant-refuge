$(function() {
  $('span.timeago').each(function () {
    var date = new Date($(this).attr('title'));
    var timeago = $.timeago(date);
    $(this).html(timeago);
  });
  $('time.timeago').timeago();
});
