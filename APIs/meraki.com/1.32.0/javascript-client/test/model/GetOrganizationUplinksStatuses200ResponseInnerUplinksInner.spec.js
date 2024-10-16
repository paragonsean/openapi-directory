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
    instance = new MerakiDashboardApi.GetOrganizationUplinksStatuses200ResponseInnerUplinksInner();
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

  describe('GetOrganizationUplinksStatuses200ResponseInnerUplinksInner', function() {
    it('should create an instance of GetOrganizationUplinksStatuses200ResponseInnerUplinksInner', function() {
      // uncomment below and update the code to test GetOrganizationUplinksStatuses200ResponseInnerUplinksInner
      //var instance = new MerakiDashboardApi.GetOrganizationUplinksStatuses200ResponseInnerUplinksInner();
      //expect(instance).to.be.a(MerakiDashboardApi.GetOrganizationUplinksStatuses200ResponseInnerUplinksInner);
    });

    it('should have the property apn (base name: "apn")', function() {
      // uncomment below and update the code to test the property apn
      //var instance = new MerakiDashboardApi.GetOrganizationUplinksStatuses200ResponseInnerUplinksInner();
      //expect(instance).to.be();
    });

    it('should have the property connectionType (base name: "connectionType")', function() {
      // uncomment below and update the code to test the property connectionType
      //var instance = new MerakiDashboardApi.GetOrganizationUplinksStatuses200ResponseInnerUplinksInner();
      //expect(instance).to.be();
    });

    it('should have the property dns1 (base name: "dns1")', function() {
      // uncomment below and update the code to test the property dns1
      //var instance = new MerakiDashboardApi.GetOrganizationUplinksStatuses200ResponseInnerUplinksInner();
      //expect(instance).to.be();
    });

    it('should have the property dns2 (base name: "dns2")', function() {
      // uncomment below and update the code to test the property dns2
      //var instance = new MerakiDashboardApi.GetOrganizationUplinksStatuses200ResponseInnerUplinksInner();
      //expect(instance).to.be();
    });

    it('should have the property gateway (base name: "gateway")', function() {
      // uncomment below and update the code to test the property gateway
      //var instance = new MerakiDashboardApi.GetOrganizationUplinksStatuses200ResponseInnerUplinksInner();
      //expect(instance).to.be();
    });

    it('should have the property iccid (base name: "iccid")', function() {
      // uncomment below and update the code to test the property iccid
      //var instance = new MerakiDashboardApi.GetOrganizationUplinksStatuses200ResponseInnerUplinksInner();
      //expect(instance).to.be();
    });

    it('should have the property _interface (base name: "interface")', function() {
      // uncomment below and update the code to test the property _interface
      //var instance = new MerakiDashboardApi.GetOrganizationUplinksStatuses200ResponseInnerUplinksInner();
      //expect(instance).to.be();
    });

    it('should have the property ip (base name: "ip")', function() {
      // uncomment below and update the code to test the property ip
      //var instance = new MerakiDashboardApi.GetOrganizationUplinksStatuses200ResponseInnerUplinksInner();
      //expect(instance).to.be();
    });

    it('should have the property ipAssignedBy (base name: "ipAssignedBy")', function() {
      // uncomment below and update the code to test the property ipAssignedBy
      //var instance = new MerakiDashboardApi.GetOrganizationUplinksStatuses200ResponseInnerUplinksInner();
      //expect(instance).to.be();
    });

    it('should have the property primaryDns (base name: "primaryDns")', function() {
      // uncomment below and update the code to test the property primaryDns
      //var instance = new MerakiDashboardApi.GetOrganizationUplinksStatuses200ResponseInnerUplinksInner();
      //expect(instance).to.be();
    });

    it('should have the property provider (base name: "provider")', function() {
      // uncomment below and update the code to test the property provider
      //var instance = new MerakiDashboardApi.GetOrganizationUplinksStatuses200ResponseInnerUplinksInner();
      //expect(instance).to.be();
    });

    it('should have the property publicIp (base name: "publicIp")', function() {
      // uncomment below and update the code to test the property publicIp
      //var instance = new MerakiDashboardApi.GetOrganizationUplinksStatuses200ResponseInnerUplinksInner();
      //expect(instance).to.be();
    });

    it('should have the property secondaryDns (base name: "secondaryDns")', function() {
      // uncomment below and update the code to test the property secondaryDns
      //var instance = new MerakiDashboardApi.GetOrganizationUplinksStatuses200ResponseInnerUplinksInner();
      //expect(instance).to.be();
    });

    it('should have the property signalStat (base name: "signalStat")', function() {
      // uncomment below and update the code to test the property signalStat
      //var instance = new MerakiDashboardApi.GetOrganizationUplinksStatuses200ResponseInnerUplinksInner();
      //expect(instance).to.be();
    });

    it('should have the property signalType (base name: "signalType")', function() {
      // uncomment below and update the code to test the property signalType
      //var instance = new MerakiDashboardApi.GetOrganizationUplinksStatuses200ResponseInnerUplinksInner();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new MerakiDashboardApi.GetOrganizationUplinksStatuses200ResponseInnerUplinksInner();
      //expect(instance).to.be();
    });

  });

}));
