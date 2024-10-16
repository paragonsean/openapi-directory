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
    instance = new CleverCloudApi.WannabeAddon();
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

  describe('WannabeAddon', function() {
    it('should create an instance of WannabeAddon', function() {
      // uncomment below and update the code to test WannabeAddon
      //var instance = new CleverCloudApi.WannabeAddon();
      //expect(instance).to.be.a(CleverCloudApi.WannabeAddon);
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new CleverCloudApi.WannabeAddon();
      //expect(instance).to.be();
    });

    it('should have the property payment (base name: "payment")', function() {
      // uncomment below and update the code to test the property payment
      //var instance = new CleverCloudApi.WannabeAddon();
      //expect(instance).to.be();
    });

    it('should have the property plan (base name: "plan")', function() {
      // uncomment below and update the code to test the property plan
      //var instance = new CleverCloudApi.WannabeAddon();
      //expect(instance).to.be();
    });

    it('should have the property providerId (base name: "providerId")', function() {
      // uncomment below and update the code to test the property providerId
      //var instance = new CleverCloudApi.WannabeAddon();
      //expect(instance).to.be();
    });

    it('should have the property region (base name: "region")', function() {
      // uncomment below and update the code to test the property region
      //var instance = new CleverCloudApi.WannabeAddon();
      //expect(instance).to.be();
    });

  });

}));
