/**
 * FrontDoorManagementClient
 * Use these APIs to manage Azure Front Door resources through the Azure Resource Manager. You must make sure that requests made to these resources are secure.
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
    factory(root.expect, root.FrontDoorManagementClient);
  }
}(this, function(expect, FrontDoorManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new FrontDoorManagementClient.HealthProbeSettingsUpdateParameters();
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

  describe('HealthProbeSettingsUpdateParameters', function() {
    it('should create an instance of HealthProbeSettingsUpdateParameters', function() {
      // uncomment below and update the code to test HealthProbeSettingsUpdateParameters
      //var instance = new FrontDoorManagementClient.HealthProbeSettingsUpdateParameters();
      //expect(instance).to.be.a(FrontDoorManagementClient.HealthProbeSettingsUpdateParameters);
    });

    it('should have the property intervalInSeconds (base name: "intervalInSeconds")', function() {
      // uncomment below and update the code to test the property intervalInSeconds
      //var instance = new FrontDoorManagementClient.HealthProbeSettingsUpdateParameters();
      //expect(instance).to.be();
    });

    it('should have the property path (base name: "path")', function() {
      // uncomment below and update the code to test the property path
      //var instance = new FrontDoorManagementClient.HealthProbeSettingsUpdateParameters();
      //expect(instance).to.be();
    });

    it('should have the property protocol (base name: "protocol")', function() {
      // uncomment below and update the code to test the property protocol
      //var instance = new FrontDoorManagementClient.HealthProbeSettingsUpdateParameters();
      //expect(instance).to.be();
    });

  });

}));
