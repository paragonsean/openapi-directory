/**
 * Storage Cache Mgmt Client
 * A Storage Cache provides scalable caching service for NAS clients, serving data from either NFSv3 or Blob at-rest storage (referred to as \"Storage Targets\"). These operations allow you to manage Caches.
 *
 * The version of the OpenAPI document: 2019-11-01
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
    factory(root.expect, root.StorageCacheMgmtClient);
  }
}(this, function(expect, StorageCacheMgmtClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new StorageCacheMgmtClient.CacheUpgradeStatus();
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

  describe('CacheUpgradeStatus', function() {
    it('should create an instance of CacheUpgradeStatus', function() {
      // uncomment below and update the code to test CacheUpgradeStatus
      //var instance = new StorageCacheMgmtClient.CacheUpgradeStatus();
      //expect(instance).to.be.a(StorageCacheMgmtClient.CacheUpgradeStatus);
    });

    it('should have the property currentFirmwareVersion (base name: "currentFirmwareVersion")', function() {
      // uncomment below and update the code to test the property currentFirmwareVersion
      //var instance = new StorageCacheMgmtClient.CacheUpgradeStatus();
      //expect(instance).to.be();
    });

    it('should have the property firmwareUpdateDeadline (base name: "firmwareUpdateDeadline")', function() {
      // uncomment below and update the code to test the property firmwareUpdateDeadline
      //var instance = new StorageCacheMgmtClient.CacheUpgradeStatus();
      //expect(instance).to.be();
    });

    it('should have the property firmwareUpdateStatus (base name: "firmwareUpdateStatus")', function() {
      // uncomment below and update the code to test the property firmwareUpdateStatus
      //var instance = new StorageCacheMgmtClient.CacheUpgradeStatus();
      //expect(instance).to.be();
    });

    it('should have the property lastFirmwareUpdate (base name: "lastFirmwareUpdate")', function() {
      // uncomment below and update the code to test the property lastFirmwareUpdate
      //var instance = new StorageCacheMgmtClient.CacheUpgradeStatus();
      //expect(instance).to.be();
    });

    it('should have the property pendingFirmwareVersion (base name: "pendingFirmwareVersion")', function() {
      // uncomment below and update the code to test the property pendingFirmwareVersion
      //var instance = new StorageCacheMgmtClient.CacheUpgradeStatus();
      //expect(instance).to.be();
    });

  });

}));
