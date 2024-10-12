/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-06-01-preview
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
    instance = new ContainerRegistryManagementClient.BaseImageTrigger();
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

  describe('BaseImageTrigger', function() {
    it('should create an instance of BaseImageTrigger', function() {
      // uncomment below and update the code to test BaseImageTrigger
      //var instance = new ContainerRegistryManagementClient.BaseImageTrigger();
      //expect(instance).to.be.a(ContainerRegistryManagementClient.BaseImageTrigger);
    });

    it('should have the property baseImageTriggerType (base name: "baseImageTriggerType")', function() {
      // uncomment below and update the code to test the property baseImageTriggerType
      //var instance = new ContainerRegistryManagementClient.BaseImageTrigger();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new ContainerRegistryManagementClient.BaseImageTrigger();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new ContainerRegistryManagementClient.BaseImageTrigger();
      //expect(instance).to.be();
    });

    it('should have the property updateTriggerEndpoint (base name: "updateTriggerEndpoint")', function() {
      // uncomment below and update the code to test the property updateTriggerEndpoint
      //var instance = new ContainerRegistryManagementClient.BaseImageTrigger();
      //expect(instance).to.be();
    });

    it('should have the property updateTriggerPayloadType (base name: "updateTriggerPayloadType")', function() {
      // uncomment below and update the code to test the property updateTriggerPayloadType
      //var instance = new ContainerRegistryManagementClient.BaseImageTrigger();
      //expect(instance).to.be();
    });

  });

}));
