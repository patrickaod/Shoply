// Initialize Bootstrap/Popper Tooltips
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})

// Handle Video Autoplay for Prefer Reduced Motion
document.addEventListener('DOMContentLoaded', function () {
  const video = document.getElementById('background-video');
  
  // Check if the user prefers reduced motion
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  
  // If the user prefers reduced motion, disable autoplay
  if (prefersReducedMotion) {
      // Pause the video if reduced motion is preferred
      video.pause();
      video.removeAttribute('autoplay'); // Ensure autoplay is removed if set
  } else {
      // Otherwise, allow autoplay
      video.play();
  }
});
