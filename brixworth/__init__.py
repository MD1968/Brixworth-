html {
    height: 100%;
}

body {
    background: url('/media/escooter-background.jpg') no-repeat center center fixed;
    background-size: cover;
    height: calc(100vh - 164px);
    color: #1d7338;
    font-family: 'Lato';
}

/* from Bulma */
.icon {
    color: white;
    background: #1d7338;
    align-items: center;
    display: inline-flex;
    justify-content: center;
    height: 1.5rem;
    width: 1.5rem;
}

.logo-font {
    text-transform: uppercase;
}

.main-logo-link {
    width: fit-content;
}

.shop-now-button {
    background: #1d7338;
    color: white;
    min-width: 260px;
}

.btn-black {
    background: #1d7338;
    color: white;
}
.text-green {
    color: #1d7338 !important;
}

.btn-green {
    background: #1d7338;
    color: white;
}


.btn-outline-black {
    background: white;
    color: black !important; /* use important to override link colors for <a> elements */
    border: 1px solid #1d7338;
}

.btn-outline-black:hover,
.btn-outline-black:active,
.btn-outline-black:focus {
    background: #1d7338;
    color: white !important;
}

.shop-now-button:hover,
.shop-now-button:active,
.shop-now-button:focus,
.btn-black:hover,
.btn-black:active,
.btn-black:focus {
    background:  #1d7338;
    color: white;
}

.text-black {
    color:  #1d7338 !important;
}

.border-black {
    border: 1px solid  #1d7338 !important;
}

.bg-black {
    background: #1d7338 !important;
}

.overlay {
	height: 100%;
	width: 100%;
	top: 0;
	left: 0;
	position: fixed;
	background: white;
	z-index: -1;
}

a.category-badge > span.badge:hover {
    background: #1d7338 !important;
    color: #fff !important;
}

.btt-button {
    height: 42px;
    width: 42px;
    position: fixed;
    bottom: 10px;
    right: 10px;
}

.btt-link,
.update-link,
.remove-item {
    cursor: pointer;
}

.product_card {
    padding-top: 10px;
    color: #1d7338;
}

input[name='q']::placeholder {
    color: #aab7c4;
}

/* ------------------------------- bootstrap toasts */

.message-container {
    position: fixed;
    top: 72px;
    right: 15px;
    z-index: 99999999999;
}

.custom-toast {
    overflow: visible;
}

.toast-capper {
    height: 2px;
}

/* from CSS-tricks.com: https://css-tricks.com/snippets/css/css-triangle/ */
.arrow-up {
    width: 0; 
    height: 0; 
    border-left: 4px solid transparent;
    border-right: 4px solid transparent; 
    border-bottom: 10px solid #1d7338;
    position: absolute;
    top: -10px;
    right: 36px;
}

/* Convenience classes - colors copied from Bootstrap */
.arrow-primary {
    border-bottom-color: #007bff !important;
}

.arrow-secondary {
    border-bottom-color: #6c757d !important;
}

.arrow-success {
    border-bottom-color: #28a745 !important;
}

.arrow-danger {
    border-bottom-color: #dc3545 !important;
}

.arrow-warning {
    border-bottom-color: #ffc107 !important;
}

.arrow-info {
    border-bottom-color: #17a2b8 !important;
}

.arrow-light {
    border-bottom-color: #f8f9fa !important;
}

.arrow-dark {
    border-bottom-color: #343a40 !important;
}

.cart-notification-wrapper {
    height: 100px;
    overflow-x: hidden;
    overflow-y: auto;
}

/* -------------------------------- Media Queries */

/* Slightly larger container on xl screens */
@media (min-width: 1200px) {
  .container {
    max-width: 80%;
  }
}

/* Allauth form formatting */

.allauth-form-inner-content p {
    margin-top: 1.5rem; /* mt-4 */
    color: #6c757d; /* text-secondary */
}

.allauth-form-inner-content input {
    border-color: #000;
    border-radius: 0;
}

.allauth-form-inner-content label:not([for='id_remember']) {
    display: none;
}

.allauth-form-inner-content input::placeholder {
    color: #aab7c4;
}

.allauth-form-inner-content button,
.allauth-form-inner-content input[type='submit'] {
	/* btn */
	display: inline-block;
    font-weight: 400;
    color: #fff;
    text-align: center;
    vertical-align: middle;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    background-color: #000;
    border: 1px solid #000;
    padding: .375rem .75rem;
    font-size: 1rem;
    line-height: 1.5;
    border-radius: 0;

    /* standard bootstrap btn transitions */
    transition: color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;
}

.allauth-form-inner-content button:hover,
.allauth-form-inner-content input[type='submit']:hover {	
	color: #fff;
    background-color: #222;
    border-color: #222;
}

.allauth-form-inner-content a {
	color: #17a2b8; /* text-info */
}

/* Product Form */

.btn-file {
    position: relative;
    overflow: hidden;
}

.btn-file input[type="file"] {
    position: absolute;
    top: 0;
    right: 0;
    min-width: 100%;
    min-height: 100%;
    opacity: 0;
    cursor: pointer;
}

.custom-checkbox .custom-control-label::before {
    border-radius: 0;
    border-color: #dc3545;
}

.custom-checkbox .custom-control-input:checked~.custom-control-label::before {
    background-color: #dc3545;
    border-color: #dc3545;
    border-radius: 0;
}


/* fixed top navbar only on medium and up */
@media (min-width: 992px) {
    .fixed-top-desktop-only {
        position: fixed;
        top: 0;
        right: 0;
        left: 0;
        z-index: 1030;
    }

    .header-container {
        padding-top: 164px;
    }
}

/* pad the top a bit when navbar is collapsed on mobile */
@media (max-width: 991px) {
    .header-container {
        padding-top: 116px;
    }

    body {
        height: calc(100vh - 116px);
    }

    .display-4.logo-font.text-black {
        font-size: 2rem;
    }

    .nav-link {
        padding: 0.15rem;
    }

    .nav-link i.fa-lg {
        font-size: 1rem;
    }

    .navbar-toggler {
        padding: .6rem .6rem;
        font-size: 1rem;
    }

    #delivery-banner h4 {
        font-size: .9rem;
    }

    .btn.btn-outline-black.rounded-0,
    .btn.btn-black.rounded-0 {
        padding: .375rem .375rem;
    }

    .btn.btn-outline-black.rounded-0.btn-lg,
    .btn.btn-black.rounded-0.btn-lg {
        padding: .375rem .375rem;
        font-size: .75rem;
    }

    .increment-qty, .decrement-qty {
        padding: .25rem .5rem !important;
    }
}