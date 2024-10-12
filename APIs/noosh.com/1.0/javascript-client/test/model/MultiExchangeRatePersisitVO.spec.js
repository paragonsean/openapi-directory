/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
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
    factory(root.expect, root.NooshApiApplication);
  }
}(this, function(expect, NooshApiApplication) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NooshApiApplication.MultiExchangeRatePersisitVO();
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

  describe('MultiExchangeRatePersisitVO', function() {
    it('should create an instance of MultiExchangeRatePersisitVO', function() {
      // uncomment below and update the code to test MultiExchangeRatePersisitVO
      //var instance = new NooshApiApplication.MultiExchangeRatePersisitVO();
      //expect(instance).to.be.a(NooshApiApplication.MultiExchangeRatePersisitVO);
    });

    it('should have the property activateDate (base name: "activate_date")', function() {
      // uncomment below and update the code to test the property activateDate
      //var instance = new NooshApiApplication.MultiExchangeRatePersisitVO();
      //expect(instance).to.be();
    });

    it('should have the property buClientWorkgroupId (base name: "buClientWorkgroupId")', function() {
      // uncomment below and update the code to test the property buClientWorkgroupId
      //var instance = new NooshApiApplication.MultiExchangeRatePersisitVO();
      //expect(instance).to.be();
    });

    it('should have the property currency (base name: "currency")', function() {
      // uncomment below and update the code to test the property currency
      //var instance = new NooshApiApplication.MultiExchangeRatePersisitVO();
      //expect(instance).to.be();
    });

    it('should have the property rate (base name: "rate")', function() {
      // uncomment below and update the code to test the property rate
      //var instance = new NooshApiApplication.MultiExchangeRatePersisitVO();
      //expect(instance).to.be();
    });

    it('should have the property target (base name: "target")', function() {
      // uncomment below and update the code to test the property target
      //var instance = new NooshApiApplication.MultiExchangeRatePersisitVO();
      //expect(instance).to.be();
    });

  });

}));
