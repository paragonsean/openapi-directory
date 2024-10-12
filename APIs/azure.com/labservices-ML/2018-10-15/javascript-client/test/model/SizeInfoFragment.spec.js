/**
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
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
    factory(root.expect, root.ManagedLabsClient);
  }
}(this, function(expect, ManagedLabsClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new ManagedLabsClient.SizeInfoFragment();
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

  describe('SizeInfoFragment', function() {
    it('should create an instance of SizeInfoFragment', function() {
      // uncomment below and update the code to test SizeInfoFragment
      //var instance = new ManagedLabsClient.SizeInfoFragment();
      //expect(instance).to.be.a(ManagedLabsClient.SizeInfoFragment);
    });

    it('should have the property computeSize (base name: "computeSize")', function() {
      // uncomment below and update the code to test the property computeSize
      //var instance = new ManagedLabsClient.SizeInfoFragment();
      //expect(instance).to.be();
    });

    it('should have the property memory (base name: "memory")', function() {
      // uncomment below and update the code to test the property memory
      //var instance = new ManagedLabsClient.SizeInfoFragment();
      //expect(instance).to.be();
    });

    it('should have the property numberOfCores (base name: "numberOfCores")', function() {
      // uncomment below and update the code to test the property numberOfCores
      //var instance = new ManagedLabsClient.SizeInfoFragment();
      //expect(instance).to.be();
    });

    it('should have the property price (base name: "price")', function() {
      // uncomment below and update the code to test the property price
      //var instance = new ManagedLabsClient.SizeInfoFragment();
      //expect(instance).to.be();
    });

  });

}));
