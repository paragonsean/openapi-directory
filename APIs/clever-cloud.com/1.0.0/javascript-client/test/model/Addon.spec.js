/**
 * Clever-Cloud API
 * Public API for managing Clever-Cloud data and products
 *
 * The version of the OpenAPI document: 1.0.0
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
    factory(root.expect, root.CleverCloudApi);
  }
}(this, function(expect, CleverCloudApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new CleverCloudApi.Addon();
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

  describe('Addon', function() {
    it('should create an instance of Addon', function() {
      // uncomment below and update the code to test Addon
      //var instance = new CleverCloudApi.Addon();
      //expect(instance).to.be.a(CleverCloudApi.Addon);
    });

    it('should have the property configKeys (base name: "configKeys")', function() {
      // uncomment below and update the code to test the property configKeys
      //var instance = new CleverCloudApi.Addon();
      //expect(instance).to.be();
    });

    it('should have the property creationDate (base name: "creationDate")', function() {
      // uncomment below and update the code to test the property creationDate
      //var instance = new CleverCloudApi.Addon();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new CleverCloudApi.Addon();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new CleverCloudApi.Addon();
      //expect(instance).to.be();
    });

    it('should have the property plan (base name: "plan")', function() {
      // uncomment below and update the code to test the property plan
      //var instance = new CleverCloudApi.Addon();
      //expect(instance).to.be();
    });

    it('should have the property provider (base name: "provider")', function() {
      // uncomment below and update the code to test the property provider
      //var instance = new CleverCloudApi.Addon();
      //expect(instance).to.be();
    });

    it('should have the property realId (base name: "realId")', function() {
      // uncomment below and update the code to test the property realId
      //var instance = new CleverCloudApi.Addon();
      //expect(instance).to.be();
    });

    it('should have the property region (base name: "region")', function() {
      // uncomment below and update the code to test the property region
      //var instance = new CleverCloudApi.Addon();
      //expect(instance).to.be();
    });

  });

}));
