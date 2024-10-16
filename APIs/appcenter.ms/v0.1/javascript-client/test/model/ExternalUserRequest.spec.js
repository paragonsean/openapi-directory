/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
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
    factory(root.expect, root.AppCenterClient);
  }
}(this, function(expect, AppCenterClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AppCenterClient.ExternalUserRequest();
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

  describe('ExternalUserRequest', function() {
    it('should create an instance of ExternalUserRequest', function() {
      // uncomment below and update the code to test ExternalUserRequest
      //var instance = new AppCenterClient.ExternalUserRequest();
      //expect(instance).to.be.a(AppCenterClient.ExternalUserRequest);
    });

    it('should have the property appInvitation (base name: "app_invitation")', function() {
      // uncomment below and update the code to test the property appInvitation
      //var instance = new AppCenterClient.ExternalUserRequest();
      //expect(instance).to.be();
    });

    it('should have the property avatarUrl (base name: "avatar_url")', function() {
      // uncomment below and update the code to test the property avatarUrl
      //var instance = new AppCenterClient.ExternalUserRequest();
      //expect(instance).to.be();
    });

    it('should have the property displayName (base name: "display_name")', function() {
      // uncomment below and update the code to test the property displayName
      //var instance = new AppCenterClient.ExternalUserRequest();
      //expect(instance).to.be();
    });

    it('should have the property email (base name: "email")', function() {
      // uncomment below and update the code to test the property email
      //var instance = new AppCenterClient.ExternalUserRequest();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new AppCenterClient.ExternalUserRequest();
      //expect(instance).to.be();
    });

    it('should have the property organizationInvitation (base name: "organization_invitation")', function() {
      // uncomment below and update the code to test the property organizationInvitation
      //var instance = new AppCenterClient.ExternalUserRequest();
      //expect(instance).to.be();
    });

    it('should have the property testerInvitation (base name: "tester_invitation")', function() {
      // uncomment below and update the code to test the property testerInvitation
      //var instance = new AppCenterClient.ExternalUserRequest();
      //expect(instance).to.be();
    });

  });

}));
