const div_result = document.getElementById('result')
const button_get_price = document.getElementById('get_price')
const select_criptos = document.getElementById('criptomoeda')

button_get_price.addEventListener("click", function() {
    const REQUESTS = new XMLHttpRequest()
    REQUESTS.open('GET', `/get-price/${select_criptos.value}`, true)
    REQUESTS.onreadystatechange = function () {
        if (REQUESTS.readyState === XMLHttpRequest.DONE) {
            if (REQUESTS.status === 200) {
                const RESPONSE = JSON.parse(REQUESTS.responseText)
                div_result.innerHTML = `R$ ${RESPONSE.price}`
            } else {
                console.error(`Erro ao obter o preço ${REQUESTS.status}`)
            }
        }
    }
    REQUESTS.send()
})
