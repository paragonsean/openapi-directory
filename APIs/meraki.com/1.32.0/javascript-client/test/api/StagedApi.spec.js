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
    instance = new MerakiDashboardApi.StagedApi();
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

  describe('StagedApi', function() {
    describe('createNetworkFirmwareUpgradesStagedEvent_2', function() {
      it('should call createNetworkFirmwareUpgradesStagedEvent_2 successfully', function(done) {
        //uncomment below and update the code to test createNetworkFirmwareUpgradesStagedEvent_2
        //instance.createNetworkFirmwareUpgradesStagedEvent_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createNetworkFirmwareUpgradesStagedGroup_2', function() {
      it('should call createNetworkFirmwareUpgradesStagedGroup_2 successfully', function(done) {
        //uncomment below and update the code to test createNetworkFirmwareUpgradesStagedGroup_2
        //instance.createNetworkFirmwareUpgradesStagedGroup_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deferNetworkFirmwareUpgradesStagedEvents_2', function() {
      it('should call deferNetworkFirmwareUpgradesStagedEvents_2 successfully', function(done) {
        //uncomment below and update the code to test deferNetworkFirmwareUpgradesStagedEvents_2
        //instance.deferNetworkFirmwareUpgradesStagedEvents_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteNetworkFirmwareUpgradesStagedGroup_2', function() {
      it('should call deleteNetworkFirmwareUpgradesStagedGroup_2 successfully', function(done) {
        //uncomment below and update the code to test deleteNetworkFirmwareUpgradesStagedGroup_2
        //instance.deleteNetworkFirmwareUpgradesStagedGroup_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkFirmwareUpgradesStagedEvents_2', function() {
      it('should call getNetworkFirmwareUpgradesStagedEvents_2 successfully', function(done) {
        //uncomment below and update the code to test getNetworkFirmwareUpgradesStagedEvents_2
        //instance.getNetworkFirmwareUpgradesStagedEvents_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkFirmwareUpgradesStagedGroup_2', function() {
      it('should call getNetworkFirmwareUpgradesStagedGroup_2 successfully', function(done) {
        //uncomment below and update the code to test getNetworkFirmwareUpgradesStagedGroup_2
        //instance.getNetworkFirmwareUpgradesStagedGroup_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkFirmwareUpgradesStagedGroups_2', function() {
      it('should call getNetworkFirmwareUpgradesStagedGroups_2 successfully', function(done) {
        //uncomment below and update the code to test getNetworkFirmwareUpgradesStagedGroups_2
        //instance.getNetworkFirmwareUpgradesStagedGroups_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkFirmwareUpgradesStagedStages_2', function() {
      it('should call getNetworkFirmwareUpgradesStagedStages_2 successfully', function(done) {
        //uncomment below and update the code to test getNetworkFirmwareUpgradesStagedStages_2
        //instance.getNetworkFirmwareUpgradesStagedStages_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('rollbacksNetworkFirmwareUpgradesStagedEvents_2', function() {
      it('should call rollbacksNetworkFirmwareUpgradesStagedEvents_2 successfully', function(done) {
        //uncomment below and update the code to test rollbacksNetworkFirmwareUpgradesStagedEvents_2
        //instance.rollbacksNetworkFirmwareUpgradesStagedEvents_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateNetworkFirmwareUpgradesStagedEvents_2', function() {
      it('should call updateNetworkFirmwareUpgradesStagedEvents_2 successfully', function(done) {
        //uncomment below and update the code to test updateNetworkFirmwareUpgradesStagedEvents_2
        //instance.updateNetworkFirmwareUpgradesStagedEvents_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateNetworkFirmwareUpgradesStagedGroup_2', function() {
      it('should call updateNetworkFirmwareUpgradesStagedGroup_2 successfully', function(done) {
        //uncomment below and update the code to test updateNetworkFirmwareUpgradesStagedGroup_2
        //instance.updateNetworkFirmwareUpgradesStagedGroup_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateNetworkFirmwareUpgradesStagedStages_2', function() {
      it('should call updateNetworkFirmwareUpgradesStagedStages_2 successfully', function(done) {
        //uncomment below and update the code to test updateNetworkFirmwareUpgradesStagedStages_2
        //instance.updateNetworkFirmwareUpgradesStagedStages_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
