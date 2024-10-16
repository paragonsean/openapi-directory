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
    instance = new MerakiDashboardApi.GetNetworkSmDeviceNetworkAdapters200ResponseInner();
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

  describe('GetNetworkSmDeviceNetworkAdapters200ResponseInner', function() {
    it('should create an instance of GetNetworkSmDeviceNetworkAdapters200ResponseInner', function() {
      // uncomment below and update the code to test GetNetworkSmDeviceNetworkAdapters200ResponseInner
      //var instance = new MerakiDashboardApi.GetNetworkSmDeviceNetworkAdapters200ResponseInner();
      //expect(instance).to.be.a(MerakiDashboardApi.GetNetworkSmDeviceNetworkAdapters200ResponseInner);
    });

    it('should have the property dhcpServer (base name: "dhcpServer")', function() {
      // uncomment below and update the code to test the property dhcpServer
      //var instance = new MerakiDashboardApi.GetNetworkSmDeviceNetworkAdapters200ResponseInner();
      //expect(instance).to.be();
    });

    it('should have the property dnsServer (base name: "dnsServer")', function() {
      // uncomment below and update the code to test the property dnsServer
      //var instance = new MerakiDashboardApi.GetNetworkSmDeviceNetworkAdapters200ResponseInner();
      //expect(instance).to.be();
    });

    it('should have the property gateway (base name: "gateway")', function() {
      // uncomment below and update the code to test the property gateway
      //var instance = new MerakiDashboardApi.GetNetworkSmDeviceNetworkAdapters200ResponseInner();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new MerakiDashboardApi.GetNetworkSmDeviceNetworkAdapters200ResponseInner();
      //expect(instance).to.be();
    });

    it('should have the property ip (base name: "ip")', function() {
      // uncomment below and update the code to test the property ip
      //var instance = new MerakiDashboardApi.GetNetworkSmDeviceNetworkAdapters200ResponseInner();
      //expect(instance).to.be();
    });

    it('should have the property mac (base name: "mac")', function() {
      // uncomment below and update the code to test the property mac
      //var instance = new MerakiDashboardApi.GetNetworkSmDeviceNetworkAdapters200ResponseInner();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new MerakiDashboardApi.GetNetworkSmDeviceNetworkAdapters200ResponseInner();
      //expect(instance).to.be();
    });

    it('should have the property subnet (base name: "subnet")', function() {
      // uncomment below and update the code to test the property subnet
      //var instance = new MerakiDashboardApi.GetNetworkSmDeviceNetworkAdapters200ResponseInner();
      //expect(instance).to.be();
    });

  });

}));
