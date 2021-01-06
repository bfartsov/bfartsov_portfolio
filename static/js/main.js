$(document).ready(function () {
    $('#slides').superslides({
        animation: 'fade',
        play: 5000,
        pagination: false,
    });
    let typed = new Typed('.typed', {
        strings: ['Multimedia Technician','WordPress ','Python', 'Live Streaming','Django','Node.js','React.js', ],
        typeSpeed:80,
        loop: true,
        startDelay:100,
        showCursor: false
    });

    $('.owl-carousel').owlCarousel({
        loop:true,
        items: 4,
        responsive:{
            0:{
                items:1
            },
            480:{
                items:2
            },
            768:{
                items:3
            },
            938:{
                items:4
            }
        }
    });

    let skillTopOffset = $('.skillsSection').offset().top;
    let statTopOffset = $('.statsSection').offset().top;
    let countUpFinished = false;

    $(window).scroll(function () {
        if (window.pageYOffset > skillTopOffset - $(window).height() + 200){
            $('.chart').easyPieChart({
                easing: 'easeInOut',
                barColor: '#fff',
                trackColor: false,
                scaleColor: false,
                lineWidth: 4,
                size: 152,
                onStep: function(from, to, percent) {
                    $(this.el).find('.percent').text(Math.round(percent));
                }
            });
        }
        if (!countUpFinished && window.pageYOffset > statTopOffset - $(window).height() + 200) {
            $('.counter').each(function () {
                let element = $(this);
                let endVal = parseInt(element.text());
                element.countup(endVal)
            });
            countUpFinished = true;
        }
    });

    $('[data-fancybox]').fancybox();
    $('.items').isotope(
        {
            filter: '*',
            animation: {
                duration:1500,
                easing:'linear',
                queue:false
            }
        }
    );
    $('#filters a').click(function () {
        $('#filters .current').removeClass('current');
        $(this).addClass('current');
        let selector = $(this).attr('data-filter');
        $('.items').isotope(
            {
                filter: selector,
                animation: {
                    duration:1500,
                    easing:'linear',
                    queue:false
                }
            }
        );
        return false

    });

    $('#navigation li a').click(function (e) {
        e.preventDefault();
        const targetElement = $(this).attr('href');
        const targetPosition = $(targetElement).offset().top;
        $('html, body').animate({
            scrollTop:targetPosition -50,
        }, 'slow')

    });

    const nav = $('#navigation');
    const navTop = nav.offset().top;
    $(window).on('scroll', stickyNavigation);
    function stickyNavigation() {
        const body = $('body');
        if ($(window).scrollTop() >= navTop) {
           body.addClass('fixedNav');
           body.css('padding-top', nav.outerHeight()+'px');
        }else {
            body.css('padding-top', 0);

            body.removeClass('fixedNav')

        }
    }

});



