function updateProd(el) {
    product_id = el.value
    fetch('/in_stock/' + product_id, {
        method: 'patch',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'in_stock': el.checked})
    })
    console.log(product_id)
}

function clearBooks() {
    fetch('/clear', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Очищаем список на странице
            const bookList = document.getElementById('book-list');
            bookList.innerHTML = '';
        } else {
            alert(data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function addProduct() {
    let prodName = document.getElementById('prod_name').value
    let price = document.getElementById('price').value
    fetch('/add', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'prod_name': prodName,
                             'price': price,
                             'in_stock': true})
    })
//    console.log("Add")
}