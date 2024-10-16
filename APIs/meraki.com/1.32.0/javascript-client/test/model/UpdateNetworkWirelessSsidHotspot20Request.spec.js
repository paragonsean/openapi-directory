/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
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
    factory(root.expect, root.MerakiDashboardApi);
  }
}(this, function(expect, MerakiDashboardApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidHotspot20Request();
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

  describe('UpdateNetworkWirelessSsidHotspot20Request', function() {
    it('should create an instance of UpdateNetworkWirelessSsidHotspot20Request', function() {
      // uncomment below and update the code to test UpdateNetworkWirelessSsidHotspot20Request
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidHotspot20Request();
      //expect(instance).to.be.a(MerakiDashboardApi.UpdateNetworkWirelessSsidHotspot20Request);
    });

    it('should have the property domains (base name: "domains")', function() {
      // uncomment below and update the code to test the property domains
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidHotspot20Request();
      //expect(instance).to.be();
    });

    it('should have the property enabled (base name: "enabled")', function() {
      // uncomment below and update the code to test the property enabled
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidHotspot20Request();
      //expect(instance).to.be();
    });

    it('should have the property mccMncs (base name: "mccMncs")', function() {
      // uncomment below and update the code to test the property mccMncs
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidHotspot20Request();
      //expect(instance).to.be();
    });

    it('should have the property naiRealms (base name: "naiRealms")', function() {
      // uncomment below and update the code to test the property naiRealms
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidHotspot20Request();
      //expect(instance).to.be();
    });

    it('should have the property networkAccessType (base name: "networkAccessType")', function() {
      // uncomment below and update the code to test the property networkAccessType
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidHotspot20Request();
      //expect(instance).to.be();
    });

    it('should have the property operator (base name: "operator")', function() {
      // uncomment below and update the code to test the property operator
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidHotspot20Request();
      //expect(instance).to.be();
    });

    it('should have the property roamConsortOis (base name: "roamConsortOis")', function() {
      // uncomment below and update the code to test the property roamConsortOis
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidHotspot20Request();
      //expect(instance).to.be();
    });

    it('should have the property venue (base name: "venue")', function() {
      // uncomment below and update the code to test the property venue
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidHotspot20Request();
      //expect(instance).to.be();
    });

  });

}));
