/**
 * Branded Fares Upsell
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.0.1
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
    factory(root.expect, root.BrandedFaresUpsell);
  }
}(this, function(expect, BrandedFaresUpsell) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new BrandedFaresUpsell.Amenity();
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

  describe('Amenity', function() {
    it('should create an instance of Amenity', function() {
      // uncomment below and update the code to test Amenity
      //var instance = new BrandedFaresUpsell.Amenity();
      //expect(instance).to.be.a(BrandedFaresUpsell.Amenity);
    });

    it('should have the property amenityType (base name: "amenityType")', function() {
      // uncomment below and update the code to test the property amenityType
      //var instance = new BrandedFaresUpsell.Amenity();
      //expect(instance).to.be();
    });

    it('should have the property code (base name: "code")', function() {
      // uncomment below and update the code to test the property code
      //var instance = new BrandedFaresUpsell.Amenity();
      //expect(instance).to.be();
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new BrandedFaresUpsell.Amenity();
      //expect(instance).to.be();
    });

    it('should have the property isChargeable (base name: "isChargeable")', function() {
      // uncomment below and update the code to test the property isChargeable
      //var instance = new BrandedFaresUpsell.Amenity();
      //expect(instance).to.be();
    });

  });

}));
