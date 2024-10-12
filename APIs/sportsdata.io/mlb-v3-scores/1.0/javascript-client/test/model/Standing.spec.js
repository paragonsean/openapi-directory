/**
 * MLB v3 Scores
 * MLB scores API.
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
    factory(root.expect, root.MlbV3Scores);
  }
}(this, function(expect, MlbV3Scores) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MlbV3Scores.Standing();
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

  describe('Standing', function() {
    it('should create an instance of Standing', function() {
      // uncomment below and update the code to test Standing
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be.a(MlbV3Scores.Standing);
    });

    it('should have the property awayLosses (base name: "AwayLosses")', function() {
      // uncomment below and update the code to test the property awayLosses
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property awayWins (base name: "AwayWins")', function() {
      // uncomment below and update the code to test the property awayWins
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property city (base name: "City")', function() {
      // uncomment below and update the code to test the property city
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property dayLosses (base name: "DayLosses")', function() {
      // uncomment below and update the code to test the property dayLosses
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property dayWins (base name: "DayWins")', function() {
      // uncomment below and update the code to test the property dayWins
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property division (base name: "Division")', function() {
      // uncomment below and update the code to test the property division
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property divisionLosses (base name: "DivisionLosses")', function() {
      // uncomment below and update the code to test the property divisionLosses
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property divisionRank (base name: "DivisionRank")', function() {
      // uncomment below and update the code to test the property divisionRank
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property divisionWins (base name: "DivisionWins")', function() {
      // uncomment below and update the code to test the property divisionWins
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property gamesBehind (base name: "GamesBehind")', function() {
      // uncomment below and update the code to test the property gamesBehind
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property globalTeamID (base name: "GlobalTeamID")', function() {
      // uncomment below and update the code to test the property globalTeamID
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property homeLosses (base name: "HomeLosses")', function() {
      // uncomment below and update the code to test the property homeLosses
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property homeWins (base name: "HomeWins")', function() {
      // uncomment below and update the code to test the property homeWins
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property key (base name: "Key")', function() {
      // uncomment below and update the code to test the property key
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property lastTenGamesLosses (base name: "LastTenGamesLosses")', function() {
      // uncomment below and update the code to test the property lastTenGamesLosses
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property lastTenGamesWins (base name: "LastTenGamesWins")', function() {
      // uncomment below and update the code to test the property lastTenGamesWins
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property league (base name: "League")', function() {
      // uncomment below and update the code to test the property league
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property leagueRank (base name: "LeagueRank")', function() {
      // uncomment below and update the code to test the property leagueRank
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property losses (base name: "Losses")', function() {
      // uncomment below and update the code to test the property losses
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "Name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property nightLosses (base name: "NightLosses")', function() {
      // uncomment below and update the code to test the property nightLosses
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property nightWins (base name: "NightWins")', function() {
      // uncomment below and update the code to test the property nightWins
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property percentage (base name: "Percentage")', function() {
      // uncomment below and update the code to test the property percentage
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property runsAgainst (base name: "RunsAgainst")', function() {
      // uncomment below and update the code to test the property runsAgainst
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property runsScored (base name: "RunsScored")', function() {
      // uncomment below and update the code to test the property runsScored
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property season (base name: "Season")', function() {
      // uncomment below and update the code to test the property season
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property seasonType (base name: "SeasonType")', function() {
      // uncomment below and update the code to test the property seasonType
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property streak (base name: "Streak")', function() {
      // uncomment below and update the code to test the property streak
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property teamID (base name: "TeamID")', function() {
      // uncomment below and update the code to test the property teamID
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property wildCardGamesBehind (base name: "WildCardGamesBehind")', function() {
      // uncomment below and update the code to test the property wildCardGamesBehind
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property wildCardRank (base name: "WildCardRank")', function() {
      // uncomment below and update the code to test the property wildCardRank
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

    it('should have the property wins (base name: "Wins")', function() {
      // uncomment below and update the code to test the property wins
      //var instance = new MlbV3Scores.Standing();
      //expect(instance).to.be();
    });

  });

}));
