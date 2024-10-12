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
    instance = new DracoonApi.OAuthAuthorization();
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

  describe('OAuthAuthorization', function() {
    it('should create an instance of OAuthAuthorization', function() {
      // uncomment below and update the code to test OAuthAuthorization
      //var instance = new DracoonApi.OAuthAuthorization();
      //expect(instance).to.be.a(DracoonApi.OAuthAuthorization);
    });

    it('should have the property clientId (base name: "clientId")', function() {
      // uncomment below and update the code to test the property clientId
      //var instance = new DracoonApi.OAuthAuthorization();
      //expect(instance).to.be();
    });

    it('should have the property clientName (base name: "clientName")', function() {
      // uncomment below and update the code to test the property clientName
      //var instance = new DracoonApi.OAuthAuthorization();
      //expect(instance).to.be();
    });

    it('should have the property createdAt (base name: "createdAt")', function() {
      // uncomment below and update the code to test the property createdAt
      //var instance = new DracoonApi.OAuthAuthorization();
      //expect(instance).to.be();
    });

    it('should have the property expiresAt (base name: "expiresAt")', function() {
      // uncomment below and update the code to test the property expiresAt
      //var instance = new DracoonApi.OAuthAuthorization();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new DracoonApi.OAuthAuthorization();
      //expect(instance).to.be();
    });

    it('should have the property isCurrentAuthorization (base name: "isCurrentAuthorization")', function() {
      // uncomment below and update the code to test the property isCurrentAuthorization
      //var instance = new DracoonApi.OAuthAuthorization();
      //expect(instance).to.be();
    });

    it('should have the property isStandard (base name: "isStandard")', function() {
      // uncomment below and update the code to test the property isStandard
      //var instance = new DracoonApi.OAuthAuthorization();
      //expect(instance).to.be();
    });

    it('should have the property usedAt (base name: "usedAt")', function() {
      // uncomment below and update the code to test the property usedAt
      //var instance = new DracoonApi.OAuthAuthorization();
      //expect(instance).to.be();
    });

    it('should have the property userAgentCategory (base name: "userAgentCategory")', function() {
      // uncomment below and update the code to test the property userAgentCategory
      //var instance = new DracoonApi.OAuthAuthorization();
      //expect(instance).to.be();
    });

    it('should have the property userAgentInfo (base name: "userAgentInfo")', function() {
      // uncomment below and update the code to test the property userAgentInfo
      //var instance = new DracoonApi.OAuthAuthorization();
      //expect(instance).to.be();
    });

    it('should have the property userAgentOs (base name: "userAgentOs")', function() {
      // uncomment below and update the code to test the property userAgentOs
      //var instance = new DracoonApi.OAuthAuthorization();
      //expect(instance).to.be();
    });

    it('should have the property userAgentType (base name: "userAgentType")', function() {
      // uncomment below and update the code to test the property userAgentType
      //var instance = new DracoonApi.OAuthAuthorization();
      //expect(instance).to.be();
    });

  });

}));
