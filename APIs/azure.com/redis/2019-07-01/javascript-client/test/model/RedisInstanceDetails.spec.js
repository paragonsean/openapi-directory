/**
 * RedisManagementClient
 * REST API for Azure Redis Cache Service.
 *
 * The version of the OpenAPI document: 2019-07-01
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
    instance = new RedisManagementClient.RedisInstanceDetails();
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

  describe('RedisInstanceDetails', function() {
    it('should create an instance of RedisInstanceDetails', function() {
      // uncomment below and update the code to test RedisInstanceDetails
      //var instance = new RedisManagementClient.RedisInstanceDetails();
      //expect(instance).to.be.a(RedisManagementClient.RedisInstanceDetails);
    });

    it('should have the property nonSslPort (base name: "nonSslPort")', function() {
      // uncomment below and update the code to test the property nonSslPort
      //var instance = new RedisManagementClient.RedisInstanceDetails();
      //expect(instance).to.be();
    });

    it('should have the property shardId (base name: "shardId")', function() {
      // uncomment below and update the code to test the property shardId
      //var instance = new RedisManagementClient.RedisInstanceDetails();
      //expect(instance).to.be();
    });

    it('should have the property sslPort (base name: "sslPort")', function() {
      // uncomment below and update the code to test the property sslPort
      //var instance = new RedisManagementClient.RedisInstanceDetails();
      //expect(instance).to.be();
    });

    it('should have the property zone (base name: "zone")', function() {
      // uncomment below and update the code to test the property zone
      //var instance = new RedisManagementClient.RedisInstanceDetails();
      //expect(instance).to.be();
    });

  });

}));
