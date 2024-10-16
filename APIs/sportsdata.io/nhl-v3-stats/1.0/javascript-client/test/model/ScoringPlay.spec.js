/**
 * NHL v3 Stats
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
    factory(root.expect, root.NhlV3Stats);
  }
}(this, function(expect, NhlV3Stats) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NhlV3Stats.ScoringPlay();
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

  describe('ScoringPlay', function() {
    it('should create an instance of ScoringPlay', function() {
      // uncomment below and update the code to test ScoringPlay
      //var instance = new NhlV3Stats.ScoringPlay();
      //expect(instance).to.be.a(NhlV3Stats.ScoringPlay);
    });

    it('should have the property allowedByTeamID (base name: "AllowedByTeamID")', function() {
      // uncomment below and update the code to test the property allowedByTeamID
      //var instance = new NhlV3Stats.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property assistedByPlayerID1 (base name: "AssistedByPlayerID1")', function() {
      // uncomment below and update the code to test the property assistedByPlayerID1
      //var instance = new NhlV3Stats.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property assistedByPlayerID2 (base name: "AssistedByPlayerID2")', function() {
      // uncomment below and update the code to test the property assistedByPlayerID2
      //var instance = new NhlV3Stats.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property awayTeamScore (base name: "AwayTeamScore")', function() {
      // uncomment below and update the code to test the property awayTeamScore
      //var instance = new NhlV3Stats.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property emptyNet (base name: "EmptyNet")', function() {
      // uncomment below and update the code to test the property emptyNet
      //var instance = new NhlV3Stats.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property homeTeamScore (base name: "HomeTeamScore")', function() {
      // uncomment below and update the code to test the property homeTeamScore
      //var instance = new NhlV3Stats.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property periodID (base name: "PeriodID")', function() {
      // uncomment below and update the code to test the property periodID
      //var instance = new NhlV3Stats.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property powerPlay (base name: "PowerPlay")', function() {
      // uncomment below and update the code to test the property powerPlay
      //var instance = new NhlV3Stats.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property scoredByPlayerID (base name: "ScoredByPlayerID")', function() {
      // uncomment below and update the code to test the property scoredByPlayerID
      //var instance = new NhlV3Stats.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property scoredByTeamID (base name: "ScoredByTeamID")', function() {
      // uncomment below and update the code to test the property scoredByTeamID
      //var instance = new NhlV3Stats.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property scoringPlayID (base name: "ScoringPlayID")', function() {
      // uncomment below and update the code to test the property scoringPlayID
      //var instance = new NhlV3Stats.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property sequence (base name: "Sequence")', function() {
      // uncomment below and update the code to test the property sequence
      //var instance = new NhlV3Stats.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property shortHanded (base name: "ShortHanded")', function() {
      // uncomment below and update the code to test the property shortHanded
      //var instance = new NhlV3Stats.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property timeRemainingMinutes (base name: "TimeRemainingMinutes")', function() {
      // uncomment below and update the code to test the property timeRemainingMinutes
      //var instance = new NhlV3Stats.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property timeRemainingSeconds (base name: "TimeRemainingSeconds")', function() {
      // uncomment below and update the code to test the property timeRemainingSeconds
      //var instance = new NhlV3Stats.ScoringPlay();
      //expect(instance).to.be();
    });

  });

}));
