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
    instance = new TravelPartnerApi.SummarizeHotelViewsResponse();
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

  describe('SummarizeHotelViewsResponse', function() {
    it('should create an instance of SummarizeHotelViewsResponse', function() {
      // uncomment below and update the code to test SummarizeHotelViewsResponse
      //var instance = new TravelPartnerApi.SummarizeHotelViewsResponse();
      //expect(instance).to.be.a(TravelPartnerApi.SummarizeHotelViewsResponse);
    });

    it('should have the property lastFeedSubmissionTime (base name: "lastFeedSubmissionTime")', function() {
      // uncomment below and update the code to test the property lastFeedSubmissionTime
      //var instance = new TravelPartnerApi.SummarizeHotelViewsResponse();
      //expect(instance).to.be();
    });

    it('should have the property lastManifestUpdateTime (base name: "lastManifestUpdateTime")', function() {
      // uncomment below and update the code to test the property lastManifestUpdateTime
      //var instance = new TravelPartnerApi.SummarizeHotelViewsResponse();
      //expect(instance).to.be();
    });

    it('should have the property liveOnGooglePropertyCount (base name: "liveOnGooglePropertyCount")', function() {
      // uncomment below and update the code to test the property liveOnGooglePropertyCount
      //var instance = new TravelPartnerApi.SummarizeHotelViewsResponse();
      //expect(instance).to.be();
    });

    it('should have the property matchedPropertyCount (base name: "matchedPropertyCount")', function() {
      // uncomment below and update the code to test the property matchedPropertyCount
      //var instance = new TravelPartnerApi.SummarizeHotelViewsResponse();
      //expect(instance).to.be();
    });

    it('should have the property overclusteredPropertyCount (base name: "overclusteredPropertyCount")', function() {
      // uncomment below and update the code to test the property overclusteredPropertyCount
      //var instance = new TravelPartnerApi.SummarizeHotelViewsResponse();
      //expect(instance).to.be();
    });

    it('should have the property overclusteredPropertyWithErrorsCount (base name: "overclusteredPropertyWithErrorsCount")', function() {
      // uncomment below and update the code to test the property overclusteredPropertyWithErrorsCount
      //var instance = new TravelPartnerApi.SummarizeHotelViewsResponse();
      //expect(instance).to.be();
    });

    it('should have the property unmatchedPropertyCount (base name: "unmatchedPropertyCount")', function() {
      // uncomment below and update the code to test the property unmatchedPropertyCount
      //var instance = new TravelPartnerApi.SummarizeHotelViewsResponse();
      //expect(instance).to.be();
    });

    it('should have the property unmatchedPropertyWithErrorsCount (base name: "unmatchedPropertyWithErrorsCount")', function() {
      // uncomment below and update the code to test the property unmatchedPropertyWithErrorsCount
      //var instance = new TravelPartnerApi.SummarizeHotelViewsResponse();
      //expect(instance).to.be();
    });

  });

}));
