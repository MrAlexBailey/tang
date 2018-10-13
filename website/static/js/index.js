console.log('loaded JS')


$('li').hover(function () { 
    console.log('Hvered');
    MotionUI.animateIn(this, 'fade-in');
});