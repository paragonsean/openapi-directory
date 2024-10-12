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
    instance = new BrandedFaresUpsell.AllotmentDetails();
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

  describe('AllotmentDetails', function() {
    it('should create an instance of AllotmentDetails', function() {
      // uncomment below and update the code to test AllotmentDetails
      //var instance = new BrandedFaresUpsell.AllotmentDetails();
      //expect(instance).to.be.a(BrandedFaresUpsell.AllotmentDetails);
    });

    it('should have the property tourName (base name: "tourName")', function() {
      // uncomment below and update the code to test the property tourName
      //var instance = new BrandedFaresUpsell.AllotmentDetails();
      //expect(instance).to.be();
    });

    it('should have the property tourReference (base name: "tourReference")', function() {
      // uncomment below and update the code to test the property tourReference
      //var instance = new BrandedFaresUpsell.AllotmentDetails();
      //expect(instance).to.be();
    });

  });

}));
