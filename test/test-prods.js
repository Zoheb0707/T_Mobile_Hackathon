var assert = require('assert');
var httpClient = require('../http-client.js');
describe('test get products', function(){
  var serv;

  before(function(){
    serv = require('../index.js');
  });

  after(function(){
    serv.close();
  });

  it.only('should download the products csv', function(done){
    httpClient.get('http://localhost:8080/products', function(res){
      var body = JSON.parse(res);
      assert.equal(body.gender === 'F' || body.gender === 'M', true);
      assert.equal(typeof body.age, 'number');
      assert.equal(typeof body.products, 'object');
      assert.equal(body.products.length > 0, true);
      done();
    });
  });
});
