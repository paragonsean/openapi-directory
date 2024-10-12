/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
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
    factory(root.expect, root.StorSimple8000SeriesManagementClient);
  }
}(this, function(expect, StorSimple8000SeriesManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new StorSimple8000SeriesManagementClient.NicIPv4();
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

  describe('NicIPv4', function() {
    it('should create an instance of NicIPv4', function() {
      // uncomment below and update the code to test NicIPv4
      //var instance = new StorSimple8000SeriesManagementClient.NicIPv4();
      //expect(instance).to.be.a(StorSimple8000SeriesManagementClient.NicIPv4);
    });

    it('should have the property controller0Ipv4Address (base name: "controller0Ipv4Address")', function() {
      // uncomment below and update the code to test the property controller0Ipv4Address
      //var instance = new StorSimple8000SeriesManagementClient.NicIPv4();
      //expect(instance).to.be();
    });

    it('should have the property controller1Ipv4Address (base name: "controller1Ipv4Address")', function() {
      // uncomment below and update the code to test the property controller1Ipv4Address
      //var instance = new StorSimple8000SeriesManagementClient.NicIPv4();
      //expect(instance).to.be();
    });

    it('should have the property ipv4Address (base name: "ipv4Address")', function() {
      // uncomment below and update the code to test the property ipv4Address
      //var instance = new StorSimple8000SeriesManagementClient.NicIPv4();
      //expect(instance).to.be();
    });

    it('should have the property ipv4Gateway (base name: "ipv4Gateway")', function() {
      // uncomment below and update the code to test the property ipv4Gateway
      //var instance = new StorSimple8000SeriesManagementClient.NicIPv4();
      //expect(instance).to.be();
    });

    it('should have the property ipv4Netmask (base name: "ipv4Netmask")', function() {
      // uncomment below and update the code to test the property ipv4Netmask
      //var instance = new StorSimple8000SeriesManagementClient.NicIPv4();
      //expect(instance).to.be();
    });

  });

}));
