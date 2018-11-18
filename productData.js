var proc = require('child_process');
var fs = require('fs');
var config = require('./config.json');
var generate = function(res){
  // TODO execute python data build
  if(fs.existsSync(config.recommendedProductsFile)){
    fs.unlinkSync(config.recommendedProductsFile);
  }
  var cmd = 'python3 ' + config.recommendationsPyScript + ' >> ' + config.recommendedProductsFile
  proc.exec(cmd, function(err, stdout, stderr){
    if(err) throw err;
    fs.readFile(config.recommendedProductsFile, function(err, data){
      if(err) throw err;
      res.writeHead(200, {'Content-Type': 'application/json'});
      res.write('{"data": "' + data + '"}');
      res.end();
    });
  });
};

module.exports = {
  generate: generate
};
