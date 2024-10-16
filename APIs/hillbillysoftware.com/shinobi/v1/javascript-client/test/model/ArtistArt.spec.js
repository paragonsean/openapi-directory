/**
 * shinobiapi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
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
    factory(root.expect, root.Shinobiapi);
  }
}(this, function(expect, Shinobiapi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new Shinobiapi.ArtistArt();
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

  describe('ArtistArt', function() {
    it('should create an instance of ArtistArt', function() {
      // uncomment below and update the code to test ArtistArt
      //var instance = new Shinobiapi.ArtistArt();
      //expect(instance).to.be.a(Shinobiapi.ArtistArt);
    });

    it('should have the property artistID (base name: "ArtistID")', function() {
      // uncomment below and update the code to test the property artistID
      //var instance = new Shinobiapi.ArtistArt();
      //expect(instance).to.be();
    });

    it('should have the property banner (base name: "Banner")', function() {
      // uncomment below and update the code to test the property banner
      //var instance = new Shinobiapi.ArtistArt();
      //expect(instance).to.be();
    });

    it('should have the property logo (base name: "Logo")', function() {
      // uncomment below and update the code to test the property logo
      //var instance = new Shinobiapi.ArtistArt();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "Name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new Shinobiapi.ArtistArt();
      //expect(instance).to.be();
    });

  });

}));
