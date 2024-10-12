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
    instance = new OtoroshiAdminApi.GlobalJwtVerifierAlgoSettings();
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

  describe('GlobalJwtVerifierAlgoSettings', function() {
    it('should create an instance of GlobalJwtVerifierAlgoSettings', function() {
      // uncomment below and update the code to test GlobalJwtVerifierAlgoSettings
      //var instance = new OtoroshiAdminApi.GlobalJwtVerifierAlgoSettings();
      //expect(instance).to.be.a(OtoroshiAdminApi.GlobalJwtVerifierAlgoSettings);
    });

    it('should have the property secret (base name: "secret")', function() {
      // uncomment below and update the code to test the property secret
      //var instance = new OtoroshiAdminApi.GlobalJwtVerifierAlgoSettings();
      //expect(instance).to.be();
    });

    it('should have the property size (base name: "size")', function() {
      // uncomment below and update the code to test the property size
      //var instance = new OtoroshiAdminApi.GlobalJwtVerifierAlgoSettings();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new OtoroshiAdminApi.GlobalJwtVerifierAlgoSettings();
      //expect(instance).to.be();
    });

    it('should have the property privateKey (base name: "privateKey")', function() {
      // uncomment below and update the code to test the property privateKey
      //var instance = new OtoroshiAdminApi.GlobalJwtVerifierAlgoSettings();
      //expect(instance).to.be();
    });

    it('should have the property publicKey (base name: "publicKey")', function() {
      // uncomment below and update the code to test the property publicKey
      //var instance = new OtoroshiAdminApi.GlobalJwtVerifierAlgoSettings();
      //expect(instance).to.be();
    });

    it('should have the property headers (base name: "headers")', function() {
      // uncomment below and update the code to test the property headers
      //var instance = new OtoroshiAdminApi.GlobalJwtVerifierAlgoSettings();
      //expect(instance).to.be();
    });

    it('should have the property kty (base name: "kty")', function() {
      // uncomment below and update the code to test the property kty
      //var instance = new OtoroshiAdminApi.GlobalJwtVerifierAlgoSettings();
      //expect(instance).to.be();
    });

    it('should have the property timeout (base name: "timeout")', function() {
      // uncomment below and update the code to test the property timeout
      //var instance = new OtoroshiAdminApi.GlobalJwtVerifierAlgoSettings();
      //expect(instance).to.be();
    });

    it('should have the property ttl (base name: "ttl")', function() {
      // uncomment below and update the code to test the property ttl
      //var instance = new OtoroshiAdminApi.GlobalJwtVerifierAlgoSettings();
      //expect(instance).to.be();
    });

    it('should have the property url (base name: "url")', function() {
      // uncomment below and update the code to test the property url
      //var instance = new OtoroshiAdminApi.GlobalJwtVerifierAlgoSettings();
      //expect(instance).to.be();
    });

  });

}));
