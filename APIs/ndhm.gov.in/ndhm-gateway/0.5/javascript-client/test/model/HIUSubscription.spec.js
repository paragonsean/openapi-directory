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
    instance = new Gateway.HIUSubscription();
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

  describe('HIUSubscription', function() {
    it('should create an instance of HIUSubscription', function() {
      // uncomment below and update the code to test HIUSubscription
      //var instance = new Gateway.HIUSubscription();
      //expect(instance).to.be.a(Gateway.HIUSubscription);
    });

    it('should have the property hiu (base name: "hiu")', function() {
      // uncomment below and update the code to test the property hiu
      //var instance = new Gateway.HIUSubscription();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new Gateway.HIUSubscription();
      //expect(instance).to.be();
    });

    it('should have the property patient (base name: "patient")', function() {
      // uncomment below and update the code to test the property patient
      //var instance = new Gateway.HIUSubscription();
      //expect(instance).to.be();
    });

    it('should have the property sources (base name: "sources")', function() {
      // uncomment below and update the code to test the property sources
      //var instance = new Gateway.HIUSubscription();
      //expect(instance).to.be();
    });

  });

}));
