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
    instance = new CleverCloudApi.WannabeConsumerRights();
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

  describe('WannabeConsumerRights', function() {
    it('should create an instance of WannabeConsumerRights', function() {
      // uncomment below and update the code to test WannabeConsumerRights
      //var instance = new CleverCloudApi.WannabeConsumerRights();
      //expect(instance).to.be.a(CleverCloudApi.WannabeConsumerRights);
    });

    it('should have the property activated (base name: "activated")', function() {
      // uncomment below and update the code to test the property activated
      //var instance = new CleverCloudApi.WannabeConsumerRights();
      //expect(instance).to.be();
    });

    it('should have the property right (base name: "right")', function() {
      // uncomment below and update the code to test the property right
      //var instance = new CleverCloudApi.WannabeConsumerRights();
      //expect(instance).to.be();
    });

  });

}));
