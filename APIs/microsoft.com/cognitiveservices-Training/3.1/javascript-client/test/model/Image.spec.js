/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.1
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
    factory(root.expect, root.CustomVisionTrainingClient);
  }
}(this, function(expect, CustomVisionTrainingClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new CustomVisionTrainingClient.Image();
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

  describe('Image', function() {
    it('should create an instance of Image', function() {
      // uncomment below and update the code to test Image
      //var instance = new CustomVisionTrainingClient.Image();
      //expect(instance).to.be.a(CustomVisionTrainingClient.Image);
    });

    it('should have the property created (base name: "created")', function() {
      // uncomment below and update the code to test the property created
      //var instance = new CustomVisionTrainingClient.Image();
      //expect(instance).to.be();
    });

    it('should have the property height (base name: "height")', function() {
      // uncomment below and update the code to test the property height
      //var instance = new CustomVisionTrainingClient.Image();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new CustomVisionTrainingClient.Image();
      //expect(instance).to.be();
    });

    it('should have the property originalImageUri (base name: "originalImageUri")', function() {
      // uncomment below and update the code to test the property originalImageUri
      //var instance = new CustomVisionTrainingClient.Image();
      //expect(instance).to.be();
    });

    it('should have the property regions (base name: "regions")', function() {
      // uncomment below and update the code to test the property regions
      //var instance = new CustomVisionTrainingClient.Image();
      //expect(instance).to.be();
    });

    it('should have the property resizedImageUri (base name: "resizedImageUri")', function() {
      // uncomment below and update the code to test the property resizedImageUri
      //var instance = new CustomVisionTrainingClient.Image();
      //expect(instance).to.be();
    });

    it('should have the property tags (base name: "tags")', function() {
      // uncomment below and update the code to test the property tags
      //var instance = new CustomVisionTrainingClient.Image();
      //expect(instance).to.be();
    });

    it('should have the property thumbnailUri (base name: "thumbnailUri")', function() {
      // uncomment below and update the code to test the property thumbnailUri
      //var instance = new CustomVisionTrainingClient.Image();
      //expect(instance).to.be();
    });

    it('should have the property width (base name: "width")', function() {
      // uncomment below and update the code to test the property width
      //var instance = new CustomVisionTrainingClient.Image();
      //expect(instance).to.be();
    });

  });

}));
