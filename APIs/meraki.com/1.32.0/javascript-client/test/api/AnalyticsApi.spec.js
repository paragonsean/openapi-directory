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
    instance = new MerakiDashboardApi.AnalyticsApi();
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

  describe('AnalyticsApi', function() {
    describe('getDeviceCameraAnalyticsLive_1', function() {
      it('should call getDeviceCameraAnalyticsLive_1 successfully', function(done) {
        //uncomment below and update the code to test getDeviceCameraAnalyticsLive_1
        //instance.getDeviceCameraAnalyticsLive_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getDeviceCameraAnalyticsOverview_1', function() {
      it('should call getDeviceCameraAnalyticsOverview_1 successfully', function(done) {
        //uncomment below and update the code to test getDeviceCameraAnalyticsOverview_1
        //instance.getDeviceCameraAnalyticsOverview_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getDeviceCameraAnalyticsRecent_1', function() {
      it('should call getDeviceCameraAnalyticsRecent_1 successfully', function(done) {
        //uncomment below and update the code to test getDeviceCameraAnalyticsRecent_1
        //instance.getDeviceCameraAnalyticsRecent_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getDeviceCameraAnalyticsZoneHistory_1', function() {
      it('should call getDeviceCameraAnalyticsZoneHistory_1 successfully', function(done) {
        //uncomment below and update the code to test getDeviceCameraAnalyticsZoneHistory_1
        //instance.getDeviceCameraAnalyticsZoneHistory_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getDeviceCameraAnalyticsZones_1', function() {
      it('should call getDeviceCameraAnalyticsZones_1 successfully', function(done) {
        //uncomment below and update the code to test getDeviceCameraAnalyticsZones_1
        //instance.getDeviceCameraAnalyticsZones_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
