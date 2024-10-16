/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
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
    factory(root.expect, root.MerakiDashboardApi);
  }
}(this, function(expect, MerakiDashboardApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MerakiDashboardApi.CreateOrganizationAlertsProfileRequestAlertCondition();
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

  describe('CreateOrganizationAlertsProfileRequestAlertCondition', function() {
    it('should create an instance of CreateOrganizationAlertsProfileRequestAlertCondition', function() {
      // uncomment below and update the code to test CreateOrganizationAlertsProfileRequestAlertCondition
      //var instance = new MerakiDashboardApi.CreateOrganizationAlertsProfileRequestAlertCondition();
      //expect(instance).to.be.a(MerakiDashboardApi.CreateOrganizationAlertsProfileRequestAlertCondition);
    });

    it('should have the property bitRateBps (base name: "bit_rate_bps")', function() {
      // uncomment below and update the code to test the property bitRateBps
      //var instance = new MerakiDashboardApi.CreateOrganizationAlertsProfileRequestAlertCondition();
      //expect(instance).to.be();
    });

    it('should have the property duration (base name: "duration")', function() {
      // uncomment below and update the code to test the property duration
      //var instance = new MerakiDashboardApi.CreateOrganizationAlertsProfileRequestAlertCondition();
      //expect(instance).to.be();
    });

    it('should have the property _interface (base name: "interface")', function() {
      // uncomment below and update the code to test the property _interface
      //var instance = new MerakiDashboardApi.CreateOrganizationAlertsProfileRequestAlertCondition();
      //expect(instance).to.be();
    });

    it('should have the property jitterMs (base name: "jitter_ms")', function() {
      // uncomment below and update the code to test the property jitterMs
      //var instance = new MerakiDashboardApi.CreateOrganizationAlertsProfileRequestAlertCondition();
      //expect(instance).to.be();
    });

    it('should have the property latencyMs (base name: "latency_ms")', function() {
      // uncomment below and update the code to test the property latencyMs
      //var instance = new MerakiDashboardApi.CreateOrganizationAlertsProfileRequestAlertCondition();
      //expect(instance).to.be();
    });

    it('should have the property lossRatio (base name: "loss_ratio")', function() {
      // uncomment below and update the code to test the property lossRatio
      //var instance = new MerakiDashboardApi.CreateOrganizationAlertsProfileRequestAlertCondition();
      //expect(instance).to.be();
    });

    it('should have the property mos (base name: "mos")', function() {
      // uncomment below and update the code to test the property mos
      //var instance = new MerakiDashboardApi.CreateOrganizationAlertsProfileRequestAlertCondition();
      //expect(instance).to.be();
    });

    it('should have the property window (base name: "window")', function() {
      // uncomment below and update the code to test the property window
      //var instance = new MerakiDashboardApi.CreateOrganizationAlertsProfileRequestAlertCondition();
      //expect(instance).to.be();
    });

  });

}));
