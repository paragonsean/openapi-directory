/**
 * vRealize Network Insight API Reference
 * vRealize Network Insight API Reference
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
    factory(root.expect, root.VRealizeNetworkInsightApiReference);
  }
}(this, function(expect, VRealizeNetworkInsightApiReference) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new VRealizeNetworkInsightApiReference.SNMP2cConfig();
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

  describe('SNMP2cConfig', function() {
    it('should create an instance of SNMP2cConfig', function() {
      // uncomment below and update the code to test SNMP2cConfig
      //var instance = new VRealizeNetworkInsightApiReference.SNMP2cConfig();
      //expect(instance).to.be.a(VRealizeNetworkInsightApiReference.SNMP2cConfig);
    });

    it('should have the property communityString (base name: "community_string")', function() {
      // uncomment below and update the code to test the property communityString
      //var instance = new VRealizeNetworkInsightApiReference.SNMP2cConfig();
      //expect(instance).to.be();
    });

  });

}));
