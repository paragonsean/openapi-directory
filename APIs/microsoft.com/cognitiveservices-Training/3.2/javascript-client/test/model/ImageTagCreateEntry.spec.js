/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.2
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
    instance = new CustomVisionTrainingClient.ImageTagCreateEntry();
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

  describe('ImageTagCreateEntry', function() {
    it('should create an instance of ImageTagCreateEntry', function() {
      // uncomment below and update the code to test ImageTagCreateEntry
      //var instance = new CustomVisionTrainingClient.ImageTagCreateEntry();
      //expect(instance).to.be.a(CustomVisionTrainingClient.ImageTagCreateEntry);
    });

    it('should have the property imageId (base name: "imageId")', function() {
      // uncomment below and update the code to test the property imageId
      //var instance = new CustomVisionTrainingClient.ImageTagCreateEntry();
      //expect(instance).to.be();
    });

    it('should have the property tagId (base name: "tagId")', function() {
      // uncomment below and update the code to test the property tagId
      //var instance = new CustomVisionTrainingClient.ImageTagCreateEntry();
      //expect(instance).to.be();
    });

  });

}));
