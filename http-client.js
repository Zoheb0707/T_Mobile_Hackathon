var http = require('http');
var get = function(url, callback){
  http.get(url, function(res){
    var resBody = '';
    res.on('data', function(data){
      resBody += data;
    });
    res.on('end', function(){
      callback(resBody);
    });
  });
};

module.exports = {
  get: get
};
