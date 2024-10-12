/**
 * NHL v3 Scores
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
    factory(root.expect, root.NhlV3Scores);
  }
}(this, function(expect, NhlV3Scores) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NhlV3Scores.OpponentSeason();
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

  describe('OpponentSeason', function() {
    it('should create an instance of OpponentSeason', function() {
      // uncomment below and update the code to test OpponentSeason
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be.a(NhlV3Scores.OpponentSeason);
    });

    it('should have the property assists (base name: "Assists")', function() {
      // uncomment below and update the code to test the property assists
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property benchPenaltyMinutes (base name: "BenchPenaltyMinutes")', function() {
      // uncomment below and update the code to test the property benchPenaltyMinutes
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property blocks (base name: "Blocks")', function() {
      // uncomment below and update the code to test the property blocks
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property emptyNetGoals (base name: "EmptyNetGoals")', function() {
      // uncomment below and update the code to test the property emptyNetGoals
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property faceoffsLost (base name: "FaceoffsLost")', function() {
      // uncomment below and update the code to test the property faceoffsLost
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property faceoffsWon (base name: "FaceoffsWon")', function() {
      // uncomment below and update the code to test the property faceoffsWon
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPoints (base name: "FantasyPoints")', function() {
      // uncomment below and update the code to test the property fantasyPoints
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPointsDraftKings (base name: "FantasyPointsDraftKings")', function() {
      // uncomment below and update the code to test the property fantasyPointsDraftKings
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPointsFanDuel (base name: "FantasyPointsFanDuel")', function() {
      // uncomment below and update the code to test the property fantasyPointsFanDuel
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPointsFantasyDraft (base name: "FantasyPointsFantasyDraft")', function() {
      // uncomment below and update the code to test the property fantasyPointsFantasyDraft
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPointsYahoo (base name: "FantasyPointsYahoo")', function() {
      // uncomment below and update the code to test the property fantasyPointsYahoo
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property games (base name: "Games")', function() {
      // uncomment below and update the code to test the property games
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property giveaways (base name: "Giveaways")', function() {
      // uncomment below and update the code to test the property giveaways
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property globalTeamID (base name: "GlobalTeamID")', function() {
      // uncomment below and update the code to test the property globalTeamID
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property goals (base name: "Goals")', function() {
      // uncomment below and update the code to test the property goals
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property goaltendingGoalsAgainst (base name: "GoaltendingGoalsAgainst")', function() {
      // uncomment below and update the code to test the property goaltendingGoalsAgainst
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property goaltendingLosses (base name: "GoaltendingLosses")', function() {
      // uncomment below and update the code to test the property goaltendingLosses
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property goaltendingMinutes (base name: "GoaltendingMinutes")', function() {
      // uncomment below and update the code to test the property goaltendingMinutes
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property goaltendingOvertimeLosses (base name: "GoaltendingOvertimeLosses")', function() {
      // uncomment below and update the code to test the property goaltendingOvertimeLosses
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property goaltendingSaves (base name: "GoaltendingSaves")', function() {
      // uncomment below and update the code to test the property goaltendingSaves
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property goaltendingSeconds (base name: "GoaltendingSeconds")', function() {
      // uncomment below and update the code to test the property goaltendingSeconds
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property goaltendingShotsAgainst (base name: "GoaltendingShotsAgainst")', function() {
      // uncomment below and update the code to test the property goaltendingShotsAgainst
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property goaltendingShutouts (base name: "GoaltendingShutouts")', function() {
      // uncomment below and update the code to test the property goaltendingShutouts
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property goaltendingWins (base name: "GoaltendingWins")', function() {
      // uncomment below and update the code to test the property goaltendingWins
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property hatTricks (base name: "HatTricks")', function() {
      // uncomment below and update the code to test the property hatTricks
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property hits (base name: "Hits")', function() {
      // uncomment below and update the code to test the property hits
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property losses (base name: "Losses")', function() {
      // uncomment below and update the code to test the property losses
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property minutes (base name: "Minutes")', function() {
      // uncomment below and update the code to test the property minutes
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "Name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property opponentPosition (base name: "OpponentPosition")', function() {
      // uncomment below and update the code to test the property opponentPosition
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property overtimeLosses (base name: "OvertimeLosses")', function() {
      // uncomment below and update the code to test the property overtimeLosses
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property penaltyMinutes (base name: "PenaltyMinutes")', function() {
      // uncomment below and update the code to test the property penaltyMinutes
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property plusMinus (base name: "PlusMinus")', function() {
      // uncomment below and update the code to test the property plusMinus
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property powerPlayAssists (base name: "PowerPlayAssists")', function() {
      // uncomment below and update the code to test the property powerPlayAssists
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property powerPlayGoals (base name: "PowerPlayGoals")', function() {
      // uncomment below and update the code to test the property powerPlayGoals
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property season (base name: "Season")', function() {
      // uncomment below and update the code to test the property season
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property seasonType (base name: "SeasonType")', function() {
      // uncomment below and update the code to test the property seasonType
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property seconds (base name: "Seconds")', function() {
      // uncomment below and update the code to test the property seconds
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property shifts (base name: "Shifts")', function() {
      // uncomment below and update the code to test the property shifts
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property shootoutGoals (base name: "ShootoutGoals")', function() {
      // uncomment below and update the code to test the property shootoutGoals
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property shortHandedAssists (base name: "ShortHandedAssists")', function() {
      // uncomment below and update the code to test the property shortHandedAssists
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property shortHandedGoals (base name: "ShortHandedGoals")', function() {
      // uncomment below and update the code to test the property shortHandedGoals
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property shotsOnGoal (base name: "ShotsOnGoal")', function() {
      // uncomment below and update the code to test the property shotsOnGoal
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property started (base name: "Started")', function() {
      // uncomment below and update the code to test the property started
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property statID (base name: "StatID")', function() {
      // uncomment below and update the code to test the property statID
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property takeaways (base name: "Takeaways")', function() {
      // uncomment below and update the code to test the property takeaways
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property team (base name: "Team")', function() {
      // uncomment below and update the code to test the property team
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property teamID (base name: "TeamID")', function() {
      // uncomment below and update the code to test the property teamID
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property updated (base name: "Updated")', function() {
      // uncomment below and update the code to test the property updated
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

    it('should have the property wins (base name: "Wins")', function() {
      // uncomment below and update the code to test the property wins
      //var instance = new NhlV3Scores.OpponentSeason();
      //expect(instance).to.be();
    });

  });

}));
