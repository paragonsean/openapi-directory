/**
 * HDInsightManagementClient
 * The HDInsight Management Client.
 *
 * The version of the OpenAPI document: 2018-06-01-preview
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
    factory(root.expect, root.HdInsightManagementClient);
  }
}(this, function(expect, HdInsightManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new HdInsightManagementClient.ApplicationPropertiesComputeProfileRolesInnerHardwareProfile();
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

  describe('ApplicationPropertiesComputeProfileRolesInnerHardwareProfile', function() {
    it('should create an instance of ApplicationPropertiesComputeProfileRolesInnerHardwareProfile', function() {
      // uncomment below and update the code to test ApplicationPropertiesComputeProfileRolesInnerHardwareProfile
      //var instance = new HdInsightManagementClient.ApplicationPropertiesComputeProfileRolesInnerHardwareProfile();
      //expect(instance).to.be.a(HdInsightManagementClient.ApplicationPropertiesComputeProfileRolesInnerHardwareProfile);
    });

    it('should have the property vmSize (base name: "vmSize")', function() {
      // uncomment below and update the code to test the property vmSize
      //var instance = new HdInsightManagementClient.ApplicationPropertiesComputeProfileRolesInnerHardwareProfile();
      //expect(instance).to.be();
    });

  });

}));
