/**
 * Hotel Search API
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production for this API it may change dynamically. For your tests, use big cities like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 3.0.8
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
    factory(root.expect, root.HotelSearchApi);
  }
}(this, function(expect, HotelSearchApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new HotelSearchApi.HotelProductCancellationPolicy();
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

  describe('HotelProductCancellationPolicy', function() {
    it('should create an instance of HotelProductCancellationPolicy', function() {
      // uncomment below and update the code to test HotelProductCancellationPolicy
      //var instance = new HotelSearchApi.HotelProductCancellationPolicy();
      //expect(instance).to.be.a(HotelSearchApi.HotelProductCancellationPolicy);
    });

    it('should have the property amount (base name: "amount")', function() {
      // uncomment below and update the code to test the property amount
      //var instance = new HotelSearchApi.HotelProductCancellationPolicy();
      //expect(instance).to.be();
    });

    it('should have the property deadline (base name: "deadline")', function() {
      // uncomment below and update the code to test the property deadline
      //var instance = new HotelSearchApi.HotelProductCancellationPolicy();
      //expect(instance).to.be();
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new HotelSearchApi.HotelProductCancellationPolicy();
      //expect(instance).to.be();
    });

    it('should have the property numberOfNights (base name: "numberOfNights")', function() {
      // uncomment below and update the code to test the property numberOfNights
      //var instance = new HotelSearchApi.HotelProductCancellationPolicy();
      //expect(instance).to.be();
    });

    it('should have the property percentage (base name: "percentage")', function() {
      // uncomment below and update the code to test the property percentage
      //var instance = new HotelSearchApi.HotelProductCancellationPolicy();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new HotelSearchApi.HotelProductCancellationPolicy();
      //expect(instance).to.be();
    });

  });

}));
