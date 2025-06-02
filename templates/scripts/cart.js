function addToCart(bookId, delta) {
    fetch('/carts/update/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            book_id: bookId,
            delta: delta
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById(`qty-${bookId}`).textContent = data.quantity;
        const cartCount = document.getElementById('cart-count');
        if (cartCount) {
            cartCount.textContent = data.cart_count;
        }
    })
    .catch(error => console.error('Ошибка:', error));
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}