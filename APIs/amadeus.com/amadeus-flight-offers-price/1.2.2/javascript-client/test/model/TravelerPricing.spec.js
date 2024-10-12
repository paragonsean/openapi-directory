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
    instance = new FlightOffersPrice.TravelerPricing();
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

  describe('TravelerPricing', function() {
    it('should create an instance of TravelerPricing', function() {
      // uncomment below and update the code to test TravelerPricing
      //var instance = new FlightOffersPrice.TravelerPricing();
      //expect(instance).to.be.a(FlightOffersPrice.TravelerPricing);
    });

    it('should have the property associatedAdultId (base name: "associatedAdultId")', function() {
      // uncomment below and update the code to test the property associatedAdultId
      //var instance = new FlightOffersPrice.TravelerPricing();
      //expect(instance).to.be();
    });

    it('should have the property fareDetailsBySegment (base name: "fareDetailsBySegment")', function() {
      // uncomment below and update the code to test the property fareDetailsBySegment
      //var instance = new FlightOffersPrice.TravelerPricing();
      //expect(instance).to.be();
    });

    it('should have the property fareOption (base name: "fareOption")', function() {
      // uncomment below and update the code to test the property fareOption
      //var instance = new FlightOffersPrice.TravelerPricing();
      //expect(instance).to.be();
    });

    it('should have the property price (base name: "price")', function() {
      // uncomment below and update the code to test the property price
      //var instance = new FlightOffersPrice.TravelerPricing();
      //expect(instance).to.be();
    });

    it('should have the property travelerId (base name: "travelerId")', function() {
      // uncomment below and update the code to test the property travelerId
      //var instance = new FlightOffersPrice.TravelerPricing();
      //expect(instance).to.be();
    });

    it('should have the property travelerType (base name: "travelerType")', function() {
      // uncomment below and update the code to test the property travelerType
      //var instance = new FlightOffersPrice.TravelerPricing();
      //expect(instance).to.be();
    });

  });

}));
