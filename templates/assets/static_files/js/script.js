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

    $('#myimage').mapster({
        fillOpacity: 0.6,
        fillColor: '1be7e3',
        stroke: true,
        strokeWidth: 3,
        strokeColor: '1be7e3',
        strokeOpacity: 1,
        mapKey: 'data-key',
        onMouseover: function (e) {
            $('#myimage').mapster('set', false, e.key);
        }
    });

    var temp = null;
    $('.sphere').each(function (i, obj) {
        $(obj).hover(function (event) {
            temp = $(this).attr('data-target');
            $('#myimage').mapster('set', true, temp);
        }, function (event) {
            $('#myimage').mapster('set', false, temp);
            temp = null;
        });
    });

    $('.slider').slick({
        cssEase: 'ease-in',
        autoplay: true,
        autoplaySpeed: 3000,
        arrows: false,
        dots: true
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


