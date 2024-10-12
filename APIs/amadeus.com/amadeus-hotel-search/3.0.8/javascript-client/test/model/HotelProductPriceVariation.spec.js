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
    instance = new HotelSearchApi.HotelProductPriceVariation();
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

  describe('HotelProductPriceVariation', function() {
    it('should create an instance of HotelProductPriceVariation', function() {
      // uncomment below and update the code to test HotelProductPriceVariation
      //var instance = new HotelSearchApi.HotelProductPriceVariation();
      //expect(instance).to.be.a(HotelSearchApi.HotelProductPriceVariation);
    });

    it('should have the property base (base name: "base")', function() {
      // uncomment below and update the code to test the property base
      //var instance = new HotelSearchApi.HotelProductPriceVariation();
      //expect(instance).to.be();
    });

    it('should have the property currency (base name: "currency")', function() {
      // uncomment below and update the code to test the property currency
      //var instance = new HotelSearchApi.HotelProductPriceVariation();
      //expect(instance).to.be();
    });

    it('should have the property endDate (base name: "endDate")', function() {
      // uncomment below and update the code to test the property endDate
      //var instance = new HotelSearchApi.HotelProductPriceVariation();
      //expect(instance).to.be();
    });

    it('should have the property markups (base name: "markups")', function() {
      // uncomment below and update the code to test the property markups
      //var instance = new HotelSearchApi.HotelProductPriceVariation();
      //expect(instance).to.be();
    });

    it('should have the property sellingTotal (base name: "sellingTotal")', function() {
      // uncomment below and update the code to test the property sellingTotal
      //var instance = new HotelSearchApi.HotelProductPriceVariation();
      //expect(instance).to.be();
    });

    it('should have the property startDate (base name: "startDate")', function() {
      // uncomment below and update the code to test the property startDate
      //var instance = new HotelSearchApi.HotelProductPriceVariation();
      //expect(instance).to.be();
    });

    it('should have the property total (base name: "total")', function() {
      // uncomment below and update the code to test the property total
      //var instance = new HotelSearchApi.HotelProductPriceVariation();
      //expect(instance).to.be();
    });

  });

}));
