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
    instance = new MesheryApi.Plugin();
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

  describe('Plugin', function() {
    it('should create an instance of Plugin', function() {
      // uncomment below and update the code to test Plugin
      //var instance = new MesheryApi.Plugin();
      //expect(instance).to.be.a(MesheryApi.Plugin);
    });

    it('should have the property config (base name: "Config")', function() {
      // uncomment below and update the code to test the property config
      //var instance = new MesheryApi.Plugin();
      //expect(instance).to.be();
    });

    it('should have the property enabled (base name: "Enabled")', function() {
      // uncomment below and update the code to test the property enabled
      //var instance = new MesheryApi.Plugin();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "Id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new MesheryApi.Plugin();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "Name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new MesheryApi.Plugin();
      //expect(instance).to.be();
    });

    it('should have the property pluginReference (base name: "PluginReference")', function() {
      // uncomment below and update the code to test the property pluginReference
      //var instance = new MesheryApi.Plugin();
      //expect(instance).to.be();
    });

    it('should have the property settings (base name: "Settings")', function() {
      // uncomment below and update the code to test the property settings
      //var instance = new MesheryApi.Plugin();
      //expect(instance).to.be();
    });

  });

}));
