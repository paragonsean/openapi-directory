/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.0
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
    instance = new CustomVisionTrainingClient.Tag();
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

  describe('Tag', function() {
    it('should create an instance of Tag', function() {
      // uncomment below and update the code to test Tag
      //var instance = new CustomVisionTrainingClient.Tag();
      //expect(instance).to.be.a(CustomVisionTrainingClient.Tag);
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new CustomVisionTrainingClient.Tag();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new CustomVisionTrainingClient.Tag();
      //expect(instance).to.be();
    });

    it('should have the property imageCount (base name: "imageCount")', function() {
      // uncomment below and update the code to test the property imageCount
      //var instance = new CustomVisionTrainingClient.Tag();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new CustomVisionTrainingClient.Tag();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new CustomVisionTrainingClient.Tag();
      //expect(instance).to.be();
    });

  });

}));
