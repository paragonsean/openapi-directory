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
    instance = new MerakiDashboardApi.StaticRoutesApi();
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

  describe('StaticRoutesApi', function() {
    describe('createDeviceSwitchRoutingStaticRoute_2', function() {
      it('should call createDeviceSwitchRoutingStaticRoute_2 successfully', function(done) {
        //uncomment below and update the code to test createDeviceSwitchRoutingStaticRoute_2
        //instance.createDeviceSwitchRoutingStaticRoute_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createNetworkApplianceStaticRoute_1', function() {
      it('should call createNetworkApplianceStaticRoute_1 successfully', function(done) {
        //uncomment below and update the code to test createNetworkApplianceStaticRoute_1
        //instance.createNetworkApplianceStaticRoute_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createNetworkSwitchStackRoutingStaticRoute_3', function() {
      it('should call createNetworkSwitchStackRoutingStaticRoute_3 successfully', function(done) {
        //uncomment below and update the code to test createNetworkSwitchStackRoutingStaticRoute_3
        //instance.createNetworkSwitchStackRoutingStaticRoute_3(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteDeviceSwitchRoutingStaticRoute_2', function() {
      it('should call deleteDeviceSwitchRoutingStaticRoute_2 successfully', function(done) {
        //uncomment below and update the code to test deleteDeviceSwitchRoutingStaticRoute_2
        //instance.deleteDeviceSwitchRoutingStaticRoute_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteNetworkApplianceStaticRoute_1', function() {
      it('should call deleteNetworkApplianceStaticRoute_1 successfully', function(done) {
        //uncomment below and update the code to test deleteNetworkApplianceStaticRoute_1
        //instance.deleteNetworkApplianceStaticRoute_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteNetworkSwitchStackRoutingStaticRoute_3', function() {
      it('should call deleteNetworkSwitchStackRoutingStaticRoute_3 successfully', function(done) {
        //uncomment below and update the code to test deleteNetworkSwitchStackRoutingStaticRoute_3
        //instance.deleteNetworkSwitchStackRoutingStaticRoute_3(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getDeviceSwitchRoutingStaticRoute_2', function() {
      it('should call getDeviceSwitchRoutingStaticRoute_2 successfully', function(done) {
        //uncomment below and update the code to test getDeviceSwitchRoutingStaticRoute_2
        //instance.getDeviceSwitchRoutingStaticRoute_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getDeviceSwitchRoutingStaticRoutes_2', function() {
      it('should call getDeviceSwitchRoutingStaticRoutes_2 successfully', function(done) {
        //uncomment below and update the code to test getDeviceSwitchRoutingStaticRoutes_2
        //instance.getDeviceSwitchRoutingStaticRoutes_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkApplianceStaticRoute_1', function() {
      it('should call getNetworkApplianceStaticRoute_1 successfully', function(done) {
        //uncomment below and update the code to test getNetworkApplianceStaticRoute_1
        //instance.getNetworkApplianceStaticRoute_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkApplianceStaticRoutes_1', function() {
      it('should call getNetworkApplianceStaticRoutes_1 successfully', function(done) {
        //uncomment below and update the code to test getNetworkApplianceStaticRoutes_1
        //instance.getNetworkApplianceStaticRoutes_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkSwitchStackRoutingStaticRoute_3', function() {
      it('should call getNetworkSwitchStackRoutingStaticRoute_3 successfully', function(done) {
        //uncomment below and update the code to test getNetworkSwitchStackRoutingStaticRoute_3
        //instance.getNetworkSwitchStackRoutingStaticRoute_3(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkSwitchStackRoutingStaticRoutes_3', function() {
      it('should call getNetworkSwitchStackRoutingStaticRoutes_3 successfully', function(done) {
        //uncomment below and update the code to test getNetworkSwitchStackRoutingStaticRoutes_3
        //instance.getNetworkSwitchStackRoutingStaticRoutes_3(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateDeviceSwitchRoutingStaticRoute_2', function() {
      it('should call updateDeviceSwitchRoutingStaticRoute_2 successfully', function(done) {
        //uncomment below and update the code to test updateDeviceSwitchRoutingStaticRoute_2
        //instance.updateDeviceSwitchRoutingStaticRoute_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateNetworkApplianceStaticRoute_1', function() {
      it('should call updateNetworkApplianceStaticRoute_1 successfully', function(done) {
        //uncomment below and update the code to test updateNetworkApplianceStaticRoute_1
        //instance.updateNetworkApplianceStaticRoute_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateNetworkSwitchStackRoutingStaticRoute_3', function() {
      it('should call updateNetworkSwitchStackRoutingStaticRoute_3 successfully', function(done) {
        //uncomment below and update the code to test updateNetworkSwitchStackRoutingStaticRoute_3
        //instance.updateNetworkSwitchStackRoutingStaticRoute_3(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
