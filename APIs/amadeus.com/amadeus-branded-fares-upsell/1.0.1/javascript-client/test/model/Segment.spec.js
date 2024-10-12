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
    instance = new BrandedFaresUpsell.Segment();
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

  describe('Segment', function() {
    it('should create an instance of Segment', function() {
      // uncomment below and update the code to test Segment
      //var instance = new BrandedFaresUpsell.Segment();
      //expect(instance).to.be.a(BrandedFaresUpsell.Segment);
    });

    it('should have the property aircraft (base name: "aircraft")', function() {
      // uncomment below and update the code to test the property aircraft
      //var instance = new BrandedFaresUpsell.Segment();
      //expect(instance).to.be();
    });

    it('should have the property arrival (base name: "arrival")', function() {
      // uncomment below and update the code to test the property arrival
      //var instance = new BrandedFaresUpsell.Segment();
      //expect(instance).to.be();
    });

    it('should have the property carrierCode (base name: "carrierCode")', function() {
      // uncomment below and update the code to test the property carrierCode
      //var instance = new BrandedFaresUpsell.Segment();
      //expect(instance).to.be();
    });

    it('should have the property departure (base name: "departure")', function() {
      // uncomment below and update the code to test the property departure
      //var instance = new BrandedFaresUpsell.Segment();
      //expect(instance).to.be();
    });

    it('should have the property duration (base name: "duration")', function() {
      // uncomment below and update the code to test the property duration
      //var instance = new BrandedFaresUpsell.Segment();
      //expect(instance).to.be();
    });

    it('should have the property number (base name: "number")', function() {
      // uncomment below and update the code to test the property number
      //var instance = new BrandedFaresUpsell.Segment();
      //expect(instance).to.be();
    });

    it('should have the property operating (base name: "operating")', function() {
      // uncomment below and update the code to test the property operating
      //var instance = new BrandedFaresUpsell.Segment();
      //expect(instance).to.be();
    });

    it('should have the property stops (base name: "stops")', function() {
      // uncomment below and update the code to test the property stops
      //var instance = new BrandedFaresUpsell.Segment();
      //expect(instance).to.be();
    });

    it('should have the property blacklistedInEU (base name: "blacklistedInEU")', function() {
      // uncomment below and update the code to test the property blacklistedInEU
      //var instance = new BrandedFaresUpsell.Segment();
      //expect(instance).to.be();
    });

    it('should have the property co2Emissions (base name: "co2Emissions")', function() {
      // uncomment below and update the code to test the property co2Emissions
      //var instance = new BrandedFaresUpsell.Segment();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new BrandedFaresUpsell.Segment();
      //expect(instance).to.be();
    });

    it('should have the property numberOfStops (base name: "numberOfStops")', function() {
      // uncomment below and update the code to test the property numberOfStops
      //var instance = new BrandedFaresUpsell.Segment();
      //expect(instance).to.be();
    });

  });

}));
