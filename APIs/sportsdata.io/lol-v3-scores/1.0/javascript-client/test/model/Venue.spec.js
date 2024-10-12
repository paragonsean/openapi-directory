/**
 * LoL v3 Scores
 * LoL v3 Scores
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
    factory(root.expect, root.LoLV3Scores);
  }
}(this, function(expect, LoLV3Scores) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new LoLV3Scores.Venue();
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

  describe('Venue', function() {
    it('should create an instance of Venue', function() {
      // uncomment below and update the code to test Venue
      //var instance = new LoLV3Scores.Venue();
      //expect(instance).to.be.a(LoLV3Scores.Venue);
    });

    it('should have the property address (base name: "Address")', function() {
      // uncomment below and update the code to test the property address
      //var instance = new LoLV3Scores.Venue();
      //expect(instance).to.be();
    });

    it('should have the property capacity (base name: "Capacity")', function() {
      // uncomment below and update the code to test the property capacity
      //var instance = new LoLV3Scores.Venue();
      //expect(instance).to.be();
    });

    it('should have the property city (base name: "City")', function() {
      // uncomment below and update the code to test the property city
      //var instance = new LoLV3Scores.Venue();
      //expect(instance).to.be();
    });

    it('should have the property country (base name: "Country")', function() {
      // uncomment below and update the code to test the property country
      //var instance = new LoLV3Scores.Venue();
      //expect(instance).to.be();
    });

    it('should have the property geoLat (base name: "GeoLat")', function() {
      // uncomment below and update the code to test the property geoLat
      //var instance = new LoLV3Scores.Venue();
      //expect(instance).to.be();
    });

    it('should have the property geoLong (base name: "GeoLong")', function() {
      // uncomment below and update the code to test the property geoLong
      //var instance = new LoLV3Scores.Venue();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "Name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new LoLV3Scores.Venue();
      //expect(instance).to.be();
    });

    it('should have the property nickname1 (base name: "Nickname1")', function() {
      // uncomment below and update the code to test the property nickname1
      //var instance = new LoLV3Scores.Venue();
      //expect(instance).to.be();
    });

    it('should have the property nickname2 (base name: "Nickname2")', function() {
      // uncomment below and update the code to test the property nickname2
      //var instance = new LoLV3Scores.Venue();
      //expect(instance).to.be();
    });

    it('should have the property open (base name: "Open")', function() {
      // uncomment below and update the code to test the property open
      //var instance = new LoLV3Scores.Venue();
      //expect(instance).to.be();
    });

    it('should have the property opened (base name: "Opened")', function() {
      // uncomment below and update the code to test the property opened
      //var instance = new LoLV3Scores.Venue();
      //expect(instance).to.be();
    });

    it('should have the property venueId (base name: "VenueId")', function() {
      // uncomment below and update the code to test the property venueId
      //var instance = new LoLV3Scores.Venue();
      //expect(instance).to.be();
    });

    it('should have the property zip (base name: "Zip")', function() {
      // uncomment below and update the code to test the property zip
      //var instance = new LoLV3Scores.Venue();
      //expect(instance).to.be();
    });

  });

}));
