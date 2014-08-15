$('.servers .server .status').each(function () {
	var status = $(this);

	var title;
	if (status.hasClass('online')) {
		title = 'Online';
	}
	else if (status.hasClass('offline')) {
		title = 'Offline';
	}

	status.attr('title', title);
});

