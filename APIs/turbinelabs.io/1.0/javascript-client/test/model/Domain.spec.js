/**
 * Turbine Labs API
 * The Turbine Labs API provides CRUD operations for core object types, and is mostly RESTy. The easiest way to interact with the API is with [tbnctl](https://docs.turbinelabs.io/advanced/tbnctl.html). If you want to make direct HTTP calls, however, you can obtain an access token using tbnctl, and then pass it in the Authorization header, prefixed by `Token `: ```console curl -H \"Authorization: Token <access token>\" https://api.turbinelabs.io/v1.0/cluster ``` 
 *
 * The version of the OpenAPI document: 1.0
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
    factory(root.expect, root.TurbineLabsApi);
  }
}(this, function(expect, TurbineLabsApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new TurbineLabsApi.Domain();
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

  describe('Domain', function() {
    it('should create an instance of Domain', function() {
      // uncomment below and update the code to test Domain
      //var instance = new TurbineLabsApi.Domain();
      //expect(instance).to.be.a(TurbineLabsApi.Domain);
    });

    it('should have the property aliases (base name: "aliases")', function() {
      // uncomment below and update the code to test the property aliases
      //var instance = new TurbineLabsApi.Domain();
      //expect(instance).to.be();
    });

    it('should have the property checksum (base name: "checksum")', function() {
      // uncomment below and update the code to test the property checksum
      //var instance = new TurbineLabsApi.Domain();
      //expect(instance).to.be();
    });

    it('should have the property corsConfig (base name: "cors_config")', function() {
      // uncomment below and update the code to test the property corsConfig
      //var instance = new TurbineLabsApi.Domain();
      //expect(instance).to.be();
    });

    it('should have the property domainKey (base name: "domain_key")', function() {
      // uncomment below and update the code to test the property domainKey
      //var instance = new TurbineLabsApi.Domain();
      //expect(instance).to.be();
    });

    it('should have the property forceHttps (base name: "force_https")', function() {
      // uncomment below and update the code to test the property forceHttps
      //var instance = new TurbineLabsApi.Domain();
      //expect(instance).to.be();
    });

    it('should have the property gzipEnabled (base name: "gzip_enabled")', function() {
      // uncomment below and update the code to test the property gzipEnabled
      //var instance = new TurbineLabsApi.Domain();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new TurbineLabsApi.Domain();
      //expect(instance).to.be();
    });

    it('should have the property port (base name: "port")', function() {
      // uncomment below and update the code to test the property port
      //var instance = new TurbineLabsApi.Domain();
      //expect(instance).to.be();
    });

    it('should have the property redirects (base name: "redirects")', function() {
      // uncomment below and update the code to test the property redirects
      //var instance = new TurbineLabsApi.Domain();
      //expect(instance).to.be();
    });

    it('should have the property sslConfig (base name: "ssl_config")', function() {
      // uncomment below and update the code to test the property sslConfig
      //var instance = new TurbineLabsApi.Domain();
      //expect(instance).to.be();
    });

    it('should have the property zoneKey (base name: "zone_key")', function() {
      // uncomment below and update the code to test the property zoneKey
      //var instance = new TurbineLabsApi.Domain();
      //expect(instance).to.be();
    });

  });

}));
