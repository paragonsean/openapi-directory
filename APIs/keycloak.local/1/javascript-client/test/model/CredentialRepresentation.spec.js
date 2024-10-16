/**
 * Keycloak Admin REST API
 * This is a REST API reference for the Keycloak Admin
 *
 * The version of the OpenAPI document: 1
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
    factory(root.expect, root.KeycloakAdminRestApi);
  }
}(this, function(expect, KeycloakAdminRestApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new KeycloakAdminRestApi.CredentialRepresentation();
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

  describe('CredentialRepresentation', function() {
    it('should create an instance of CredentialRepresentation', function() {
      // uncomment below and update the code to test CredentialRepresentation
      //var instance = new KeycloakAdminRestApi.CredentialRepresentation();
      //expect(instance).to.be.a(KeycloakAdminRestApi.CredentialRepresentation);
    });

    it('should have the property createdDate (base name: "createdDate")', function() {
      // uncomment below and update the code to test the property createdDate
      //var instance = new KeycloakAdminRestApi.CredentialRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property credentialData (base name: "credentialData")', function() {
      // uncomment below and update the code to test the property credentialData
      //var instance = new KeycloakAdminRestApi.CredentialRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new KeycloakAdminRestApi.CredentialRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property priority (base name: "priority")', function() {
      // uncomment below and update the code to test the property priority
      //var instance = new KeycloakAdminRestApi.CredentialRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property secretData (base name: "secretData")', function() {
      // uncomment below and update the code to test the property secretData
      //var instance = new KeycloakAdminRestApi.CredentialRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property temporary (base name: "temporary")', function() {
      // uncomment below and update the code to test the property temporary
      //var instance = new KeycloakAdminRestApi.CredentialRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new KeycloakAdminRestApi.CredentialRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property userLabel (base name: "userLabel")', function() {
      // uncomment below and update the code to test the property userLabel
      //var instance = new KeycloakAdminRestApi.CredentialRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property value (base name: "value")', function() {
      // uncomment below and update the code to test the property value
      //var instance = new KeycloakAdminRestApi.CredentialRepresentation();
      //expect(instance).to.be();
    });

  });

}));
