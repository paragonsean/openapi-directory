/**
 * MySQLManagementClient
 * The Microsoft Azure management API provides create, read, update, and delete functionality for Azure MySQL resources including servers, databases, firewall rules, VNET rules, security alert policies, log files and configurations with new business model.
 *
 * The version of the OpenAPI document: 2018-06-01-privatepreview
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
    instance = new MySqlManagementClient.PrivateEndpointConnectionProperties();
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

  describe('PrivateEndpointConnectionProperties', function() {
    it('should create an instance of PrivateEndpointConnectionProperties', function() {
      // uncomment below and update the code to test PrivateEndpointConnectionProperties
      //var instance = new MySqlManagementClient.PrivateEndpointConnectionProperties();
      //expect(instance).to.be.a(MySqlManagementClient.PrivateEndpointConnectionProperties);
    });

    it('should have the property privateEndpoint (base name: "privateEndpoint")', function() {
      // uncomment below and update the code to test the property privateEndpoint
      //var instance = new MySqlManagementClient.PrivateEndpointConnectionProperties();
      //expect(instance).to.be();
    });

    it('should have the property privateLinkServiceConnectionState (base name: "privateLinkServiceConnectionState")', function() {
      // uncomment below and update the code to test the property privateLinkServiceConnectionState
      //var instance = new MySqlManagementClient.PrivateEndpointConnectionProperties();
      //expect(instance).to.be();
    });

    it('should have the property provisioningState (base name: "provisioningState")', function() {
      // uncomment below and update the code to test the property provisioningState
      //var instance = new MySqlManagementClient.PrivateEndpointConnectionProperties();
      //expect(instance).to.be();
    });

  });

}));
