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
    instance = new ClickMeterApi.ApiCoreRequestsPatchBody();
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

  describe('ApiCoreRequestsPatchBody', function() {
    it('should create an instance of ApiCoreRequestsPatchBody', function() {
      // uncomment below and update the code to test ApiCoreRequestsPatchBody
      //var instance = new ClickMeterApi.ApiCoreRequestsPatchBody();
      //expect(instance).to.be.a(ClickMeterApi.ApiCoreRequestsPatchBody);
    });

    it('should have the property action (base name: "Action")', function() {
      // uncomment below and update the code to test the property action
      //var instance = new ClickMeterApi.ApiCoreRequestsPatchBody();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "Id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new ClickMeterApi.ApiCoreRequestsPatchBody();
      //expect(instance).to.be();
    });

  });

}));
