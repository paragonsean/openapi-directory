/**
 * OOXML Automation
 * This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.
 *
 * The version of the OpenAPI document: 0.1.0
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
    factory(root.expect, root.OoxmlAutomation);
  }
}(this, function(expect, OoxmlAutomation) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new OoxmlAutomation.SlideSlidesDetails();
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

  describe('SlideSlidesDetails', function() {
    it('should create an instance of SlideSlidesDetails', function() {
      // uncomment below and update the code to test SlideSlidesDetails
      //var instance = new OoxmlAutomation.SlideSlidesDetails();
      //expect(instance).to.be.a(OoxmlAutomation.SlideSlidesDetails);
    });

    it('should have the property baseElementBlobUrl (base name: "baseElementBlobUrl")', function() {
      // uncomment below and update the code to test the property baseElementBlobUrl
      //var instance = new OoxmlAutomation.SlideSlidesDetails();
      //expect(instance).to.be();
    });

    it('should have the property changedBaseElementBlobUrl (base name: "changedBaseElementBlobUrl")', function() {
      // uncomment below and update the code to test the property changedBaseElementBlobUrl
      //var instance = new OoxmlAutomation.SlideSlidesDetails();
      //expect(instance).to.be();
    });

    it('should have the property dateCreated (base name: "dateCreated")', function() {
      // uncomment below and update the code to test the property dateCreated
      //var instance = new OoxmlAutomation.SlideSlidesDetails();
      //expect(instance).to.be();
    });

    it('should have the property dateModified (base name: "dateModified")', function() {
      // uncomment below and update the code to test the property dateModified
      //var instance = new OoxmlAutomation.SlideSlidesDetails();
      //expect(instance).to.be();
    });

    it('should have the property document (base name: "document")', function() {
      // uncomment below and update the code to test the property document
      //var instance = new OoxmlAutomation.SlideSlidesDetails();
      //expect(instance).to.be();
    });

    it('should have the property documentId (base name: "documentId")', function() {
      // uncomment below and update the code to test the property documentId
      //var instance = new OoxmlAutomation.SlideSlidesDetails();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new OoxmlAutomation.SlideSlidesDetails();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new OoxmlAutomation.SlideSlidesDetails();
      //expect(instance).to.be();
    });

    it('should have the property number (base name: "number")', function() {
      // uncomment below and update the code to test the property number
      //var instance = new OoxmlAutomation.SlideSlidesDetails();
      //expect(instance).to.be();
    });

    it('should have the property ooxmlId (base name: "ooxmlId")', function() {
      // uncomment below and update the code to test the property ooxmlId
      //var instance = new OoxmlAutomation.SlideSlidesDetails();
      //expect(instance).to.be();
    });

    it('should have the property packageUri (base name: "packageUri")', function() {
      // uncomment below and update the code to test the property packageUri
      //var instance = new OoxmlAutomation.SlideSlidesDetails();
      //expect(instance).to.be();
    });

    it('should have the property shapeTree (base name: "shapeTree")', function() {
      // uncomment below and update the code to test the property shapeTree
      //var instance = new OoxmlAutomation.SlideSlidesDetails();
      //expect(instance).to.be();
    });

    it('should have the property slideDocumentUrl (base name: "slideDocumentUrl")', function() {
      // uncomment below and update the code to test the property slideDocumentUrl
      //var instance = new OoxmlAutomation.SlideSlidesDetails();
      //expect(instance).to.be();
    });

    it('should have the property slideMaster (base name: "slideMaster")', function() {
      // uncomment below and update the code to test the property slideMaster
      //var instance = new OoxmlAutomation.SlideSlidesDetails();
      //expect(instance).to.be();
    });

    it('should have the property svgBlobUrl (base name: "svgBlobUrl")', function() {
      // uncomment below and update the code to test the property svgBlobUrl
      //var instance = new OoxmlAutomation.SlideSlidesDetails();
      //expect(instance).to.be();
    });

    it('should have the property theme (base name: "theme")', function() {
      // uncomment below and update the code to test the property theme
      //var instance = new OoxmlAutomation.SlideSlidesDetails();
      //expect(instance).to.be();
    });

    it('should have the property userCreated (base name: "userCreated")', function() {
      // uncomment below and update the code to test the property userCreated
      //var instance = new OoxmlAutomation.SlideSlidesDetails();
      //expect(instance).to.be();
    });

    it('should have the property userModified (base name: "userModified")', function() {
      // uncomment below and update the code to test the property userModified
      //var instance = new OoxmlAutomation.SlideSlidesDetails();
      //expect(instance).to.be();
    });

  });

}));
