/**
 * LoL v3 Stats
 * LoL v3 Stats
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
    factory(root.expect, root.LoLV3Stats);
  }
}(this, function(expect, LoLV3Stats) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new LoLV3Stats.Player();
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

  describe('Player', function() {
    it('should create an instance of Player', function() {
      // uncomment below and update the code to test Player
      //var instance = new LoLV3Stats.Player();
      //expect(instance).to.be.a(LoLV3Stats.Player);
    });

    it('should have the property birthCity (base name: "BirthCity")', function() {
      // uncomment below and update the code to test the property birthCity
      //var instance = new LoLV3Stats.Player();
      //expect(instance).to.be();
    });

    it('should have the property birthCountry (base name: "BirthCountry")', function() {
      // uncomment below and update the code to test the property birthCountry
      //var instance = new LoLV3Stats.Player();
      //expect(instance).to.be();
    });

    it('should have the property birthDate (base name: "BirthDate")', function() {
      // uncomment below and update the code to test the property birthDate
      //var instance = new LoLV3Stats.Player();
      //expect(instance).to.be();
    });

    it('should have the property commonName (base name: "CommonName")', function() {
      // uncomment below and update the code to test the property commonName
      //var instance = new LoLV3Stats.Player();
      //expect(instance).to.be();
    });

    it('should have the property firstName (base name: "FirstName")', function() {
      // uncomment below and update the code to test the property firstName
      //var instance = new LoLV3Stats.Player();
      //expect(instance).to.be();
    });

    it('should have the property gender (base name: "Gender")', function() {
      // uncomment below and update the code to test the property gender
      //var instance = new LoLV3Stats.Player();
      //expect(instance).to.be();
    });

    it('should have the property lastName (base name: "LastName")', function() {
      // uncomment below and update the code to test the property lastName
      //var instance = new LoLV3Stats.Player();
      //expect(instance).to.be();
    });

    it('should have the property matchName (base name: "MatchName")', function() {
      // uncomment below and update the code to test the property matchName
      //var instance = new LoLV3Stats.Player();
      //expect(instance).to.be();
    });

    it('should have the property nationality (base name: "Nationality")', function() {
      // uncomment below and update the code to test the property nationality
      //var instance = new LoLV3Stats.Player();
      //expect(instance).to.be();
    });

    it('should have the property playerId (base name: "PlayerId")', function() {
      // uncomment below and update the code to test the property playerId
      //var instance = new LoLV3Stats.Player();
      //expect(instance).to.be();
    });

    it('should have the property position (base name: "Position")', function() {
      // uncomment below and update the code to test the property position
      //var instance = new LoLV3Stats.Player();
      //expect(instance).to.be();
    });

    it('should have the property updated (base name: "Updated")', function() {
      // uncomment below and update the code to test the property updated
      //var instance = new LoLV3Stats.Player();
      //expect(instance).to.be();
    });

  });

}));
