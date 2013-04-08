$(document).ready(function () {
  $("a.tag").click(function() {
    var googleCseUrl = "http://www.google.com/cse?cx=001652393842387460493%3Aoof-xpbgn7y&ie=UTF-8&sa=Search"
    var uriEncodedTag = encodeURI($(this).text());
    var tagUrl = googleCseUrl + "&q=" + uriEncodedTag;
    window.location.href = tagUrl;
    return false;
  });
});
