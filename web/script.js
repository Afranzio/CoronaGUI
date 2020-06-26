async function check(){
    const inputvalue = document.getElementById("input").value
    const out = document.getElementById("output")
    const button = document.getElementById("button")
    const chart = document.getElementById("charts")
    const g = await eel.get(inputvalue)();
    out.innerText = g
    chart.innerHTML = "<img src ='./img.png' />"
    button.innerHTML = "<button type = 'button'  onClick = goBack() >Clear</button>"
}

function goBack(){
    window.location.replace('index.html');
}
