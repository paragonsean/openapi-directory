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
    instance = new MerakiDashboardApi.GetDeviceLiveToolsPing200ResponseResultsLatencies();
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

  describe('GetDeviceLiveToolsPing200ResponseResultsLatencies', function() {
    it('should create an instance of GetDeviceLiveToolsPing200ResponseResultsLatencies', function() {
      // uncomment below and update the code to test GetDeviceLiveToolsPing200ResponseResultsLatencies
      //var instance = new MerakiDashboardApi.GetDeviceLiveToolsPing200ResponseResultsLatencies();
      //expect(instance).to.be.a(MerakiDashboardApi.GetDeviceLiveToolsPing200ResponseResultsLatencies);
    });

    it('should have the property average (base name: "average")', function() {
      // uncomment below and update the code to test the property average
      //var instance = new MerakiDashboardApi.GetDeviceLiveToolsPing200ResponseResultsLatencies();
      //expect(instance).to.be();
    });

    it('should have the property maximum (base name: "maximum")', function() {
      // uncomment below and update the code to test the property maximum
      //var instance = new MerakiDashboardApi.GetDeviceLiveToolsPing200ResponseResultsLatencies();
      //expect(instance).to.be();
    });

    it('should have the property minimum (base name: "minimum")', function() {
      // uncomment below and update the code to test the property minimum
      //var instance = new MerakiDashboardApi.GetDeviceLiveToolsPing200ResponseResultsLatencies();
      //expect(instance).to.be();
    });

  });

}));
