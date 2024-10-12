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
    instance = new TravelPartnerApi.MissedParticipationCountDetails();
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

  describe('MissedParticipationCountDetails', function() {
    it('should create an instance of MissedParticipationCountDetails', function() {
      // uncomment below and update the code to test MissedParticipationCountDetails
      //var instance = new TravelPartnerApi.MissedParticipationCountDetails();
      //expect(instance).to.be.a(TravelPartnerApi.MissedParticipationCountDetails);
    });

    it('should have the property hotelSuspendedCount (base name: "hotelSuspendedCount")', function() {
      // uncomment below and update the code to test the property hotelSuspendedCount
      //var instance = new TravelPartnerApi.MissedParticipationCountDetails();
      //expect(instance).to.be();
    });

    it('should have the property noAvailabilityCount (base name: "noAvailabilityCount")', function() {
      // uncomment below and update the code to test the property noAvailabilityCount
      //var instance = new TravelPartnerApi.MissedParticipationCountDetails();
      //expect(instance).to.be();
    });

    it('should have the property noLandingPageCount (base name: "noLandingPageCount")', function() {
      // uncomment below and update the code to test the property noLandingPageCount
      //var instance = new TravelPartnerApi.MissedParticipationCountDetails();
      //expect(instance).to.be();
    });

    it('should have the property noPriceCount (base name: "noPriceCount")', function() {
      // uncomment below and update the code to test the property noPriceCount
      //var instance = new TravelPartnerApi.MissedParticipationCountDetails();
      //expect(instance).to.be();
    });

    it('should have the property noPriceCountDetails (base name: "noPriceCountDetails")', function() {
      // uncomment below and update the code to test the property noPriceCountDetails
      //var instance = new TravelPartnerApi.MissedParticipationCountDetails();
      //expect(instance).to.be();
    });

    it('should have the property noTaxBreakdownCount (base name: "noTaxBreakdownCount")', function() {
      // uncomment below and update the code to test the property noTaxBreakdownCount
      //var instance = new TravelPartnerApi.MissedParticipationCountDetails();
      //expect(instance).to.be();
    });

    it('should have the property otherReasonCount (base name: "otherReasonCount")', function() {
      // uncomment below and update the code to test the property otherReasonCount
      //var instance = new TravelPartnerApi.MissedParticipationCountDetails();
      //expect(instance).to.be();
    });

    it('should have the property priceMissingCount (base name: "priceMissingCount")', function() {
      // uncomment below and update the code to test the property priceMissingCount
      //var instance = new TravelPartnerApi.MissedParticipationCountDetails();
      //expect(instance).to.be();
    });

    it('should have the property priceMissingCountDetails (base name: "priceMissingCountDetails")', function() {
      // uncomment below and update the code to test the property priceMissingCountDetails
      //var instance = new TravelPartnerApi.MissedParticipationCountDetails();
      //expect(instance).to.be();
    });

    it('should have the property priceProblemCount (base name: "priceProblemCount")', function() {
      // uncomment below and update the code to test the property priceProblemCount
      //var instance = new TravelPartnerApi.MissedParticipationCountDetails();
      //expect(instance).to.be();
    });

    it('should have the property priceProblemCountDetails (base name: "priceProblemCountDetails")', function() {
      // uncomment below and update the code to test the property priceProblemCountDetails
      //var instance = new TravelPartnerApi.MissedParticipationCountDetails();
      //expect(instance).to.be();
    });

    it('should have the property priceUnavailableCount (base name: "priceUnavailableCount")', function() {
      // uncomment below and update the code to test the property priceUnavailableCount
      //var instance = new TravelPartnerApi.MissedParticipationCountDetails();
      //expect(instance).to.be();
    });

    it('should have the property priceUnavailableCountDetails (base name: "priceUnavailableCountDetails")', function() {
      // uncomment below and update the code to test the property priceUnavailableCountDetails
      //var instance = new TravelPartnerApi.MissedParticipationCountDetails();
      //expect(instance).to.be();
    });

  });

}));
