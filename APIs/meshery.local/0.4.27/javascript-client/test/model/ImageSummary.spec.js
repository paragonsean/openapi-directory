/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
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
    factory(root.expect, root.MesheryApi);
  }
}(this, function(expect, MesheryApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MesheryApi.ImageSummary();
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

  describe('ImageSummary', function() {
    it('should create an instance of ImageSummary', function() {
      // uncomment below and update the code to test ImageSummary
      //var instance = new MesheryApi.ImageSummary();
      //expect(instance).to.be.a(MesheryApi.ImageSummary);
    });

    it('should have the property containers (base name: "Containers")', function() {
      // uncomment below and update the code to test the property containers
      //var instance = new MesheryApi.ImageSummary();
      //expect(instance).to.be();
    });

    it('should have the property created (base name: "Created")', function() {
      // uncomment below and update the code to test the property created
      //var instance = new MesheryApi.ImageSummary();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "Id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new MesheryApi.ImageSummary();
      //expect(instance).to.be();
    });

    it('should have the property labels (base name: "Labels")', function() {
      // uncomment below and update the code to test the property labels
      //var instance = new MesheryApi.ImageSummary();
      //expect(instance).to.be();
    });

    it('should have the property parentId (base name: "ParentId")', function() {
      // uncomment below and update the code to test the property parentId
      //var instance = new MesheryApi.ImageSummary();
      //expect(instance).to.be();
    });

    it('should have the property repoDigests (base name: "RepoDigests")', function() {
      // uncomment below and update the code to test the property repoDigests
      //var instance = new MesheryApi.ImageSummary();
      //expect(instance).to.be();
    });

    it('should have the property repoTags (base name: "RepoTags")', function() {
      // uncomment below and update the code to test the property repoTags
      //var instance = new MesheryApi.ImageSummary();
      //expect(instance).to.be();
    });

    it('should have the property sharedSize (base name: "SharedSize")', function() {
      // uncomment below and update the code to test the property sharedSize
      //var instance = new MesheryApi.ImageSummary();
      //expect(instance).to.be();
    });

    it('should have the property size (base name: "Size")', function() {
      // uncomment below and update the code to test the property size
      //var instance = new MesheryApi.ImageSummary();
      //expect(instance).to.be();
    });

    it('should have the property virtualSize (base name: "VirtualSize")', function() {
      // uncomment below and update the code to test the property virtualSize
      //var instance = new MesheryApi.ImageSummary();
      //expect(instance).to.be();
    });

  });

}));
