(function () {
    $('.slider').slick({
        cssEase: 'ease-in',
        autoplay: true,
        autoplaySpeed: 3000,
        arrows: false,
        dots: true
    });

    // get the name of uploaded file
    $('input[type="file"]').change(function () {
        var value = $("input[type='file']").val();
        $('.js-value').text(value);
    });
})();

$(".menu-collapsed").click(function () {
    $(this).toggleClass("menu-expanded");
});
