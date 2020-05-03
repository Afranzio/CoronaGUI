async function covid(){
    const out = document.getElementById("output")
    const data=document.getElementById("data").value
    let a = await eel.finder(data)();
    out.innerText = a
}