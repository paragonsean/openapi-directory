/**
 * ClickMeter API
 * Api dashboard for ClickMeter API
 *
 * The version of the OpenAPI document: v2
 * Contact: api@clickmeter.com
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
    factory(root.expect, root.ClickMeterApi);
  }
}(this, function(expect, ClickMeterApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
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

  describe('ApiCoreDtoDatapointsTrackingLinkSpecifics', function() {
    it('should create an instance of ApiCoreDtoDatapointsTrackingLinkSpecifics', function() {
      // uncomment below and update the code to test ApiCoreDtoDatapointsTrackingLinkSpecifics
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be.a(ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics);
    });

    it('should have the property appendQuery (base name: "appendQuery")', function() {
      // uncomment below and update the code to test the property appendQuery
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

    it('should have the property browserDestinationItem (base name: "browserDestinationItem")', function() {
      // uncomment below and update the code to test the property browserDestinationItem
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

    it('should have the property destinationMode (base name: "destinationMode")', function() {
      // uncomment below and update the code to test the property destinationMode
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

    it('should have the property domainId (base name: "domainId")', function() {
      // uncomment below and update the code to test the property domainId
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

    it('should have the property encodeUrl (base name: "encodeUrl")', function() {
      // uncomment below and update the code to test the property encodeUrl
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

    it('should have the property expirationClicks (base name: "expirationClicks")', function() {
      // uncomment below and update the code to test the property expirationClicks
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

    it('should have the property expirationDate (base name: "expirationDate")', function() {
      // uncomment below and update the code to test the property expirationDate
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

    it('should have the property firstUrl (base name: "firstUrl")', function() {
      // uncomment below and update the code to test the property firstUrl
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

    it('should have the property goDomainId (base name: "goDomainId")', function() {
      // uncomment below and update the code to test the property goDomainId
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

    it('should have the property hideUrl (base name: "hideUrl")', function() {
      // uncomment below and update the code to test the property hideUrl
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

    it('should have the property hideUrlTitle (base name: "hideUrlTitle")', function() {
      // uncomment below and update the code to test the property hideUrlTitle
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

    it('should have the property isABTest (base name: "isABTest")', function() {
      // uncomment below and update the code to test the property isABTest
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

    it('should have the property password (base name: "password")', function() {
      // uncomment below and update the code to test the property password
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

    it('should have the property pauseAfterClicksExpiration (base name: "pauseAfterClicksExpiration")', function() {
      // uncomment below and update the code to test the property pauseAfterClicksExpiration
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

    it('should have the property pauseAfterDateExpiration (base name: "pauseAfterDateExpiration")', function() {
      // uncomment below and update the code to test the property pauseAfterDateExpiration
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

    it('should have the property randomDestinationItems (base name: "randomDestinationItems")', function() {
      // uncomment below and update the code to test the property randomDestinationItems
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

    it('should have the property redirectType (base name: "redirectType")', function() {
      // uncomment below and update the code to test the property redirectType
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

    it('should have the property referrerClean (base name: "referrerClean")', function() {
      // uncomment below and update the code to test the property referrerClean
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

    it('should have the property scripts (base name: "scripts")', function() {
      // uncomment below and update the code to test the property scripts
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

    it('should have the property sequentialDestinationItems (base name: "sequentialDestinationItems")', function() {
      // uncomment below and update the code to test the property sequentialDestinationItems
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

    it('should have the property spilloverDestinationItems (base name: "spilloverDestinationItems")', function() {
      // uncomment below and update the code to test the property spilloverDestinationItems
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

    it('should have the property uniqueDestinationItem (base name: "uniqueDestinationItem")', function() {
      // uncomment below and update the code to test the property uniqueDestinationItem
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

    it('should have the property url (base name: "url")', function() {
      // uncomment below and update the code to test the property url
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

    it('should have the property urlAfterClicksExpiration (base name: "urlAfterClicksExpiration")', function() {
      // uncomment below and update the code to test the property urlAfterClicksExpiration
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

    it('should have the property urlAfterDateExpiration (base name: "urlAfterDateExpiration")', function() {
      // uncomment below and update the code to test the property urlAfterDateExpiration
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

    it('should have the property urlsByLanguage (base name: "urlsByLanguage")', function() {
      // uncomment below and update the code to test the property urlsByLanguage
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

    it('should have the property urlsByNation (base name: "urlsByNation")', function() {
      // uncomment below and update the code to test the property urlsByNation
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

    it('should have the property weightedDestinationItems (base name: "weightedDestinationItems")', function() {
      // uncomment below and update the code to test the property weightedDestinationItems
      //var instance = new ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics();
      //expect(instance).to.be();
    });

  });

}));
