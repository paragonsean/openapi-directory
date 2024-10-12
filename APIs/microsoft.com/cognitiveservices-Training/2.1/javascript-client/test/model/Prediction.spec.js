/**
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.1
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
    instance = new TrainingApi.Prediction();
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

  describe('Prediction', function() {
    it('should create an instance of Prediction', function() {
      // uncomment below and update the code to test Prediction
      //var instance = new TrainingApi.Prediction();
      //expect(instance).to.be.a(TrainingApi.Prediction);
    });

    it('should have the property boundingBox (base name: "boundingBox")', function() {
      // uncomment below and update the code to test the property boundingBox
      //var instance = new TrainingApi.Prediction();
      //expect(instance).to.be();
    });

    it('should have the property probability (base name: "probability")', function() {
      // uncomment below and update the code to test the property probability
      //var instance = new TrainingApi.Prediction();
      //expect(instance).to.be();
    });

    it('should have the property tagId (base name: "tagId")', function() {
      // uncomment below and update the code to test the property tagId
      //var instance = new TrainingApi.Prediction();
      //expect(instance).to.be();
    });

    it('should have the property tagName (base name: "tagName")', function() {
      // uncomment below and update the code to test the property tagName
      //var instance = new TrainingApi.Prediction();
      //expect(instance).to.be();
    });

  });

}));
