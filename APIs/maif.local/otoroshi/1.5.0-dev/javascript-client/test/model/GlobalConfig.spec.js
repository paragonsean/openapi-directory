/**
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
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
    factory(root.expect, root.OtoroshiAdminApi);
  }
}(this, function(expect, OtoroshiAdminApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new OtoroshiAdminApi.GlobalConfig();
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

  describe('GlobalConfig', function() {
    it('should create an instance of GlobalConfig', function() {
      // uncomment below and update the code to test GlobalConfig
      //var instance = new OtoroshiAdminApi.GlobalConfig();
      //expect(instance).to.be.a(OtoroshiAdminApi.GlobalConfig);
    });

    it('should have the property alertsEmails (base name: "alertsEmails")', function() {
      // uncomment below and update the code to test the property alertsEmails
      //var instance = new OtoroshiAdminApi.GlobalConfig();
      //expect(instance).to.be();
    });

    it('should have the property alertsWebhooks (base name: "alertsWebhooks")', function() {
      // uncomment below and update the code to test the property alertsWebhooks
      //var instance = new OtoroshiAdminApi.GlobalConfig();
      //expect(instance).to.be();
    });

    it('should have the property analyticsWebhooks (base name: "analyticsWebhooks")', function() {
      // uncomment below and update the code to test the property analyticsWebhooks
      //var instance = new OtoroshiAdminApi.GlobalConfig();
      //expect(instance).to.be();
    });

    it('should have the property apiReadOnly (base name: "apiReadOnly")', function() {
      // uncomment below and update the code to test the property apiReadOnly
      //var instance = new OtoroshiAdminApi.GlobalConfig();
      //expect(instance).to.be();
    });

    it('should have the property autoLinkToDefaultGroup (base name: "autoLinkToDefaultGroup")', function() {
      // uncomment below and update the code to test the property autoLinkToDefaultGroup
      //var instance = new OtoroshiAdminApi.GlobalConfig();
      //expect(instance).to.be();
    });

    it('should have the property backofficeAuth0Config (base name: "backofficeAuth0Config")', function() {
      // uncomment below and update the code to test the property backofficeAuth0Config
      //var instance = new OtoroshiAdminApi.GlobalConfig();
      //expect(instance).to.be();
    });

    it('should have the property cleverSettings (base name: "cleverSettings")', function() {
      // uncomment below and update the code to test the property cleverSettings
      //var instance = new OtoroshiAdminApi.GlobalConfig();
      //expect(instance).to.be();
    });

    it('should have the property elasticReadsConfig (base name: "elasticReadsConfig")', function() {
      // uncomment below and update the code to test the property elasticReadsConfig
      //var instance = new OtoroshiAdminApi.GlobalConfig();
      //expect(instance).to.be();
    });

    it('should have the property elasticWritesConfigs (base name: "elasticWritesConfigs")', function() {
      // uncomment below and update the code to test the property elasticWritesConfigs
      //var instance = new OtoroshiAdminApi.GlobalConfig();
      //expect(instance).to.be();
    });

    it('should have the property endlessIpAddresses (base name: "endlessIpAddresses")', function() {
      // uncomment below and update the code to test the property endlessIpAddresses
      //var instance = new OtoroshiAdminApi.GlobalConfig();
      //expect(instance).to.be();
    });

    it('should have the property ipFiltering (base name: "ipFiltering")', function() {
      // uncomment below and update the code to test the property ipFiltering
      //var instance = new OtoroshiAdminApi.GlobalConfig();
      //expect(instance).to.be();
    });

    it('should have the property limitConcurrentRequests (base name: "limitConcurrentRequests")', function() {
      // uncomment below and update the code to test the property limitConcurrentRequests
      //var instance = new OtoroshiAdminApi.GlobalConfig();
      //expect(instance).to.be();
    });

    it('should have the property lines (base name: "lines")', function() {
      // uncomment below and update the code to test the property lines
      //var instance = new OtoroshiAdminApi.GlobalConfig();
      //expect(instance).to.be();
    });

    it('should have the property mailerSettings (base name: "mailerSettings")', function() {
      // uncomment below and update the code to test the property mailerSettings
      //var instance = new OtoroshiAdminApi.GlobalConfig();
      //expect(instance).to.be();
    });

    it('should have the property maxConcurrentRequests (base name: "maxConcurrentRequests")', function() {
      // uncomment below and update the code to test the property maxConcurrentRequests
      //var instance = new OtoroshiAdminApi.GlobalConfig();
      //expect(instance).to.be();
    });

    it('should have the property maxHttp10ResponseSize (base name: "maxHttp10ResponseSize")', function() {
      // uncomment below and update the code to test the property maxHttp10ResponseSize
      //var instance = new OtoroshiAdminApi.GlobalConfig();
      //expect(instance).to.be();
    });

    it('should have the property maxLogsSize (base name: "maxLogsSize")', function() {
      // uncomment below and update the code to test the property maxLogsSize
      //var instance = new OtoroshiAdminApi.GlobalConfig();
      //expect(instance).to.be();
    });

    it('should have the property middleFingers (base name: "middleFingers")', function() {
      // uncomment below and update the code to test the property middleFingers
      //var instance = new OtoroshiAdminApi.GlobalConfig();
      //expect(instance).to.be();
    });

    it('should have the property perIpThrottlingQuota (base name: "perIpThrottlingQuota")', function() {
      // uncomment below and update the code to test the property perIpThrottlingQuota
      //var instance = new OtoroshiAdminApi.GlobalConfig();
      //expect(instance).to.be();
    });

    it('should have the property privateAppsAuth0Config (base name: "privateAppsAuth0Config")', function() {
      // uncomment below and update the code to test the property privateAppsAuth0Config
      //var instance = new OtoroshiAdminApi.GlobalConfig();
      //expect(instance).to.be();
    });

    it('should have the property streamEntityOnly (base name: "streamEntityOnly")', function() {
      // uncomment below and update the code to test the property streamEntityOnly
      //var instance = new OtoroshiAdminApi.GlobalConfig();
      //expect(instance).to.be();
    });

    it('should have the property throttlingQuota (base name: "throttlingQuota")', function() {
      // uncomment below and update the code to test the property throttlingQuota
      //var instance = new OtoroshiAdminApi.GlobalConfig();
      //expect(instance).to.be();
    });

    it('should have the property u2fLoginOnly (base name: "u2fLoginOnly")', function() {
      // uncomment below and update the code to test the property u2fLoginOnly
      //var instance = new OtoroshiAdminApi.GlobalConfig();
      //expect(instance).to.be();
    });

    it('should have the property useCircuitBreakers (base name: "useCircuitBreakers")', function() {
      // uncomment below and update the code to test the property useCircuitBreakers
      //var instance = new OtoroshiAdminApi.GlobalConfig();
      //expect(instance).to.be();
    });

  });

}));
