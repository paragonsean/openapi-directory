/**
 * ClickMeter API
 * Api dashboard for ClickMeter API
 *
 * The version of the OpenAPI document: v2
 * Contact: api@clickmeter.com
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
    factory(root.expect, root.ClickMeterApi);
  }
}(this, function(expect, ClickMeterApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new ClickMeterApi.ApiCoreDtoAccountingConversionOptions();
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

  describe('ApiCoreDtoAccountingConversionOptions', function() {
    it('should create an instance of ApiCoreDtoAccountingConversionOptions', function() {
      // uncomment below and update the code to test ApiCoreDtoAccountingConversionOptions
      //var instance = new ClickMeterApi.ApiCoreDtoAccountingConversionOptions();
      //expect(instance).to.be.a(ClickMeterApi.ApiCoreDtoAccountingConversionOptions);
    });

    it('should have the property hideComCost (base name: "hideComCost")', function() {
      // uncomment below and update the code to test the property hideComCost
      //var instance = new ClickMeterApi.ApiCoreDtoAccountingConversionOptions();
      //expect(instance).to.be();
    });

    it('should have the property hideCost (base name: "hideCost")', function() {
      // uncomment below and update the code to test the property hideCost
      //var instance = new ClickMeterApi.ApiCoreDtoAccountingConversionOptions();
      //expect(instance).to.be();
    });

    it('should have the property hideCount (base name: "hideCount")', function() {
      // uncomment below and update the code to test the property hideCount
      //var instance = new ClickMeterApi.ApiCoreDtoAccountingConversionOptions();
      //expect(instance).to.be();
    });

    it('should have the property hideParams (base name: "hideParams")', function() {
      // uncomment below and update the code to test the property hideParams
      //var instance = new ClickMeterApi.ApiCoreDtoAccountingConversionOptions();
      //expect(instance).to.be();
    });

    it('should have the property hideValue (base name: "hideValue")', function() {
      // uncomment below and update the code to test the property hideValue
      //var instance = new ClickMeterApi.ApiCoreDtoAccountingConversionOptions();
      //expect(instance).to.be();
    });

    it('should have the property percentCommission (base name: "percentCommission")', function() {
      // uncomment below and update the code to test the property percentCommission
      //var instance = new ClickMeterApi.ApiCoreDtoAccountingConversionOptions();
      //expect(instance).to.be();
    });

    it('should have the property percentValue (base name: "percentValue")', function() {
      // uncomment below and update the code to test the property percentValue
      //var instance = new ClickMeterApi.ApiCoreDtoAccountingConversionOptions();
      //expect(instance).to.be();
    });

  });

}));
