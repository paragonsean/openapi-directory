/**
 * RedisManagementClient
 * REST API for Azure Redis Cache Service.
 *
 * The version of the OpenAPI document: 2017-02-01
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
    factory(root.expect, root.RedisManagementClient);
  }
}(this, function(expect, RedisManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new RedisManagementClient.Operation();
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

  describe('Operation', function() {
    it('should create an instance of Operation', function() {
      // uncomment below and update the code to test Operation
      //var instance = new RedisManagementClient.Operation();
      //expect(instance).to.be.a(RedisManagementClient.Operation);
    });

    it('should have the property display (base name: "display")', function() {
      // uncomment below and update the code to test the property display
      //var instance = new RedisManagementClient.Operation();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new RedisManagementClient.Operation();
      //expect(instance).to.be();
    });

  });

}));
