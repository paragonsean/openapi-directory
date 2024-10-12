/**
 * HDInsightManagementClient
 * The HDInsight Management Client.
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
    factory(root.expect, root.HdInsightManagementClient);
  }
}(this, function(expect, HdInsightManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new HdInsightManagementClient.ApplicationPropertiesInstallScriptActionsInner();
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

  describe('ApplicationPropertiesInstallScriptActionsInner', function() {
    it('should create an instance of ApplicationPropertiesInstallScriptActionsInner', function() {
      // uncomment below and update the code to test ApplicationPropertiesInstallScriptActionsInner
      //var instance = new HdInsightManagementClient.ApplicationPropertiesInstallScriptActionsInner();
      //expect(instance).to.be.a(HdInsightManagementClient.ApplicationPropertiesInstallScriptActionsInner);
    });

    it('should have the property applicationName (base name: "applicationName")', function() {
      // uncomment below and update the code to test the property applicationName
      //var instance = new HdInsightManagementClient.ApplicationPropertiesInstallScriptActionsInner();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new HdInsightManagementClient.ApplicationPropertiesInstallScriptActionsInner();
      //expect(instance).to.be();
    });

    it('should have the property parameters (base name: "parameters")', function() {
      // uncomment below and update the code to test the property parameters
      //var instance = new HdInsightManagementClient.ApplicationPropertiesInstallScriptActionsInner();
      //expect(instance).to.be();
    });

    it('should have the property roles (base name: "roles")', function() {
      // uncomment below and update the code to test the property roles
      //var instance = new HdInsightManagementClient.ApplicationPropertiesInstallScriptActionsInner();
      //expect(instance).to.be();
    });

    it('should have the property uri (base name: "uri")', function() {
      // uncomment below and update the code to test the property uri
      //var instance = new HdInsightManagementClient.ApplicationPropertiesInstallScriptActionsInner();
      //expect(instance).to.be();
    });

  });

}));
