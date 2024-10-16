/**
 * CS:GO v3 Scores
 * CS:GO v3 Scores
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
    factory(root.expect, root.CsgoV3Scores);
  }
}(this, function(expect, CsgoV3Scores) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new CsgoV3Scores.CompetitionDetail();
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

  describe('CompetitionDetail', function() {
    it('should create an instance of CompetitionDetail', function() {
      // uncomment below and update the code to test CompetitionDetail
      //var instance = new CsgoV3Scores.CompetitionDetail();
      //expect(instance).to.be.a(CsgoV3Scores.CompetitionDetail);
    });

    it('should have the property areaId (base name: "AreaId")', function() {
      // uncomment below and update the code to test the property areaId
      //var instance = new CsgoV3Scores.CompetitionDetail();
      //expect(instance).to.be();
    });

    it('should have the property areaName (base name: "AreaName")', function() {
      // uncomment below and update the code to test the property areaName
      //var instance = new CsgoV3Scores.CompetitionDetail();
      //expect(instance).to.be();
    });

    it('should have the property competitionId (base name: "CompetitionId")', function() {
      // uncomment below and update the code to test the property competitionId
      //var instance = new CsgoV3Scores.CompetitionDetail();
      //expect(instance).to.be();
    });

    it('should have the property currentSeason (base name: "CurrentSeason")', function() {
      // uncomment below and update the code to test the property currentSeason
      //var instance = new CsgoV3Scores.CompetitionDetail();
      //expect(instance).to.be();
    });

    it('should have the property format (base name: "Format")', function() {
      // uncomment below and update the code to test the property format
      //var instance = new CsgoV3Scores.CompetitionDetail();
      //expect(instance).to.be();
    });

    it('should have the property games (base name: "Games")', function() {
      // uncomment below and update the code to test the property games
      //var instance = new CsgoV3Scores.CompetitionDetail();
      //expect(instance).to.be();
    });

    it('should have the property gender (base name: "Gender")', function() {
      // uncomment below and update the code to test the property gender
      //var instance = new CsgoV3Scores.CompetitionDetail();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "Name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new CsgoV3Scores.CompetitionDetail();
      //expect(instance).to.be();
    });

    it('should have the property playerStatsCoverage (base name: "PlayerStatsCoverage")', function() {
      // uncomment below and update the code to test the property playerStatsCoverage
      //var instance = new CsgoV3Scores.CompetitionDetail();
      //expect(instance).to.be();
    });

    it('should have the property seasons (base name: "Seasons")', function() {
      // uncomment below and update the code to test the property seasons
      //var instance = new CsgoV3Scores.CompetitionDetail();
      //expect(instance).to.be();
    });

    it('should have the property teams (base name: "Teams")', function() {
      // uncomment below and update the code to test the property teams
      //var instance = new CsgoV3Scores.CompetitionDetail();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "Type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new CsgoV3Scores.CompetitionDetail();
      //expect(instance).to.be();
    });

  });

}));
