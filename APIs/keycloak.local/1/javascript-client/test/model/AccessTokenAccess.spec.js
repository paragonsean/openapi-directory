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
    instance = new KeycloakAdminRestApi.AccessTokenAccess();
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

  describe('AccessTokenAccess', function() {
    it('should create an instance of AccessTokenAccess', function() {
      // uncomment below and update the code to test AccessTokenAccess
      //var instance = new KeycloakAdminRestApi.AccessTokenAccess();
      //expect(instance).to.be.a(KeycloakAdminRestApi.AccessTokenAccess);
    });

    it('should have the property roles (base name: "roles")', function() {
      // uncomment below and update the code to test the property roles
      //var instance = new KeycloakAdminRestApi.AccessTokenAccess();
      //expect(instance).to.be();
    });

    it('should have the property verifyCaller (base name: "verify_caller")', function() {
      // uncomment below and update the code to test the property verifyCaller
      //var instance = new KeycloakAdminRestApi.AccessTokenAccess();
      //expect(instance).to.be();
    });

  });

}));
