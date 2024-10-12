/**
 * DataLakeStoreAccountManagementClient
 * Creates an Azure Data Lake Store account management client.
 *
 * The version of the OpenAPI document: 2016-11-01
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
    factory(root.expect, root.DataLakeStoreAccountManagementClient);
  }
}(this, function(expect, DataLakeStoreAccountManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new DataLakeStoreAccountManagementClient.CreateOrUpdateFirewallRuleProperties();
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

  describe('CreateOrUpdateFirewallRuleProperties', function() {
    it('should create an instance of CreateOrUpdateFirewallRuleProperties', function() {
      // uncomment below and update the code to test CreateOrUpdateFirewallRuleProperties
      //var instance = new DataLakeStoreAccountManagementClient.CreateOrUpdateFirewallRuleProperties();
      //expect(instance).to.be.a(DataLakeStoreAccountManagementClient.CreateOrUpdateFirewallRuleProperties);
    });

    it('should have the property endIpAddress (base name: "endIpAddress")', function() {
      // uncomment below and update the code to test the property endIpAddress
      //var instance = new DataLakeStoreAccountManagementClient.CreateOrUpdateFirewallRuleProperties();
      //expect(instance).to.be();
    });

    it('should have the property startIpAddress (base name: "startIpAddress")', function() {
      // uncomment below and update the code to test the property startIpAddress
      //var instance = new DataLakeStoreAccountManagementClient.CreateOrUpdateFirewallRuleProperties();
      //expect(instance).to.be();
    });

  });

}));
