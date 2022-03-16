console.log('hello world!')

const copyBtns = [...document.getElementsByClassName('copy-btn')]

let previous = null

copyBtns.forEach(btn => btn.addEventListener('click', ()=>{
    const code = btn.getAttribute('data-code');
    navigator.clipboard.writeText(code)

    navigator.clipboard.readText().then(clipText=>{
        btn.textContent = `saved to clipboard`
    })

    if (previous) {
        previous.textContent = 'copy'
    }
    previous = btn
}))