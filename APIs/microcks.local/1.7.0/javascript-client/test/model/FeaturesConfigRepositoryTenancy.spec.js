/**
 * Microcks API v1.7
 * API offered by Microcks, the Kubernetes native tools for API and microservices mocking and testing (microcks.io)
 *
 * The version of the OpenAPI document: 1.7.0
 * Contact: laurent@microcks.io
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
    factory(root.expect, root.MicrocksApiV17);
  }
}(this, function(expect, MicrocksApiV17) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MicrocksApiV17.FeaturesConfigRepositoryTenancy();
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

  describe('FeaturesConfigRepositoryTenancy', function() {
    it('should create an instance of FeaturesConfigRepositoryTenancy', function() {
      // uncomment below and update the code to test FeaturesConfigRepositoryTenancy
      //var instance = new MicrocksApiV17.FeaturesConfigRepositoryTenancy();
      //expect(instance).to.be.a(MicrocksApiV17.FeaturesConfigRepositoryTenancy);
    });

    it('should have the property artifactImportAllowedRoles (base name: "artifact-import-allowed-roles")', function() {
      // uncomment below and update the code to test the property artifactImportAllowedRoles
      //var instance = new MicrocksApiV17.FeaturesConfigRepositoryTenancy();
      //expect(instance).to.be();
    });

    it('should have the property enabled (base name: "enabled")', function() {
      // uncomment below and update the code to test the property enabled
      //var instance = new MicrocksApiV17.FeaturesConfigRepositoryTenancy();
      //expect(instance).to.be();
    });

  });

}));
