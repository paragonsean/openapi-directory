/**
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
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
    factory(root.expect, root.VocaDbWeb);
  }
}(this, function(expect, VocaDbWeb) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new VocaDbWeb.ArtistForSongContract();
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

  describe('ArtistForSongContract', function() {
    it('should create an instance of ArtistForSongContract', function() {
      // uncomment below and update the code to test ArtistForSongContract
      //var instance = new VocaDbWeb.ArtistForSongContract();
      //expect(instance).to.be.a(VocaDbWeb.ArtistForSongContract);
    });

    it('should have the property artist (base name: "artist")', function() {
      // uncomment below and update the code to test the property artist
      //var instance = new VocaDbWeb.ArtistForSongContract();
      //expect(instance).to.be();
    });

    it('should have the property categories (base name: "categories")', function() {
      // uncomment below and update the code to test the property categories
      //var instance = new VocaDbWeb.ArtistForSongContract();
      //expect(instance).to.be();
    });

    it('should have the property effectiveRoles (base name: "effectiveRoles")', function() {
      // uncomment below and update the code to test the property effectiveRoles
      //var instance = new VocaDbWeb.ArtistForSongContract();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new VocaDbWeb.ArtistForSongContract();
      //expect(instance).to.be();
    });

    it('should have the property isCustomName (base name: "isCustomName")', function() {
      // uncomment below and update the code to test the property isCustomName
      //var instance = new VocaDbWeb.ArtistForSongContract();
      //expect(instance).to.be();
    });

    it('should have the property isSupport (base name: "isSupport")', function() {
      // uncomment below and update the code to test the property isSupport
      //var instance = new VocaDbWeb.ArtistForSongContract();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new VocaDbWeb.ArtistForSongContract();
      //expect(instance).to.be();
    });

    it('should have the property roles (base name: "roles")', function() {
      // uncomment below and update the code to test the property roles
      //var instance = new VocaDbWeb.ArtistForSongContract();
      //expect(instance).to.be();
    });

  });

}));
