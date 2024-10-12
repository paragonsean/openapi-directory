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
    instance = new ContainerRegistryManagementClient.SourceTrigger();
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

  describe('SourceTrigger', function() {
    it('should create an instance of SourceTrigger', function() {
      // uncomment below and update the code to test SourceTrigger
      //var instance = new ContainerRegistryManagementClient.SourceTrigger();
      //expect(instance).to.be.a(ContainerRegistryManagementClient.SourceTrigger);
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new ContainerRegistryManagementClient.SourceTrigger();
      //expect(instance).to.be();
    });

    it('should have the property sourceRepository (base name: "sourceRepository")', function() {
      // uncomment below and update the code to test the property sourceRepository
      //var instance = new ContainerRegistryManagementClient.SourceTrigger();
      //expect(instance).to.be();
    });

    it('should have the property sourceTriggerEvents (base name: "sourceTriggerEvents")', function() {
      // uncomment below and update the code to test the property sourceTriggerEvents
      //var instance = new ContainerRegistryManagementClient.SourceTrigger();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new ContainerRegistryManagementClient.SourceTrigger();
      //expect(instance).to.be();
    });

  });

}));
