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
    instance = new AppCenterClient.CrashDetails();
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

  describe('CrashDetails', function() {
    it('should create an instance of CrashDetails', function() {
      // uncomment below and update the code to test CrashDetails
      //var instance = new AppCenterClient.CrashDetails();
      //expect(instance).to.be.a(AppCenterClient.CrashDetails);
    });

    it('should have the property appStartTimestamp (base name: "app_start_timestamp")', function() {
      // uncomment below and update the code to test the property appStartTimestamp
      //var instance = new AppCenterClient.CrashDetails();
      //expect(instance).to.be();
    });

    it('should have the property carrierCountry (base name: "carrier_country")', function() {
      // uncomment below and update the code to test the property carrierCountry
      //var instance = new AppCenterClient.CrashDetails();
      //expect(instance).to.be();
    });

    it('should have the property carrierName (base name: "carrier_name")', function() {
      // uncomment below and update the code to test the property carrierName
      //var instance = new AppCenterClient.CrashDetails();
      //expect(instance).to.be();
    });

    it('should have the property locale (base name: "locale")', function() {
      // uncomment below and update the code to test the property locale
      //var instance = new AppCenterClient.CrashDetails();
      //expect(instance).to.be();
    });

    it('should have the property osBuild (base name: "os_build")', function() {
      // uncomment below and update the code to test the property osBuild
      //var instance = new AppCenterClient.CrashDetails();
      //expect(instance).to.be();
    });

    it('should have the property rooted (base name: "rooted")', function() {
      // uncomment below and update the code to test the property rooted
      //var instance = new AppCenterClient.CrashDetails();
      //expect(instance).to.be();
    });

    it('should have the property screenSize (base name: "screen_size")', function() {
      // uncomment below and update the code to test the property screenSize
      //var instance = new AppCenterClient.CrashDetails();
      //expect(instance).to.be();
    });

  });

}));
