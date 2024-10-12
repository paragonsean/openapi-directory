/**
 * NBA v3 Scores
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
    factory(root.expect, root.NbaV3Scores);
  }
}(this, function(expect, NbaV3Scores) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NbaV3Scores.TeamSeason();
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

  describe('TeamSeason', function() {
    it('should create an instance of TeamSeason', function() {
      // uncomment below and update the code to test TeamSeason
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be.a(NbaV3Scores.TeamSeason);
    });

    it('should have the property assists (base name: "Assists")', function() {
      // uncomment below and update the code to test the property assists
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property assistsPercentage (base name: "AssistsPercentage")', function() {
      // uncomment below and update the code to test the property assistsPercentage
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property blockedShots (base name: "BlockedShots")', function() {
      // uncomment below and update the code to test the property blockedShots
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property blocksPercentage (base name: "BlocksPercentage")', function() {
      // uncomment below and update the code to test the property blocksPercentage
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property defensiveRebounds (base name: "DefensiveRebounds")', function() {
      // uncomment below and update the code to test the property defensiveRebounds
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property defensiveReboundsPercentage (base name: "DefensiveReboundsPercentage")', function() {
      // uncomment below and update the code to test the property defensiveReboundsPercentage
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property doubleDoubles (base name: "DoubleDoubles")', function() {
      // uncomment below and update the code to test the property doubleDoubles
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property effectiveFieldGoalsPercentage (base name: "EffectiveFieldGoalsPercentage")', function() {
      // uncomment below and update the code to test the property effectiveFieldGoalsPercentage
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPoints (base name: "FantasyPoints")', function() {
      // uncomment below and update the code to test the property fantasyPoints
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPointsDraftKings (base name: "FantasyPointsDraftKings")', function() {
      // uncomment below and update the code to test the property fantasyPointsDraftKings
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPointsFanDuel (base name: "FantasyPointsFanDuel")', function() {
      // uncomment below and update the code to test the property fantasyPointsFanDuel
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPointsFantasyDraft (base name: "FantasyPointsFantasyDraft")', function() {
      // uncomment below and update the code to test the property fantasyPointsFantasyDraft
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPointsYahoo (base name: "FantasyPointsYahoo")', function() {
      // uncomment below and update the code to test the property fantasyPointsYahoo
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property fieldGoalsAttempted (base name: "FieldGoalsAttempted")', function() {
      // uncomment below and update the code to test the property fieldGoalsAttempted
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property fieldGoalsMade (base name: "FieldGoalsMade")', function() {
      // uncomment below and update the code to test the property fieldGoalsMade
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property fieldGoalsPercentage (base name: "FieldGoalsPercentage")', function() {
      // uncomment below and update the code to test the property fieldGoalsPercentage
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property freeThrowsAttempted (base name: "FreeThrowsAttempted")', function() {
      // uncomment below and update the code to test the property freeThrowsAttempted
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property freeThrowsMade (base name: "FreeThrowsMade")', function() {
      // uncomment below and update the code to test the property freeThrowsMade
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property freeThrowsPercentage (base name: "FreeThrowsPercentage")', function() {
      // uncomment below and update the code to test the property freeThrowsPercentage
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property games (base name: "Games")', function() {
      // uncomment below and update the code to test the property games
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property globalTeamID (base name: "GlobalTeamID")', function() {
      // uncomment below and update the code to test the property globalTeamID
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property isClosed (base name: "IsClosed")', function() {
      // uncomment below and update the code to test the property isClosed
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property lineupConfirmed (base name: "LineupConfirmed")', function() {
      // uncomment below and update the code to test the property lineupConfirmed
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property lineupStatus (base name: "LineupStatus")', function() {
      // uncomment below and update the code to test the property lineupStatus
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property losses (base name: "Losses")', function() {
      // uncomment below and update the code to test the property losses
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property minutes (base name: "Minutes")', function() {
      // uncomment below and update the code to test the property minutes
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "Name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property offensiveRebounds (base name: "OffensiveRebounds")', function() {
      // uncomment below and update the code to test the property offensiveRebounds
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property offensiveReboundsPercentage (base name: "OffensiveReboundsPercentage")', function() {
      // uncomment below and update the code to test the property offensiveReboundsPercentage
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property opponentPosition (base name: "OpponentPosition")', function() {
      // uncomment below and update the code to test the property opponentPosition
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property opponentStat (base name: "OpponentStat")', function() {
      // uncomment below and update the code to test the property opponentStat
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property personalFouls (base name: "PersonalFouls")', function() {
      // uncomment below and update the code to test the property personalFouls
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property playerEfficiencyRating (base name: "PlayerEfficiencyRating")', function() {
      // uncomment below and update the code to test the property playerEfficiencyRating
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property plusMinus (base name: "PlusMinus")', function() {
      // uncomment below and update the code to test the property plusMinus
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property points (base name: "Points")', function() {
      // uncomment below and update the code to test the property points
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property possessions (base name: "Possessions")', function() {
      // uncomment below and update the code to test the property possessions
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property rebounds (base name: "Rebounds")', function() {
      // uncomment below and update the code to test the property rebounds
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property season (base name: "Season")', function() {
      // uncomment below and update the code to test the property season
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property seasonType (base name: "SeasonType")', function() {
      // uncomment below and update the code to test the property seasonType
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property seconds (base name: "Seconds")', function() {
      // uncomment below and update the code to test the property seconds
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property statID (base name: "StatID")', function() {
      // uncomment below and update the code to test the property statID
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property steals (base name: "Steals")', function() {
      // uncomment below and update the code to test the property steals
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property stealsPercentage (base name: "StealsPercentage")', function() {
      // uncomment below and update the code to test the property stealsPercentage
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property team (base name: "Team")', function() {
      // uncomment below and update the code to test the property team
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property teamID (base name: "TeamID")', function() {
      // uncomment below and update the code to test the property teamID
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property threePointersAttempted (base name: "ThreePointersAttempted")', function() {
      // uncomment below and update the code to test the property threePointersAttempted
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property threePointersMade (base name: "ThreePointersMade")', function() {
      // uncomment below and update the code to test the property threePointersMade
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property threePointersPercentage (base name: "ThreePointersPercentage")', function() {
      // uncomment below and update the code to test the property threePointersPercentage
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property totalReboundsPercentage (base name: "TotalReboundsPercentage")', function() {
      // uncomment below and update the code to test the property totalReboundsPercentage
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property tripleDoubles (base name: "TripleDoubles")', function() {
      // uncomment below and update the code to test the property tripleDoubles
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property trueShootingAttempts (base name: "TrueShootingAttempts")', function() {
      // uncomment below and update the code to test the property trueShootingAttempts
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property trueShootingPercentage (base name: "TrueShootingPercentage")', function() {
      // uncomment below and update the code to test the property trueShootingPercentage
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property turnOversPercentage (base name: "TurnOversPercentage")', function() {
      // uncomment below and update the code to test the property turnOversPercentage
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property turnovers (base name: "Turnovers")', function() {
      // uncomment below and update the code to test the property turnovers
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property twoPointersAttempted (base name: "TwoPointersAttempted")', function() {
      // uncomment below and update the code to test the property twoPointersAttempted
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property twoPointersMade (base name: "TwoPointersMade")', function() {
      // uncomment below and update the code to test the property twoPointersMade
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property twoPointersPercentage (base name: "TwoPointersPercentage")', function() {
      // uncomment below and update the code to test the property twoPointersPercentage
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property updated (base name: "Updated")', function() {
      // uncomment below and update the code to test the property updated
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property usageRatePercentage (base name: "UsageRatePercentage")', function() {
      // uncomment below and update the code to test the property usageRatePercentage
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property wins (base name: "Wins")', function() {
      // uncomment below and update the code to test the property wins
      //var instance = new NbaV3Scores.TeamSeason();
      //expect(instance).to.be();
    });

  });

}));
