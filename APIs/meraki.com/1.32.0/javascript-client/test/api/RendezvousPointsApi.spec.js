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
    instance = new MerakiDashboardApi.RendezvousPointsApi();
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

  describe('RendezvousPointsApi', function() {
    describe('createNetworkSwitchRoutingMulticastRendezvousPoint_3', function() {
      it('should call createNetworkSwitchRoutingMulticastRendezvousPoint_3 successfully', function(done) {
        //uncomment below and update the code to test createNetworkSwitchRoutingMulticastRendezvousPoint_3
        //instance.createNetworkSwitchRoutingMulticastRendezvousPoint_3(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteNetworkSwitchRoutingMulticastRendezvousPoint_3', function() {
      it('should call deleteNetworkSwitchRoutingMulticastRendezvousPoint_3 successfully', function(done) {
        //uncomment below and update the code to test deleteNetworkSwitchRoutingMulticastRendezvousPoint_3
        //instance.deleteNetworkSwitchRoutingMulticastRendezvousPoint_3(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkSwitchRoutingMulticastRendezvousPoint_3', function() {
      it('should call getNetworkSwitchRoutingMulticastRendezvousPoint_3 successfully', function(done) {
        //uncomment below and update the code to test getNetworkSwitchRoutingMulticastRendezvousPoint_3
        //instance.getNetworkSwitchRoutingMulticastRendezvousPoint_3(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkSwitchRoutingMulticastRendezvousPoints_3', function() {
      it('should call getNetworkSwitchRoutingMulticastRendezvousPoints_3 successfully', function(done) {
        //uncomment below and update the code to test getNetworkSwitchRoutingMulticastRendezvousPoints_3
        //instance.getNetworkSwitchRoutingMulticastRendezvousPoints_3(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateNetworkSwitchRoutingMulticastRendezvousPoint_3', function() {
      it('should call updateNetworkSwitchRoutingMulticastRendezvousPoint_3 successfully', function(done) {
        //uncomment below and update the code to test updateNetworkSwitchRoutingMulticastRendezvousPoint_3
        //instance.updateNetworkSwitchRoutingMulticastRendezvousPoint_3(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
