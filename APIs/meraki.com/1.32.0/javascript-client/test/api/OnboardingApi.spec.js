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
    instance = new MerakiDashboardApi.OnboardingApi();
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

  describe('OnboardingApi', function() {
    describe('createOrganizationInventoryOnboardingCloudMonitoringExportEvent_2', function() {
      it('should call createOrganizationInventoryOnboardingCloudMonitoringExportEvent_2 successfully', function(done) {
        //uncomment below and update the code to test createOrganizationInventoryOnboardingCloudMonitoringExportEvent_2
        //instance.createOrganizationInventoryOnboardingCloudMonitoringExportEvent_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createOrganizationInventoryOnboardingCloudMonitoringImport_2', function() {
      it('should call createOrganizationInventoryOnboardingCloudMonitoringImport_2 successfully', function(done) {
        //uncomment below and update the code to test createOrganizationInventoryOnboardingCloudMonitoringImport_2
        //instance.createOrganizationInventoryOnboardingCloudMonitoringImport_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createOrganizationInventoryOnboardingCloudMonitoringPrepare_2', function() {
      it('should call createOrganizationInventoryOnboardingCloudMonitoringPrepare_2 successfully', function(done) {
        //uncomment below and update the code to test createOrganizationInventoryOnboardingCloudMonitoringPrepare_2
        //instance.createOrganizationInventoryOnboardingCloudMonitoringPrepare_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getOrganizationCameraOnboardingStatuses_1', function() {
      it('should call getOrganizationCameraOnboardingStatuses_1 successfully', function(done) {
        //uncomment below and update the code to test getOrganizationCameraOnboardingStatuses_1
        //instance.getOrganizationCameraOnboardingStatuses_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getOrganizationInventoryOnboardingCloudMonitoringImports_2', function() {
      it('should call getOrganizationInventoryOnboardingCloudMonitoringImports_2 successfully', function(done) {
        //uncomment below and update the code to test getOrganizationInventoryOnboardingCloudMonitoringImports_2
        //instance.getOrganizationInventoryOnboardingCloudMonitoringImports_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getOrganizationInventoryOnboardingCloudMonitoringNetworks_2', function() {
      it('should call getOrganizationInventoryOnboardingCloudMonitoringNetworks_2 successfully', function(done) {
        //uncomment below and update the code to test getOrganizationInventoryOnboardingCloudMonitoringNetworks_2
        //instance.getOrganizationInventoryOnboardingCloudMonitoringNetworks_2(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateOrganizationCameraOnboardingStatuses_1', function() {
      it('should call updateOrganizationCameraOnboardingStatuses_1 successfully', function(done) {
        //uncomment below and update the code to test updateOrganizationCameraOnboardingStatuses_1
        //instance.updateOrganizationCameraOnboardingStatuses_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
