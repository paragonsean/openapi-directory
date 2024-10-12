/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.2
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
    instance = new CustomVisionTrainingClient.ImageRegion();
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

  describe('ImageRegion', function() {
    it('should create an instance of ImageRegion', function() {
      // uncomment below and update the code to test ImageRegion
      //var instance = new CustomVisionTrainingClient.ImageRegion();
      //expect(instance).to.be.a(CustomVisionTrainingClient.ImageRegion);
    });

    it('should have the property created (base name: "created")', function() {
      // uncomment below and update the code to test the property created
      //var instance = new CustomVisionTrainingClient.ImageRegion();
      //expect(instance).to.be();
    });

    it('should have the property height (base name: "height")', function() {
      // uncomment below and update the code to test the property height
      //var instance = new CustomVisionTrainingClient.ImageRegion();
      //expect(instance).to.be();
    });

    it('should have the property left (base name: "left")', function() {
      // uncomment below and update the code to test the property left
      //var instance = new CustomVisionTrainingClient.ImageRegion();
      //expect(instance).to.be();
    });

    it('should have the property regionId (base name: "regionId")', function() {
      // uncomment below and update the code to test the property regionId
      //var instance = new CustomVisionTrainingClient.ImageRegion();
      //expect(instance).to.be();
    });

    it('should have the property tagId (base name: "tagId")', function() {
      // uncomment below and update the code to test the property tagId
      //var instance = new CustomVisionTrainingClient.ImageRegion();
      //expect(instance).to.be();
    });

    it('should have the property tagName (base name: "tagName")', function() {
      // uncomment below and update the code to test the property tagName
      //var instance = new CustomVisionTrainingClient.ImageRegion();
      //expect(instance).to.be();
    });

    it('should have the property top (base name: "top")', function() {
      // uncomment below and update the code to test the property top
      //var instance = new CustomVisionTrainingClient.ImageRegion();
      //expect(instance).to.be();
    });

    it('should have the property width (base name: "width")', function() {
      // uncomment below and update the code to test the property width
      //var instance = new CustomVisionTrainingClient.ImageRegion();
      //expect(instance).to.be();
    });

  });

}));
