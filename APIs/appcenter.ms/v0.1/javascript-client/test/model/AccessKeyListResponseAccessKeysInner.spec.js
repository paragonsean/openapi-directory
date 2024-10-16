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
    instance = new AppCenterClient.AccessKeyListResponseAccessKeysInner();
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

  describe('AccessKeyListResponseAccessKeysInner', function() {
    it('should create an instance of AccessKeyListResponseAccessKeysInner', function() {
      // uncomment below and update the code to test AccessKeyListResponseAccessKeysInner
      //var instance = new AppCenterClient.AccessKeyListResponseAccessKeysInner();
      //expect(instance).to.be.a(AppCenterClient.AccessKeyListResponseAccessKeysInner);
    });

    it('should have the property createdBy (base name: "createdBy")', function() {
      // uncomment below and update the code to test the property createdBy
      //var instance = new AppCenterClient.AccessKeyListResponseAccessKeysInner();
      //expect(instance).to.be();
    });

    it('should have the property createdTime (base name: "createdTime")', function() {
      // uncomment below and update the code to test the property createdTime
      //var instance = new AppCenterClient.AccessKeyListResponseAccessKeysInner();
      //expect(instance).to.be();
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new AppCenterClient.AccessKeyListResponseAccessKeysInner();
      //expect(instance).to.be();
    });

    it('should have the property expires (base name: "expires")', function() {
      // uncomment below and update the code to test the property expires
      //var instance = new AppCenterClient.AccessKeyListResponseAccessKeysInner();
      //expect(instance).to.be();
    });

    it('should have the property friendlyName (base name: "friendlyName")', function() {
      // uncomment below and update the code to test the property friendlyName
      //var instance = new AppCenterClient.AccessKeyListResponseAccessKeysInner();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new AppCenterClient.AccessKeyListResponseAccessKeysInner();
      //expect(instance).to.be();
    });

    it('should have the property isSession (base name: "isSession")', function() {
      // uncomment below and update the code to test the property isSession
      //var instance = new AppCenterClient.AccessKeyListResponseAccessKeysInner();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new AppCenterClient.AccessKeyListResponseAccessKeysInner();
      //expect(instance).to.be();
    });

  });

}));
