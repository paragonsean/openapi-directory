/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
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
    factory(root.expect, root.StorSimple8000SeriesManagementClient);
  }
}(this, function(expect, StorSimple8000SeriesManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new StorSimple8000SeriesManagementClient.DeviceSettingsApi();
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

  describe('DeviceSettingsApi', function() {
    describe('deviceSettingsCreateOrUpdateAlertSettings', function() {
      it('should call deviceSettingsCreateOrUpdateAlertSettings successfully', function(done) {
        //uncomment below and update the code to test deviceSettingsCreateOrUpdateAlertSettings
        //instance.deviceSettingsCreateOrUpdateAlertSettings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deviceSettingsCreateOrUpdateTimeSettings', function() {
      it('should call deviceSettingsCreateOrUpdateTimeSettings successfully', function(done) {
        //uncomment below and update the code to test deviceSettingsCreateOrUpdateTimeSettings
        //instance.deviceSettingsCreateOrUpdateTimeSettings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deviceSettingsGetAlertSettings', function() {
      it('should call deviceSettingsGetAlertSettings successfully', function(done) {
        //uncomment below and update the code to test deviceSettingsGetAlertSettings
        //instance.deviceSettingsGetAlertSettings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deviceSettingsGetNetworkSettings', function() {
      it('should call deviceSettingsGetNetworkSettings successfully', function(done) {
        //uncomment below and update the code to test deviceSettingsGetNetworkSettings
        //instance.deviceSettingsGetNetworkSettings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deviceSettingsGetSecuritySettings', function() {
      it('should call deviceSettingsGetSecuritySettings successfully', function(done) {
        //uncomment below and update the code to test deviceSettingsGetSecuritySettings
        //instance.deviceSettingsGetSecuritySettings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deviceSettingsGetTimeSettings', function() {
      it('should call deviceSettingsGetTimeSettings successfully', function(done) {
        //uncomment below and update the code to test deviceSettingsGetTimeSettings
        //instance.deviceSettingsGetTimeSettings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deviceSettingsSyncRemotemanagementCertificate', function() {
      it('should call deviceSettingsSyncRemotemanagementCertificate successfully', function(done) {
        //uncomment below and update the code to test deviceSettingsSyncRemotemanagementCertificate
        //instance.deviceSettingsSyncRemotemanagementCertificate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deviceSettingsUpdateNetworkSettings', function() {
      it('should call deviceSettingsUpdateNetworkSettings successfully', function(done) {
        //uncomment below and update the code to test deviceSettingsUpdateNetworkSettings
        //instance.deviceSettingsUpdateNetworkSettings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deviceSettingsUpdateSecuritySettings', function() {
      it('should call deviceSettingsUpdateSecuritySettings successfully', function(done) {
        //uncomment below and update the code to test deviceSettingsUpdateSecuritySettings
        //instance.deviceSettingsUpdateSecuritySettings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
