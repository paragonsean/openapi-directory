/**
 * ManagedNetworkManagementClient
 * The Microsoft Azure Managed Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to programmatically view, control, change, and monitor your entire Azure network centrally and with ease.
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
    factory(root.expect, root.ManagedNetworkManagementClient);
  }
}(this, function(expect, ManagedNetworkManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new ManagedNetworkManagementClient.ErrorResponse();
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

  describe('ErrorResponse', function() {
    it('should create an instance of ErrorResponse', function() {
      // uncomment below and update the code to test ErrorResponse
      //var instance = new ManagedNetworkManagementClient.ErrorResponse();
      //expect(instance).to.be.a(ManagedNetworkManagementClient.ErrorResponse);
    });

    it('should have the property code (base name: "code")', function() {
      // uncomment below and update the code to test the property code
      //var instance = new ManagedNetworkManagementClient.ErrorResponse();
      //expect(instance).to.be();
    });

    it('should have the property message (base name: "message")', function() {
      // uncomment below and update the code to test the property message
      //var instance = new ManagedNetworkManagementClient.ErrorResponse();
      //expect(instance).to.be();
    });

  });

}));
