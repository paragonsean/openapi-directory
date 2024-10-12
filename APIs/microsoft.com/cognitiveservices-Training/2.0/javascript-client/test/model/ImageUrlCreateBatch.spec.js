/**
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.0
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
    factory(root.expect, root.TrainingApi);
  }
}(this, function(expect, TrainingApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new TrainingApi.ImageUrlCreateBatch();
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

  describe('ImageUrlCreateBatch', function() {
    it('should create an instance of ImageUrlCreateBatch', function() {
      // uncomment below and update the code to test ImageUrlCreateBatch
      //var instance = new TrainingApi.ImageUrlCreateBatch();
      //expect(instance).to.be.a(TrainingApi.ImageUrlCreateBatch);
    });

    it('should have the property images (base name: "images")', function() {
      // uncomment below and update the code to test the property images
      //var instance = new TrainingApi.ImageUrlCreateBatch();
      //expect(instance).to.be();
    });

    it('should have the property tagIds (base name: "tagIds")', function() {
      // uncomment below and update the code to test the property tagIds
      //var instance = new TrainingApi.ImageUrlCreateBatch();
      //expect(instance).to.be();
    });

  });

}));
