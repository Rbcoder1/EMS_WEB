// (function ($) {
//     "use strict";

//     // Spinner
//     var spinner = function () {
//         setTimeout(function () {
//             if ($('#spinner').length > 0) {
//                 $('#spinner').removeClass('show');
//             }
//         }, 1);
//     };
//     spinner();


//     // Initiate the wowjs
//     new WOW().init();


//     // Sticky Navbar
//     $(window).scroll(function () {
//         if ($(this).scrollTop() > 300) {
//             $('.sticky-top').css('top', '0px');
//         } else {
//             $('.sticky-top').css('top', '-100px');
//         }
//     });


//     // Dropdown on mouse hover
//     const $dropdown = $(".dropdown");
//     const $dropdownToggle = $(".dropdown-toggle");
//     const $dropdownMenu = $(".dropdown-menu");
//     const showClass = "show";

//     $(window).on("load resize", function () {
//         if (this.matchMedia("(min-width: 992px)").matches) {
//             $dropdown.hover(
//                 function () {
//                     const $this = $(this);
//                     $this.addClass(showClass);
//                     $this.find($dropdownToggle).attr("aria-expanded", "true");
//                     $this.find($dropdownMenu).addClass(showClass);
//                 },
//                 function () {
//                     const $this = $(this);
//                     $this.removeClass(showClass);
//                     $this.find($dropdownToggle).attr("aria-expanded", "false");
//                     $this.find($dropdownMenu).removeClass(showClass);
//                 }
//             );
//         } else {
//             $dropdown.off("mouseenter mouseleave");
//         }
//     });


//     // Back to top button
//     $(window).scroll(function () {
//         if ($(this).scrollTop() > 300) {
//             $('.back-to-top').fadeIn('slow');
//         } else {
//             $('.back-to-top').fadeOut('slow');
//         }
//     });
//     $('.back-to-top').click(function () {
//         $('html, body').animate({ scrollTop: 0 }, 1500, 'easeInOutExpo');
//         return false;
//     });


//     // Header carousel
//     $(".header-carousel").owlCarousel({
//         autoplay: true,
//         smartSpeed: 1500,
//         items: 1,
//         dots: false,
//         loop: true,
//         nav: true,
//         navText: [
//             '<i class="bi bi-chevron-left"></i>',
//             '<i class="bi bi-chevron-right"></i>'
//         ]
//     });


//     // Testimonials carousel
//     $(".testimonial-carousel").owlCarousel({
//         autoplay: true,
//         smartSpeed: 1000,
//         center: true,
//         margin: 24,
//         dots: true,
//         loop: true,
//         nav: false,
//         responsive: {
//             0: {
//                 items: 1
//             },
//             768: {
//                 items: 2
//             },
//             992: {
//                 items: 3
//             }
//         }
//     });

// })(jQuery);


// code for render dynamic organization in popular organization session 

var container = document.getElementById("orgCon");
let orgArray = [
    {
        "id": "1",
        "title": "Google Cloud",
        "linkedin": "",
        "website": "",
        "img": "static/img/gcp.jfif"
    },
    {
        "id": "2",
        "title": "Aws",
        "linkedin": "",
        "website": "",
        "img": "static/img/aws.png"
    },
    {
        "id": "3",
        "title": "Microsoft Azure",
        "linkedin": "",
        "website": "",
        "img": "static/img/azure.png"
    },
    {
        "id": "4",
        "title": "Salesforce",
        "linkedin": "",
        "website": "",
        "img": "static/img/salesforce.jfif"
    },
    {
        "id": "5",
        "title": "GitHub",
        "linkedin": "",
        "website": "",
        "img": "static/img/github.jfif"
    },

]

var str = "";

for (item of orgArray) {
    let strcp = `<div class="col-md - 3 col - sm - 6">
                    <div class="" style=" width: 200px; text-align: center; >
                        <h4 class="card-title text-right"><i class="material-icons">${item.title}</i></h4>
                        <img src=${item.img} alt="Photo of sunset" style="width:200px;  height:100px; border:1px; border-radius:10px;">
                        <div style="display:flex; justify-content:center; align-item:center;" class="my-2">
                            <a class="mx-2  linkorg" href=${item.linkedin}><i class="fa-brands fa-linkedin"></i></a>
                            <a class="mx-2 linkorg" href=${item.website}><i class="fa-solid fa-link"></i></a>
                        </div>    
                    </div>
                </div > `

    str += strcp;
}
container.innerHTML = str
console.log(container)


