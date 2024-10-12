/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
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
    factory(root.expect, root.DracoonApi);
  }
}(this, function(expect, DracoonApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new DracoonApi.OpenIdIdpConfig();
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

  describe('OpenIdIdpConfig', function() {
    it('should create an instance of OpenIdIdpConfig', function() {
      // uncomment below and update the code to test OpenIdIdpConfig
      //var instance = new DracoonApi.OpenIdIdpConfig();
      //expect(instance).to.be.a(DracoonApi.OpenIdIdpConfig);
    });

    it('should have the property authorizationEndPointUrl (base name: "authorizationEndPointUrl")', function() {
      // uncomment below and update the code to test the property authorizationEndPointUrl
      //var instance = new DracoonApi.OpenIdIdpConfig();
      //expect(instance).to.be();
    });

    it('should have the property clientId (base name: "clientId")', function() {
      // uncomment below and update the code to test the property clientId
      //var instance = new DracoonApi.OpenIdIdpConfig();
      //expect(instance).to.be();
    });

    it('should have the property clientSecret (base name: "clientSecret")', function() {
      // uncomment below and update the code to test the property clientSecret
      //var instance = new DracoonApi.OpenIdIdpConfig();
      //expect(instance).to.be();
    });

    it('should have the property fallbackMappingClaim (base name: "fallbackMappingClaim")', function() {
      // uncomment below and update the code to test the property fallbackMappingClaim
      //var instance = new DracoonApi.OpenIdIdpConfig();
      //expect(instance).to.be();
    });

    it('should have the property flow (base name: "flow")', function() {
      // uncomment below and update the code to test the property flow
      //var instance = new DracoonApi.OpenIdIdpConfig();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new DracoonApi.OpenIdIdpConfig();
      //expect(instance).to.be();
    });

    it('should have the property issuer (base name: "issuer")', function() {
      // uncomment below and update the code to test the property issuer
      //var instance = new DracoonApi.OpenIdIdpConfig();
      //expect(instance).to.be();
    });

    it('should have the property jwksEndPointUrl (base name: "jwksEndPointUrl")', function() {
      // uncomment below and update the code to test the property jwksEndPointUrl
      //var instance = new DracoonApi.OpenIdIdpConfig();
      //expect(instance).to.be();
    });

    it('should have the property mappingClaim (base name: "mappingClaim")', function() {
      // uncomment below and update the code to test the property mappingClaim
      //var instance = new DracoonApi.OpenIdIdpConfig();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new DracoonApi.OpenIdIdpConfig();
      //expect(instance).to.be();
    });

    it('should have the property pkceChallengeMethod (base name: "pkceChallengeMethod")', function() {
      // uncomment below and update the code to test the property pkceChallengeMethod
      //var instance = new DracoonApi.OpenIdIdpConfig();
      //expect(instance).to.be();
    });

    it('should have the property pkceEnabled (base name: "pkceEnabled")', function() {
      // uncomment below and update the code to test the property pkceEnabled
      //var instance = new DracoonApi.OpenIdIdpConfig();
      //expect(instance).to.be();
    });

    it('should have the property redirectUris (base name: "redirectUris")', function() {
      // uncomment below and update the code to test the property redirectUris
      //var instance = new DracoonApi.OpenIdIdpConfig();
      //expect(instance).to.be();
    });

    it('should have the property scopes (base name: "scopes")', function() {
      // uncomment below and update the code to test the property scopes
      //var instance = new DracoonApi.OpenIdIdpConfig();
      //expect(instance).to.be();
    });

    it('should have the property tokenEndPointUrl (base name: "tokenEndPointUrl")', function() {
      // uncomment below and update the code to test the property tokenEndPointUrl
      //var instance = new DracoonApi.OpenIdIdpConfig();
      //expect(instance).to.be();
    });

    it('should have the property userImportEnabled (base name: "userImportEnabled")', function() {
      // uncomment below and update the code to test the property userImportEnabled
      //var instance = new DracoonApi.OpenIdIdpConfig();
      //expect(instance).to.be();
    });

    it('should have the property userImportGroup (base name: "userImportGroup")', function() {
      // uncomment below and update the code to test the property userImportGroup
      //var instance = new DracoonApi.OpenIdIdpConfig();
      //expect(instance).to.be();
    });

    it('should have the property userInfoEndPointUrl (base name: "userInfoEndPointUrl")', function() {
      // uncomment below and update the code to test the property userInfoEndPointUrl
      //var instance = new DracoonApi.OpenIdIdpConfig();
      //expect(instance).to.be();
    });

    it('should have the property userInfoSource (base name: "userInfoSource")', function() {
      // uncomment below and update the code to test the property userInfoSource
      //var instance = new DracoonApi.OpenIdIdpConfig();
      //expect(instance).to.be();
    });

    it('should have the property userManagementUrl (base name: "userManagementUrl")', function() {
      // uncomment below and update the code to test the property userManagementUrl
      //var instance = new DracoonApi.OpenIdIdpConfig();
      //expect(instance).to.be();
    });

    it('should have the property userUpdateEnabled (base name: "userUpdateEnabled")', function() {
      // uncomment below and update the code to test the property userUpdateEnabled
      //var instance = new DracoonApi.OpenIdIdpConfig();
      //expect(instance).to.be();
    });

  });

}));
