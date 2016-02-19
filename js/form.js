// A basic sample on how to submit ajax data

// validate data
function validateData(){

    return true;    
}

// use ajax to submit the form data to /submit
// study notes in week 4
function sendData(){
    
}

$(document).ready(function(){    
  
  // call this when user submit the form
  // but when adding event.preventDefault() or return false
  // this will tell the page not to submit anything
  // call your function to submit the data instead
  
    $( "form" ).submit(function( event ) { 
        event.preventDefault();
        
        var success = validateData();
        
        if(success)
            sendData();
        
        // do not use alert in your assignment
        alert("Form not submitted!");
         
        return false;
    });  
    
});

