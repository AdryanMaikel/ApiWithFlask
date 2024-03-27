const div_result = document.getElementById('result')
const button_get_price = document.getElementById('get_price')
const select_criptos = document.getElementById('criptos')

console.log('teste')

button_get_price.addEventListener("click", function() {
    console.log(select_criptos.value)
    const REQUESTS = new XMLHttpRequest()
    REQUESTS.open('GET', `/get-price/${select_criptos.value}`, true)
    REQUESTS.onreadystatechange = function () {
        if (REQUESTS.readyState === XMLHttpRequest.DONE) {
            if (REQUESTS.status === 200) {
                const RESPONSE = JSON.parse(REQUESTS.responseText)
                div_result.innerHTML = `O preço do ${RESPONSE.name} é  de ${RESPONSE.price}.`
            } else {
                console.error(`Erro ao obter o preço ${REQUESTS.status}`)
            }
        }
    }
    REQUESTS.send()
})
