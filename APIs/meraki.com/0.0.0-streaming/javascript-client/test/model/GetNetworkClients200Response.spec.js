/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 23 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 0.0.0-streaming
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
    instance = new MerakiDashboardApi.GetNetworkClients200Response();
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

  describe('GetNetworkClients200Response', function() {
    it('should create an instance of GetNetworkClients200Response', function() {
      // uncomment below and update the code to test GetNetworkClients200Response
      //var instance = new MerakiDashboardApi.GetNetworkClients200Response();
      //expect(instance).to.be.a(MerakiDashboardApi.GetNetworkClients200Response);
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new MerakiDashboardApi.GetNetworkClients200Response();
      //expect(instance).to.be();
    });

    it('should have the property firstSeen (base name: "firstSeen")', function() {
      // uncomment below and update the code to test the property firstSeen
      //var instance = new MerakiDashboardApi.GetNetworkClients200Response();
      //expect(instance).to.be();
    });

    it('should have the property groupPolicy8021x (base name: "groupPolicy8021x")', function() {
      // uncomment below and update the code to test the property groupPolicy8021x
      //var instance = new MerakiDashboardApi.GetNetworkClients200Response();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new MerakiDashboardApi.GetNetworkClients200Response();
      //expect(instance).to.be();
    });

    it('should have the property ip (base name: "ip")', function() {
      // uncomment below and update the code to test the property ip
      //var instance = new MerakiDashboardApi.GetNetworkClients200Response();
      //expect(instance).to.be();
    });

    it('should have the property ip6 (base name: "ip6")', function() {
      // uncomment below and update the code to test the property ip6
      //var instance = new MerakiDashboardApi.GetNetworkClients200Response();
      //expect(instance).to.be();
    });

    it('should have the property ip6Local (base name: "ip6Local")', function() {
      // uncomment below and update the code to test the property ip6Local
      //var instance = new MerakiDashboardApi.GetNetworkClients200Response();
      //expect(instance).to.be();
    });

    it('should have the property lastSeen (base name: "lastSeen")', function() {
      // uncomment below and update the code to test the property lastSeen
      //var instance = new MerakiDashboardApi.GetNetworkClients200Response();
      //expect(instance).to.be();
    });

    it('should have the property mac (base name: "mac")', function() {
      // uncomment below and update the code to test the property mac
      //var instance = new MerakiDashboardApi.GetNetworkClients200Response();
      //expect(instance).to.be();
    });

    it('should have the property manufacturer (base name: "manufacturer")', function() {
      // uncomment below and update the code to test the property manufacturer
      //var instance = new MerakiDashboardApi.GetNetworkClients200Response();
      //expect(instance).to.be();
    });

    it('should have the property notes (base name: "notes")', function() {
      // uncomment below and update the code to test the property notes
      //var instance = new MerakiDashboardApi.GetNetworkClients200Response();
      //expect(instance).to.be();
    });

    it('should have the property os (base name: "os")', function() {
      // uncomment below and update the code to test the property os
      //var instance = new MerakiDashboardApi.GetNetworkClients200Response();
      //expect(instance).to.be();
    });

    it('should have the property recentDeviceMac (base name: "recentDeviceMac")', function() {
      // uncomment below and update the code to test the property recentDeviceMac
      //var instance = new MerakiDashboardApi.GetNetworkClients200Response();
      //expect(instance).to.be();
    });

    it('should have the property recentDeviceName (base name: "recentDeviceName")', function() {
      // uncomment below and update the code to test the property recentDeviceName
      //var instance = new MerakiDashboardApi.GetNetworkClients200Response();
      //expect(instance).to.be();
    });

    it('should have the property recentDeviceSerial (base name: "recentDeviceSerial")', function() {
      // uncomment below and update the code to test the property recentDeviceSerial
      //var instance = new MerakiDashboardApi.GetNetworkClients200Response();
      //expect(instance).to.be();
    });

    it('should have the property smInstalled (base name: "smInstalled")', function() {
      // uncomment below and update the code to test the property smInstalled
      //var instance = new MerakiDashboardApi.GetNetworkClients200Response();
      //expect(instance).to.be();
    });

    it('should have the property ssid (base name: "ssid")', function() {
      // uncomment below and update the code to test the property ssid
      //var instance = new MerakiDashboardApi.GetNetworkClients200Response();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new MerakiDashboardApi.GetNetworkClients200Response();
      //expect(instance).to.be();
    });

    it('should have the property switchport (base name: "switchport")', function() {
      // uncomment below and update the code to test the property switchport
      //var instance = new MerakiDashboardApi.GetNetworkClients200Response();
      //expect(instance).to.be();
    });

    it('should have the property usage (base name: "usage")', function() {
      // uncomment below and update the code to test the property usage
      //var instance = new MerakiDashboardApi.GetNetworkClients200Response();
      //expect(instance).to.be();
    });

    it('should have the property user (base name: "user")', function() {
      // uncomment below and update the code to test the property user
      //var instance = new MerakiDashboardApi.GetNetworkClients200Response();
      //expect(instance).to.be();
    });

    it('should have the property vlan (base name: "vlan")', function() {
      // uncomment below and update the code to test the property vlan
      //var instance = new MerakiDashboardApi.GetNetworkClients200Response();
      //expect(instance).to.be();
    });

  });

}));
