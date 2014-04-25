$(document).ready(function(){

	s9backup = {
		"Cups Flour" : 3,
		"Eggs" : 2,
		"Tbsp Sugar" : 1
	}

	ingredients = (s9 && s9.initialParams && s9.initialParams['ingredients']) ? $.parseJSON(unescape(s9.initialParams['ingredients'])) : s9backup;

	listParent = $("#ingredientList")
	listParent.html(makeList(ingredients));
	
	ingredient_list = $('#ingredientList > li');

	$("#buttons").on('click','button',function(e){
			multiple = (this.id == "half") ? 0.5 : 2;
			scaleIngredients(multiple);
	});

	// pass in height & width
	s9.view.size({
		height: 400,
		width: document.documentElement.offsetWidth
	}) 
	
}) // end DOM ready

// construct ingredient list from s9.initialParams
function makeList(ingredients){
	var docFrag = document.createDocumentFragment(), x =1;

	$.each(ingredients,function(key,val){

		var qty = val,
		name = key,
		li, span_qty, span_name;

		li = document.createElement('li'), li.id = "item-"+x;
		span_qty = document.createElement('span'), span_qty.className = "qty", span_qty.innerHTML = qty;
		span_name = document.createElement('span'), span_name.className = "name", span_name.innerHTML = name;
		
		li.appendChild(span_qty)
		li.appendChild(span_name);
		docFrag.appendChild(li);
		x++;
	})

	return docFrag;
} 

// scale ingredients
function scaleIngredients(multiple){
	$.each(ingredient_list,function(i,el){
		var qty = this.getElementsByClassName('qty')[0].innerHTML;
		this.getElementsByClassName('qty')[0].innerHTML = (qty * multiple);
	})
	console.log('saving'),
	save();
}

// save function
function save(){
	saveObj = {};
	$.each(ingredient_list,function(i,el){
		saveObj[el.id] = this.getElementsByClassName('qty')[0].innerHTML;
	})

	s9.data.save({
		"saveObj" : saveObj,
	}), 
	console.log('saved data!', saveObj);
}

// process synced data
function restore(data){
	$.each(data,function(k,v){
		$("#"+k).find('.qty').text(v)
		console.log('restored data!', k, v)
	})
}

// sync saved data
s9.data.restore(function(data){
	restore(data.saveObj);
});





