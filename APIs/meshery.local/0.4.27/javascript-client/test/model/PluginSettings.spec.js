/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
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
    factory(root.expect, root.MesheryApi);
  }
}(this, function(expect, MesheryApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MesheryApi.PluginSettings();
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

  describe('PluginSettings', function() {
    it('should create an instance of PluginSettings', function() {
      // uncomment below and update the code to test PluginSettings
      //var instance = new MesheryApi.PluginSettings();
      //expect(instance).to.be.a(MesheryApi.PluginSettings);
    });

    it('should have the property args (base name: "Args")', function() {
      // uncomment below and update the code to test the property args
      //var instance = new MesheryApi.PluginSettings();
      //expect(instance).to.be();
    });

    it('should have the property devices (base name: "Devices")', function() {
      // uncomment below and update the code to test the property devices
      //var instance = new MesheryApi.PluginSettings();
      //expect(instance).to.be();
    });

    it('should have the property env (base name: "Env")', function() {
      // uncomment below and update the code to test the property env
      //var instance = new MesheryApi.PluginSettings();
      //expect(instance).to.be();
    });

    it('should have the property mounts (base name: "Mounts")', function() {
      // uncomment below and update the code to test the property mounts
      //var instance = new MesheryApi.PluginSettings();
      //expect(instance).to.be();
    });

  });

}));
