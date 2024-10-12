/**
 * Request Baskets API
 * RESTful API of [Request Baskets](https://rbaskets.in) service.  Request Baskets is an open source project of a service to collect HTTP requests and inspect them via RESTful API or web UI.  Check out the [project page](https://github.com/darklynx/request-baskets) for more detailed description. 
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd()+'/src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd()+'/src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.RequestBasketsApi);
  }
}(this, function(expect, RequestBasketsApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new RequestBasketsApi.Config();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('Config', function() {
    it('should create an instance of Config', function() {
      // uncomment below and update the code to test Config
      //var instance = new RequestBasketsApi.Config();
      //expect(instance).to.be.a(RequestBasketsApi.Config);
    });

    it('should have the property capacity (base name: "capacity")', function() {
      // uncomment below and update the code to test the property capacity
      //var instance = new RequestBasketsApi.Config();
      //expect(instance).to.be();
    });

    it('should have the property expandPath (base name: "expand_path")', function() {
      // uncomment below and update the code to test the property expandPath
      //var instance = new RequestBasketsApi.Config();
      //expect(instance).to.be();
    });

    it('should have the property forwardUrl (base name: "forward_url")', function() {
      // uncomment below and update the code to test the property forwardUrl
      //var instance = new RequestBasketsApi.Config();
      //expect(instance).to.be();
    });

    it('should have the property insecureTls (base name: "insecure_tls")', function() {
      // uncomment below and update the code to test the property insecureTls
      //var instance = new RequestBasketsApi.Config();
      //expect(instance).to.be();
    });

    it('should have the property proxyResponse (base name: "proxy_response")', function() {
      // uncomment below and update the code to test the property proxyResponse
      //var instance = new RequestBasketsApi.Config();
      //expect(instance).to.be();
    });

  });

}));
