/**
 * Runscope API
 * Manage Runscope programmatically.
 *
 * The version of the OpenAPI document: 1.0.0
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
    factory(root.expect, root.RunscopeApi);
  }
}(this, function(expect, RunscopeApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new RunscopeApi.MetricsResponseTimesInner();
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

  describe('MetricsResponseTimesInner', function() {
    it('should create an instance of MetricsResponseTimesInner', function() {
      // uncomment below and update the code to test MetricsResponseTimesInner
      //var instance = new RunscopeApi.MetricsResponseTimesInner();
      //expect(instance).to.be.a(RunscopeApi.MetricsResponseTimesInner);
    });

    it('should have the property avgResponseTimeMs (base name: "avg_response_time_ms")', function() {
      // uncomment below and update the code to test the property avgResponseTimeMs
      //var instance = new RunscopeApi.MetricsResponseTimesInner();
      //expect(instance).to.be();
    });

    it('should have the property successRatio (base name: "success_ratio")', function() {
      // uncomment below and update the code to test the property successRatio
      //var instance = new RunscopeApi.MetricsResponseTimesInner();
      //expect(instance).to.be();
    });

    it('should have the property timestamp (base name: "timestamp")', function() {
      // uncomment below and update the code to test the property timestamp
      //var instance = new RunscopeApi.MetricsResponseTimesInner();
      //expect(instance).to.be();
    });

  });

}));
