/**
 * SqlManagementClient
 * The Azure SQL Database management API provides a RESTful set of web APIs that interact with Azure SQL Database services to manage your databases. The API enables users to create, retrieve, update, and delete databases, servers, and other entities.
 *
 * The version of the OpenAPI document: 2015-05-01-preview
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
    factory(root.expect, root.SqlManagementClient);
  }
}(this, function(expect, SqlManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new SqlManagementClient.FailoverGroupReadWriteEndpoint();
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

  describe('FailoverGroupReadWriteEndpoint', function() {
    it('should create an instance of FailoverGroupReadWriteEndpoint', function() {
      // uncomment below and update the code to test FailoverGroupReadWriteEndpoint
      //var instance = new SqlManagementClient.FailoverGroupReadWriteEndpoint();
      //expect(instance).to.be.a(SqlManagementClient.FailoverGroupReadWriteEndpoint);
    });

    it('should have the property failoverPolicy (base name: "failoverPolicy")', function() {
      // uncomment below and update the code to test the property failoverPolicy
      //var instance = new SqlManagementClient.FailoverGroupReadWriteEndpoint();
      //expect(instance).to.be();
    });

    it('should have the property failoverWithDataLossGracePeriodMinutes (base name: "failoverWithDataLossGracePeriodMinutes")', function() {
      // uncomment below and update the code to test the property failoverWithDataLossGracePeriodMinutes
      //var instance = new SqlManagementClient.FailoverGroupReadWriteEndpoint();
      //expect(instance).to.be();
    });

  });

}));
