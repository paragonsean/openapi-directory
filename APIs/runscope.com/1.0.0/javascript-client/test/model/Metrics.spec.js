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
    instance = new RunscopeApi.Metrics();
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

  describe('Metrics', function() {
    it('should create an instance of Metrics', function() {
      // uncomment below and update the code to test Metrics
      //var instance = new RunscopeApi.Metrics();
      //expect(instance).to.be.a(RunscopeApi.Metrics);
    });

    it('should have the property changesFromLastPeriod (base name: "changes_from_last_period")', function() {
      // uncomment below and update the code to test the property changesFromLastPeriod
      //var instance = new RunscopeApi.Metrics();
      //expect(instance).to.be();
    });

    it('should have the property environmentUuid (base name: "environment_uuid")', function() {
      // uncomment below and update the code to test the property environmentUuid
      //var instance = new RunscopeApi.Metrics();
      //expect(instance).to.be();
    });

    it('should have the property region (base name: "region")', function() {
      // uncomment below and update the code to test the property region
      //var instance = new RunscopeApi.Metrics();
      //expect(instance).to.be();
    });

    it('should have the property responseTimes (base name: "response_times")', function() {
      // uncomment below and update the code to test the property responseTimes
      //var instance = new RunscopeApi.Metrics();
      //expect(instance).to.be();
    });

    it('should have the property thisTimePeriod (base name: "this_time_period")', function() {
      // uncomment below and update the code to test the property thisTimePeriod
      //var instance = new RunscopeApi.Metrics();
      //expect(instance).to.be();
    });

    it('should have the property timeframe (base name: "timeframe")', function() {
      // uncomment below and update the code to test the property timeframe
      //var instance = new RunscopeApi.Metrics();
      //expect(instance).to.be();
    });

  });

}));
