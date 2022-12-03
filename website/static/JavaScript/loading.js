(function($) {
    $( window ).on("load", function (e) {
        $("#status").delay(2000).fadeOut(2000); //delay --> 延遲幾秒才fadeOut
        $("#preloader").delay(4000).fadeOut(1000);
      })
})(jQuery)