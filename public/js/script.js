/**
 * Portfolio Website JavaScript
 * Interactive functionality for the portfolio
 */

document.addEventListener('DOMContentLoaded', () => {
    // Initialize all functionality
    initMobileMenu();
    initSmoothScroll();
    initScrollAnimations();
    initActiveNavLink();
});

/**
 * Mobile Menu Toggle
 * Handles the mobile navigation menu
 */
function initMobileMenu() {
    const menuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');
    
    if (!menuBtn || !navLinks) return;
    
    menuBtn.addEventListener('click', () => {
        // Toggle menu visibility
        navLinks.classList.toggle('active');
        
        // Animate hamburger icon
        menuBtn.classList.toggle('open');
        
        // Update accessibility
        const isExpanded = navLinks.classList.contains('active');
        menuBtn.setAttribute('aria-expanded', isExpanded);
    });
    
    // Close menu when clicking a link
    navLinks.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('active');
            menuBtn.classList.remove('open');
            menuBtn.setAttribute('aria-expanded', 'false');
        });
    });
    
    // Close menu on escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && navLinks.classList.contains('active')) {
            navLinks.classList.remove('active');
            menuBtn.classList.remove('open');
            menuBtn.setAttribute('aria-expanded', 'false');
        }
    });
}

/**
 * Smooth Scroll
 * Implements smooth scrolling for anchor links
 */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            // Skip if it's just "#"
            if (href === '#') return;
            
            const targetElement = document.querySelector(href);
            
            if (targetElement) {
                e.preventDefault();
                
                const navHeight = document.querySelector('.navbar').offsetHeight;
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - navHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

/**
 * Scroll Animations
 * Adds fade-in animations when elements come into view
 */
function initScrollAnimations() {
    // Get all sections
    const sections = document.querySelectorAll('section');
    
    // Create intersection observer
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animationPlayState = 'running';
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);
    
    // Observe each section
    sections.forEach(section => {
        section.style.animationPlayState = 'paused';
        observer.observe(section);
    });
    
    // Animate project cards with stagger
    const projectCards = document.querySelectorAll('.project-card');
    projectCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = `all 0.5s ease-out ${index * 0.1}s`;
    });
    
    const projectObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1 });
    
    projectCards.forEach(card => {
        projectObserver.observe(card);
    });
}

/**
 * Active Navigation Link
 * Highlights the current section in the navigation
 */
function initActiveNavLink() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-links a');
    
    if (sections.length === 0 || navLinks.length === 0) return;
    
    const observerOptions = {
        root: null,
        rootMargin: '-50% 0px -50% 0px',
        threshold: 0
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    
                    if (link.getAttribute('href') === `#${id}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }, observerOptions);
    
    sections.forEach(section => {
        observer.observe(section);
    });
}

/**
 * Optional: Typewriter Effect for Hero Section
 * Uncomment to enable typewriter animation
 */
// function initTypewriter() {
//     const textElement = document.querySelector('.hero-text h1');
//     if (!textElement) return;
//     
//     const text = textElement.textContent;
//     textElement.textContent = '';
//     
//     let index = 0;
//     
//     function type() {
//         if (index < text.length) {
//             textElement.textContent += text.charAt(index);
//             index++;
//             setTimeout(type, 50);
//         }
//     }
//     
//     setTimeout(type, 1000);
// }

/**
 * Optional: Dynamic Year in Footer
 * Uncomment to enable
 */
// function updateFooterYear() {
//     const yearElement = document.querySelector('.footer-year');
//     if (yearElement) {
//         yearElement.textContent = new Date().getFullYear();
//     }
// }