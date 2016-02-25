// A basic sample on how to submit ajax data

// validate data, this is your validate functions
function validateData(){
    return true;    
}

// use ajax to submit the form data to server (see notes in week 4)
function sendData(){ 
    console.log("Assignment2: Submit data to server using ajax");    
}

$(document).ready(function(){    
  
  // call this when user submit the form
  // but when adding event.preventDefault() or return false
  // this will tell the page not to submit anything
  // call your ajax function to submit the data instead  
    $( "#target" ).submit(function( event ) { 
        event.preventDefault();
        
        var success = validateData();
        
        if(success)
            sendData();
        
        return false;
    });  
    
});

