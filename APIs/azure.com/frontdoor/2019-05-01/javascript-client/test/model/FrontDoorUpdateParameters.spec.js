/**
 * FrontDoorManagementClient
 * Use these APIs to manage Azure Front Door resources through the Azure Resource Manager. You must make sure that requests made to these resources are secure.
 *
 * The version of the OpenAPI document: 2019-05-01
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
    factory(root.expect, root.FrontDoorManagementClient);
  }
}(this, function(expect, FrontDoorManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new FrontDoorManagementClient.FrontDoorUpdateParameters();
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

  describe('FrontDoorUpdateParameters', function() {
    it('should create an instance of FrontDoorUpdateParameters', function() {
      // uncomment below and update the code to test FrontDoorUpdateParameters
      //var instance = new FrontDoorManagementClient.FrontDoorUpdateParameters();
      //expect(instance).to.be.a(FrontDoorManagementClient.FrontDoorUpdateParameters);
    });

    it('should have the property backendPools (base name: "backendPools")', function() {
      // uncomment below and update the code to test the property backendPools
      //var instance = new FrontDoorManagementClient.FrontDoorUpdateParameters();
      //expect(instance).to.be();
    });

    it('should have the property backendPoolsSettings (base name: "backendPoolsSettings")', function() {
      // uncomment below and update the code to test the property backendPoolsSettings
      //var instance = new FrontDoorManagementClient.FrontDoorUpdateParameters();
      //expect(instance).to.be();
    });

    it('should have the property enabledState (base name: "enabledState")', function() {
      // uncomment below and update the code to test the property enabledState
      //var instance = new FrontDoorManagementClient.FrontDoorUpdateParameters();
      //expect(instance).to.be();
    });

    it('should have the property friendlyName (base name: "friendlyName")', function() {
      // uncomment below and update the code to test the property friendlyName
      //var instance = new FrontDoorManagementClient.FrontDoorUpdateParameters();
      //expect(instance).to.be();
    });

    it('should have the property frontendEndpoints (base name: "frontendEndpoints")', function() {
      // uncomment below and update the code to test the property frontendEndpoints
      //var instance = new FrontDoorManagementClient.FrontDoorUpdateParameters();
      //expect(instance).to.be();
    });

    it('should have the property healthProbeSettings (base name: "healthProbeSettings")', function() {
      // uncomment below and update the code to test the property healthProbeSettings
      //var instance = new FrontDoorManagementClient.FrontDoorUpdateParameters();
      //expect(instance).to.be();
    });

    it('should have the property loadBalancingSettings (base name: "loadBalancingSettings")', function() {
      // uncomment below and update the code to test the property loadBalancingSettings
      //var instance = new FrontDoorManagementClient.FrontDoorUpdateParameters();
      //expect(instance).to.be();
    });

    it('should have the property routingRules (base name: "routingRules")', function() {
      // uncomment below and update the code to test the property routingRules
      //var instance = new FrontDoorManagementClient.FrontDoorUpdateParameters();
      //expect(instance).to.be();
    });

  });

}));
