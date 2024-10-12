/**
 * Flight Offers Price
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.2.2
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
    factory(root.expect, root.FlightOffersPrice);
  }
}(this, function(expect, FlightOffersPrice) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new FlightOffersPrice.SuccessPricing();
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

  describe('SuccessPricing', function() {
    it('should create an instance of SuccessPricing', function() {
      // uncomment below and update the code to test SuccessPricing
      //var instance = new FlightOffersPrice.SuccessPricing();
      //expect(instance).to.be.a(FlightOffersPrice.SuccessPricing);
    });

    it('should have the property data (base name: "data")', function() {
      // uncomment below and update the code to test the property data
      //var instance = new FlightOffersPrice.SuccessPricing();
      //expect(instance).to.be();
    });

    it('should have the property dictionaries (base name: "dictionaries")', function() {
      // uncomment below and update the code to test the property dictionaries
      //var instance = new FlightOffersPrice.SuccessPricing();
      //expect(instance).to.be();
    });

    it('should have the property included (base name: "included")', function() {
      // uncomment below and update the code to test the property included
      //var instance = new FlightOffersPrice.SuccessPricing();
      //expect(instance).to.be();
    });

    it('should have the property warnings (base name: "warnings")', function() {
      // uncomment below and update the code to test the property warnings
      //var instance = new FlightOffersPrice.SuccessPricing();
      //expect(instance).to.be();
    });

  });

}));
