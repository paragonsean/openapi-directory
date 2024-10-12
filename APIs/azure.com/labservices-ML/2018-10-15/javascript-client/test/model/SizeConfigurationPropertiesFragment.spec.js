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
    instance = new ManagedLabsClient.SizeConfigurationPropertiesFragment();
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

  describe('SizeConfigurationPropertiesFragment', function() {
    it('should create an instance of SizeConfigurationPropertiesFragment', function() {
      // uncomment below and update the code to test SizeConfigurationPropertiesFragment
      //var instance = new ManagedLabsClient.SizeConfigurationPropertiesFragment();
      //expect(instance).to.be.a(ManagedLabsClient.SizeConfigurationPropertiesFragment);
    });

    it('should have the property environmentSizes (base name: "environmentSizes")', function() {
      // uncomment below and update the code to test the property environmentSizes
      //var instance = new ManagedLabsClient.SizeConfigurationPropertiesFragment();
      //expect(instance).to.be();
    });

  });

}));
