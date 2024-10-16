/**
 * Story
 * This API is the main entry point for creating, editing and publishing analytics throught the Presalytics API
 *
 * The version of the OpenAPI document: 0.3.1
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
    factory(root.expect, root.Story);
  }
}(this, function(expect, Story) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new Story.Story();
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

  describe('Story', function() {
    it('should create an instance of Story', function() {
      // uncomment below and update the code to test Story
      //var instance = new Story.Story();
      //expect(instance).to.be.a(Story.Story);
    });

    it('should have the property createdAt (base name: "created_at")', function() {
      // uncomment below and update the code to test the property createdAt
      //var instance = new Story.Story();
      //expect(instance).to.be();
    });

    it('should have the property createdBy (base name: "created_by")', function() {
      // uncomment below and update the code to test the property createdBy
      //var instance = new Story.Story();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new Story.Story();
      //expect(instance).to.be();
    });

    it('should have the property updatedAt (base name: "updated_at")', function() {
      // uncomment below and update the code to test the property updatedAt
      //var instance = new Story.Story();
      //expect(instance).to.be();
    });

    it('should have the property updatedBy (base name: "updated_by")', function() {
      // uncomment below and update the code to test the property updatedBy
      //var instance = new Story.Story();
      //expect(instance).to.be();
    });

    it('should have the property collaborators (base name: "collaborators")', function() {
      // uncomment below and update the code to test the property collaborators
      //var instance = new Story.Story();
      //expect(instance).to.be();
    });

    it('should have the property isPublic (base name: "is_public")', function() {
      // uncomment below and update the code to test the property isPublic
      //var instance = new Story.Story();
      //expect(instance).to.be();
    });

    it('should have the property ooxmlDocuments (base name: "ooxml_documents")', function() {
      // uncomment below and update the code to test the property ooxmlDocuments
      //var instance = new Story.Story();
      //expect(instance).to.be();
    });

    it('should have the property outline (base name: "outline")', function() {
      // uncomment below and update the code to test the property outline
      //var instance = new Story.Story();
      //expect(instance).to.be();
    });

    it('should have the property outlineHistory (base name: "outline_history")', function() {
      // uncomment below and update the code to test the property outlineHistory
      //var instance = new Story.Story();
      //expect(instance).to.be();
    });

    it('should have the property revision (base name: "revision")', function() {
      // uncomment below and update the code to test the property revision
      //var instance = new Story.Story();
      //expect(instance).to.be();
    });

    it('should have the property title (base name: "title")', function() {
      // uncomment below and update the code to test the property title
      //var instance = new Story.Story();
      //expect(instance).to.be();
    });

  });

}));
