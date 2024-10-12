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
    instance = new VRealizeNetworkInsightApiReference.NSXFirewallRule();
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

  describe('NSXFirewallRule', function() {
    it('should create an instance of NSXFirewallRule', function() {
      // uncomment below and update the code to test NSXFirewallRule
      //var instance = new VRealizeNetworkInsightApiReference.NSXFirewallRule();
      //expect(instance).to.be.a(VRealizeNetworkInsightApiReference.NSXFirewallRule);
    });

    it('should have the property direction (base name: "direction")', function() {
      // uncomment below and update the code to test the property direction
      //var instance = new VRealizeNetworkInsightApiReference.NSXFirewallRule();
      //expect(instance).to.be();
    });

    it('should have the property loggingEnabled (base name: "logging_enabled")', function() {
      // uncomment below and update the code to test the property loggingEnabled
      //var instance = new VRealizeNetworkInsightApiReference.NSXFirewallRule();
      //expect(instance).to.be();
    });

    it('should have the property nsxManagers (base name: "nsx_managers")', function() {
      // uncomment below and update the code to test the property nsxManagers
      //var instance = new VRealizeNetworkInsightApiReference.NSXFirewallRule();
      //expect(instance).to.be();
    });

    it('should have the property scope (base name: "scope")', function() {
      // uncomment below and update the code to test the property scope
      //var instance = new VRealizeNetworkInsightApiReference.NSXFirewallRule();
      //expect(instance).to.be();
    });

  });

}));
