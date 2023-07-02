const btnCart = document.querySelector('.container-cart-icon')
const containerCartProducts = document.querySelector('.container-cart-products')

btnCart.addEventListener('click', () => {
    containerCartProducts.classList.toggle('hidden-cart')
})

const Clickbutton = document.querySelectorAll('.btn-add-to-cart')
console.log(Clickbutton);

let carrito = []

Clickbutton.forEach(btn => {
    btn.addEventListener('click', addToCarritoItem)
})

function addToCarritoItem(e){
    const button = e.target
    const item = button.closest('.items')
    const itemTitle = item.querySelector('.nombre-producto').textContet;
    console.log(itemTitle)
}

//const cartinfo = document.querySelector('.cart-product')
//const rowproduct = document.querySelector('.row-product')

//const productsList = document.querySelector('.container-item')

//let productos = []

//productsList.addEventListener('click', e =>{
    
//    if(e.target.classList.contains('btn-add-to-cart')){
//        const product = e.target.parentElement

//        const infoproducto ={
//            quantity: product.querySelector(number).input-cantidad
//        }
//    }
//})


const inputQuantity = document.querySelector('.input-cantidad')
const btnIncrement = document.querySelector('#mas')
const btnDecrement = document.querySelector('#menos')

let cantidad = parseInt(inputQuantity.value)

btnIncrement.addEventListener('click', () => {
    cantidad += 1
    inputQuantity.value = cantidad
})

btnDecrement.addEventListener('click', () => {
    if (cantidad ===1){
        return
    }

    cantidad -= 1
    inputQuantity.value = cantidad
})

const toggleDescripcion = document.querySelector('.titulo-descripcion')

const contentDescripcion = document.querySelector('.texto-descripcion');

toggleDescripcion.addEventListener('click', () => {
    contentDescripcion.classList.toggle('hidden');
});