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
    instance = new TurbineLabsApi.DomainFilter();
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

  describe('DomainFilter', function() {
    it('should create an instance of DomainFilter', function() {
      // uncomment below and update the code to test DomainFilter
      //var instance = new TurbineLabsApi.DomainFilter();
      //expect(instance).to.be.a(TurbineLabsApi.DomainFilter);
    });

    it('should have the property domainKey (base name: "domain_key")', function() {
      // uncomment below and update the code to test the property domainKey
      //var instance = new TurbineLabsApi.DomainFilter();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new TurbineLabsApi.DomainFilter();
      //expect(instance).to.be();
    });

    it('should have the property proxyKeys (base name: "proxy_keys")', function() {
      // uncomment below and update the code to test the property proxyKeys
      //var instance = new TurbineLabsApi.DomainFilter();
      //expect(instance).to.be();
    });

    it('should have the property zoneKey (base name: "zone_key")', function() {
      // uncomment below and update the code to test the property zoneKey
      //var instance = new TurbineLabsApi.DomainFilter();
      //expect(instance).to.be();
    });

  });

}));
