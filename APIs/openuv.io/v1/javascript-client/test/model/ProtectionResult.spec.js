/**
 * OpenUV - Global Real-Time UV Index Forecast API
 * The missing minimalistic JSON real-time UV Index API for awesome Developers, Innovators and Smart Home Enthusiasts
 *
 * The version of the OpenAPI document: v1
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
    factory(root.expect, root.OpenUvGlobalRealTimeUvIndexForecastApi);
  }
}(this, function(expect, OpenUvGlobalRealTimeUvIndexForecastApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new OpenUvGlobalRealTimeUvIndexForecastApi.ProtectionResult();
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

  describe('ProtectionResult', function() {
    it('should create an instance of ProtectionResult', function() {
      // uncomment below and update the code to test ProtectionResult
      //var instance = new OpenUvGlobalRealTimeUvIndexForecastApi.ProtectionResult();
      //expect(instance).to.be.a(OpenUvGlobalRealTimeUvIndexForecastApi.ProtectionResult);
    });

    it('should have the property ozone (base name: "ozone")', function() {
      // uncomment below and update the code to test the property ozone
      //var instance = new OpenUvGlobalRealTimeUvIndexForecastApi.ProtectionResult();
      //expect(instance).to.be();
    });

    it('should have the property ozoneTime (base name: "ozone_time")', function() {
      // uncomment below and update the code to test the property ozoneTime
      //var instance = new OpenUvGlobalRealTimeUvIndexForecastApi.ProtectionResult();
      //expect(instance).to.be();
    });

    it('should have the property uv (base name: "uv")', function() {
      // uncomment below and update the code to test the property uv
      //var instance = new OpenUvGlobalRealTimeUvIndexForecastApi.ProtectionResult();
      //expect(instance).to.be();
    });

    it('should have the property uvMax (base name: "uv_max")', function() {
      // uncomment below and update the code to test the property uvMax
      //var instance = new OpenUvGlobalRealTimeUvIndexForecastApi.ProtectionResult();
      //expect(instance).to.be();
    });

    it('should have the property uvMaxTime (base name: "uv_max_time")', function() {
      // uncomment below and update the code to test the property uvMaxTime
      //var instance = new OpenUvGlobalRealTimeUvIndexForecastApi.ProtectionResult();
      //expect(instance).to.be();
    });

    it('should have the property uvTime (base name: "uv_time")', function() {
      // uncomment below and update the code to test the property uvTime
      //var instance = new OpenUvGlobalRealTimeUvIndexForecastApi.ProtectionResult();
      //expect(instance).to.be();
    });

  });

}));
