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
    instance = new MesheryApi.RunnerResults();
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

  describe('RunnerResults', function() {
    it('should create an instance of RunnerResults', function() {
      // uncomment below and update the code to test RunnerResults
      //var instance = new MesheryApi.RunnerResults();
      //expect(instance).to.be.a(MesheryApi.RunnerResults);
    });

    it('should have the property actualDuration (base name: "ActualDuration")', function() {
      // uncomment below and update the code to test the property actualDuration
      //var instance = new MesheryApi.RunnerResults();
      //expect(instance).to.be();
    });

    it('should have the property actualQPS (base name: "ActualQPS")', function() {
      // uncomment below and update the code to test the property actualQPS
      //var instance = new MesheryApi.RunnerResults();
      //expect(instance).to.be();
    });

    it('should have the property durationHistogram (base name: "DurationHistogram")', function() {
      // uncomment below and update the code to test the property durationHistogram
      //var instance = new MesheryApi.RunnerResults();
      //expect(instance).to.be();
    });

    it('should have the property startTime (base name: "StartTime")', function() {
      // uncomment below and update the code to test the property startTime
      //var instance = new MesheryApi.RunnerResults();
      //expect(instance).to.be();
    });

    it('should have the property URL (base name: "URL")', function() {
      // uncomment below and update the code to test the property URL
      //var instance = new MesheryApi.RunnerResults();
      //expect(instance).to.be();
    });

    it('should have the property loadGenerator (base name: "load-generator")', function() {
      // uncomment below and update the code to test the property loadGenerator
      //var instance = new MesheryApi.RunnerResults();
      //expect(instance).to.be();
    });

  });

}));
