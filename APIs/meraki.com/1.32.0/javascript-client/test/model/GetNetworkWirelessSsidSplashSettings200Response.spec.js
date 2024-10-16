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
    instance = new MerakiDashboardApi.GetNetworkWirelessSsidSplashSettings200Response();
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

  describe('GetNetworkWirelessSsidSplashSettings200Response', function() {
    it('should create an instance of GetNetworkWirelessSsidSplashSettings200Response', function() {
      // uncomment below and update the code to test GetNetworkWirelessSsidSplashSettings200Response
      //var instance = new MerakiDashboardApi.GetNetworkWirelessSsidSplashSettings200Response();
      //expect(instance).to.be.a(MerakiDashboardApi.GetNetworkWirelessSsidSplashSettings200Response);
    });

    it('should have the property allowSimultaneousLogins (base name: "allowSimultaneousLogins")', function() {
      // uncomment below and update the code to test the property allowSimultaneousLogins
      //var instance = new MerakiDashboardApi.GetNetworkWirelessSsidSplashSettings200Response();
      //expect(instance).to.be();
    });

    it('should have the property billing (base name: "billing")', function() {
      // uncomment below and update the code to test the property billing
      //var instance = new MerakiDashboardApi.GetNetworkWirelessSsidSplashSettings200Response();
      //expect(instance).to.be();
    });

    it('should have the property blockAllTrafficBeforeSignOn (base name: "blockAllTrafficBeforeSignOn")', function() {
      // uncomment below and update the code to test the property blockAllTrafficBeforeSignOn
      //var instance = new MerakiDashboardApi.GetNetworkWirelessSsidSplashSettings200Response();
      //expect(instance).to.be();
    });

    it('should have the property controllerDisconnectionBehavior (base name: "controllerDisconnectionBehavior")', function() {
      // uncomment below and update the code to test the property controllerDisconnectionBehavior
      //var instance = new MerakiDashboardApi.GetNetworkWirelessSsidSplashSettings200Response();
      //expect(instance).to.be();
    });

    it('should have the property guestSponsorship (base name: "guestSponsorship")', function() {
      // uncomment below and update the code to test the property guestSponsorship
      //var instance = new MerakiDashboardApi.GetNetworkWirelessSsidSplashSettings200Response();
      //expect(instance).to.be();
    });

    it('should have the property redirectUrl (base name: "redirectUrl")', function() {
      // uncomment below and update the code to test the property redirectUrl
      //var instance = new MerakiDashboardApi.GetNetworkWirelessSsidSplashSettings200Response();
      //expect(instance).to.be();
    });

    it('should have the property selfRegistration (base name: "selfRegistration")', function() {
      // uncomment below and update the code to test the property selfRegistration
      //var instance = new MerakiDashboardApi.GetNetworkWirelessSsidSplashSettings200Response();
      //expect(instance).to.be();
    });

    it('should have the property sentryEnrollment (base name: "sentryEnrollment")', function() {
      // uncomment below and update the code to test the property sentryEnrollment
      //var instance = new MerakiDashboardApi.GetNetworkWirelessSsidSplashSettings200Response();
      //expect(instance).to.be();
    });

    it('should have the property splashImage (base name: "splashImage")', function() {
      // uncomment below and update the code to test the property splashImage
      //var instance = new MerakiDashboardApi.GetNetworkWirelessSsidSplashSettings200Response();
      //expect(instance).to.be();
    });

    it('should have the property splashLogo (base name: "splashLogo")', function() {
      // uncomment below and update the code to test the property splashLogo
      //var instance = new MerakiDashboardApi.GetNetworkWirelessSsidSplashSettings200Response();
      //expect(instance).to.be();
    });

    it('should have the property splashPage (base name: "splashPage")', function() {
      // uncomment below and update the code to test the property splashPage
      //var instance = new MerakiDashboardApi.GetNetworkWirelessSsidSplashSettings200Response();
      //expect(instance).to.be();
    });

    it('should have the property splashPrepaidFront (base name: "splashPrepaidFront")', function() {
      // uncomment below and update the code to test the property splashPrepaidFront
      //var instance = new MerakiDashboardApi.GetNetworkWirelessSsidSplashSettings200Response();
      //expect(instance).to.be();
    });

    it('should have the property splashTimeout (base name: "splashTimeout")', function() {
      // uncomment below and update the code to test the property splashTimeout
      //var instance = new MerakiDashboardApi.GetNetworkWirelessSsidSplashSettings200Response();
      //expect(instance).to.be();
    });

    it('should have the property splashUrl (base name: "splashUrl")', function() {
      // uncomment below and update the code to test the property splashUrl
      //var instance = new MerakiDashboardApi.GetNetworkWirelessSsidSplashSettings200Response();
      //expect(instance).to.be();
    });

    it('should have the property ssidNumber (base name: "ssidNumber")', function() {
      // uncomment below and update the code to test the property ssidNumber
      //var instance = new MerakiDashboardApi.GetNetworkWirelessSsidSplashSettings200Response();
      //expect(instance).to.be();
    });

    it('should have the property useRedirectUrl (base name: "useRedirectUrl")', function() {
      // uncomment below and update the code to test the property useRedirectUrl
      //var instance = new MerakiDashboardApi.GetNetworkWirelessSsidSplashSettings200Response();
      //expect(instance).to.be();
    });

    it('should have the property useSplashUrl (base name: "useSplashUrl")', function() {
      // uncomment below and update the code to test the property useSplashUrl
      //var instance = new MerakiDashboardApi.GetNetworkWirelessSsidSplashSettings200Response();
      //expect(instance).to.be();
    });

    it('should have the property welcomeMessage (base name: "welcomeMessage")', function() {
      // uncomment below and update the code to test the property welcomeMessage
      //var instance = new MerakiDashboardApi.GetNetworkWirelessSsidSplashSettings200Response();
      //expect(instance).to.be();
    });

  });

}));
