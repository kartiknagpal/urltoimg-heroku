var args = require('system').args;
if (args.length === 1) {
    var url = 'http://google.in';
}
else {
    var url = args[1];
}
var page = require('webpage').create();
page.open(url, function () {
	//page.zoomFactor = 0.25;
	page.viewportSize = { width: 960, height: 600 };
	page.clipRect = { top: 0, left: 0, width: 960, height: 600 };
	var title = page.title;
	var filename = url.replace(/[^a-z0-9]/gi, '_').toLowerCase();
    page.render('static/capture-'+filename+'.png');
    console.log(filename);
    phantom.exit();
});