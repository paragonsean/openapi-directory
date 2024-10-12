/**
 * SqlManagementClient
 * The Azure SQL Database management API provides a RESTful set of web APIs that interact with Azure SQL Database services to manage your databases. The API enables users to create, retrieve, update, and delete databases, servers, and other entities.
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
    factory(root.expect, root.SqlManagementClient);
  }
}(this, function(expect, SqlManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new SqlManagementClient.Usage();
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

  describe('Usage', function() {
    it('should create an instance of Usage', function() {
      // uncomment below and update the code to test Usage
      //var instance = new SqlManagementClient.Usage();
      //expect(instance).to.be.a(SqlManagementClient.Usage);
    });

    it('should have the property currentValue (base name: "currentValue")', function() {
      // uncomment below and update the code to test the property currentValue
      //var instance = new SqlManagementClient.Usage();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new SqlManagementClient.Usage();
      //expect(instance).to.be();
    });

    it('should have the property limit (base name: "limit")', function() {
      // uncomment below and update the code to test the property limit
      //var instance = new SqlManagementClient.Usage();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new SqlManagementClient.Usage();
      //expect(instance).to.be();
    });

    it('should have the property requestedLimit (base name: "requestedLimit")', function() {
      // uncomment below and update the code to test the property requestedLimit
      //var instance = new SqlManagementClient.Usage();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new SqlManagementClient.Usage();
      //expect(instance).to.be();
    });

    it('should have the property unit (base name: "unit")', function() {
      // uncomment below and update the code to test the property unit
      //var instance = new SqlManagementClient.Usage();
      //expect(instance).to.be();
    });

  });

}));
