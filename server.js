var express = require('express');
var ipFilter = require('express-ipfilter');
var app = express();

// IPs Blacklist
var ips = ['127.0.0.1', '::ffff:127.0.0.1'];
// var ips = [];
 
app.use(ipFilter(ips, {mode: 'deny'}));

app.get('/', function(req, res){
  	res.send('<h1>Hello World!</h1>');
});

app.listen(3000);