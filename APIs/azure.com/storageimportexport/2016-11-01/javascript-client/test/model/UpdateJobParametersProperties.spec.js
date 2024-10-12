/**
 * StorageImportExport
 * The Storage Import/Export Resource Provider API.
 *
 * The version of the OpenAPI document: 2016-11-01
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
    factory(root.expect, root.StorageImportExport);
  }
}(this, function(expect, StorageImportExport) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new StorageImportExport.UpdateJobParametersProperties();
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

  describe('UpdateJobParametersProperties', function() {
    it('should create an instance of UpdateJobParametersProperties', function() {
      // uncomment below and update the code to test UpdateJobParametersProperties
      //var instance = new StorageImportExport.UpdateJobParametersProperties();
      //expect(instance).to.be.a(StorageImportExport.UpdateJobParametersProperties);
    });

    it('should have the property backupDriveManifest (base name: "backupDriveManifest")', function() {
      // uncomment below and update the code to test the property backupDriveManifest
      //var instance = new StorageImportExport.UpdateJobParametersProperties();
      //expect(instance).to.be();
    });

    it('should have the property cancelRequested (base name: "cancelRequested")', function() {
      // uncomment below and update the code to test the property cancelRequested
      //var instance = new StorageImportExport.UpdateJobParametersProperties();
      //expect(instance).to.be();
    });

    it('should have the property deliveryPackage (base name: "deliveryPackage")', function() {
      // uncomment below and update the code to test the property deliveryPackage
      //var instance = new StorageImportExport.UpdateJobParametersProperties();
      //expect(instance).to.be();
    });

    it('should have the property driveList (base name: "driveList")', function() {
      // uncomment below and update the code to test the property driveList
      //var instance = new StorageImportExport.UpdateJobParametersProperties();
      //expect(instance).to.be();
    });

    it('should have the property logLevel (base name: "logLevel")', function() {
      // uncomment below and update the code to test the property logLevel
      //var instance = new StorageImportExport.UpdateJobParametersProperties();
      //expect(instance).to.be();
    });

    it('should have the property returnAddress (base name: "returnAddress")', function() {
      // uncomment below and update the code to test the property returnAddress
      //var instance = new StorageImportExport.UpdateJobParametersProperties();
      //expect(instance).to.be();
    });

    it('should have the property returnShipping (base name: "returnShipping")', function() {
      // uncomment below and update the code to test the property returnShipping
      //var instance = new StorageImportExport.UpdateJobParametersProperties();
      //expect(instance).to.be();
    });

    it('should have the property state (base name: "state")', function() {
      // uncomment below and update the code to test the property state
      //var instance = new StorageImportExport.UpdateJobParametersProperties();
      //expect(instance).to.be();
    });

  });

}));
