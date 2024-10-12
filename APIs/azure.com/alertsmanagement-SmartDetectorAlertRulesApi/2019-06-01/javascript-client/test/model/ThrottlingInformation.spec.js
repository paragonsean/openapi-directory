/**
 * Azure Alerts Management Service Resource Provider
 * APIs for Azure Smart Detector Alert Rules CRUD operations.
 *
 * The version of the OpenAPI document: 2019-06-01
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
    factory(root.expect, root.AzureAlertsManagementServiceResourceProvider);
  }
}(this, function(expect, AzureAlertsManagementServiceResourceProvider) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AzureAlertsManagementServiceResourceProvider.ThrottlingInformation();
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

  describe('ThrottlingInformation', function() {
    it('should create an instance of ThrottlingInformation', function() {
      // uncomment below and update the code to test ThrottlingInformation
      //var instance = new AzureAlertsManagementServiceResourceProvider.ThrottlingInformation();
      //expect(instance).to.be.a(AzureAlertsManagementServiceResourceProvider.ThrottlingInformation);
    });

    it('should have the property duration (base name: "duration")', function() {
      // uncomment below and update the code to test the property duration
      //var instance = new AzureAlertsManagementServiceResourceProvider.ThrottlingInformation();
      //expect(instance).to.be();
    });

  });

}));
