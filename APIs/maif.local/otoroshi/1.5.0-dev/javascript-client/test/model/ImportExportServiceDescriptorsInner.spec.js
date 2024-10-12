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
    instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
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

  describe('ImportExportServiceDescriptorsInner', function() {
    it('should create an instance of ImportExportServiceDescriptorsInner', function() {
      // uncomment below and update the code to test ImportExportServiceDescriptorsInner
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be.a(OtoroshiAdminApi.ImportExportServiceDescriptorsInner);
    });

    it('should have the property canary (base name: "Canary")', function() {
      // uncomment below and update the code to test the property canary
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property additionalHeaders (base name: "additionalHeaders")', function() {
      // uncomment below and update the code to test the property additionalHeaders
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property api (base name: "api")', function() {
      // uncomment below and update the code to test the property api
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property authConfigRef (base name: "authConfigRef")', function() {
      // uncomment below and update the code to test the property authConfigRef
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property buildMode (base name: "buildMode")', function() {
      // uncomment below and update the code to test the property buildMode
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property chaosConfig (base name: "chaosConfig")', function() {
      // uncomment below and update the code to test the property chaosConfig
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property clientConfig (base name: "clientConfig")', function() {
      // uncomment below and update the code to test the property clientConfig
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property clientValidatorRef (base name: "clientValidatorRef")', function() {
      // uncomment below and update the code to test the property clientValidatorRef
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property cors (base name: "cors")', function() {
      // uncomment below and update the code to test the property cors
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property domain (base name: "domain")', function() {
      // uncomment below and update the code to test the property domain
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property enabled (base name: "enabled")', function() {
      // uncomment below and update the code to test the property enabled
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property enforceSecureCommunication (base name: "enforceSecureCommunication")', function() {
      // uncomment below and update the code to test the property enforceSecureCommunication
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property env (base name: "env")', function() {
      // uncomment below and update the code to test the property env
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property forceHttps (base name: "forceHttps")', function() {
      // uncomment below and update the code to test the property forceHttps
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property groups (base name: "groups")', function() {
      // uncomment below and update the code to test the property groups
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property gzip (base name: "gzip")', function() {
      // uncomment below and update the code to test the property gzip
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property headersVerification (base name: "headersVerification")', function() {
      // uncomment below and update the code to test the property headersVerification
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property healthCheck (base name: "healthCheck")', function() {
      // uncomment below and update the code to test the property healthCheck
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property ipFiltering (base name: "ipFiltering")', function() {
      // uncomment below and update the code to test the property ipFiltering
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property jwtVerifier (base name: "jwtVerifier")', function() {
      // uncomment below and update the code to test the property jwtVerifier
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property localHost (base name: "localHost")', function() {
      // uncomment below and update the code to test the property localHost
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property localScheme (base name: "localScheme")', function() {
      // uncomment below and update the code to test the property localScheme
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property maintenanceMode (base name: "maintenanceMode")', function() {
      // uncomment below and update the code to test the property maintenanceMode
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property matchingHeaders (base name: "matchingHeaders")', function() {
      // uncomment below and update the code to test the property matchingHeaders
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property matchingRoot (base name: "matchingRoot")', function() {
      // uncomment below and update the code to test the property matchingRoot
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property metadata (base name: "metadata")', function() {
      // uncomment below and update the code to test the property metadata
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property overrideHost (base name: "overrideHost")', function() {
      // uncomment below and update the code to test the property overrideHost
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property privateApp (base name: "privateApp")', function() {
      // uncomment below and update the code to test the property privateApp
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property privatePatterns (base name: "privatePatterns")', function() {
      // uncomment below and update the code to test the property privatePatterns
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property publicPatterns (base name: "publicPatterns")', function() {
      // uncomment below and update the code to test the property publicPatterns
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property redirectToLocal (base name: "redirectToLocal")', function() {
      // uncomment below and update the code to test the property redirectToLocal
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property redirection (base name: "redirection")', function() {
      // uncomment below and update the code to test the property redirection
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property root (base name: "root")', function() {
      // uncomment below and update the code to test the property root
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property secComExcludedPatterns (base name: "secComExcludedPatterns")', function() {
      // uncomment below and update the code to test the property secComExcludedPatterns
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property secComSettings (base name: "secComSettings")', function() {
      // uncomment below and update the code to test the property secComSettings
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property sendOtoroshiHeadersBack (base name: "sendOtoroshiHeadersBack")', function() {
      // uncomment below and update the code to test the property sendOtoroshiHeadersBack
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property statsdConfig (base name: "statsdConfig")', function() {
      // uncomment below and update the code to test the property statsdConfig
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property subdomain (base name: "subdomain")', function() {
      // uncomment below and update the code to test the property subdomain
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property targets (base name: "targets")', function() {
      // uncomment below and update the code to test the property targets
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property transformerRef (base name: "transformerRef")', function() {
      // uncomment below and update the code to test the property transformerRef
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property userFacing (base name: "userFacing")', function() {
      // uncomment below and update the code to test the property userFacing
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

    it('should have the property xForwardedHeaders (base name: "xForwardedHeaders")', function() {
      // uncomment below and update the code to test the property xForwardedHeaders
      //var instance = new OtoroshiAdminApi.ImportExportServiceDescriptorsInner();
      //expect(instance).to.be();
    });

  });

}));
