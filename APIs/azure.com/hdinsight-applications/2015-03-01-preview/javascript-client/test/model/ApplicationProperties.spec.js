/**
 * HDInsightManagementClient
 * The HDInsight Management Client.
 *
 * The version of the OpenAPI document: 2015-03-01-preview
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
    factory(root.expect, root.HdInsightManagementClient);
  }
}(this, function(expect, HdInsightManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new HdInsightManagementClient.ApplicationProperties();
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

  describe('ApplicationProperties', function() {
    it('should create an instance of ApplicationProperties', function() {
      // uncomment below and update the code to test ApplicationProperties
      //var instance = new HdInsightManagementClient.ApplicationProperties();
      //expect(instance).to.be.a(HdInsightManagementClient.ApplicationProperties);
    });

    it('should have the property applicationState (base name: "applicationState")', function() {
      // uncomment below and update the code to test the property applicationState
      //var instance = new HdInsightManagementClient.ApplicationProperties();
      //expect(instance).to.be();
    });

    it('should have the property applicationType (base name: "applicationType")', function() {
      // uncomment below and update the code to test the property applicationType
      //var instance = new HdInsightManagementClient.ApplicationProperties();
      //expect(instance).to.be();
    });

    it('should have the property computeProfile (base name: "computeProfile")', function() {
      // uncomment below and update the code to test the property computeProfile
      //var instance = new HdInsightManagementClient.ApplicationProperties();
      //expect(instance).to.be();
    });

    it('should have the property createdDate (base name: "createdDate")', function() {
      // uncomment below and update the code to test the property createdDate
      //var instance = new HdInsightManagementClient.ApplicationProperties();
      //expect(instance).to.be();
    });

    it('should have the property errors (base name: "errors")', function() {
      // uncomment below and update the code to test the property errors
      //var instance = new HdInsightManagementClient.ApplicationProperties();
      //expect(instance).to.be();
    });

    it('should have the property httpsEndpoints (base name: "httpsEndpoints")', function() {
      // uncomment below and update the code to test the property httpsEndpoints
      //var instance = new HdInsightManagementClient.ApplicationProperties();
      //expect(instance).to.be();
    });

    it('should have the property installScriptActions (base name: "installScriptActions")', function() {
      // uncomment below and update the code to test the property installScriptActions
      //var instance = new HdInsightManagementClient.ApplicationProperties();
      //expect(instance).to.be();
    });

    it('should have the property marketplaceIdentifier (base name: "marketplaceIdentifier")', function() {
      // uncomment below and update the code to test the property marketplaceIdentifier
      //var instance = new HdInsightManagementClient.ApplicationProperties();
      //expect(instance).to.be();
    });

    it('should have the property provisioningState (base name: "provisioningState")', function() {
      // uncomment below and update the code to test the property provisioningState
      //var instance = new HdInsightManagementClient.ApplicationProperties();
      //expect(instance).to.be();
    });

    it('should have the property sshEndpoints (base name: "sshEndpoints")', function() {
      // uncomment below and update the code to test the property sshEndpoints
      //var instance = new HdInsightManagementClient.ApplicationProperties();
      //expect(instance).to.be();
    });

    it('should have the property uninstallScriptActions (base name: "uninstallScriptActions")', function() {
      // uncomment below and update the code to test the property uninstallScriptActions
      //var instance = new HdInsightManagementClient.ApplicationProperties();
      //expect(instance).to.be();
    });

  });

}));
