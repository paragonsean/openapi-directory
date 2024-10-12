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
    instance = new VRealizeNetworkInsightApiReference.SwitchDataSourceRequest();
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

  describe('SwitchDataSourceRequest', function() {
    it('should create an instance of SwitchDataSourceRequest', function() {
      // uncomment below and update the code to test SwitchDataSourceRequest
      //var instance = new VRealizeNetworkInsightApiReference.SwitchDataSourceRequest();
      //expect(instance).to.be.a(VRealizeNetworkInsightApiReference.SwitchDataSourceRequest);
    });

    it('should have the property enabled (base name: "enabled")', function() {
      // uncomment below and update the code to test the property enabled
      //var instance = new VRealizeNetworkInsightApiReference.SwitchDataSourceRequest();
      //expect(instance).to.be();
    });

    it('should have the property fqdn (base name: "fqdn")', function() {
      // uncomment below and update the code to test the property fqdn
      //var instance = new VRealizeNetworkInsightApiReference.SwitchDataSourceRequest();
      //expect(instance).to.be();
    });

    it('should have the property ip (base name: "ip")', function() {
      // uncomment below and update the code to test the property ip
      //var instance = new VRealizeNetworkInsightApiReference.SwitchDataSourceRequest();
      //expect(instance).to.be();
    });

    it('should have the property nickname (base name: "nickname")', function() {
      // uncomment below and update the code to test the property nickname
      //var instance = new VRealizeNetworkInsightApiReference.SwitchDataSourceRequest();
      //expect(instance).to.be();
    });

    it('should have the property notes (base name: "notes")', function() {
      // uncomment below and update the code to test the property notes
      //var instance = new VRealizeNetworkInsightApiReference.SwitchDataSourceRequest();
      //expect(instance).to.be();
    });

    it('should have the property proxyId (base name: "proxy_id")', function() {
      // uncomment below and update the code to test the property proxyId
      //var instance = new VRealizeNetworkInsightApiReference.SwitchDataSourceRequest();
      //expect(instance).to.be();
    });

    it('should have the property credentials (base name: "credentials")', function() {
      // uncomment below and update the code to test the property credentials
      //var instance = new VRealizeNetworkInsightApiReference.SwitchDataSourceRequest();
      //expect(instance).to.be();
    });

  });

}));
