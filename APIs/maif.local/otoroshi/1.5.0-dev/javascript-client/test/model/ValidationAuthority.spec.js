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
    instance = new OtoroshiAdminApi.ValidationAuthority();
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

  describe('ValidationAuthority', function() {
    it('should create an instance of ValidationAuthority', function() {
      // uncomment below and update the code to test ValidationAuthority
      //var instance = new OtoroshiAdminApi.ValidationAuthority();
      //expect(instance).to.be.a(OtoroshiAdminApi.ValidationAuthority);
    });

    it('should have the property alwaysValid (base name: "alwaysValid")', function() {
      // uncomment below and update the code to test the property alwaysValid
      //var instance = new OtoroshiAdminApi.ValidationAuthority();
      //expect(instance).to.be();
    });

    it('should have the property badTtl (base name: "badTtl")', function() {
      // uncomment below and update the code to test the property badTtl
      //var instance = new OtoroshiAdminApi.ValidationAuthority();
      //expect(instance).to.be();
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new OtoroshiAdminApi.ValidationAuthority();
      //expect(instance).to.be();
    });

    it('should have the property goodTtl (base name: "goodTtl")', function() {
      // uncomment below and update the code to test the property goodTtl
      //var instance = new OtoroshiAdminApi.ValidationAuthority();
      //expect(instance).to.be();
    });

    it('should have the property headers (base name: "headers")', function() {
      // uncomment below and update the code to test the property headers
      //var instance = new OtoroshiAdminApi.ValidationAuthority();
      //expect(instance).to.be();
    });

    it('should have the property host (base name: "host")', function() {
      // uncomment below and update the code to test the property host
      //var instance = new OtoroshiAdminApi.ValidationAuthority();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new OtoroshiAdminApi.ValidationAuthority();
      //expect(instance).to.be();
    });

    it('should have the property method (base name: "method")', function() {
      // uncomment below and update the code to test the property method
      //var instance = new OtoroshiAdminApi.ValidationAuthority();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new OtoroshiAdminApi.ValidationAuthority();
      //expect(instance).to.be();
    });

    it('should have the property noCache (base name: "noCache")', function() {
      // uncomment below and update the code to test the property noCache
      //var instance = new OtoroshiAdminApi.ValidationAuthority();
      //expect(instance).to.be();
    });

    it('should have the property path (base name: "path")', function() {
      // uncomment below and update the code to test the property path
      //var instance = new OtoroshiAdminApi.ValidationAuthority();
      //expect(instance).to.be();
    });

    it('should have the property timeout (base name: "timeout")', function() {
      // uncomment below and update the code to test the property timeout
      //var instance = new OtoroshiAdminApi.ValidationAuthority();
      //expect(instance).to.be();
    });

    it('should have the property url (base name: "url")', function() {
      // uncomment below and update the code to test the property url
      //var instance = new OtoroshiAdminApi.ValidationAuthority();
      //expect(instance).to.be();
    });

  });

}));
