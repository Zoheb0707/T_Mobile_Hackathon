var assert = require('assert');
var httpClient = require('../http-client.js');
describe('test ping', function(){
  var serv;

  before(function(){
    serv = require('../index.js');
  });

  after(function(){
    serv.close();
  });

  it('ping responds', function(done){
    httpClient.get('http://localhost:8080/ping', function(res){
      var body = JSON.parse(res);
      assert.equal(typeof body.message, 'string');
      done();
    });
  });
});
