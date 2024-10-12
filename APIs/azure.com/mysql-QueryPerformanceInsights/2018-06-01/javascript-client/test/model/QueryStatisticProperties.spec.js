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
    instance = new MySqlManagementClient.QueryStatisticProperties();
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

  describe('QueryStatisticProperties', function() {
    it('should create an instance of QueryStatisticProperties', function() {
      // uncomment below and update the code to test QueryStatisticProperties
      //var instance = new MySqlManagementClient.QueryStatisticProperties();
      //expect(instance).to.be.a(MySqlManagementClient.QueryStatisticProperties);
    });

    it('should have the property aggregationFunction (base name: "aggregationFunction")', function() {
      // uncomment below and update the code to test the property aggregationFunction
      //var instance = new MySqlManagementClient.QueryStatisticProperties();
      //expect(instance).to.be();
    });

    it('should have the property databaseNames (base name: "databaseNames")', function() {
      // uncomment below and update the code to test the property databaseNames
      //var instance = new MySqlManagementClient.QueryStatisticProperties();
      //expect(instance).to.be();
    });

    it('should have the property endTime (base name: "endTime")', function() {
      // uncomment below and update the code to test the property endTime
      //var instance = new MySqlManagementClient.QueryStatisticProperties();
      //expect(instance).to.be();
    });

    it('should have the property metricDisplayName (base name: "metricDisplayName")', function() {
      // uncomment below and update the code to test the property metricDisplayName
      //var instance = new MySqlManagementClient.QueryStatisticProperties();
      //expect(instance).to.be();
    });

    it('should have the property metricName (base name: "metricName")', function() {
      // uncomment below and update the code to test the property metricName
      //var instance = new MySqlManagementClient.QueryStatisticProperties();
      //expect(instance).to.be();
    });

    it('should have the property metricValue (base name: "metricValue")', function() {
      // uncomment below and update the code to test the property metricValue
      //var instance = new MySqlManagementClient.QueryStatisticProperties();
      //expect(instance).to.be();
    });

    it('should have the property metricValueUnit (base name: "metricValueUnit")', function() {
      // uncomment below and update the code to test the property metricValueUnit
      //var instance = new MySqlManagementClient.QueryStatisticProperties();
      //expect(instance).to.be();
    });

    it('should have the property queryExecutionCount (base name: "queryExecutionCount")', function() {
      // uncomment below and update the code to test the property queryExecutionCount
      //var instance = new MySqlManagementClient.QueryStatisticProperties();
      //expect(instance).to.be();
    });

    it('should have the property queryId (base name: "queryId")', function() {
      // uncomment below and update the code to test the property queryId
      //var instance = new MySqlManagementClient.QueryStatisticProperties();
      //expect(instance).to.be();
    });

    it('should have the property startTime (base name: "startTime")', function() {
      // uncomment below and update the code to test the property startTime
      //var instance = new MySqlManagementClient.QueryStatisticProperties();
      //expect(instance).to.be();
    });

  });

}));
