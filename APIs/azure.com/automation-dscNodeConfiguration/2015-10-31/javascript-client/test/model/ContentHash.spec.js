/**
 * AutomationManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2015-10-31
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
    factory(root.expect, root.AutomationManagement);
  }
}(this, function(expect, AutomationManagement) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AutomationManagement.ContentHash();
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

  describe('ContentHash', function() {
    it('should create an instance of ContentHash', function() {
      // uncomment below and update the code to test ContentHash
      //var instance = new AutomationManagement.ContentHash();
      //expect(instance).to.be.a(AutomationManagement.ContentHash);
    });

    it('should have the property algorithm (base name: "algorithm")', function() {
      // uncomment below and update the code to test the property algorithm
      //var instance = new AutomationManagement.ContentHash();
      //expect(instance).to.be();
    });

    it('should have the property value (base name: "value")', function() {
      // uncomment below and update the code to test the property value
      //var instance = new AutomationManagement.ContentHash();
      //expect(instance).to.be();
    });

  });

}));
