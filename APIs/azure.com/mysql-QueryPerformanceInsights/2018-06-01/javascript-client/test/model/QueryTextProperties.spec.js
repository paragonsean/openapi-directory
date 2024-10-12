/**
 * MySQLManagementClient
 * The Microsoft Azure management API provides create, read, update, and delete functionality for Azure MySQL resources including servers, databases, firewall rules, VNET rules, security alert policies, log files and configurations with new business model.
 *
 * The version of the OpenAPI document: 2018-06-01
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
    factory(root.expect, root.MySqlManagementClient);
  }
}(this, function(expect, MySqlManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MySqlManagementClient.QueryTextProperties();
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

  describe('QueryTextProperties', function() {
    it('should create an instance of QueryTextProperties', function() {
      // uncomment below and update the code to test QueryTextProperties
      //var instance = new MySqlManagementClient.QueryTextProperties();
      //expect(instance).to.be.a(MySqlManagementClient.QueryTextProperties);
    });

    it('should have the property queryId (base name: "queryId")', function() {
      // uncomment below and update the code to test the property queryId
      //var instance = new MySqlManagementClient.QueryTextProperties();
      //expect(instance).to.be();
    });

    it('should have the property queryText (base name: "queryText")', function() {
      // uncomment below and update the code to test the property queryText
      //var instance = new MySqlManagementClient.QueryTextProperties();
      //expect(instance).to.be();
    });

  });

}));
