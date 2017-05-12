function OpenPopup(){
    var sblock = $('.search_drop');
    sblock.toggle(300);
}

function FavLike() {
    $(this).parent('.like_share').parent('.review_desc').parent('.review').fadeOut(300);
}

function Like() {
    $(this).addClass('favourite');
}

$(document).ready(function () {
    $('.extra_menu > li:first-child').click(OpenPopup);
    $('.like_share > .like').click(FavLike);
    $('.r_block1 > .like').click(Like);

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

    var txt = $('.comment > p');
    $(txt).each(function (i, obj) {
        if($(obj).text().length > 280) {
            $(obj).text($(obj).text().substring(0,277)+'...')
        }
    });

    $(".menu-collapsed").click(function() {
        $(this).toggleClass("menu-expanded");
    });


});




//(function () {
//
//    //// get the name of uploaded file
//    //$('input[type="file"]').change(function(){
//    //    var value = $("input[type='file']").val();
//    //    $('.js-value').text(value);
//    //});
//
//
//
//})();


