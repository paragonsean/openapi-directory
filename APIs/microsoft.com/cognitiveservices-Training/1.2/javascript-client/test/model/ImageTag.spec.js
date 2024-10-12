/**
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.2
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
    instance = new TrainingApi.ImageTag();
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

  describe('ImageTag', function() {
    it('should create an instance of ImageTag', function() {
      // uncomment below and update the code to test ImageTag
      //var instance = new TrainingApi.ImageTag();
      //expect(instance).to.be.a(TrainingApi.ImageTag);
    });

    it('should have the property created (base name: "Created")', function() {
      // uncomment below and update the code to test the property created
      //var instance = new TrainingApi.ImageTag();
      //expect(instance).to.be();
    });

    it('should have the property tagId (base name: "TagId")', function() {
      // uncomment below and update the code to test the property tagId
      //var instance = new TrainingApi.ImageTag();
      //expect(instance).to.be();
    });

  });

}));
