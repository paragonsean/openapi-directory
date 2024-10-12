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
    instance = new OtoroshiAdminApi.GlobalJwtVerifier();
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

  describe('GlobalJwtVerifier', function() {
    it('should create an instance of GlobalJwtVerifier', function() {
      // uncomment below and update the code to test GlobalJwtVerifier
      //var instance = new OtoroshiAdminApi.GlobalJwtVerifier();
      //expect(instance).to.be.a(OtoroshiAdminApi.GlobalJwtVerifier);
    });

    it('should have the property algoSettings (base name: "algoSettings")', function() {
      // uncomment below and update the code to test the property algoSettings
      //var instance = new OtoroshiAdminApi.GlobalJwtVerifier();
      //expect(instance).to.be();
    });

    it('should have the property desc (base name: "desc")', function() {
      // uncomment below and update the code to test the property desc
      //var instance = new OtoroshiAdminApi.GlobalJwtVerifier();
      //expect(instance).to.be();
    });

    it('should have the property enabled (base name: "enabled")', function() {
      // uncomment below and update the code to test the property enabled
      //var instance = new OtoroshiAdminApi.GlobalJwtVerifier();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new OtoroshiAdminApi.GlobalJwtVerifier();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new OtoroshiAdminApi.GlobalJwtVerifier();
      //expect(instance).to.be();
    });

    it('should have the property source (base name: "source")', function() {
      // uncomment below and update the code to test the property source
      //var instance = new OtoroshiAdminApi.GlobalJwtVerifier();
      //expect(instance).to.be();
    });

    it('should have the property strategy (base name: "strategy")', function() {
      // uncomment below and update the code to test the property strategy
      //var instance = new OtoroshiAdminApi.GlobalJwtVerifier();
      //expect(instance).to.be();
    });

    it('should have the property strict (base name: "strict")', function() {
      // uncomment below and update the code to test the property strict
      //var instance = new OtoroshiAdminApi.GlobalJwtVerifier();
      //expect(instance).to.be();
    });

  });

}));
