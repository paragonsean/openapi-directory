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
    instance = new ObonoRksvApi.Posten();
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

  describe('Posten', function() {
    it('should create an instance of Posten', function() {
      // uncomment below and update the code to test Posten
      //var instance = new ObonoRksvApi.Posten();
      //expect(instance).to.be.a(ObonoRksvApi.Posten);
    });

    it('should have the property bezeichnung (base name: "Bezeichnung")', function() {
      // uncomment below and update the code to test the property bezeichnung
      //var instance = new ObonoRksvApi.Posten();
      //expect(instance).to.be();
    });

    it('should have the property bruttoBetrag (base name: "BruttoBetrag")', function() {
      // uncomment below and update the code to test the property bruttoBetrag
      //var instance = new ObonoRksvApi.Posten();
      //expect(instance).to.be();
    });

    it('should have the property externerBelegBelegkreis (base name: "Externer-Beleg-Belegkreis")', function() {
      // uncomment below and update the code to test the property externerBelegBelegkreis
      //var instance = new ObonoRksvApi.Posten();
      //expect(instance).to.be();
    });

    it('should have the property externerBelegBezeichnung (base name: "Externer-Beleg-Bezeichnung")', function() {
      // uncomment below and update the code to test the property externerBelegBezeichnung
      //var instance = new ObonoRksvApi.Posten();
      //expect(instance).to.be();
    });

    it('should have the property externerBelegReferenz (base name: "Externer-Beleg-Referenz")', function() {
      // uncomment below and update the code to test the property externerBelegReferenz
      //var instance = new ObonoRksvApi.Posten();
      //expect(instance).to.be();
    });

    it('should have the property menge (base name: "Menge")', function() {
      // uncomment below and update the code to test the property menge
      //var instance = new ObonoRksvApi.Posten();
      //expect(instance).to.be();
    });

    it('should have the property nettoBetrag (base name: "NettoBetrag")', function() {
      // uncomment below and update the code to test the property nettoBetrag
      //var instance = new ObonoRksvApi.Posten();
      //expect(instance).to.be();
    });

    it('should have the property satz (base name: "Satz")', function() {
      // uncomment below and update the code to test the property satz
      //var instance = new ObonoRksvApi.Posten();
      //expect(instance).to.be();
    });

  });

}));
