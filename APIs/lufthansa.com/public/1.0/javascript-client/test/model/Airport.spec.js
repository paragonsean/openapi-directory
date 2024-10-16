/**
 * LH Public API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
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
    factory(root.expect, root.LhPublicApi);
  }
}(this, function(expect, LhPublicApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new LhPublicApi.Airport();
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

  describe('Airport', function() {
    it('should create an instance of Airport', function() {
      // uncomment below and update the code to test Airport
      //var instance = new LhPublicApi.Airport();
      //expect(instance).to.be.a(LhPublicApi.Airport);
    });

    it('should have the property airportCode (base name: "AirportCode")', function() {
      // uncomment below and update the code to test the property airportCode
      //var instance = new LhPublicApi.Airport();
      //expect(instance).to.be();
    });

    it('should have the property cityCode (base name: "CityCode")', function() {
      // uncomment below and update the code to test the property cityCode
      //var instance = new LhPublicApi.Airport();
      //expect(instance).to.be();
    });

    it('should have the property countryCode (base name: "CountryCode")', function() {
      // uncomment below and update the code to test the property countryCode
      //var instance = new LhPublicApi.Airport();
      //expect(instance).to.be();
    });

    it('should have the property locationType (base name: "LocationType")', function() {
      // uncomment below and update the code to test the property locationType
      //var instance = new LhPublicApi.Airport();
      //expect(instance).to.be();
    });

    it('should have the property names (base name: "Names")', function() {
      // uncomment below and update the code to test the property names
      //var instance = new LhPublicApi.Airport();
      //expect(instance).to.be();
    });

    it('should have the property position (base name: "Position")', function() {
      // uncomment below and update the code to test the property position
      //var instance = new LhPublicApi.Airport();
      //expect(instance).to.be();
    });

    it('should have the property timeZoneId (base name: "TimeZoneId")', function() {
      // uncomment below and update the code to test the property timeZoneId
      //var instance = new LhPublicApi.Airport();
      //expect(instance).to.be();
    });

    it('should have the property utcOffset (base name: "UtcOffset")', function() {
      // uncomment below and update the code to test the property utcOffset
      //var instance = new LhPublicApi.Airport();
      //expect(instance).to.be();
    });

  });

}));
