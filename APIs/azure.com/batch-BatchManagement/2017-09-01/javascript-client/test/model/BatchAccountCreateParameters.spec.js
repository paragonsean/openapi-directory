/**
 * BatchManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-09-01
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
    factory(root.expect, root.BatchManagement);
  }
}(this, function(expect, BatchManagement) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new BatchManagement.BatchAccountCreateParameters();
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

  describe('BatchAccountCreateParameters', function() {
    it('should create an instance of BatchAccountCreateParameters', function() {
      // uncomment below and update the code to test BatchAccountCreateParameters
      //var instance = new BatchManagement.BatchAccountCreateParameters();
      //expect(instance).to.be.a(BatchManagement.BatchAccountCreateParameters);
    });

    it('should have the property location (base name: "location")', function() {
      // uncomment below and update the code to test the property location
      //var instance = new BatchManagement.BatchAccountCreateParameters();
      //expect(instance).to.be();
    });

    it('should have the property properties (base name: "properties")', function() {
      // uncomment below and update the code to test the property properties
      //var instance = new BatchManagement.BatchAccountCreateParameters();
      //expect(instance).to.be();
    });

    it('should have the property tags (base name: "tags")', function() {
      // uncomment below and update the code to test the property tags
      //var instance = new BatchManagement.BatchAccountCreateParameters();
      //expect(instance).to.be();
    });

  });

}));
