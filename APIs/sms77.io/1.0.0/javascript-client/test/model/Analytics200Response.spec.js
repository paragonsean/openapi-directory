/**
 * seven.io API
 * seven.io Swagger API. Get your API-Key now at seven.io.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@seven.io
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
    factory(root.expect, root.SevenIoApi);
  }
}(this, function(expect, SevenIoApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new SevenIoApi.Analytics200Response();
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

  describe('Analytics200Response', function() {
    it('should create an instance of Analytics200Response', function() {
      // uncomment below and update the code to test Analytics200Response
      //var instance = new SevenIoApi.Analytics200Response();
      //expect(instance).to.be.a(SevenIoApi.Analytics200Response);
    });

    it('should have the property date (base name: "date")', function() {
      // uncomment below and update the code to test the property date
      //var instance = new SevenIoApi.Analytics200Response();
      //expect(instance).to.be();
    });

    it('should have the property direct (base name: "direct")', function() {
      // uncomment below and update the code to test the property direct
      //var instance = new SevenIoApi.Analytics200Response();
      //expect(instance).to.be();
    });

    it('should have the property economy (base name: "economy")', function() {
      // uncomment below and update the code to test the property economy
      //var instance = new SevenIoApi.Analytics200Response();
      //expect(instance).to.be();
    });

    it('should have the property hlr (base name: "hlr")', function() {
      // uncomment below and update the code to test the property hlr
      //var instance = new SevenIoApi.Analytics200Response();
      //expect(instance).to.be();
    });

    it('should have the property inbound (base name: "inbound")', function() {
      // uncomment below and update the code to test the property inbound
      //var instance = new SevenIoApi.Analytics200Response();
      //expect(instance).to.be();
    });

    it('should have the property mnp (base name: "mnp")', function() {
      // uncomment below and update the code to test the property mnp
      //var instance = new SevenIoApi.Analytics200Response();
      //expect(instance).to.be();
    });

    it('should have the property usageEur (base name: "usage_eur")', function() {
      // uncomment below and update the code to test the property usageEur
      //var instance = new SevenIoApi.Analytics200Response();
      //expect(instance).to.be();
    });

    it('should have the property voice (base name: "voice")', function() {
      // uncomment below and update the code to test the property voice
      //var instance = new SevenIoApi.Analytics200Response();
      //expect(instance).to.be();
    });

  });

}));
