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
    instance = new DracoonApi.UpdateLoginPasswordPolicies();
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

  describe('UpdateLoginPasswordPolicies', function() {
    it('should create an instance of UpdateLoginPasswordPolicies', function() {
      // uncomment below and update the code to test UpdateLoginPasswordPolicies
      //var instance = new DracoonApi.UpdateLoginPasswordPolicies();
      //expect(instance).to.be.a(DracoonApi.UpdateLoginPasswordPolicies);
    });

    it('should have the property characterRules (base name: "characterRules")', function() {
      // uncomment below and update the code to test the property characterRules
      //var instance = new DracoonApi.UpdateLoginPasswordPolicies();
      //expect(instance).to.be();
    });

    it('should have the property enforceLoginPasswordChange (base name: "enforceLoginPasswordChange")', function() {
      // uncomment below and update the code to test the property enforceLoginPasswordChange
      //var instance = new DracoonApi.UpdateLoginPasswordPolicies();
      //expect(instance).to.be();
    });

    it('should have the property minLength (base name: "minLength")', function() {
      // uncomment below and update the code to test the property minLength
      //var instance = new DracoonApi.UpdateLoginPasswordPolicies();
      //expect(instance).to.be();
    });

    it('should have the property numberOfArchivedPasswords (base name: "numberOfArchivedPasswords")', function() {
      // uncomment below and update the code to test the property numberOfArchivedPasswords
      //var instance = new DracoonApi.UpdateLoginPasswordPolicies();
      //expect(instance).to.be();
    });

    it('should have the property passwordExpiration (base name: "passwordExpiration")', function() {
      // uncomment below and update the code to test the property passwordExpiration
      //var instance = new DracoonApi.UpdateLoginPasswordPolicies();
      //expect(instance).to.be();
    });

    it('should have the property rejectDictionaryWords (base name: "rejectDictionaryWords")', function() {
      // uncomment below and update the code to test the property rejectDictionaryWords
      //var instance = new DracoonApi.UpdateLoginPasswordPolicies();
      //expect(instance).to.be();
    });

    it('should have the property rejectKeyboardPatterns (base name: "rejectKeyboardPatterns")', function() {
      // uncomment below and update the code to test the property rejectKeyboardPatterns
      //var instance = new DracoonApi.UpdateLoginPasswordPolicies();
      //expect(instance).to.be();
    });

    it('should have the property rejectUserInfo (base name: "rejectUserInfo")', function() {
      // uncomment below and update the code to test the property rejectUserInfo
      //var instance = new DracoonApi.UpdateLoginPasswordPolicies();
      //expect(instance).to.be();
    });

    it('should have the property userLockout (base name: "userLockout")', function() {
      // uncomment below and update the code to test the property userLockout
      //var instance = new DracoonApi.UpdateLoginPasswordPolicies();
      //expect(instance).to.be();
    });

  });

}));
