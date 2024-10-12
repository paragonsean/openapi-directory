/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-04-01
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
    factory(root.expect, root.ContainerRegistryManagementClient);
  }
}(this, function(expect, ContainerRegistryManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new ContainerRegistryManagementClient.RunProperties();
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

  describe('RunProperties', function() {
    it('should create an instance of RunProperties', function() {
      // uncomment below and update the code to test RunProperties
      //var instance = new ContainerRegistryManagementClient.RunProperties();
      //expect(instance).to.be.a(ContainerRegistryManagementClient.RunProperties);
    });

    it('should have the property agentConfiguration (base name: "agentConfiguration")', function() {
      // uncomment below and update the code to test the property agentConfiguration
      //var instance = new ContainerRegistryManagementClient.RunProperties();
      //expect(instance).to.be();
    });

    it('should have the property createTime (base name: "createTime")', function() {
      // uncomment below and update the code to test the property createTime
      //var instance = new ContainerRegistryManagementClient.RunProperties();
      //expect(instance).to.be();
    });

    it('should have the property customRegistries (base name: "customRegistries")', function() {
      // uncomment below and update the code to test the property customRegistries
      //var instance = new ContainerRegistryManagementClient.RunProperties();
      //expect(instance).to.be();
    });

    it('should have the property finishTime (base name: "finishTime")', function() {
      // uncomment below and update the code to test the property finishTime
      //var instance = new ContainerRegistryManagementClient.RunProperties();
      //expect(instance).to.be();
    });

    it('should have the property imageUpdateTrigger (base name: "imageUpdateTrigger")', function() {
      // uncomment below and update the code to test the property imageUpdateTrigger
      //var instance = new ContainerRegistryManagementClient.RunProperties();
      //expect(instance).to.be();
    });

    it('should have the property isArchiveEnabled (base name: "isArchiveEnabled")', function() {
      // uncomment below and update the code to test the property isArchiveEnabled
      //var instance = new ContainerRegistryManagementClient.RunProperties();
      //expect(instance).to.be();
    });

    it('should have the property lastUpdatedTime (base name: "lastUpdatedTime")', function() {
      // uncomment below and update the code to test the property lastUpdatedTime
      //var instance = new ContainerRegistryManagementClient.RunProperties();
      //expect(instance).to.be();
    });

    it('should have the property outputImages (base name: "outputImages")', function() {
      // uncomment below and update the code to test the property outputImages
      //var instance = new ContainerRegistryManagementClient.RunProperties();
      //expect(instance).to.be();
    });

    it('should have the property platform (base name: "platform")', function() {
      // uncomment below and update the code to test the property platform
      //var instance = new ContainerRegistryManagementClient.RunProperties();
      //expect(instance).to.be();
    });

    it('should have the property provisioningState (base name: "provisioningState")', function() {
      // uncomment below and update the code to test the property provisioningState
      //var instance = new ContainerRegistryManagementClient.RunProperties();
      //expect(instance).to.be();
    });

    it('should have the property runErrorMessage (base name: "runErrorMessage")', function() {
      // uncomment below and update the code to test the property runErrorMessage
      //var instance = new ContainerRegistryManagementClient.RunProperties();
      //expect(instance).to.be();
    });

    it('should have the property runId (base name: "runId")', function() {
      // uncomment below and update the code to test the property runId
      //var instance = new ContainerRegistryManagementClient.RunProperties();
      //expect(instance).to.be();
    });

    it('should have the property runType (base name: "runType")', function() {
      // uncomment below and update the code to test the property runType
      //var instance = new ContainerRegistryManagementClient.RunProperties();
      //expect(instance).to.be();
    });

    it('should have the property sourceRegistryAuth (base name: "sourceRegistryAuth")', function() {
      // uncomment below and update the code to test the property sourceRegistryAuth
      //var instance = new ContainerRegistryManagementClient.RunProperties();
      //expect(instance).to.be();
    });

    it('should have the property sourceTrigger (base name: "sourceTrigger")', function() {
      // uncomment below and update the code to test the property sourceTrigger
      //var instance = new ContainerRegistryManagementClient.RunProperties();
      //expect(instance).to.be();
    });

    it('should have the property startTime (base name: "startTime")', function() {
      // uncomment below and update the code to test the property startTime
      //var instance = new ContainerRegistryManagementClient.RunProperties();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new ContainerRegistryManagementClient.RunProperties();
      //expect(instance).to.be();
    });

    it('should have the property task (base name: "task")', function() {
      // uncomment below and update the code to test the property task
      //var instance = new ContainerRegistryManagementClient.RunProperties();
      //expect(instance).to.be();
    });

    it('should have the property timerTrigger (base name: "timerTrigger")', function() {
      // uncomment below and update the code to test the property timerTrigger
      //var instance = new ContainerRegistryManagementClient.RunProperties();
      //expect(instance).to.be();
    });

  });

}));
