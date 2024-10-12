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
    instance = new Gateway.Endpoint();
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

  describe('Endpoint', function() {
    it('should create an instance of Endpoint', function() {
      // uncomment below and update the code to test Endpoint
      //var instance = new Gateway.Endpoint();
      //expect(instance).to.be.a(Gateway.Endpoint);
    });

    it('should have the property address (base name: "address")', function() {
      // uncomment below and update the code to test the property address
      //var instance = new Gateway.Endpoint();
      //expect(instance).to.be();
    });

    it('should have the property connectionType (base name: "connectionType")', function() {
      // uncomment below and update the code to test the property connectionType
      //var instance = new Gateway.Endpoint();
      //expect(instance).to.be();
    });

    it('should have the property use (base name: "use")', function() {
      // uncomment below and update the code to test the property use
      //var instance = new Gateway.Endpoint();
      //expect(instance).to.be();
    });

  });

}));
