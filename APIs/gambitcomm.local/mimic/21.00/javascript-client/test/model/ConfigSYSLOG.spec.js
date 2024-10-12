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
    instance = new MimicRestApi.ConfigSYSLOG();
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

  describe('ConfigSYSLOG', function() {
    it('should create an instance of ConfigSYSLOG', function() {
      // uncomment below and update the code to test ConfigSYSLOG
      //var instance = new MimicRestApi.ConfigSYSLOG();
      //expect(instance).to.be.a(MimicRestApi.ConfigSYSLOG);
    });

    it('should have the property client (base name: "client")', function() {
      // uncomment below and update the code to test the property client
      //var instance = new MimicRestApi.ConfigSYSLOG();
      //expect(instance).to.be();
    });

    it('should have the property hostname (base name: "hostname")', function() {
      // uncomment below and update the code to test the property hostname
      //var instance = new MimicRestApi.ConfigSYSLOG();
      //expect(instance).to.be();
    });

    it('should have the property localport (base name: "localport")', function() {
      // uncomment below and update the code to test the property localport
      //var instance = new MimicRestApi.ConfigSYSLOG();
      //expect(instance).to.be();
    });

    it('should have the property separator (base name: "separator")', function() {
      // uncomment below and update the code to test the property separator
      //var instance = new MimicRestApi.ConfigSYSLOG();
      //expect(instance).to.be();
    });

    it('should have the property sequence (base name: "sequence")', function() {
      // uncomment below and update the code to test the property sequence
      //var instance = new MimicRestApi.ConfigSYSLOG();
      //expect(instance).to.be();
    });

    it('should have the property server (base name: "server")', function() {
      // uncomment below and update the code to test the property server
      //var instance = new MimicRestApi.ConfigSYSLOG();
      //expect(instance).to.be();
    });

    it('should have the property serverport (base name: "serverport")', function() {
      // uncomment below and update the code to test the property serverport
      //var instance = new MimicRestApi.ConfigSYSLOG();
      //expect(instance).to.be();
    });

    it('should have the property timestamp (base name: "timestamp")', function() {
      // uncomment below and update the code to test the property timestamp
      //var instance = new MimicRestApi.ConfigSYSLOG();
      //expect(instance).to.be();
    });

  });

}));
