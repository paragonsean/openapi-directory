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
    instance = new MerakiDashboardApi.LatencyStatsApi();
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

  describe('LatencyStatsApi', function() {
    describe('getDeviceWirelessLatencyStats_1', function() {
      it('should call getDeviceWirelessLatencyStats_1 successfully', function(done) {
        //uncomment below and update the code to test getDeviceWirelessLatencyStats_1
        //instance.getDeviceWirelessLatencyStats_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessClientLatencyStats_2', function() {
      it('should call getNetworkWirelessClientLatencyStats_2 successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessClientLatencyStats_2
        //instance.getNetworkWirelessClientLatencyStats_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessClientsLatencyStats_2', function() {
      it('should call getNetworkWirelessClientsLatencyStats_2 successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessClientsLatencyStats_2
        //instance.getNetworkWirelessClientsLatencyStats_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessDevicesLatencyStats_2', function() {
      it('should call getNetworkWirelessDevicesLatencyStats_2 successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessDevicesLatencyStats_2
        //instance.getNetworkWirelessDevicesLatencyStats_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessLatencyStats_1', function() {
      it('should call getNetworkWirelessLatencyStats_1 successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessLatencyStats_1
        //instance.getNetworkWirelessLatencyStats_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
