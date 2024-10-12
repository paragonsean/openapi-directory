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
    instance = new CustomVisionTrainingClient.ImageUrlCreateEntry();
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

  describe('ImageUrlCreateEntry', function() {
    it('should create an instance of ImageUrlCreateEntry', function() {
      // uncomment below and update the code to test ImageUrlCreateEntry
      //var instance = new CustomVisionTrainingClient.ImageUrlCreateEntry();
      //expect(instance).to.be.a(CustomVisionTrainingClient.ImageUrlCreateEntry);
    });

    it('should have the property regions (base name: "regions")', function() {
      // uncomment below and update the code to test the property regions
      //var instance = new CustomVisionTrainingClient.ImageUrlCreateEntry();
      //expect(instance).to.be();
    });

    it('should have the property tagIds (base name: "tagIds")', function() {
      // uncomment below and update the code to test the property tagIds
      //var instance = new CustomVisionTrainingClient.ImageUrlCreateEntry();
      //expect(instance).to.be();
    });

    it('should have the property url (base name: "url")', function() {
      // uncomment below and update the code to test the property url
      //var instance = new CustomVisionTrainingClient.ImageUrlCreateEntry();
      //expect(instance).to.be();
    });

  });

}));
