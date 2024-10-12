/**
 * SqlManagementClient
 * The Azure SQL Database management API provides a RESTful set of web APIs that interact with Azure SQL Database services to manage your databases. The API enables users to create, retrieve, update, and delete databases, servers, and other entities.
 *
 * The version of the OpenAPI document: 2017-03-01-preview
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
    instance = new SqlManagementClient.SecurityAlertPolicyProperties();
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

  describe('SecurityAlertPolicyProperties', function() {
    it('should create an instance of SecurityAlertPolicyProperties', function() {
      // uncomment below and update the code to test SecurityAlertPolicyProperties
      //var instance = new SqlManagementClient.SecurityAlertPolicyProperties();
      //expect(instance).to.be.a(SqlManagementClient.SecurityAlertPolicyProperties);
    });

    it('should have the property creationTime (base name: "creationTime")', function() {
      // uncomment below and update the code to test the property creationTime
      //var instance = new SqlManagementClient.SecurityAlertPolicyProperties();
      //expect(instance).to.be();
    });

    it('should have the property disabledAlerts (base name: "disabledAlerts")', function() {
      // uncomment below and update the code to test the property disabledAlerts
      //var instance = new SqlManagementClient.SecurityAlertPolicyProperties();
      //expect(instance).to.be();
    });

    it('should have the property emailAccountAdmins (base name: "emailAccountAdmins")', function() {
      // uncomment below and update the code to test the property emailAccountAdmins
      //var instance = new SqlManagementClient.SecurityAlertPolicyProperties();
      //expect(instance).to.be();
    });

    it('should have the property emailAddresses (base name: "emailAddresses")', function() {
      // uncomment below and update the code to test the property emailAddresses
      //var instance = new SqlManagementClient.SecurityAlertPolicyProperties();
      //expect(instance).to.be();
    });

    it('should have the property retentionDays (base name: "retentionDays")', function() {
      // uncomment below and update the code to test the property retentionDays
      //var instance = new SqlManagementClient.SecurityAlertPolicyProperties();
      //expect(instance).to.be();
    });

    it('should have the property state (base name: "state")', function() {
      // uncomment below and update the code to test the property state
      //var instance = new SqlManagementClient.SecurityAlertPolicyProperties();
      //expect(instance).to.be();
    });

    it('should have the property storageAccountAccessKey (base name: "storageAccountAccessKey")', function() {
      // uncomment below and update the code to test the property storageAccountAccessKey
      //var instance = new SqlManagementClient.SecurityAlertPolicyProperties();
      //expect(instance).to.be();
    });

    it('should have the property storageEndpoint (base name: "storageEndpoint")', function() {
      // uncomment below and update the code to test the property storageEndpoint
      //var instance = new SqlManagementClient.SecurityAlertPolicyProperties();
      //expect(instance).to.be();
    });

  });

}));
