/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on the ApiVersionSet entity associated with your Azure API Management deployment. Using this entity you create and manage API Version Sets that are used to group APIs for consistent versioning.
 *
 * The version of the OpenAPI document: 2017-03-01
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
    factory(root.expect, root.ApiManagementClient);
  }
}(this, function(expect, ApiManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new ApiManagementClient.ApiVersionSetUpdateParametersProperties();
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

  describe('ApiVersionSetUpdateParametersProperties', function() {
    it('should create an instance of ApiVersionSetUpdateParametersProperties', function() {
      // uncomment below and update the code to test ApiVersionSetUpdateParametersProperties
      //var instance = new ApiManagementClient.ApiVersionSetUpdateParametersProperties();
      //expect(instance).to.be.a(ApiManagementClient.ApiVersionSetUpdateParametersProperties);
    });

    it('should have the property displayName (base name: "displayName")', function() {
      // uncomment below and update the code to test the property displayName
      //var instance = new ApiManagementClient.ApiVersionSetUpdateParametersProperties();
      //expect(instance).to.be();
    });

    it('should have the property versioningScheme (base name: "versioningScheme")', function() {
      // uncomment below and update the code to test the property versioningScheme
      //var instance = new ApiManagementClient.ApiVersionSetUpdateParametersProperties();
      //expect(instance).to.be();
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new ApiManagementClient.ApiVersionSetUpdateParametersProperties();
      //expect(instance).to.be();
    });

    it('should have the property versionHeaderName (base name: "versionHeaderName")', function() {
      // uncomment below and update the code to test the property versionHeaderName
      //var instance = new ApiManagementClient.ApiVersionSetUpdateParametersProperties();
      //expect(instance).to.be();
    });

    it('should have the property versionQueryName (base name: "versionQueryName")', function() {
      // uncomment below and update the code to test the property versionQueryName
      //var instance = new ApiManagementClient.ApiVersionSetUpdateParametersProperties();
      //expect(instance).to.be();
    });

  });

}));
