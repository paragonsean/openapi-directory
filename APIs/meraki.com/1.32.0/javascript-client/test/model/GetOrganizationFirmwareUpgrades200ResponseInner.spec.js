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
    instance = new MerakiDashboardApi.GetOrganizationFirmwareUpgrades200ResponseInner();
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

  describe('GetOrganizationFirmwareUpgrades200ResponseInner', function() {
    it('should create an instance of GetOrganizationFirmwareUpgrades200ResponseInner', function() {
      // uncomment below and update the code to test GetOrganizationFirmwareUpgrades200ResponseInner
      //var instance = new MerakiDashboardApi.GetOrganizationFirmwareUpgrades200ResponseInner();
      //expect(instance).to.be.a(MerakiDashboardApi.GetOrganizationFirmwareUpgrades200ResponseInner);
    });

    it('should have the property completedAt (base name: "completedAt")', function() {
      // uncomment below and update the code to test the property completedAt
      //var instance = new MerakiDashboardApi.GetOrganizationFirmwareUpgrades200ResponseInner();
      //expect(instance).to.be();
    });

    it('should have the property fromVersion (base name: "fromVersion")', function() {
      // uncomment below and update the code to test the property fromVersion
      //var instance = new MerakiDashboardApi.GetOrganizationFirmwareUpgrades200ResponseInner();
      //expect(instance).to.be();
    });

    it('should have the property network (base name: "network")', function() {
      // uncomment below and update the code to test the property network
      //var instance = new MerakiDashboardApi.GetOrganizationFirmwareUpgrades200ResponseInner();
      //expect(instance).to.be();
    });

    it('should have the property productType (base name: "productType")', function() {
      // uncomment below and update the code to test the property productType
      //var instance = new MerakiDashboardApi.GetOrganizationFirmwareUpgrades200ResponseInner();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new MerakiDashboardApi.GetOrganizationFirmwareUpgrades200ResponseInner();
      //expect(instance).to.be();
    });

    it('should have the property time (base name: "time")', function() {
      // uncomment below and update the code to test the property time
      //var instance = new MerakiDashboardApi.GetOrganizationFirmwareUpgrades200ResponseInner();
      //expect(instance).to.be();
    });

    it('should have the property toVersion (base name: "toVersion")', function() {
      // uncomment below and update the code to test the property toVersion
      //var instance = new MerakiDashboardApi.GetOrganizationFirmwareUpgrades200ResponseInner();
      //expect(instance).to.be();
    });

    it('should have the property upgradeBatchId (base name: "upgradeBatchId")', function() {
      // uncomment below and update the code to test the property upgradeBatchId
      //var instance = new MerakiDashboardApi.GetOrganizationFirmwareUpgrades200ResponseInner();
      //expect(instance).to.be();
    });

    it('should have the property upgradeId (base name: "upgradeId")', function() {
      // uncomment below and update the code to test the property upgradeId
      //var instance = new MerakiDashboardApi.GetOrganizationFirmwareUpgrades200ResponseInner();
      //expect(instance).to.be();
    });

  });

}));
