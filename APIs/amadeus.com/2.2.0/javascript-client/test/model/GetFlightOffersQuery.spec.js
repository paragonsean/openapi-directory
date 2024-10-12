/**
 * Flight Offers Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 2.2.0
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
    factory(root.expect, root.FlightOffersSearch);
  }
}(this, function(expect, FlightOffersSearch) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new FlightOffersSearch.GetFlightOffersQuery();
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

  describe('GetFlightOffersQuery', function() {
    it('should create an instance of GetFlightOffersQuery', function() {
      // uncomment below and update the code to test GetFlightOffersQuery
      //var instance = new FlightOffersSearch.GetFlightOffersQuery();
      //expect(instance).to.be.a(FlightOffersSearch.GetFlightOffersQuery);
    });

    it('should have the property currencyCode (base name: "currencyCode")', function() {
      // uncomment below and update the code to test the property currencyCode
      //var instance = new FlightOffersSearch.GetFlightOffersQuery();
      //expect(instance).to.be();
    });

    it('should have the property originDestinations (base name: "originDestinations")', function() {
      // uncomment below and update the code to test the property originDestinations
      //var instance = new FlightOffersSearch.GetFlightOffersQuery();
      //expect(instance).to.be();
    });

    it('should have the property searchCriteria (base name: "searchCriteria")', function() {
      // uncomment below and update the code to test the property searchCriteria
      //var instance = new FlightOffersSearch.GetFlightOffersQuery();
      //expect(instance).to.be();
    });

    it('should have the property sources (base name: "sources")', function() {
      // uncomment below and update the code to test the property sources
      //var instance = new FlightOffersSearch.GetFlightOffersQuery();
      //expect(instance).to.be();
    });

    it('should have the property travelers (base name: "travelers")', function() {
      // uncomment below and update the code to test the property travelers
      //var instance = new FlightOffersSearch.GetFlightOffersQuery();
      //expect(instance).to.be();
    });

  });

}));
