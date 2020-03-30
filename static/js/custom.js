var navbar = $('.navbar')
var loop = setInterval(function() {
    var condition = $(window).scrollTop() >= (navbar.height()/2)
    navbar.toggleClass('bg-dark', condition)
}, 100)

$(document).ready(function() {
	$('#fullpage').fullpage({
		//options here
		autoScrolling:true,
		scrollHorizontally: true
	});

	//methods
	$.fn.fullpage.setAllowScrolling(false);
});
