/**
 * Tradeworks
 * Authentication is required to access all methods of the API. Enter username and password.                 Credentials are automatically set as you type.
 *
 * The version of the OpenAPI document: 1.0
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
    factory(root.expect, root.Tradeworks);
  }
}(this, function(expect, Tradeworks) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new Tradeworks.UserDTO();
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

  describe('UserDTO', function() {
    it('should create an instance of UserDTO', function() {
      // uncomment below and update the code to test UserDTO
      //var instance = new Tradeworks.UserDTO();
      //expect(instance).to.be.a(Tradeworks.UserDTO);
    });

    it('should have the property affiliateId (base name: "affiliateId")', function() {
      // uncomment below and update the code to test the property affiliateId
      //var instance = new Tradeworks.UserDTO();
      //expect(instance).to.be();
    });

    it('should have the property email (base name: "email")', function() {
      // uncomment below and update the code to test the property email
      //var instance = new Tradeworks.UserDTO();
      //expect(instance).to.be();
    });

    it('should have the property firstName (base name: "firstName")', function() {
      // uncomment below and update the code to test the property firstName
      //var instance = new Tradeworks.UserDTO();
      //expect(instance).to.be();
    });

    it('should have the property lastName (base name: "lastName")', function() {
      // uncomment below and update the code to test the property lastName
      //var instance = new Tradeworks.UserDTO();
      //expect(instance).to.be();
    });

    it('should have the property password (base name: "password")', function() {
      // uncomment below and update the code to test the property password
      //var instance = new Tradeworks.UserDTO();
      //expect(instance).to.be();
    });

    it('should have the property subscriptionType (base name: "subscriptionType")', function() {
      // uncomment below and update the code to test the property subscriptionType
      //var instance = new Tradeworks.UserDTO();
      //expect(instance).to.be();
    });

    it('should have the property username (base name: "username")', function() {
      // uncomment below and update the code to test the property username
      //var instance = new Tradeworks.UserDTO();
      //expect(instance).to.be();
    });

  });

}));
