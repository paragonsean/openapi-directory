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
    instance = new VRealizeNetworkInsightApiReference.RuleSet();
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

  describe('RuleSet', function() {
    it('should create an instance of RuleSet', function() {
      // uncomment below and update the code to test RuleSet
      //var instance = new VRealizeNetworkInsightApiReference.RuleSet();
      //expect(instance).to.be.a(VRealizeNetworkInsightApiReference.RuleSet);
    });

    it('should have the property firewall (base name: "firewall")', function() {
      // uncomment below and update the code to test the property firewall
      //var instance = new VRealizeNetworkInsightApiReference.RuleSet();
      //expect(instance).to.be();
    });

    it('should have the property ruleSetType (base name: "rule_set_type")', function() {
      // uncomment below and update the code to test the property ruleSetType
      //var instance = new VRealizeNetworkInsightApiReference.RuleSet();
      //expect(instance).to.be();
    });

    it('should have the property rules (base name: "rules")', function() {
      // uncomment below and update the code to test the property rules
      //var instance = new VRealizeNetworkInsightApiReference.RuleSet();
      //expect(instance).to.be();
    });

  });

}));
