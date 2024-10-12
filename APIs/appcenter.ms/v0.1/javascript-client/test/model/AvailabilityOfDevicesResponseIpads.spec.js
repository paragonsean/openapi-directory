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
    instance = new AppCenterClient.AvailabilityOfDevicesResponseIpads();
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

  describe('AvailabilityOfDevicesResponseIpads', function() {
    it('should create an instance of AvailabilityOfDevicesResponseIpads', function() {
      // uncomment below and update the code to test AvailabilityOfDevicesResponseIpads
      //var instance = new AppCenterClient.AvailabilityOfDevicesResponseIpads();
      //expect(instance).to.be.a(AppCenterClient.AvailabilityOfDevicesResponseIpads);
    });

    it('should have the property available (base name: "available")', function() {
      // uncomment below and update the code to test the property available
      //var instance = new AppCenterClient.AvailabilityOfDevicesResponseIpads();
      //expect(instance).to.be();
    });

    it('should have the property maximum (base name: "maximum")', function() {
      // uncomment below and update the code to test the property maximum
      //var instance = new AppCenterClient.AvailabilityOfDevicesResponseIpads();
      //expect(instance).to.be();
    });

    it('should have the property registered (base name: "registered")', function() {
      // uncomment below and update the code to test the property registered
      //var instance = new AppCenterClient.AvailabilityOfDevicesResponseIpads();
      //expect(instance).to.be();
    });

  });

}));
