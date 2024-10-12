/**
 * AutomationManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-01-15
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
    factory(root.expect, root.AutomationManagement);
  }
}(this, function(expect, AutomationManagement) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AutomationManagement.DscCompilationJobProperties();
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

  describe('DscCompilationJobProperties', function() {
    it('should create an instance of DscCompilationJobProperties', function() {
      // uncomment below and update the code to test DscCompilationJobProperties
      //var instance = new AutomationManagement.DscCompilationJobProperties();
      //expect(instance).to.be.a(AutomationManagement.DscCompilationJobProperties);
    });

    it('should have the property configuration (base name: "configuration")', function() {
      // uncomment below and update the code to test the property configuration
      //var instance = new AutomationManagement.DscCompilationJobProperties();
      //expect(instance).to.be();
    });

    it('should have the property creationTime (base name: "creationTime")', function() {
      // uncomment below and update the code to test the property creationTime
      //var instance = new AutomationManagement.DscCompilationJobProperties();
      //expect(instance).to.be();
    });

    it('should have the property endTime (base name: "endTime")', function() {
      // uncomment below and update the code to test the property endTime
      //var instance = new AutomationManagement.DscCompilationJobProperties();
      //expect(instance).to.be();
    });

    it('should have the property exception (base name: "exception")', function() {
      // uncomment below and update the code to test the property exception
      //var instance = new AutomationManagement.DscCompilationJobProperties();
      //expect(instance).to.be();
    });

    it('should have the property jobId (base name: "jobId")', function() {
      // uncomment below and update the code to test the property jobId
      //var instance = new AutomationManagement.DscCompilationJobProperties();
      //expect(instance).to.be();
    });

    it('should have the property lastModifiedTime (base name: "lastModifiedTime")', function() {
      // uncomment below and update the code to test the property lastModifiedTime
      //var instance = new AutomationManagement.DscCompilationJobProperties();
      //expect(instance).to.be();
    });

    it('should have the property lastStatusModifiedTime (base name: "lastStatusModifiedTime")', function() {
      // uncomment below and update the code to test the property lastStatusModifiedTime
      //var instance = new AutomationManagement.DscCompilationJobProperties();
      //expect(instance).to.be();
    });

    it('should have the property parameters (base name: "parameters")', function() {
      // uncomment below and update the code to test the property parameters
      //var instance = new AutomationManagement.DscCompilationJobProperties();
      //expect(instance).to.be();
    });

    it('should have the property provisioningState (base name: "provisioningState")', function() {
      // uncomment below and update the code to test the property provisioningState
      //var instance = new AutomationManagement.DscCompilationJobProperties();
      //expect(instance).to.be();
    });

    it('should have the property runOn (base name: "runOn")', function() {
      // uncomment below and update the code to test the property runOn
      //var instance = new AutomationManagement.DscCompilationJobProperties();
      //expect(instance).to.be();
    });

    it('should have the property startTime (base name: "startTime")', function() {
      // uncomment below and update the code to test the property startTime
      //var instance = new AutomationManagement.DscCompilationJobProperties();
      //expect(instance).to.be();
    });

    it('should have the property startedBy (base name: "startedBy")', function() {
      // uncomment below and update the code to test the property startedBy
      //var instance = new AutomationManagement.DscCompilationJobProperties();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new AutomationManagement.DscCompilationJobProperties();
      //expect(instance).to.be();
    });

    it('should have the property statusDetails (base name: "statusDetails")', function() {
      // uncomment below and update the code to test the property statusDetails
      //var instance = new AutomationManagement.DscCompilationJobProperties();
      //expect(instance).to.be();
    });

  });

}));
