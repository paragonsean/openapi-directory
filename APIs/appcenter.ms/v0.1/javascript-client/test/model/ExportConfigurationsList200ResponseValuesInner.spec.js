/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
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
    factory(root.expect, root.AppCenterClient);
  }
}(this, function(expect, AppCenterClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AppCenterClient.ExportConfigurationsList200ResponseValuesInner();
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

  describe('ExportConfigurationsList200ResponseValuesInner', function() {
    it('should create an instance of ExportConfigurationsList200ResponseValuesInner', function() {
      // uncomment below and update the code to test ExportConfigurationsList200ResponseValuesInner
      //var instance = new AppCenterClient.ExportConfigurationsList200ResponseValuesInner();
      //expect(instance).to.be.a(AppCenterClient.ExportConfigurationsList200ResponseValuesInner);
    });

    it('should have the property creationTime (base name: "creation_time")', function() {
      // uncomment below and update the code to test the property creationTime
      //var instance = new AppCenterClient.ExportConfigurationsList200ResponseValuesInner();
      //expect(instance).to.be();
    });

    it('should have the property exportConfiguration (base name: "export_configuration")', function() {
      // uncomment below and update the code to test the property exportConfiguration
      //var instance = new AppCenterClient.ExportConfigurationsList200ResponseValuesInner();
      //expect(instance).to.be();
    });

    it('should have the property exportEntities (base name: "export_entities")', function() {
      // uncomment below and update the code to test the property exportEntities
      //var instance = new AppCenterClient.ExportConfigurationsList200ResponseValuesInner();
      //expect(instance).to.be();
    });

    it('should have the property exportType (base name: "export_type")', function() {
      // uncomment below and update the code to test the property exportType
      //var instance = new AppCenterClient.ExportConfigurationsList200ResponseValuesInner();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new AppCenterClient.ExportConfigurationsList200ResponseValuesInner();
      //expect(instance).to.be();
    });

    it('should have the property lastRunTime (base name: "last_run_time")', function() {
      // uncomment below and update the code to test the property lastRunTime
      //var instance = new AppCenterClient.ExportConfigurationsList200ResponseValuesInner();
      //expect(instance).to.be();
    });

    it('should have the property resourceGroup (base name: "resource_group")', function() {
      // uncomment below and update the code to test the property resourceGroup
      //var instance = new AppCenterClient.ExportConfigurationsList200ResponseValuesInner();
      //expect(instance).to.be();
    });

    it('should have the property resourceName (base name: "resource_name")', function() {
      // uncomment below and update the code to test the property resourceName
      //var instance = new AppCenterClient.ExportConfigurationsList200ResponseValuesInner();
      //expect(instance).to.be();
    });

    it('should have the property state (base name: "state")', function() {
      // uncomment below and update the code to test the property state
      //var instance = new AppCenterClient.ExportConfigurationsList200ResponseValuesInner();
      //expect(instance).to.be();
    });

    it('should have the property stateInfo (base name: "state_info")', function() {
      // uncomment below and update the code to test the property stateInfo
      //var instance = new AppCenterClient.ExportConfigurationsList200ResponseValuesInner();
      //expect(instance).to.be();
    });

  });

}));
