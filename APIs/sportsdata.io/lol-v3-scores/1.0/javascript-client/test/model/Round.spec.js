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
    instance = new LoLV3Scores.Round();
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

  describe('Round', function() {
    it('should create an instance of Round', function() {
      // uncomment below and update the code to test Round
      //var instance = new LoLV3Scores.Round();
      //expect(instance).to.be.a(LoLV3Scores.Round);
    });

    it('should have the property currentRound (base name: "CurrentRound")', function() {
      // uncomment below and update the code to test the property currentRound
      //var instance = new LoLV3Scores.Round();
      //expect(instance).to.be();
    });

    it('should have the property currentWeek (base name: "CurrentWeek")', function() {
      // uncomment below and update the code to test the property currentWeek
      //var instance = new LoLV3Scores.Round();
      //expect(instance).to.be();
    });

    it('should have the property endDate (base name: "EndDate")', function() {
      // uncomment below and update the code to test the property endDate
      //var instance = new LoLV3Scores.Round();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "Name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new LoLV3Scores.Round();
      //expect(instance).to.be();
    });

    it('should have the property roundId (base name: "RoundId")', function() {
      // uncomment below and update the code to test the property roundId
      //var instance = new LoLV3Scores.Round();
      //expect(instance).to.be();
    });

    it('should have the property season (base name: "Season")', function() {
      // uncomment below and update the code to test the property season
      //var instance = new LoLV3Scores.Round();
      //expect(instance).to.be();
    });

    it('should have the property seasonId (base name: "SeasonId")', function() {
      // uncomment below and update the code to test the property seasonId
      //var instance = new LoLV3Scores.Round();
      //expect(instance).to.be();
    });

    it('should have the property seasonType (base name: "SeasonType")', function() {
      // uncomment below and update the code to test the property seasonType
      //var instance = new LoLV3Scores.Round();
      //expect(instance).to.be();
    });

    it('should have the property startDate (base name: "StartDate")', function() {
      // uncomment below and update the code to test the property startDate
      //var instance = new LoLV3Scores.Round();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "Type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new LoLV3Scores.Round();
      //expect(instance).to.be();
    });

  });

}));
