/**
 * obono RKSV API
 * Provides a RESTful API for interacting with virtual cash registers and creating receipts that are conform with the Registrierkassensicherheitsverordnung (RKSV).  You may find our [automatically generated clients](./clients) for various programming languages and environments helpful... 
 *
 * The version of the OpenAPI document: 1.4.0.0
 * Contact: info@obono.at
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
    factory(root.expect, root.ObonoRksvApi);
  }
}(this, function(expect, ObonoRksvApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new ObonoRksvApi.Belege();
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

  describe('Belege', function() {
    it('should create an instance of Belege', function() {
      // uncomment below and update the code to test Belege
      //var instance = new ObonoRksvApi.Belege();
      //expect(instance).to.be.a(ObonoRksvApi.Belege);
    });

    it('should have the property belege (base name: "Belege")', function() {
      // uncomment below and update the code to test the property belege
      //var instance = new ObonoRksvApi.Belege();
      //expect(instance).to.be();
    });

    it('should have the property belegeGruppe (base name: "Belege-Gruppe")', function() {
      // uncomment below and update the code to test the property belegeGruppe
      //var instance = new ObonoRksvApi.Belege();
      //expect(instance).to.be();
    });

  });

}));
