/**
 * Bufferapp
 * Social media management for marketers and agencies
 *
 * The version of the OpenAPI document: 1
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
    factory(root.expect, root.Bufferapp);
  }
}(this, function(expect, Bufferapp) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new Bufferapp.ConfigurationServicesFacebookTypes();
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

  describe('ConfigurationServicesFacebookTypes', function() {
    it('should create an instance of ConfigurationServicesFacebookTypes', function() {
      // uncomment below and update the code to test ConfigurationServicesFacebookTypes
      //var instance = new Bufferapp.ConfigurationServicesFacebookTypes();
      //expect(instance).to.be.a(Bufferapp.ConfigurationServicesFacebookTypes);
    });

    it('should have the property group (base name: "group")', function() {
      // uncomment below and update the code to test the property group
      //var instance = new Bufferapp.ConfigurationServicesFacebookTypes();
      //expect(instance).to.be();
    });

    it('should have the property page (base name: "page")', function() {
      // uncomment below and update the code to test the property page
      //var instance = new Bufferapp.ConfigurationServicesFacebookTypes();
      //expect(instance).to.be();
    });

    it('should have the property profile (base name: "profile")', function() {
      // uncomment below and update the code to test the property profile
      //var instance = new Bufferapp.ConfigurationServicesFacebookTypes();
      //expect(instance).to.be();
    });

  });

}));
