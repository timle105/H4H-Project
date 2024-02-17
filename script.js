var userinput;

if (inputbutton) {
    factButton.addEventListener("click", storeInput);
    userinput.value = "";
}

function storeInput() {
    userinput = document.getElementById("inp");
    print(userinput);
}