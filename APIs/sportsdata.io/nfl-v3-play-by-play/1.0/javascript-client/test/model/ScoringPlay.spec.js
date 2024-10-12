/**
 * NFL v3 Play-by-Play
 * NFL play-by-play API.
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
    factory(root.expect, root.NflV3PlayByPlay);
  }
}(this, function(expect, NflV3PlayByPlay) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NflV3PlayByPlay.ScoringPlay();
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
      //var instance = new NflV3PlayByPlay.ScoringPlay();
      //expect(instance).to.be.a(NflV3PlayByPlay.ScoringPlay);
    });

    it('should have the property awayScore (base name: "AwayScore")', function() {
      // uncomment below and update the code to test the property awayScore
      //var instance = new NflV3PlayByPlay.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property awayTeam (base name: "AwayTeam")', function() {
      // uncomment below and update the code to test the property awayTeam
      //var instance = new NflV3PlayByPlay.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property date (base name: "Date")', function() {
      // uncomment below and update the code to test the property date
      //var instance = new NflV3PlayByPlay.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property gameKey (base name: "GameKey")', function() {
      // uncomment below and update the code to test the property gameKey
      //var instance = new NflV3PlayByPlay.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property homeScore (base name: "HomeScore")', function() {
      // uncomment below and update the code to test the property homeScore
      //var instance = new NflV3PlayByPlay.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property homeTeam (base name: "HomeTeam")', function() {
      // uncomment below and update the code to test the property homeTeam
      //var instance = new NflV3PlayByPlay.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property playDescription (base name: "PlayDescription")', function() {
      // uncomment below and update the code to test the property playDescription
      //var instance = new NflV3PlayByPlay.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property quarter (base name: "Quarter")', function() {
      // uncomment below and update the code to test the property quarter
      //var instance = new NflV3PlayByPlay.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property scoreID (base name: "ScoreID")', function() {
      // uncomment below and update the code to test the property scoreID
      //var instance = new NflV3PlayByPlay.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property scoringPlayID (base name: "ScoringPlayID")', function() {
      // uncomment below and update the code to test the property scoringPlayID
      //var instance = new NflV3PlayByPlay.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property season (base name: "Season")', function() {
      // uncomment below and update the code to test the property season
      //var instance = new NflV3PlayByPlay.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property seasonType (base name: "SeasonType")', function() {
      // uncomment below and update the code to test the property seasonType
      //var instance = new NflV3PlayByPlay.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property sequence (base name: "Sequence")', function() {
      // uncomment below and update the code to test the property sequence
      //var instance = new NflV3PlayByPlay.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property team (base name: "Team")', function() {
      // uncomment below and update the code to test the property team
      //var instance = new NflV3PlayByPlay.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property timeRemaining (base name: "TimeRemaining")', function() {
      // uncomment below and update the code to test the property timeRemaining
      //var instance = new NflV3PlayByPlay.ScoringPlay();
      //expect(instance).to.be();
    });

    it('should have the property week (base name: "Week")', function() {
      // uncomment below and update the code to test the property week
      //var instance = new NflV3PlayByPlay.ScoringPlay();
      //expect(instance).to.be();
    });

  });

}));
