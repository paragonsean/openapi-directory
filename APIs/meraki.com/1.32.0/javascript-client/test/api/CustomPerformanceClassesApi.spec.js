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
    instance = new MerakiDashboardApi.CustomPerformanceClassesApi();
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

  describe('CustomPerformanceClassesApi', function() {
    describe('createNetworkApplianceTrafficShapingCustomPerformanceClass_2', function() {
      it('should call createNetworkApplianceTrafficShapingCustomPerformanceClass_2 successfully', function(done) {
        //uncomment below and update the code to test createNetworkApplianceTrafficShapingCustomPerformanceClass_2
        //instance.createNetworkApplianceTrafficShapingCustomPerformanceClass_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteNetworkApplianceTrafficShapingCustomPerformanceClass_2', function() {
      it('should call deleteNetworkApplianceTrafficShapingCustomPerformanceClass_2 successfully', function(done) {
        //uncomment below and update the code to test deleteNetworkApplianceTrafficShapingCustomPerformanceClass_2
        //instance.deleteNetworkApplianceTrafficShapingCustomPerformanceClass_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkApplianceTrafficShapingCustomPerformanceClass_2', function() {
      it('should call getNetworkApplianceTrafficShapingCustomPerformanceClass_2 successfully', function(done) {
        //uncomment below and update the code to test getNetworkApplianceTrafficShapingCustomPerformanceClass_2
        //instance.getNetworkApplianceTrafficShapingCustomPerformanceClass_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkApplianceTrafficShapingCustomPerformanceClasses_2', function() {
      it('should call getNetworkApplianceTrafficShapingCustomPerformanceClasses_2 successfully', function(done) {
        //uncomment below and update the code to test getNetworkApplianceTrafficShapingCustomPerformanceClasses_2
        //instance.getNetworkApplianceTrafficShapingCustomPerformanceClasses_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateNetworkApplianceTrafficShapingCustomPerformanceClass_2', function() {
      it('should call updateNetworkApplianceTrafficShapingCustomPerformanceClass_2 successfully', function(done) {
        //uncomment below and update the code to test updateNetworkApplianceTrafficShapingCustomPerformanceClass_2
        //instance.updateNetworkApplianceTrafficShapingCustomPerformanceClass_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
