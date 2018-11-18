var http = require('http');
var productData = require('./productData.js');
var router = function (req, res){
  if(req.method === 'GET' && req.url == '/ping'){
    res.writeHead(200, {'Content-Type': 'application/json'});
    res.write('{"message": "' + (new Date()) + '"}');
    res.end();
  } else if(req.method === 'GET' && req.url == '/products'){
    productData.generate(res);
  } else {
    res.writeHead(404, {'Content-Type': 'application/json'});
    res.write('{"message": "Not found ' + req.url + '"}');
    res.end();
  }
};

module.exports = http.createServer(router).listen(8080);
