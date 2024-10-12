/**
 * CBB v3 Scores
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
    factory(root.expect, root.CbbV3Scores);
  }
}(this, function(expect, CbbV3Scores) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new CbbV3Scores.ScoreBasic();
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

  describe('ScoreBasic', function() {
    it('should create an instance of ScoreBasic', function() {
      // uncomment below and update the code to test ScoreBasic
      //var instance = new CbbV3Scores.ScoreBasic();
      //expect(instance).to.be.a(CbbV3Scores.ScoreBasic);
    });

    it('should have the property awayTeam (base name: "AwayTeam")', function() {
      // uncomment below and update the code to test the property awayTeam
      //var instance = new CbbV3Scores.ScoreBasic();
      //expect(instance).to.be();
    });

    it('should have the property awayTeamID (base name: "AwayTeamID")', function() {
      // uncomment below and update the code to test the property awayTeamID
      //var instance = new CbbV3Scores.ScoreBasic();
      //expect(instance).to.be();
    });

    it('should have the property awayTeamScore (base name: "AwayTeamScore")', function() {
      // uncomment below and update the code to test the property awayTeamScore
      //var instance = new CbbV3Scores.ScoreBasic();
      //expect(instance).to.be();
    });

    it('should have the property awayTeamSeed (base name: "AwayTeamSeed")', function() {
      // uncomment below and update the code to test the property awayTeamSeed
      //var instance = new CbbV3Scores.ScoreBasic();
      //expect(instance).to.be();
    });

    it('should have the property bracket (base name: "Bracket")', function() {
      // uncomment below and update the code to test the property bracket
      //var instance = new CbbV3Scores.ScoreBasic();
      //expect(instance).to.be();
    });

    it('should have the property dateTime (base name: "DateTime")', function() {
      // uncomment below and update the code to test the property dateTime
      //var instance = new CbbV3Scores.ScoreBasic();
      //expect(instance).to.be();
    });

    it('should have the property dateTimeUTC (base name: "DateTimeUTC")', function() {
      // uncomment below and update the code to test the property dateTimeUTC
      //var instance = new CbbV3Scores.ScoreBasic();
      //expect(instance).to.be();
    });

    it('should have the property day (base name: "Day")', function() {
      // uncomment below and update the code to test the property day
      //var instance = new CbbV3Scores.ScoreBasic();
      //expect(instance).to.be();
    });

    it('should have the property gameEndDateTime (base name: "GameEndDateTime")', function() {
      // uncomment below and update the code to test the property gameEndDateTime
      //var instance = new CbbV3Scores.ScoreBasic();
      //expect(instance).to.be();
    });

    it('should have the property gameID (base name: "GameID")', function() {
      // uncomment below and update the code to test the property gameID
      //var instance = new CbbV3Scores.ScoreBasic();
      //expect(instance).to.be();
    });

    it('should have the property homeTeam (base name: "HomeTeam")', function() {
      // uncomment below and update the code to test the property homeTeam
      //var instance = new CbbV3Scores.ScoreBasic();
      //expect(instance).to.be();
    });

    it('should have the property homeTeamID (base name: "HomeTeamID")', function() {
      // uncomment below and update the code to test the property homeTeamID
      //var instance = new CbbV3Scores.ScoreBasic();
      //expect(instance).to.be();
    });

    it('should have the property homeTeamScore (base name: "HomeTeamScore")', function() {
      // uncomment below and update the code to test the property homeTeamScore
      //var instance = new CbbV3Scores.ScoreBasic();
      //expect(instance).to.be();
    });

    it('should have the property homeTeamSeed (base name: "HomeTeamSeed")', function() {
      // uncomment below and update the code to test the property homeTeamSeed
      //var instance = new CbbV3Scores.ScoreBasic();
      //expect(instance).to.be();
    });

    it('should have the property isClosed (base name: "IsClosed")', function() {
      // uncomment below and update the code to test the property isClosed
      //var instance = new CbbV3Scores.ScoreBasic();
      //expect(instance).to.be();
    });

    it('should have the property neutralVenue (base name: "NeutralVenue")', function() {
      // uncomment below and update the code to test the property neutralVenue
      //var instance = new CbbV3Scores.ScoreBasic();
      //expect(instance).to.be();
    });

    it('should have the property round (base name: "Round")', function() {
      // uncomment below and update the code to test the property round
      //var instance = new CbbV3Scores.ScoreBasic();
      //expect(instance).to.be();
    });

    it('should have the property season (base name: "Season")', function() {
      // uncomment below and update the code to test the property season
      //var instance = new CbbV3Scores.ScoreBasic();
      //expect(instance).to.be();
    });

    it('should have the property seasonType (base name: "SeasonType")', function() {
      // uncomment below and update the code to test the property seasonType
      //var instance = new CbbV3Scores.ScoreBasic();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "Status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new CbbV3Scores.ScoreBasic();
      //expect(instance).to.be();
    });

    it('should have the property tournamentID (base name: "TournamentID")', function() {
      // uncomment below and update the code to test the property tournamentID
      //var instance = new CbbV3Scores.ScoreBasic();
      //expect(instance).to.be();
    });

    it('should have the property updated (base name: "Updated")', function() {
      // uncomment below and update the code to test the property updated
      //var instance = new CbbV3Scores.ScoreBasic();
      //expect(instance).to.be();
    });

  });

}));
