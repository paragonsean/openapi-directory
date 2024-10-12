/**
 * MIMIC REST API
 * This is the API for MIMIC client to connect to MIMIC daemon.
 *
 * The version of the OpenAPI document: 21.00
 * Contact: support@gambitcomm.com
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
    factory(root.expect, root.MimicRestApi);
  }
}(this, function(expect, MimicRestApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MimicRestApi.ConfigWEB();
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

  describe('ConfigWEB', function() {
    it('should create an instance of ConfigWEB', function() {
      // uncomment below and update the code to test ConfigWEB
      //var instance = new MimicRestApi.ConfigWEB();
      //expect(instance).to.be.a(MimicRestApi.ConfigWEB);
    });

    it('should have the property isPersistentConnections (base name: "is_persistent_connections")', function() {
      // uncomment below and update the code to test the property isPersistentConnections
      //var instance = new MimicRestApi.ConfigWEB();
      //expect(instance).to.be();
    });

    it('should have the property password (base name: "password")', function() {
      // uncomment below and update the code to test the property password
      //var instance = new MimicRestApi.ConfigWEB();
      //expect(instance).to.be();
    });

    it('should have the property port (base name: "port")', function() {
      // uncomment below and update the code to test the property port
      //var instance = new MimicRestApi.ConfigWEB();
      //expect(instance).to.be();
    });

    it('should have the property rule (base name: "rule")', function() {
      // uncomment below and update the code to test the property rule
      //var instance = new MimicRestApi.ConfigWEB();
      //expect(instance).to.be();
    });

    it('should have the property username (base name: "username")', function() {
      // uncomment below and update the code to test the property username
      //var instance = new MimicRestApi.ConfigWEB();
      //expect(instance).to.be();
    });

    it('should have the property wsdl (base name: "wsdl")', function() {
      // uncomment below and update the code to test the property wsdl
      //var instance = new MimicRestApi.ConfigWEB();
      //expect(instance).to.be();
    });

  });

}));
