/**
 * ManagementLockClient
 * Azure resources can be locked to prevent other users in your organization from deleting or modifying resources.
 *
 * The version of the OpenAPI document: 2016-09-01
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
    factory(root.expect, root.ManagementLockClient);
  }
}(this, function(expect, ManagementLockClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new ManagementLockClient.ManagementLockProperties();
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

  describe('ManagementLockProperties', function() {
    it('should create an instance of ManagementLockProperties', function() {
      // uncomment below and update the code to test ManagementLockProperties
      //var instance = new ManagementLockClient.ManagementLockProperties();
      //expect(instance).to.be.a(ManagementLockClient.ManagementLockProperties);
    });

    it('should have the property level (base name: "level")', function() {
      // uncomment below and update the code to test the property level
      //var instance = new ManagementLockClient.ManagementLockProperties();
      //expect(instance).to.be();
    });

    it('should have the property notes (base name: "notes")', function() {
      // uncomment below and update the code to test the property notes
      //var instance = new ManagementLockClient.ManagementLockProperties();
      //expect(instance).to.be();
    });

    it('should have the property owners (base name: "owners")', function() {
      // uncomment below and update the code to test the property owners
      //var instance = new ManagementLockClient.ManagementLockProperties();
      //expect(instance).to.be();
    });

  });

}));
