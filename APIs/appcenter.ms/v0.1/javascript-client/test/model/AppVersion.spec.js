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
    instance = new AppCenterClient.AppVersion();
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

  describe('AppVersion', function() {
    it('should create an instance of AppVersion', function() {
      // uncomment below and update the code to test AppVersion
      //var instance = new AppCenterClient.AppVersion();
      //expect(instance).to.be.a(AppCenterClient.AppVersion);
    });

    it('should have the property appId (base name: "app_id")', function() {
      // uncomment below and update the code to test the property appId
      //var instance = new AppCenterClient.AppVersion();
      //expect(instance).to.be();
    });

    it('should have the property appVersion (base name: "app_version")', function() {
      // uncomment below and update the code to test the property appVersion
      //var instance = new AppCenterClient.AppVersion();
      //expect(instance).to.be();
    });

    it('should have the property appVersionId (base name: "app_version_id")', function() {
      // uncomment below and update the code to test the property appVersionId
      //var instance = new AppCenterClient.AppVersion();
      //expect(instance).to.be();
    });

    it('should have the property buildNumber (base name: "build_number")', function() {
      // uncomment below and update the code to test the property buildNumber
      //var instance = new AppCenterClient.AppVersion();
      //expect(instance).to.be();
    });

    it('should have the property displayName (base name: "display_name")', function() {
      // uncomment below and update the code to test the property displayName
      //var instance = new AppCenterClient.AppVersion();
      //expect(instance).to.be();
    });

  });

}));
