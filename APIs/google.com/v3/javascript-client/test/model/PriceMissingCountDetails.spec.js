/**
 * Travel Partner API
 * The Travel Partner API provides you with a RESTful interface to the Google Hotel Center platform. It enables an app to efficiently retrieve and change Hotel Center data, and is thus suitable for managing large or complex accounts.
 *
 * The version of the OpenAPI document: v3
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
    factory(root.expect, root.TravelPartnerApi);
  }
}(this, function(expect, TravelPartnerApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new TravelPartnerApi.PriceMissingCountDetails();
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

  describe('PriceMissingCountDetails', function() {
    it('should create an instance of PriceMissingCountDetails', function() {
      // uncomment below and update the code to test PriceMissingCountDetails
      //var instance = new TravelPartnerApi.PriceMissingCountDetails();
      //expect(instance).to.be.a(TravelPartnerApi.PriceMissingCountDetails);
    });

    it('should have the property bandwidthDepletedCount (base name: "bandwidthDepletedCount")', function() {
      // uncomment below and update the code to test the property bandwidthDepletedCount
      //var instance = new TravelPartnerApi.PriceMissingCountDetails();
      //expect(instance).to.be();
    });

    it('should have the property cacheRateMissingCount (base name: "cacheRateMissingCount")', function() {
      // uncomment below and update the code to test the property cacheRateMissingCount
      //var instance = new TravelPartnerApi.PriceMissingCountDetails();
      //expect(instance).to.be();
    });

    it('should have the property itineraryBlockedCount (base name: "itineraryBlockedCount")', function() {
      // uncomment below and update the code to test the property itineraryBlockedCount
      //var instance = new TravelPartnerApi.PriceMissingCountDetails();
      //expect(instance).to.be();
    });

    it('should have the property livePricingErrorCount (base name: "livePricingErrorCount")', function() {
      // uncomment below and update the code to test the property livePricingErrorCount
      //var instance = new TravelPartnerApi.PriceMissingCountDetails();
      //expect(instance).to.be();
    });

    it('should have the property livePricingNotSetupCount (base name: "livePricingNotSetupCount")', function() {
      // uncomment below and update the code to test the property livePricingNotSetupCount
      //var instance = new TravelPartnerApi.PriceMissingCountDetails();
      //expect(instance).to.be();
    });

    it('should have the property livePricingTimeoutCount (base name: "livePricingTimeoutCount")', function() {
      // uncomment below and update the code to test the property livePricingTimeoutCount
      //var instance = new TravelPartnerApi.PriceMissingCountDetails();
      //expect(instance).to.be();
    });

  });

}));
