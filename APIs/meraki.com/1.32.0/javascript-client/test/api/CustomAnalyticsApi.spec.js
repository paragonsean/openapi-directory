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
    instance = new MerakiDashboardApi.CustomAnalyticsApi();
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

  describe('CustomAnalyticsApi', function() {
    describe('createOrganizationCameraCustomAnalyticsArtifact_1', function() {
      it('should call createOrganizationCameraCustomAnalyticsArtifact_1 successfully', function(done) {
        //uncomment below and update the code to test createOrganizationCameraCustomAnalyticsArtifact_1
        //instance.createOrganizationCameraCustomAnalyticsArtifact_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteOrganizationCameraCustomAnalyticsArtifact_1', function() {
      it('should call deleteOrganizationCameraCustomAnalyticsArtifact_1 successfully', function(done) {
        //uncomment below and update the code to test deleteOrganizationCameraCustomAnalyticsArtifact_1
        //instance.deleteOrganizationCameraCustomAnalyticsArtifact_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getDeviceCameraCustomAnalytics_1', function() {
      it('should call getDeviceCameraCustomAnalytics_1 successfully', function(done) {
        //uncomment below and update the code to test getDeviceCameraCustomAnalytics_1
        //instance.getDeviceCameraCustomAnalytics_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getOrganizationCameraCustomAnalyticsArtifact_1', function() {
      it('should call getOrganizationCameraCustomAnalyticsArtifact_1 successfully', function(done) {
        //uncomment below and update the code to test getOrganizationCameraCustomAnalyticsArtifact_1
        //instance.getOrganizationCameraCustomAnalyticsArtifact_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getOrganizationCameraCustomAnalyticsArtifacts_1', function() {
      it('should call getOrganizationCameraCustomAnalyticsArtifacts_1 successfully', function(done) {
        //uncomment below and update the code to test getOrganizationCameraCustomAnalyticsArtifacts_1
        //instance.getOrganizationCameraCustomAnalyticsArtifacts_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateDeviceCameraCustomAnalytics_1', function() {
      it('should call updateDeviceCameraCustomAnalytics_1 successfully', function(done) {
        //uncomment below and update the code to test updateDeviceCameraCustomAnalytics_1
        //instance.updateDeviceCameraCustomAnalytics_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
