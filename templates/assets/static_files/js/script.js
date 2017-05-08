function OpenPopup(){
    var sblock = $('.search_drop');
    sblock.toggle(300);
}

$(document).ready(function () {
    $('.extra_menu > li:first-child').click(OpenPopup);
});

(function () {

    //// get the name of uploaded file
    //$('input[type="file"]').change(function(){
    //    var value = $("input[type='file']").val();
    //    $('.js-value').text(value);
    //});

    $('#custom-file-upload').change(function(e) {
        var filename = e.target.files[0].name;
        console.log(filename);
        $('.filupp-file-name').html(filename);
    });

    $('.menu > li > a').on('click', function () {
        //event.preventDefault();
        $('.menu > li a').removeClass('link_active');
        $(this).addClass('link_active');
    });

    $('.language > li:first-child a').addClass('l_active');
    $('.language > li > a').on('click', function (event) {
        event.preventDefault();
        $('.language > li a').removeClass('l_active');
        $(this).addClass('l_active');
    });

    $('.slider').slick({
        cssEase: 'ease-in',
        autoplay: true,
        autoplaySpeed: 3000,
        arrows: false,
        dots: true
    });

})();


