/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 23 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 0.0.0-streaming
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
    instance = new MerakiDashboardApi.UpdateNetworkClientSplashAuthorizationStatusRequestSsids();
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

  describe('UpdateNetworkClientSplashAuthorizationStatusRequestSsids', function() {
    it('should create an instance of UpdateNetworkClientSplashAuthorizationStatusRequestSsids', function() {
      // uncomment below and update the code to test UpdateNetworkClientSplashAuthorizationStatusRequestSsids
      //var instance = new MerakiDashboardApi.UpdateNetworkClientSplashAuthorizationStatusRequestSsids();
      //expect(instance).to.be.a(MerakiDashboardApi.UpdateNetworkClientSplashAuthorizationStatusRequestSsids);
    });

    it('should have the property _0 (base name: "0")', function() {
      // uncomment below and update the code to test the property _0
      //var instance = new MerakiDashboardApi.UpdateNetworkClientSplashAuthorizationStatusRequestSsids();
      //expect(instance).to.be();
    });

    it('should have the property _1 (base name: "1")', function() {
      // uncomment below and update the code to test the property _1
      //var instance = new MerakiDashboardApi.UpdateNetworkClientSplashAuthorizationStatusRequestSsids();
      //expect(instance).to.be();
    });

    it('should have the property _2 (base name: "2")', function() {
      // uncomment below and update the code to test the property _2
      //var instance = new MerakiDashboardApi.UpdateNetworkClientSplashAuthorizationStatusRequestSsids();
      //expect(instance).to.be();
    });

    it('should have the property _3 (base name: "3")', function() {
      // uncomment below and update the code to test the property _3
      //var instance = new MerakiDashboardApi.UpdateNetworkClientSplashAuthorizationStatusRequestSsids();
      //expect(instance).to.be();
    });

    it('should have the property _4 (base name: "4")', function() {
      // uncomment below and update the code to test the property _4
      //var instance = new MerakiDashboardApi.UpdateNetworkClientSplashAuthorizationStatusRequestSsids();
      //expect(instance).to.be();
    });

    it('should have the property _5 (base name: "5")', function() {
      // uncomment below and update the code to test the property _5
      //var instance = new MerakiDashboardApi.UpdateNetworkClientSplashAuthorizationStatusRequestSsids();
      //expect(instance).to.be();
    });

    it('should have the property _6 (base name: "6")', function() {
      // uncomment below and update the code to test the property _6
      //var instance = new MerakiDashboardApi.UpdateNetworkClientSplashAuthorizationStatusRequestSsids();
      //expect(instance).to.be();
    });

    it('should have the property _7 (base name: "7")', function() {
      // uncomment below and update the code to test the property _7
      //var instance = new MerakiDashboardApi.UpdateNetworkClientSplashAuthorizationStatusRequestSsids();
      //expect(instance).to.be();
    });

    it('should have the property _8 (base name: "8")', function() {
      // uncomment below and update the code to test the property _8
      //var instance = new MerakiDashboardApi.UpdateNetworkClientSplashAuthorizationStatusRequestSsids();
      //expect(instance).to.be();
    });

    it('should have the property _9 (base name: "9")', function() {
      // uncomment below and update the code to test the property _9
      //var instance = new MerakiDashboardApi.UpdateNetworkClientSplashAuthorizationStatusRequestSsids();
      //expect(instance).to.be();
    });

    it('should have the property _10 (base name: "10")', function() {
      // uncomment below and update the code to test the property _10
      //var instance = new MerakiDashboardApi.UpdateNetworkClientSplashAuthorizationStatusRequestSsids();
      //expect(instance).to.be();
    });

    it('should have the property _11 (base name: "11")', function() {
      // uncomment below and update the code to test the property _11
      //var instance = new MerakiDashboardApi.UpdateNetworkClientSplashAuthorizationStatusRequestSsids();
      //expect(instance).to.be();
    });

    it('should have the property _12 (base name: "12")', function() {
      // uncomment below and update the code to test the property _12
      //var instance = new MerakiDashboardApi.UpdateNetworkClientSplashAuthorizationStatusRequestSsids();
      //expect(instance).to.be();
    });

    it('should have the property _13 (base name: "13")', function() {
      // uncomment below and update the code to test the property _13
      //var instance = new MerakiDashboardApi.UpdateNetworkClientSplashAuthorizationStatusRequestSsids();
      //expect(instance).to.be();
    });

    it('should have the property _14 (base name: "14")', function() {
      // uncomment below and update the code to test the property _14
      //var instance = new MerakiDashboardApi.UpdateNetworkClientSplashAuthorizationStatusRequestSsids();
      //expect(instance).to.be();
    });

  });

}));
