console.log('loaded JS')

$(document).ready(function() {
    console.log('Doc Ready')
    console.log(sessionStorage.visited)
    if (!sessionStorage.visited2) {
        console.log('Visited False')
        sessionStorage.setItem('visited', true)
        MotionUI.animateIn('.content-holder', 'fade-in');
        MotionUI.animateIn('ul', 'hinge-in');
        $('.loader').addClass('delayed-fade')
        MotionUI.animateIn('.loader', 'fade-in');
    } else {
        $('.loader').addClass('instant-fade')
    };
    // var $animation = $('.content').data('#animation')
    // MotionUI.animateIn($('.content .delayed-fade'), 'fade-in')
    // MotionUI.animateIn('.content', 'fade-in');
    
    $('a').click(function (){
        console.log($(this).prop("name"))
        var $page = $(this).prop("name")
        window.history.pushState("", "Alex and Melissa", $page)
        $.get($page + '?slim=True', function(data) {
            $('.loader').removeClass('delayed-fade')
            $('.loader').addClass('instant-fade')
            $('.loader').hide()
            $('.loader').html(data)
            MotionUI.animateIn('.loader', 'fade-in')
            console.log(data)
        });
        // $('.content').html(jQuery.get($page))
        // console.log(jQuery.get($page))
        return false;
    })
});

// $('li').hover(function () { 
//     console.log('Hvered');
//     MotionUI.animateIn(this, 'fade-in');
// });

        // $.get('/engagement', function(data) {
        //     $('.loader').html(data)
        //     console.log(data)
        // })