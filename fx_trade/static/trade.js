
function func() {
    console.log("welcome");
    document.querySelector("#but").onclick=function(event){
        element=event.target
        if (element.innerHTML==="stopTrade"){
            console.log("button click");
            element.innerHTML="startTrade";
            element.value="False";
            
        }
        else {
        element.innerHTML='stopTrade';
            element.value="True" ;
        }
        }
            }
document.addEventListener("DOMContentLoaded",func)

