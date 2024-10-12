/**
 * RedisManagementClient
 * REST API for Azure Redis Cache Service.
 *
 * The version of the OpenAPI document: 2018-03-01
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
    instance = new RedisManagementClient.FirewallRulesApi();
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

  describe('FirewallRulesApi', function() {
    describe('firewallRulesCreateOrUpdate_0', function() {
      it('should call firewallRulesCreateOrUpdate_0 successfully', function(done) {
        //uncomment below and update the code to test firewallRulesCreateOrUpdate_0
        //instance.firewallRulesCreateOrUpdate_0(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('firewallRulesDelete_0', function() {
      it('should call firewallRulesDelete_0 successfully', function(done) {
        //uncomment below and update the code to test firewallRulesDelete_0
        //instance.firewallRulesDelete_0(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('firewallRulesGet_0', function() {
      it('should call firewallRulesGet_0 successfully', function(done) {
        //uncomment below and update the code to test firewallRulesGet_0
        //instance.firewallRulesGet_0(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('firewallRulesListByRedisResource_0', function() {
      it('should call firewallRulesListByRedisResource_0 successfully', function(done) {
        //uncomment below and update the code to test firewallRulesListByRedisResource_0
        //instance.firewallRulesListByRedisResource_0(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
