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
    instance = new OtoroshiAdminApi.ImportExportApiKeysInner();
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

  describe('ImportExportApiKeysInner', function() {
    it('should create an instance of ImportExportApiKeysInner', function() {
      // uncomment below and update the code to test ImportExportApiKeysInner
      //var instance = new OtoroshiAdminApi.ImportExportApiKeysInner();
      //expect(instance).to.be.a(OtoroshiAdminApi.ImportExportApiKeysInner);
    });

    it('should have the property authorizedEntities (base name: "authorizedEntities")', function() {
      // uncomment below and update the code to test the property authorizedEntities
      //var instance = new OtoroshiAdminApi.ImportExportApiKeysInner();
      //expect(instance).to.be();
    });

    it('should have the property clientId (base name: "clientId")', function() {
      // uncomment below and update the code to test the property clientId
      //var instance = new OtoroshiAdminApi.ImportExportApiKeysInner();
      //expect(instance).to.be();
    });

    it('should have the property clientName (base name: "clientName")', function() {
      // uncomment below and update the code to test the property clientName
      //var instance = new OtoroshiAdminApi.ImportExportApiKeysInner();
      //expect(instance).to.be();
    });

    it('should have the property clientSecret (base name: "clientSecret")', function() {
      // uncomment below and update the code to test the property clientSecret
      //var instance = new OtoroshiAdminApi.ImportExportApiKeysInner();
      //expect(instance).to.be();
    });

    it('should have the property dailyQuota (base name: "dailyQuota")', function() {
      // uncomment below and update the code to test the property dailyQuota
      //var instance = new OtoroshiAdminApi.ImportExportApiKeysInner();
      //expect(instance).to.be();
    });

    it('should have the property enabled (base name: "enabled")', function() {
      // uncomment below and update the code to test the property enabled
      //var instance = new OtoroshiAdminApi.ImportExportApiKeysInner();
      //expect(instance).to.be();
    });

    it('should have the property metadata (base name: "metadata")', function() {
      // uncomment below and update the code to test the property metadata
      //var instance = new OtoroshiAdminApi.ImportExportApiKeysInner();
      //expect(instance).to.be();
    });

    it('should have the property monthlyQuota (base name: "monthlyQuota")', function() {
      // uncomment below and update the code to test the property monthlyQuota
      //var instance = new OtoroshiAdminApi.ImportExportApiKeysInner();
      //expect(instance).to.be();
    });

    it('should have the property throttlingQuota (base name: "throttlingQuota")', function() {
      // uncomment below and update the code to test the property throttlingQuota
      //var instance = new OtoroshiAdminApi.ImportExportApiKeysInner();
      //expect(instance).to.be();
    });

  });

}));
