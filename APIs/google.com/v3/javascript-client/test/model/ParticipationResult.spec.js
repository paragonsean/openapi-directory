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
    instance = new TravelPartnerApi.ParticipationResult();
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

  describe('ParticipationResult', function() {
    it('should create an instance of ParticipationResult', function() {
      // uncomment below and update the code to test ParticipationResult
      //var instance = new TravelPartnerApi.ParticipationResult();
      //expect(instance).to.be.a(TravelPartnerApi.ParticipationResult);
    });

    it('should have the property key (base name: "key")', function() {
      // uncomment below and update the code to test the property key
      //var instance = new TravelPartnerApi.ParticipationResult();
      //expect(instance).to.be();
    });

    it('should have the property missedParticipationCount (base name: "missedParticipationCount")', function() {
      // uncomment below and update the code to test the property missedParticipationCount
      //var instance = new TravelPartnerApi.ParticipationResult();
      //expect(instance).to.be();
    });

    it('should have the property missedParticipationCountDetails (base name: "missedParticipationCountDetails")', function() {
      // uncomment below and update the code to test the property missedParticipationCountDetails
      //var instance = new TravelPartnerApi.ParticipationResult();
      //expect(instance).to.be();
    });

    it('should have the property opportunityCount (base name: "opportunityCount")', function() {
      // uncomment below and update the code to test the property opportunityCount
      //var instance = new TravelPartnerApi.ParticipationResult();
      //expect(instance).to.be();
    });

    it('should have the property participationCount (base name: "participationCount")', function() {
      // uncomment below and update the code to test the property participationCount
      //var instance = new TravelPartnerApi.ParticipationResult();
      //expect(instance).to.be();
    });

    it('should have the property participationPercent (base name: "participationPercent")', function() {
      // uncomment below and update the code to test the property participationPercent
      //var instance = new TravelPartnerApi.ParticipationResult();
      //expect(instance).to.be();
    });

    it('should have the property partnerHotelDisplayName (base name: "partnerHotelDisplayName")', function() {
      // uncomment below and update the code to test the property partnerHotelDisplayName
      //var instance = new TravelPartnerApi.ParticipationResult();
      //expect(instance).to.be();
    });

  });

}));
