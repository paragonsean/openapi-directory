/**
 * FrontDoorManagementClient
 * Use these APIs to manage Azure Front Door resources through the Azure Resource Manager. You must make sure that requests made to these resources are secure.
 *
 * The version of the OpenAPI document: 2020-01-01
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
    instance = new FrontDoorManagementClient.LoadBalancingSettingsUpdateParameters();
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

  describe('LoadBalancingSettingsUpdateParameters', function() {
    it('should create an instance of LoadBalancingSettingsUpdateParameters', function() {
      // uncomment below and update the code to test LoadBalancingSettingsUpdateParameters
      //var instance = new FrontDoorManagementClient.LoadBalancingSettingsUpdateParameters();
      //expect(instance).to.be.a(FrontDoorManagementClient.LoadBalancingSettingsUpdateParameters);
    });

    it('should have the property additionalLatencyMilliseconds (base name: "additionalLatencyMilliseconds")', function() {
      // uncomment below and update the code to test the property additionalLatencyMilliseconds
      //var instance = new FrontDoorManagementClient.LoadBalancingSettingsUpdateParameters();
      //expect(instance).to.be();
    });

    it('should have the property sampleSize (base name: "sampleSize")', function() {
      // uncomment below and update the code to test the property sampleSize
      //var instance = new FrontDoorManagementClient.LoadBalancingSettingsUpdateParameters();
      //expect(instance).to.be();
    });

    it('should have the property successfulSamplesRequired (base name: "successfulSamplesRequired")', function() {
      // uncomment below and update the code to test the property successfulSamplesRequired
      //var instance = new FrontDoorManagementClient.LoadBalancingSettingsUpdateParameters();
      //expect(instance).to.be();
    });

  });

}));
