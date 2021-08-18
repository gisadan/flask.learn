function onDisplay(){
    $('#noneDiv').show();
}
function offDisplay() {
    $('#noneDiv').hide();
}

function toggle_display(){
    el = document.querySelector('.content_section');
    
    if(el.style.visibility == 'hidden'){
        el.style.visibility = 'visible'
    }else{
       el.style.visibility = 'hidden'
    }
  }