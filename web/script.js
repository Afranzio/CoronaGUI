async function check(){
    const inputvalue = document.getElementById("input").value
    const out = document.getElementById("output")
    const chart = document.getElementById("charts")
    const g = await eel.get(inputvalue)();
    out.innerText = g
    chart.innerHTML = "<img src ='./img.png' />"
}
