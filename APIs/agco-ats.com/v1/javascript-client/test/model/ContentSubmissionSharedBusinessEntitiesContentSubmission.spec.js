/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
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
    factory(root.expect, root.AgcoApi);
  }
}(this, function(expect, AgcoApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentSubmission();
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

  describe('ContentSubmissionSharedBusinessEntitiesContentSubmission', function() {
    it('should create an instance of ContentSubmissionSharedBusinessEntitiesContentSubmission', function() {
      // uncomment below and update the code to test ContentSubmissionSharedBusinessEntitiesContentSubmission
      //var instance = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentSubmission();
      //expect(instance).to.be.a(AgcoApi.ContentSubmissionSharedBusinessEntitiesContentSubmission);
    });

    it('should have the property attributes (base name: "Attributes")', function() {
      // uncomment below and update the code to test the property attributes
      //var instance = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentSubmission();
      //expect(instance).to.be();
    });

    it('should have the property buildID (base name: "BuildID")', function() {
      // uncomment below and update the code to test the property buildID
      //var instance = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentSubmission();
      //expect(instance).to.be();
    });

    it('should have the property contentDefinitionID (base name: "ContentDefinitionID")', function() {
      // uncomment below and update the code to test the property contentDefinitionID
      //var instance = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentSubmission();
      //expect(instance).to.be();
    });

    it('should have the property contentSubmissionID (base name: "ContentSubmissionID")', function() {
      // uncomment below and update the code to test the property contentSubmissionID
      //var instance = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentSubmission();
      //expect(instance).to.be();
    });

    it('should have the property definition (base name: "Definition")', function() {
      // uncomment below and update the code to test the property definition
      //var instance = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentSubmission();
      //expect(instance).to.be();
    });

    it('should have the property jobRunID (base name: "JobRunID")', function() {
      // uncomment below and update the code to test the property jobRunID
      //var instance = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentSubmission();
      //expect(instance).to.be();
    });

    it('should have the property packageID (base name: "PackageID")', function() {
      // uncomment below and update the code to test the property packageID
      //var instance = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentSubmission();
      //expect(instance).to.be();
    });

    it('should have the property releaseNotes (base name: "ReleaseNotes")', function() {
      // uncomment below and update the code to test the property releaseNotes
      //var instance = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentSubmission();
      //expect(instance).to.be();
    });

    it('should have the property repository (base name: "Repository")', function() {
      // uncomment below and update the code to test the property repository
      //var instance = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentSubmission();
      //expect(instance).to.be();
    });

    it('should have the property revision (base name: "Revision")', function() {
      // uncomment below and update the code to test the property revision
      //var instance = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentSubmission();
      //expect(instance).to.be();
    });

    it('should have the property submissionDate (base name: "SubmissionDate")', function() {
      // uncomment below and update the code to test the property submissionDate
      //var instance = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentSubmission();
      //expect(instance).to.be();
    });

    it('should have the property userID (base name: "UserID")', function() {
      // uncomment below and update the code to test the property userID
      //var instance = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentSubmission();
      //expect(instance).to.be();
    });

    it('should have the property version (base name: "Version")', function() {
      // uncomment below and update the code to test the property version
      //var instance = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentSubmission();
      //expect(instance).to.be();
    });

  });

}));
