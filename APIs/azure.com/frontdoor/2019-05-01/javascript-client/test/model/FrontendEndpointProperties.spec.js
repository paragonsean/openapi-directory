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
    instance = new FrontDoorManagementClient.FrontendEndpointProperties();
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

  describe('FrontendEndpointProperties', function() {
    it('should create an instance of FrontendEndpointProperties', function() {
      // uncomment below and update the code to test FrontendEndpointProperties
      //var instance = new FrontDoorManagementClient.FrontendEndpointProperties();
      //expect(instance).to.be.a(FrontDoorManagementClient.FrontendEndpointProperties);
    });

    it('should have the property customHttpsConfiguration (base name: "customHttpsConfiguration")', function() {
      // uncomment below and update the code to test the property customHttpsConfiguration
      //var instance = new FrontDoorManagementClient.FrontendEndpointProperties();
      //expect(instance).to.be();
    });

    it('should have the property customHttpsProvisioningState (base name: "customHttpsProvisioningState")', function() {
      // uncomment below and update the code to test the property customHttpsProvisioningState
      //var instance = new FrontDoorManagementClient.FrontendEndpointProperties();
      //expect(instance).to.be();
    });

    it('should have the property customHttpsProvisioningSubstate (base name: "customHttpsProvisioningSubstate")', function() {
      // uncomment below and update the code to test the property customHttpsProvisioningSubstate
      //var instance = new FrontDoorManagementClient.FrontendEndpointProperties();
      //expect(instance).to.be();
    });

    it('should have the property resourceState (base name: "resourceState")', function() {
      // uncomment below and update the code to test the property resourceState
      //var instance = new FrontDoorManagementClient.FrontendEndpointProperties();
      //expect(instance).to.be();
    });

    it('should have the property hostName (base name: "hostName")', function() {
      // uncomment below and update the code to test the property hostName
      //var instance = new FrontDoorManagementClient.FrontendEndpointProperties();
      //expect(instance).to.be();
    });

    it('should have the property sessionAffinityEnabledState (base name: "sessionAffinityEnabledState")', function() {
      // uncomment below and update the code to test the property sessionAffinityEnabledState
      //var instance = new FrontDoorManagementClient.FrontendEndpointProperties();
      //expect(instance).to.be();
    });

    it('should have the property sessionAffinityTtlSeconds (base name: "sessionAffinityTtlSeconds")', function() {
      // uncomment below and update the code to test the property sessionAffinityTtlSeconds
      //var instance = new FrontDoorManagementClient.FrontendEndpointProperties();
      //expect(instance).to.be();
    });

    it('should have the property webApplicationFirewallPolicyLink (base name: "webApplicationFirewallPolicyLink")', function() {
      // uncomment below and update the code to test the property webApplicationFirewallPolicyLink
      //var instance = new FrontDoorManagementClient.FrontendEndpointProperties();
      //expect(instance).to.be();
    });

  });

}));
