/**
 * ApiManagementClient
 * Use this REST API to get all the issues across an Azure Api Management service.
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
    factory(root.expect, root.ApiManagementClient);
  }
}(this, function(expect, ApiManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new ApiManagementClient.IssueListByServiceDefaultResponseErrorDetailsInner();
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

  describe('IssueListByServiceDefaultResponseErrorDetailsInner', function() {
    it('should create an instance of IssueListByServiceDefaultResponseErrorDetailsInner', function() {
      // uncomment below and update the code to test IssueListByServiceDefaultResponseErrorDetailsInner
      //var instance = new ApiManagementClient.IssueListByServiceDefaultResponseErrorDetailsInner();
      //expect(instance).to.be.a(ApiManagementClient.IssueListByServiceDefaultResponseErrorDetailsInner);
    });

    it('should have the property code (base name: "code")', function() {
      // uncomment below and update the code to test the property code
      //var instance = new ApiManagementClient.IssueListByServiceDefaultResponseErrorDetailsInner();
      //expect(instance).to.be();
    });

    it('should have the property message (base name: "message")', function() {
      // uncomment below and update the code to test the property message
      //var instance = new ApiManagementClient.IssueListByServiceDefaultResponseErrorDetailsInner();
      //expect(instance).to.be();
    });

    it('should have the property target (base name: "target")', function() {
      // uncomment below and update the code to test the property target
      //var instance = new ApiManagementClient.IssueListByServiceDefaultResponseErrorDetailsInner();
      //expect(instance).to.be();
    });

  });

}));
