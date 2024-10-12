/**
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
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
    factory(root.expect, root.OtoroshiAdminApi);
  }
}(this, function(expect, OtoroshiAdminApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new OtoroshiAdminApi.ClientConfig();
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

  describe('ClientConfig', function() {
    it('should create an instance of ClientConfig', function() {
      // uncomment below and update the code to test ClientConfig
      //var instance = new OtoroshiAdminApi.ClientConfig();
      //expect(instance).to.be.a(OtoroshiAdminApi.ClientConfig);
    });

    it('should have the property backoffFactor (base name: "backoffFactor")', function() {
      // uncomment below and update the code to test the property backoffFactor
      //var instance = new OtoroshiAdminApi.ClientConfig();
      //expect(instance).to.be();
    });

    it('should have the property callTimeout (base name: "callTimeout")', function() {
      // uncomment below and update the code to test the property callTimeout
      //var instance = new OtoroshiAdminApi.ClientConfig();
      //expect(instance).to.be();
    });

    it('should have the property globalTimeout (base name: "globalTimeout")', function() {
      // uncomment below and update the code to test the property globalTimeout
      //var instance = new OtoroshiAdminApi.ClientConfig();
      //expect(instance).to.be();
    });

    it('should have the property maxErrors (base name: "maxErrors")', function() {
      // uncomment below and update the code to test the property maxErrors
      //var instance = new OtoroshiAdminApi.ClientConfig();
      //expect(instance).to.be();
    });

    it('should have the property retries (base name: "retries")', function() {
      // uncomment below and update the code to test the property retries
      //var instance = new OtoroshiAdminApi.ClientConfig();
      //expect(instance).to.be();
    });

    it('should have the property retryInitialDelay (base name: "retryInitialDelay")', function() {
      // uncomment below and update the code to test the property retryInitialDelay
      //var instance = new OtoroshiAdminApi.ClientConfig();
      //expect(instance).to.be();
    });

    it('should have the property sampleInterval (base name: "sampleInterval")', function() {
      // uncomment below and update the code to test the property sampleInterval
      //var instance = new OtoroshiAdminApi.ClientConfig();
      //expect(instance).to.be();
    });

    it('should have the property useCircuitBreaker (base name: "useCircuitBreaker")', function() {
      // uncomment below and update the code to test the property useCircuitBreaker
      //var instance = new OtoroshiAdminApi.ClientConfig();
      //expect(instance).to.be();
    });

  });

}));
