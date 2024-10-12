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
    instance = new VocaDbWeb.UserForApiContract();
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

  describe('UserForApiContract', function() {
    it('should create an instance of UserForApiContract', function() {
      // uncomment below and update the code to test UserForApiContract
      //var instance = new VocaDbWeb.UserForApiContract();
      //expect(instance).to.be.a(VocaDbWeb.UserForApiContract);
    });

    it('should have the property active (base name: "active")', function() {
      // uncomment below and update the code to test the property active
      //var instance = new VocaDbWeb.UserForApiContract();
      //expect(instance).to.be();
    });

    it('should have the property groupId (base name: "groupId")', function() {
      // uncomment below and update the code to test the property groupId
      //var instance = new VocaDbWeb.UserForApiContract();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new VocaDbWeb.UserForApiContract();
      //expect(instance).to.be();
    });

    it('should have the property knownLanguages (base name: "knownLanguages")', function() {
      // uncomment below and update the code to test the property knownLanguages
      //var instance = new VocaDbWeb.UserForApiContract();
      //expect(instance).to.be();
    });

    it('should have the property mainPicture (base name: "mainPicture")', function() {
      // uncomment below and update the code to test the property mainPicture
      //var instance = new VocaDbWeb.UserForApiContract();
      //expect(instance).to.be();
    });

    it('should have the property memberSince (base name: "memberSince")', function() {
      // uncomment below and update the code to test the property memberSince
      //var instance = new VocaDbWeb.UserForApiContract();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new VocaDbWeb.UserForApiContract();
      //expect(instance).to.be();
    });

    it('should have the property oldUsernames (base name: "oldUsernames")', function() {
      // uncomment below and update the code to test the property oldUsernames
      //var instance = new VocaDbWeb.UserForApiContract();
      //expect(instance).to.be();
    });

    it('should have the property verifiedArtist (base name: "verifiedArtist")', function() {
      // uncomment below and update the code to test the property verifiedArtist
      //var instance = new VocaDbWeb.UserForApiContract();
      //expect(instance).to.be();
    });

  });

}));
