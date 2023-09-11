document.addEventListener('DOMContentLoaded', function () {
    const testimonials = document.querySelectorAll('.testimonial');
    const markers = document.querySelectorAll('.page-marker');
    const prevButton = document.getElementById('prev');
    const nextButton = document.getElementById('next');
    const numTestimonials = testimonials.length;
    const numVisibleTestimonials = 3;
    let currentIndex = 0;

    function showTestimonials() {
        testimonials.forEach((testimonial, i) => {
            const position = (i - currentIndex + numTestimonials) % numTestimonials;
            if (position >= 0 && position < numVisibleTestimonials) {
                testimonial.style.display = 'block';
            } else {
                testimonial.style.display = 'none';
            }
        });

        markers.forEach((marker, i) => {
            marker.classList.remove('active');
            if (i >= currentIndex && i < currentIndex + numVisibleTestimonials) {
                marker.classList.add('active');
            }
        });
    }

    prevButton.addEventListener('click', function () {
        currentIndex = (currentIndex - 1 + numTestimonials) % numTestimonials;
        showTestimonials();
    });

    nextButton.addEventListener('click', function () {
        currentIndex = (currentIndex + 1) % numTestimonials;
        showTestimonials();
    });

    // Show the initial testimonials
    showTestimonials();
});
