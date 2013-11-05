var args = require('system').args;
if (args.length === 1) {
    var url = 'http://google.in';
}
else {
    var url = args[1];
}
var page = require('webpage').create();
page.open(url, function () {
    page.render('capture.png');
    phantom.exit();
});