/**
 * CodeScan API
 * Manage your Hosted CodeScan Service
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@villagechief.com
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
    factory(root.expect, root.CodeScanApi);
  }
}(this, function(expect, CodeScanApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new CodeScanApi.Job();
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

  describe('Job', function() {
    it('should create an instance of Job', function() {
      // uncomment below and update the code to test Job
      //var instance = new CodeScanApi.Job();
      //expect(instance).to.be.a(CodeScanApi.Job);
    });

    it('should have the property alert (base name: "alert")', function() {
      // uncomment below and update the code to test the property alert
      //var instance = new CodeScanApi.Job();
      //expect(instance).to.be();
    });

    it('should have the property alertDescription (base name: "alertDescription")', function() {
      // uncomment below and update the code to test the property alertDescription
      //var instance = new CodeScanApi.Job();
      //expect(instance).to.be();
    });

    it('should have the property analysisMode (base name: "analysisMode")', function() {
      // uncomment below and update the code to test the property analysisMode
      //var instance = new CodeScanApi.Job();
      //expect(instance).to.be();
    });

    it('should have the property commit (base name: "commit")', function() {
      // uncomment below and update the code to test the property commit
      //var instance = new CodeScanApi.Job();
      //expect(instance).to.be();
    });

    it('should have the property created (base name: "created")', function() {
      // uncomment below and update the code to test the property created
      //var instance = new CodeScanApi.Job();
      //expect(instance).to.be();
    });

    it('should have the property emailReportTo (base name: "emailReportTo")', function() {
      // uncomment below and update the code to test the property emailReportTo
      //var instance = new CodeScanApi.Job();
      //expect(instance).to.be();
    });

    it('should have the property finished (base name: "finished")', function() {
      // uncomment below and update the code to test the property finished
      //var instance = new CodeScanApi.Job();
      //expect(instance).to.be();
    });

    it('should have the property jobId (base name: "jobId")', function() {
      // uncomment below and update the code to test the property jobId
      //var instance = new CodeScanApi.Job();
      //expect(instance).to.be();
    });

    it('should have the property projectBranch (base name: "projectBranch")', function() {
      // uncomment below and update the code to test the property projectBranch
      //var instance = new CodeScanApi.Job();
      //expect(instance).to.be();
    });

    it('should have the property projectKey (base name: "projectKey")', function() {
      // uncomment below and update the code to test the property projectKey
      //var instance = new CodeScanApi.Job();
      //expect(instance).to.be();
    });

    it('should have the property started (base name: "started")', function() {
      // uncomment below and update the code to test the property started
      //var instance = new CodeScanApi.Job();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new CodeScanApi.Job();
      //expect(instance).to.be();
    });

    it('should have the property url (base name: "url")', function() {
      // uncomment below and update the code to test the property url
      //var instance = new CodeScanApi.Job();
      //expect(instance).to.be();
    });

    it('should have the property version (base name: "version")', function() {
      // uncomment below and update the code to test the property version
      //var instance = new CodeScanApi.Job();
      //expect(instance).to.be();
    });

    it('should have the property warnings (base name: "warnings")', function() {
      // uncomment below and update the code to test the property warnings
      //var instance = new CodeScanApi.Job();
      //expect(instance).to.be();
    });

  });

}));
