$(document).ready(function() {
	$('.tableViewButtons').click(function() {

		$('.tableViewButtons').removeClass('active');
		$(this).addClass('active');

		var idVar;
		idVar = $(this).attr('data-categoryid');
		$.get('/myevents/subset/',
			{'category_id': idVar},
			function(data) {
				var myTable;
				myTable = '<tbody id="indexTable">';
				$.each(data, function(key,value) {
					tableRow = '<tr data-toggle="collapse" data-target="#id' + value.id + '\" ' + 'class="colorChange">';
					tableRow += '<td>' + value.title + '</td>';
					tableRow += '<td>' + value.day + '</td>';
					tableRow += '<td>' + value.time + '</td>';
					tableRow += '<td>' + value.duration + '</td>';
					tableRow += '</tr>';

					tableRow2 = '<tr id="id' + value.id + '\" ' + 'class="collapse hiddenRow">';
					tableRow2 += '<td colspan="6">';
					tableRow2 += '<div class="card-body">';
					tableRow2 += '<strong>Description: </strong>' + value.description + '<br>';
					tableRow2 += '<strong>Link to join meeting: </strong>' + value.join;
					tableRow2 += '</div>' + '</td>' + '</tr>';
							
					myTable += tableRow;
					myTable += tableRow2;

				});
				myTable += '</tbody>';

				$('#indexTable').replaceWith(myTable);

				if (!$.trim(data)) {
					$('#emptyResult').html("Sorry, there don't seem to be any events right now :/");
				}
				else {
					$('#emptyResult').html('');
				}
			});


	}); 


	$(document).on('show.bs.collapse', '.collapse', function () {
    	$('.collapse').removeClass('show');
    	$('.colorChange').removeClass('table-success');
    	$(this).addClass('show');
    	$(this).prev().addClass('table-success');
	});


	$('.cardViewButtons').click(function() {

		$('.cardViewButtons').removeClass('active');
		$(this).addClass('active');

		var idVar;
		idVar = $(this).attr('data-categoryid');
		$.get('/myevents/subset/',
			{'category_id': idVar},
			function(data) {
				var myCards;
				myCards = '<div class="row mt-4 pl-2 justify-content-left" id="cardView">';
				$.each(data, function(key,value) {
					card = '<a href="/myevents/event/' + value.id + '/\"' + " " + 'style="text-decoration: none;">';
					card += '<div class="card box-shadow mx-2 mb-3 indexCard" style="width:12rem; height:15rem;">';
					card += '<div class="card-body">';
					card += '<h5 class="card-title text-danger">' + value.title + '</h5>';
					card += '<h6 class="card-subtitle mb-2 text-dark">' + value.day + ' @ ' + value.time + '</h6>';
					card += '<p class="card-text text-truncate text-muted">' + value.description + '</p>';
					card += '</div>';
					card += '</div>';
					card += '</a>';

					myCards += card;
				});
				myCards += '</div>';

				$('#cardView').replaceWith(myCards);

				if (!$.trim(data)) {
					$('#emptyResult').html("Sorry, there don't seem to be any events right now :/");
				}
				else {
					$('#emptyResult').html('');
				}
			});


	});

	$('input.custom-control-input').on('change.bootstrapSwitch', function() {

	    if($(this).is(':checked')) {
	    	var url_state = (document.location.href.indexOf("myevents") > -1);
	    	if (url_state) 
	    		document.location.href = 'table_view';
	    	else 
	    		document.location.href = 'myevents/table_view';
	    }
	    else {
	        document.location.href = '/';
	    }

	    //code..

	    $.ajax({
            success: function(result) {
            	console.log(result)
            }

	    });

	});

	$(document).on('click', '.confirm-delete', function(){
    	return confirm('Are you sure you want to delete this?');
	});

});
