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
    instance = new ContainerRegistryManagementClient.DockerBuildRequest();
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

  describe('DockerBuildRequest', function() {
    it('should create an instance of DockerBuildRequest', function() {
      // uncomment below and update the code to test DockerBuildRequest
      //var instance = new ContainerRegistryManagementClient.DockerBuildRequest();
      //expect(instance).to.be.a(ContainerRegistryManagementClient.DockerBuildRequest);
    });

    it('should have the property agentConfiguration (base name: "agentConfiguration")', function() {
      // uncomment below and update the code to test the property agentConfiguration
      //var instance = new ContainerRegistryManagementClient.DockerBuildRequest();
      //expect(instance).to.be();
    });

    it('should have the property _arguments (base name: "arguments")', function() {
      // uncomment below and update the code to test the property _arguments
      //var instance = new ContainerRegistryManagementClient.DockerBuildRequest();
      //expect(instance).to.be();
    });

    it('should have the property credentials (base name: "credentials")', function() {
      // uncomment below and update the code to test the property credentials
      //var instance = new ContainerRegistryManagementClient.DockerBuildRequest();
      //expect(instance).to.be();
    });

    it('should have the property dockerFilePath (base name: "dockerFilePath")', function() {
      // uncomment below and update the code to test the property dockerFilePath
      //var instance = new ContainerRegistryManagementClient.DockerBuildRequest();
      //expect(instance).to.be();
    });

    it('should have the property imageNames (base name: "imageNames")', function() {
      // uncomment below and update the code to test the property imageNames
      //var instance = new ContainerRegistryManagementClient.DockerBuildRequest();
      //expect(instance).to.be();
    });

    it('should have the property isPushEnabled (base name: "isPushEnabled")', function() {
      // uncomment below and update the code to test the property isPushEnabled
      //var instance = new ContainerRegistryManagementClient.DockerBuildRequest();
      //expect(instance).to.be();
    });

    it('should have the property noCache (base name: "noCache")', function() {
      // uncomment below and update the code to test the property noCache
      //var instance = new ContainerRegistryManagementClient.DockerBuildRequest();
      //expect(instance).to.be();
    });

    it('should have the property platform (base name: "platform")', function() {
      // uncomment below and update the code to test the property platform
      //var instance = new ContainerRegistryManagementClient.DockerBuildRequest();
      //expect(instance).to.be();
    });

    it('should have the property sourceLocation (base name: "sourceLocation")', function() {
      // uncomment below and update the code to test the property sourceLocation
      //var instance = new ContainerRegistryManagementClient.DockerBuildRequest();
      //expect(instance).to.be();
    });

    it('should have the property target (base name: "target")', function() {
      // uncomment below and update the code to test the property target
      //var instance = new ContainerRegistryManagementClient.DockerBuildRequest();
      //expect(instance).to.be();
    });

    it('should have the property timeout (base name: "timeout")', function() {
      // uncomment below and update the code to test the property timeout
      //var instance = new ContainerRegistryManagementClient.DockerBuildRequest();
      //expect(instance).to.be();
    });

  });

}));
