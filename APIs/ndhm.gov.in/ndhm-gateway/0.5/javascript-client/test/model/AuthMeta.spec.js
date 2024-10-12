/**
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
 *
 * The version of the OpenAPI document: 0.5
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
    factory(root.expect, root.Gateway);
  }
}(this, function(expect, Gateway) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new Gateway.AuthMeta();
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

  describe('AuthMeta', function() {
    it('should create an instance of AuthMeta', function() {
      // uncomment below and update the code to test AuthMeta
      //var instance = new Gateway.AuthMeta();
      //expect(instance).to.be.a(Gateway.AuthMeta);
    });

    it('should have the property expiry (base name: "expiry")', function() {
      // uncomment below and update the code to test the property expiry
      //var instance = new Gateway.AuthMeta();
      //expect(instance).to.be();
    });

    it('should have the property hint (base name: "hint")', function() {
      // uncomment below and update the code to test the property hint
      //var instance = new Gateway.AuthMeta();
      //expect(instance).to.be();
    });

  });

}));
