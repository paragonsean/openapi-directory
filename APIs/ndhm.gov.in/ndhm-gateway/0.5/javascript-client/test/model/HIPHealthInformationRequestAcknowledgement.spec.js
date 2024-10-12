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
    instance = new Gateway.HIPHealthInformationRequestAcknowledgement();
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

  describe('HIPHealthInformationRequestAcknowledgement', function() {
    it('should create an instance of HIPHealthInformationRequestAcknowledgement', function() {
      // uncomment below and update the code to test HIPHealthInformationRequestAcknowledgement
      //var instance = new Gateway.HIPHealthInformationRequestAcknowledgement();
      //expect(instance).to.be.a(Gateway.HIPHealthInformationRequestAcknowledgement);
    });

    it('should have the property error (base name: "error")', function() {
      // uncomment below and update the code to test the property error
      //var instance = new Gateway.HIPHealthInformationRequestAcknowledgement();
      //expect(instance).to.be();
    });

    it('should have the property hiRequest (base name: "hiRequest")', function() {
      // uncomment below and update the code to test the property hiRequest
      //var instance = new Gateway.HIPHealthInformationRequestAcknowledgement();
      //expect(instance).to.be();
    });

    it('should have the property requestId (base name: "requestId")', function() {
      // uncomment below and update the code to test the property requestId
      //var instance = new Gateway.HIPHealthInformationRequestAcknowledgement();
      //expect(instance).to.be();
    });

    it('should have the property resp (base name: "resp")', function() {
      // uncomment below and update the code to test the property resp
      //var instance = new Gateway.HIPHealthInformationRequestAcknowledgement();
      //expect(instance).to.be();
    });

    it('should have the property timestamp (base name: "timestamp")', function() {
      // uncomment below and update the code to test the property timestamp
      //var instance = new Gateway.HIPHealthInformationRequestAcknowledgement();
      //expect(instance).to.be();
    });

  });

}));
