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
    instance = new MySqlManagementClient.WaitStatisticProperties();
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

  describe('WaitStatisticProperties', function() {
    it('should create an instance of WaitStatisticProperties', function() {
      // uncomment below and update the code to test WaitStatisticProperties
      //var instance = new MySqlManagementClient.WaitStatisticProperties();
      //expect(instance).to.be.a(MySqlManagementClient.WaitStatisticProperties);
    });

    it('should have the property count (base name: "count")', function() {
      // uncomment below and update the code to test the property count
      //var instance = new MySqlManagementClient.WaitStatisticProperties();
      //expect(instance).to.be();
    });

    it('should have the property databaseName (base name: "databaseName")', function() {
      // uncomment below and update the code to test the property databaseName
      //var instance = new MySqlManagementClient.WaitStatisticProperties();
      //expect(instance).to.be();
    });

    it('should have the property endTime (base name: "endTime")', function() {
      // uncomment below and update the code to test the property endTime
      //var instance = new MySqlManagementClient.WaitStatisticProperties();
      //expect(instance).to.be();
    });

    it('should have the property eventName (base name: "eventName")', function() {
      // uncomment below and update the code to test the property eventName
      //var instance = new MySqlManagementClient.WaitStatisticProperties();
      //expect(instance).to.be();
    });

    it('should have the property eventTypeName (base name: "eventTypeName")', function() {
      // uncomment below and update the code to test the property eventTypeName
      //var instance = new MySqlManagementClient.WaitStatisticProperties();
      //expect(instance).to.be();
    });

    it('should have the property queryId (base name: "queryId")', function() {
      // uncomment below and update the code to test the property queryId
      //var instance = new MySqlManagementClient.WaitStatisticProperties();
      //expect(instance).to.be();
    });

    it('should have the property startTime (base name: "startTime")', function() {
      // uncomment below and update the code to test the property startTime
      //var instance = new MySqlManagementClient.WaitStatisticProperties();
      //expect(instance).to.be();
    });

    it('should have the property totalTimeInMs (base name: "totalTimeInMs")', function() {
      // uncomment below and update the code to test the property totalTimeInMs
      //var instance = new MySqlManagementClient.WaitStatisticProperties();
      //expect(instance).to.be();
    });

    it('should have the property userId (base name: "userId")', function() {
      // uncomment below and update the code to test the property userId
      //var instance = new MySqlManagementClient.WaitStatisticProperties();
      //expect(instance).to.be();
    });

  });

}));
