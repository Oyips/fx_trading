
function func() {
    console.log("welcome");
    document.querySelector("#but").onclick=function(event){
        element=event.target
        if (element.value==="True"){
            console.log("button click");
            element.value="False";
            
        }
        else {
            console.log("button click");
            element.value="True" ;
        }
        }
            }
document.addEventListener("DOMContentLoaded",func)

