



















$(window).on("load resize", function () {
    var maxCatHeight = 0;
    let containerBelow = $('.page-part_index-first');
    $('.index-intro').find('.adv-list').height('auto').each(function () {
        if ($(this).height() > maxCatHeight) {
            maxCatHeight = $(this).height();
            containerBelow.css('margin-top', "-"+Math.ceil($(this).height())+'px');
            containerBelow.css('padding-top', Math.floor($(this).height()+40)+'px');
        }
    }).height(maxCatHeight);
});




















