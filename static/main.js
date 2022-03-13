console.log('hello world!')

const copyBtns = [...document.getElementsByClassName('copy-btn')]
console.log(copyBtns)

let previous = null

copyBtns.forEach(btn => btn.addEventListener('click', ()=>{
    const button = btn.getAttribute('data-code')
    navigator.clipboard.writeText(button)

    navigator.clipboard.readText().then(clipText=>{
        console.log(clipText)
        btn.textContent = `copied ${clipText}`
    })

    if (previous) {
        previous.textContent = 'click'
    }
    previous = btn
}))