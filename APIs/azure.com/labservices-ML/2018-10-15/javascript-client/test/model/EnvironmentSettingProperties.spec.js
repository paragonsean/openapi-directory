/**
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
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
    factory(root.expect, root.ManagedLabsClient);
  }
}(this, function(expect, ManagedLabsClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new ManagedLabsClient.EnvironmentSettingProperties();
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

  describe('EnvironmentSettingProperties', function() {
    it('should create an instance of EnvironmentSettingProperties', function() {
      // uncomment below and update the code to test EnvironmentSettingProperties
      //var instance = new ManagedLabsClient.EnvironmentSettingProperties();
      //expect(instance).to.be.a(ManagedLabsClient.EnvironmentSettingProperties);
    });

    it('should have the property configurationState (base name: "configurationState")', function() {
      // uncomment below and update the code to test the property configurationState
      //var instance = new ManagedLabsClient.EnvironmentSettingProperties();
      //expect(instance).to.be();
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new ManagedLabsClient.EnvironmentSettingProperties();
      //expect(instance).to.be();
    });

    it('should have the property lastChanged (base name: "lastChanged")', function() {
      // uncomment below and update the code to test the property lastChanged
      //var instance = new ManagedLabsClient.EnvironmentSettingProperties();
      //expect(instance).to.be();
    });

    it('should have the property lastPublished (base name: "lastPublished")', function() {
      // uncomment below and update the code to test the property lastPublished
      //var instance = new ManagedLabsClient.EnvironmentSettingProperties();
      //expect(instance).to.be();
    });

    it('should have the property latestOperationResult (base name: "latestOperationResult")', function() {
      // uncomment below and update the code to test the property latestOperationResult
      //var instance = new ManagedLabsClient.EnvironmentSettingProperties();
      //expect(instance).to.be();
    });

    it('should have the property provisioningState (base name: "provisioningState")', function() {
      // uncomment below and update the code to test the property provisioningState
      //var instance = new ManagedLabsClient.EnvironmentSettingProperties();
      //expect(instance).to.be();
    });

    it('should have the property publishingState (base name: "publishingState")', function() {
      // uncomment below and update the code to test the property publishingState
      //var instance = new ManagedLabsClient.EnvironmentSettingProperties();
      //expect(instance).to.be();
    });

    it('should have the property resourceSettings (base name: "resourceSettings")', function() {
      // uncomment below and update the code to test the property resourceSettings
      //var instance = new ManagedLabsClient.EnvironmentSettingProperties();
      //expect(instance).to.be();
    });

    it('should have the property title (base name: "title")', function() {
      // uncomment below and update the code to test the property title
      //var instance = new ManagedLabsClient.EnvironmentSettingProperties();
      //expect(instance).to.be();
    });

    it('should have the property uniqueIdentifier (base name: "uniqueIdentifier")', function() {
      // uncomment below and update the code to test the property uniqueIdentifier
      //var instance = new ManagedLabsClient.EnvironmentSettingProperties();
      //expect(instance).to.be();
    });

  });

}));
