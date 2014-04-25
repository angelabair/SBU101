// Answers
var answer = {
  0:"answer 1",
	1:"answer 2",
	2:"answer 3",
	3:"answer 4",
	4:"answer 5",
	5:"answer 6",
	6:"answer 7",
	7:"answer 8",
	8:"answer 9",
	9:"answer 10",
	10:"answer 11",
	11:"answer 12",
	12:"answer 13",
	13:"answer 14",
	14:"answer 15",
	15:"answer 16",
	16:"answer 17",
	17:"answer 18",
	18:"answer 19",
	19:"answer 20",
	20:"answer 21",
	21:"answer 22",
	22:"answer 23",
	23:"answer 24",
	24:"answer 25",
}

var saved_data = {}; 
var noRestore = false;

$(window).load(function() {
	var container = $("#s9-container");
	var type_inputs = $("input[type=text]");
	var textareas = $("textarea");
	
	// Set height of iframe to height of widget contents
  var interval = setInterval(function(){
  	var ht = document.documentElement.offsetHeight + 5;
      s9.view.size({
          height: ht
      });
  }, 1000);
  setTimeout(function(){
      clearInterval(interval);
  }, 10000)
  
  // Reflow iframe on device orientation change  
  s9.view.onrotate(function(data){
	  var ht = document.documentElement.offsetHeight + 5;
    s9.view.size({
        height: ht
    });
	});

	// Add placeholder text for IE support
	function sup_placeholder() {
	  var i = document.createElement('input');
	  i = 'placeholder' in i;
	  
	  var j = document.createElement('textarea');
	  j = 'placeholder' in j;
	  
	  if (i && j) return true;
		else return false;
	}
	
	if(!sup_placeholder()) {
		$('[placeholder]').focus(function() {
		  var input = $(this);
		  if (input.val() == input.attr('placeholder')) {
		    input.val('');
		    input.removeClass('s9-placeholder');
		  }
		}).blur(function() {
		  var input = $(this);
		  if (input.val() == '' || input.val() == input.attr('placeholder')) {
		    input.addClass('s9-placeholder');
		    input.val(input.attr('placeholder'));
		  }
		}).blur();
	}

	// Input type=text Validation	
	var check = $("#s9-check");
  var show = $("#s9-show");
  var reset = $(".s9-reset");
  
  function _setupSavedData(){
	  $.each(type_inputs,function() { 
	    input = $(this);
	
	    saved_data[input.attr('id')] = input.value;
	  })
	}
	
	function trim1 (str) {
    return str.replace(/^\s\s*/, '').replace(/\s\s*$/, '').toLowerCase();
  }
	
	function validate(id) { 
    el = $("#"+id);
    if(answer[id].search(' or ') != -1) {
			tempA = answer[id].split(' or ');

      for(i in tempA) {
        if(trim1(String(el.attr('value'))) == tempA[i].toLowerCase())
          return true;
      }
    }
    return (trim1(String(el.attr('value'))) == answer[id].toLowerCase());
  }
	
	_setupSavedData();
  
  // CHECK ANSWERS
  check.on('click',function(e) {   
	  container.toggleClass('s9-c_a'); 
	  
	  // Toggle On: Check Answers
	  if(container.hasClass('s9-c_a')) {
		  this.className = 's9-toggle-on'; 
		  noRestore = true;
		  
		  if(container.hasClass('s9-s_a')) {
		  	container.removeClass('s9-s_a');
		    type_inputs.removeClass('s9-show-answer');
		    show.removeClass('s9-toggle-on');
		  	
		  	for(x=0;x<type_inputs.length;x++){
	        id = type_inputs[x].id;
	        input = $("#"+id);
	        input.className='';
	        if(saved_data[id]) input.attr('value', saved_data[id]);
	        else input.attr('value', '');
	      }
		  }
		  
		  $.each(type_inputs,function(k,v){
        this.className = 'v';
        id = v.id;
        if(validate(id)){
          this.className += ' s9-correct';          
        } 
        
        else {
          this.className += ' s9-incorrect';
        }
      })  
	  }
	  	  
	  // Toggle Off: Uncheck Answers
	  else { 
	    this.className = '';
	    type_inputs.removeClass('s9-correct s9-incorrect');
	    noRestore = false;
	    // restore saved data, ok sync
	    
	    for(x=0;x<type_inputs.length;x++){
        id = type_inputs[x].id;
        input = $("#"+id);
        input.className='';
        if(saved_data[id]) input.attr('value', saved_data[id]);
        else input.attr('value', '');
      }
	  }
     
  })
  
  // SHOW ANSWERS
  show.on('click',function(e) {  
	  if(container.hasClass('s9-c_a')){
	    container.removeClass('s9-c_a');
	    type_inputs.removeClass('s9-correct s9-incorrect');
	    check.removeClass('s9-toggle-on');
	  }
	  
	  container.toggleClass('s9-s_a'); 
	  
	  // Toggle On: Show Answers
	  if(container.hasClass('s9-s_a')) {
		  this.className = 's9-toggle-on'; 
		  noRestore = true;
		  
		  for(x=0; x < type_inputs.length; x++){ 
	      id = type_inputs[x].id;
	      input = $("#"+id);
	      input.attr('value', answer[id]).addClass("s9-show-answer");
	    }
	    
	  }
	  
	  // Toggle Off: Hide Answers (restore saved data, ok to sync)
	  else { 
	    this.className = '';
	    type_inputs.removeClass('s9-show-answer');
	    noRestore = false;
	    
	    for(x=0;x<type_inputs.length;x++){
        id = type_inputs[x].id;
        input = $("#"+id);
        input.className='';
        if(saved_data[id]) input.attr('value', saved_data[id]);
        else input.attr('value', '');
      }
    }
     
  })
  
  // RESET
  reset.on('click',function(e) {
		type_inputs.removeClass('s9-show-answer').removeClass('s9-correct s9-incorrect');
		type_inputs.attr('value', '').value('');  
		textareas.attr('value', '');
		$('button').removeClass('s9-toggle-on');
		container.removeClass('s9-c_a').removeClass('s9-s_a');
		
		s9.data.save(saved_data);
    noRestore = false;
  })
  
  // SAVE ON INPUT BLUR
  container.on('blur','input[type=text]',function(e) {
    this.setAttribute('value', this.value);
    saved_data[this.id] = this.value;
    s9.data.save(saved_data);
    noRestore = false;
    
    console.log(saved_data);
    console.log("\n");
  })
  
  
  // INPUT FOCUS EVENTS
  container.on('focus','input[type=text]',function(e) {
  	if(container.hasClass('s9-c_a') || container.hasClass('s9-s_a')) {
  		
  		container.removeClass('s9-c_a s9-s_a');
	     
	    for(x=0;x<type_inputs.length;x++){ 
	      id = type_inputs[x].id;
	      input = $("#"+id);
	      input.className='';
	      
      	if(saved_data[id]) input.attr('value', saved_data[id]);
        else input.attr('value', '');
	    	
	  		input.removeClass('s9-show-answer s9-correct s9-incorrect');
	    }
	
	    $(".s9-toggle-on").removeClass("s9-toggle-on");
	    noRestore = true;
  	}
  	
  	else return;
  })
  
  // RESTORE
  s9.data.onrestore(function(data){
    if(noRestore) return;
    $.each(data,function(k,v){
      if (!v) return;
      $('#'+k).attr('value', v);
      saved_data[k] = v;
    })
  })
   
});





