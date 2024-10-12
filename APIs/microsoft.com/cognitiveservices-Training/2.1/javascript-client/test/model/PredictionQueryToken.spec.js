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
    instance = new TrainingApi.PredictionQueryToken();
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

  describe('PredictionQueryToken', function() {
    it('should create an instance of PredictionQueryToken', function() {
      // uncomment below and update the code to test PredictionQueryToken
      //var instance = new TrainingApi.PredictionQueryToken();
      //expect(instance).to.be.a(TrainingApi.PredictionQueryToken);
    });

    it('should have the property application (base name: "application")', function() {
      // uncomment below and update the code to test the property application
      //var instance = new TrainingApi.PredictionQueryToken();
      //expect(instance).to.be();
    });

    it('should have the property continuation (base name: "continuation")', function() {
      // uncomment below and update the code to test the property continuation
      //var instance = new TrainingApi.PredictionQueryToken();
      //expect(instance).to.be();
    });

    it('should have the property endTime (base name: "endTime")', function() {
      // uncomment below and update the code to test the property endTime
      //var instance = new TrainingApi.PredictionQueryToken();
      //expect(instance).to.be();
    });

    it('should have the property iterationId (base name: "iterationId")', function() {
      // uncomment below and update the code to test the property iterationId
      //var instance = new TrainingApi.PredictionQueryToken();
      //expect(instance).to.be();
    });

    it('should have the property maxCount (base name: "maxCount")', function() {
      // uncomment below and update the code to test the property maxCount
      //var instance = new TrainingApi.PredictionQueryToken();
      //expect(instance).to.be();
    });

    it('should have the property orderBy (base name: "orderBy")', function() {
      // uncomment below and update the code to test the property orderBy
      //var instance = new TrainingApi.PredictionQueryToken();
      //expect(instance).to.be();
    });

    it('should have the property session (base name: "session")', function() {
      // uncomment below and update the code to test the property session
      //var instance = new TrainingApi.PredictionQueryToken();
      //expect(instance).to.be();
    });

    it('should have the property startTime (base name: "startTime")', function() {
      // uncomment below and update the code to test the property startTime
      //var instance = new TrainingApi.PredictionQueryToken();
      //expect(instance).to.be();
    });

    it('should have the property tags (base name: "tags")', function() {
      // uncomment below and update the code to test the property tags
      //var instance = new TrainingApi.PredictionQueryToken();
      //expect(instance).to.be();
    });

  });

}));
