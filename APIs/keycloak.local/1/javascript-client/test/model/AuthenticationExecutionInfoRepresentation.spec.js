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
    instance = new KeycloakAdminRestApi.AuthenticationExecutionInfoRepresentation();
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

  describe('AuthenticationExecutionInfoRepresentation', function() {
    it('should create an instance of AuthenticationExecutionInfoRepresentation', function() {
      // uncomment below and update the code to test AuthenticationExecutionInfoRepresentation
      //var instance = new KeycloakAdminRestApi.AuthenticationExecutionInfoRepresentation();
      //expect(instance).to.be.a(KeycloakAdminRestApi.AuthenticationExecutionInfoRepresentation);
    });

    it('should have the property alias (base name: "alias")', function() {
      // uncomment below and update the code to test the property alias
      //var instance = new KeycloakAdminRestApi.AuthenticationExecutionInfoRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property authenticationConfig (base name: "authenticationConfig")', function() {
      // uncomment below and update the code to test the property authenticationConfig
      //var instance = new KeycloakAdminRestApi.AuthenticationExecutionInfoRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property authenticationFlow (base name: "authenticationFlow")', function() {
      // uncomment below and update the code to test the property authenticationFlow
      //var instance = new KeycloakAdminRestApi.AuthenticationExecutionInfoRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property configurable (base name: "configurable")', function() {
      // uncomment below and update the code to test the property configurable
      //var instance = new KeycloakAdminRestApi.AuthenticationExecutionInfoRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property displayName (base name: "displayName")', function() {
      // uncomment below and update the code to test the property displayName
      //var instance = new KeycloakAdminRestApi.AuthenticationExecutionInfoRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property flowId (base name: "flowId")', function() {
      // uncomment below and update the code to test the property flowId
      //var instance = new KeycloakAdminRestApi.AuthenticationExecutionInfoRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new KeycloakAdminRestApi.AuthenticationExecutionInfoRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property index (base name: "index")', function() {
      // uncomment below and update the code to test the property index
      //var instance = new KeycloakAdminRestApi.AuthenticationExecutionInfoRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property level (base name: "level")', function() {
      // uncomment below and update the code to test the property level
      //var instance = new KeycloakAdminRestApi.AuthenticationExecutionInfoRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property providerId (base name: "providerId")', function() {
      // uncomment below and update the code to test the property providerId
      //var instance = new KeycloakAdminRestApi.AuthenticationExecutionInfoRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property requirement (base name: "requirement")', function() {
      // uncomment below and update the code to test the property requirement
      //var instance = new KeycloakAdminRestApi.AuthenticationExecutionInfoRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property requirementChoices (base name: "requirementChoices")', function() {
      // uncomment below and update the code to test the property requirementChoices
      //var instance = new KeycloakAdminRestApi.AuthenticationExecutionInfoRepresentation();
      //expect(instance).to.be();
    });

  });

}));
