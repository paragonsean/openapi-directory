/**
 * QuickChart API
 * An API to generate charts and QR codes using QuickChart services.
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
    factory(root.expect, root.QuickChartApi);
  }
}(this, function(expect, QuickChartApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new QuickChartApi.ChartPostRequest();
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

  describe('ChartPostRequest', function() {
    it('should create an instance of ChartPostRequest', function() {
      // uncomment below and update the code to test ChartPostRequest
      //var instance = new QuickChartApi.ChartPostRequest();
      //expect(instance).to.be.a(QuickChartApi.ChartPostRequest);
    });

    it('should have the property backgroundColor (base name: "backgroundColor")', function() {
      // uncomment below and update the code to test the property backgroundColor
      //var instance = new QuickChartApi.ChartPostRequest();
      //expect(instance).to.be();
    });

    it('should have the property chart (base name: "chart")', function() {
      // uncomment below and update the code to test the property chart
      //var instance = new QuickChartApi.ChartPostRequest();
      //expect(instance).to.be();
    });

    it('should have the property format (base name: "format")', function() {
      // uncomment below and update the code to test the property format
      //var instance = new QuickChartApi.ChartPostRequest();
      //expect(instance).to.be();
    });

    it('should have the property height (base name: "height")', function() {
      // uncomment below and update the code to test the property height
      //var instance = new QuickChartApi.ChartPostRequest();
      //expect(instance).to.be();
    });

    it('should have the property width (base name: "width")', function() {
      // uncomment below and update the code to test the property width
      //var instance = new QuickChartApi.ChartPostRequest();
      //expect(instance).to.be();
    });

  });

}));
