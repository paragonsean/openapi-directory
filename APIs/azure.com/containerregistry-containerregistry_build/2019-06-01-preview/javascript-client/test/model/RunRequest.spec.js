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
    instance = new ContainerRegistryManagementClient.RunRequest();
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

  describe('RunRequest', function() {
    it('should create an instance of RunRequest', function() {
      // uncomment below and update the code to test RunRequest
      //var instance = new ContainerRegistryManagementClient.RunRequest();
      //expect(instance).to.be.a(ContainerRegistryManagementClient.RunRequest);
    });

    it('should have the property isArchiveEnabled (base name: "isArchiveEnabled")', function() {
      // uncomment below and update the code to test the property isArchiveEnabled
      //var instance = new ContainerRegistryManagementClient.RunRequest();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new ContainerRegistryManagementClient.RunRequest();
      //expect(instance).to.be();
    });

  });

}));
