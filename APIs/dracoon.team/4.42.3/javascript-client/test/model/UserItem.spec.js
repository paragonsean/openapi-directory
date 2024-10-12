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
    instance = new DracoonApi.UserItem();
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

  describe('UserItem', function() {
    it('should create an instance of UserItem', function() {
      // uncomment below and update the code to test UserItem
      //var instance = new DracoonApi.UserItem();
      //expect(instance).to.be.a(DracoonApi.UserItem);
    });

    it('should have the property avatarUuid (base name: "avatarUuid")', function() {
      // uncomment below and update the code to test the property avatarUuid
      //var instance = new DracoonApi.UserItem();
      //expect(instance).to.be();
    });

    it('should have the property createdAt (base name: "createdAt")', function() {
      // uncomment below and update the code to test the property createdAt
      //var instance = new DracoonApi.UserItem();
      //expect(instance).to.be();
    });

    it('should have the property email (base name: "email")', function() {
      // uncomment below and update the code to test the property email
      //var instance = new DracoonApi.UserItem();
      //expect(instance).to.be();
    });

    it('should have the property expireAt (base name: "expireAt")', function() {
      // uncomment below and update the code to test the property expireAt
      //var instance = new DracoonApi.UserItem();
      //expect(instance).to.be();
    });

    it('should have the property firstName (base name: "firstName")', function() {
      // uncomment below and update the code to test the property firstName
      //var instance = new DracoonApi.UserItem();
      //expect(instance).to.be();
    });

    it('should have the property gender (base name: "gender")', function() {
      // uncomment below and update the code to test the property gender
      //var instance = new DracoonApi.UserItem();
      //expect(instance).to.be();
    });

    it('should have the property hasManageableRooms (base name: "hasManageableRooms")', function() {
      // uncomment below and update the code to test the property hasManageableRooms
      //var instance = new DracoonApi.UserItem();
      //expect(instance).to.be();
    });

    it('should have the property homeRoomId (base name: "homeRoomId")', function() {
      // uncomment below and update the code to test the property homeRoomId
      //var instance = new DracoonApi.UserItem();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new DracoonApi.UserItem();
      //expect(instance).to.be();
    });

    it('should have the property isEncryptionEnabled (base name: "isEncryptionEnabled")', function() {
      // uncomment below and update the code to test the property isEncryptionEnabled
      //var instance = new DracoonApi.UserItem();
      //expect(instance).to.be();
    });

    it('should have the property isLocked (base name: "isLocked")', function() {
      // uncomment below and update the code to test the property isLocked
      //var instance = new DracoonApi.UserItem();
      //expect(instance).to.be();
    });

    it('should have the property lastLoginSuccessAt (base name: "lastLoginSuccessAt")', function() {
      // uncomment below and update the code to test the property lastLoginSuccessAt
      //var instance = new DracoonApi.UserItem();
      //expect(instance).to.be();
    });

    it('should have the property lastName (base name: "lastName")', function() {
      // uncomment below and update the code to test the property lastName
      //var instance = new DracoonApi.UserItem();
      //expect(instance).to.be();
    });

    it('should have the property lockStatus (base name: "lockStatus")', function() {
      // uncomment below and update the code to test the property lockStatus
      //var instance = new DracoonApi.UserItem();
      //expect(instance).to.be();
    });

    it('should have the property login (base name: "login")', function() {
      // uncomment below and update the code to test the property login
      //var instance = new DracoonApi.UserItem();
      //expect(instance).to.be();
    });

    it('should have the property phone (base name: "phone")', function() {
      // uncomment below and update the code to test the property phone
      //var instance = new DracoonApi.UserItem();
      //expect(instance).to.be();
    });

    it('should have the property title (base name: "title")', function() {
      // uncomment below and update the code to test the property title
      //var instance = new DracoonApi.UserItem();
      //expect(instance).to.be();
    });

    it('should have the property userAttributes (base name: "userAttributes")', function() {
      // uncomment below and update the code to test the property userAttributes
      //var instance = new DracoonApi.UserItem();
      //expect(instance).to.be();
    });

    it('should have the property userName (base name: "userName")', function() {
      // uncomment below and update the code to test the property userName
      //var instance = new DracoonApi.UserItem();
      //expect(instance).to.be();
    });

    it('should have the property userRoles (base name: "userRoles")', function() {
      // uncomment below and update the code to test the property userRoles
      //var instance = new DracoonApi.UserItem();
      //expect(instance).to.be();
    });

  });

}));
