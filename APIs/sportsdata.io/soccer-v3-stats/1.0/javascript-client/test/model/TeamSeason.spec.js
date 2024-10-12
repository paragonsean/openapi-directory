/**
 * Soccer v3 Stats
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
    factory(root.expect, root.SoccerV3Stats);
  }
}(this, function(expect, SoccerV3Stats) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new SoccerV3Stats.TeamSeason();
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
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be.a(SoccerV3Stats.TeamSeason);
    });

    it('should have the property assists (base name: "Assists")', function() {
      // uncomment below and update the code to test the property assists
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property blockedShots (base name: "BlockedShots")', function() {
      // uncomment below and update the code to test the property blockedShots
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property cornersWon (base name: "CornersWon")', function() {
      // uncomment below and update the code to test the property cornersWon
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property crosses (base name: "Crosses")', function() {
      // uncomment below and update the code to test the property crosses
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property defenderCleanSheets (base name: "DefenderCleanSheets")', function() {
      // uncomment below and update the code to test the property defenderCleanSheets
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPoints (base name: "FantasyPoints")', function() {
      // uncomment below and update the code to test the property fantasyPoints
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPointsDraftKings (base name: "FantasyPointsDraftKings")', function() {
      // uncomment below and update the code to test the property fantasyPointsDraftKings
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPointsFanDuel (base name: "FantasyPointsFanDuel")', function() {
      // uncomment below and update the code to test the property fantasyPointsFanDuel
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPointsMondogoal (base name: "FantasyPointsMondogoal")', function() {
      // uncomment below and update the code to test the property fantasyPointsMondogoal
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPointsYahoo (base name: "FantasyPointsYahoo")', function() {
      // uncomment below and update the code to test the property fantasyPointsYahoo
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property fouled (base name: "Fouled")', function() {
      // uncomment below and update the code to test the property fouled
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property fouls (base name: "Fouls")', function() {
      // uncomment below and update the code to test the property fouls
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property games (base name: "Games")', function() {
      // uncomment below and update the code to test the property games
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property globalTeamId (base name: "GlobalTeamId")', function() {
      // uncomment below and update the code to test the property globalTeamId
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property goalkeeperCleanSheets (base name: "GoalkeeperCleanSheets")', function() {
      // uncomment below and update the code to test the property goalkeeperCleanSheets
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property goalkeeperGoalsAgainst (base name: "GoalkeeperGoalsAgainst")', function() {
      // uncomment below and update the code to test the property goalkeeperGoalsAgainst
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property goalkeeperSaves (base name: "GoalkeeperSaves")', function() {
      // uncomment below and update the code to test the property goalkeeperSaves
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property goalkeeperSingleGoalAgainst (base name: "GoalkeeperSingleGoalAgainst")', function() {
      // uncomment below and update the code to test the property goalkeeperSingleGoalAgainst
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property goalkeeperWins (base name: "GoalkeeperWins")', function() {
      // uncomment below and update the code to test the property goalkeeperWins
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property goals (base name: "Goals")', function() {
      // uncomment below and update the code to test the property goals
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property interceptions (base name: "Interceptions")', function() {
      // uncomment below and update the code to test the property interceptions
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property lastManTackle (base name: "LastManTackle")', function() {
      // uncomment below and update the code to test the property lastManTackle
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property minutes (base name: "Minutes")', function() {
      // uncomment below and update the code to test the property minutes
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "Name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property offsides (base name: "Offsides")', function() {
      // uncomment below and update the code to test the property offsides
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property opponentScore (base name: "OpponentScore")', function() {
      // uncomment below and update the code to test the property opponentScore
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property ownGoals (base name: "OwnGoals")', function() {
      // uncomment below and update the code to test the property ownGoals
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property passes (base name: "Passes")', function() {
      // uncomment below and update the code to test the property passes
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property passesCompleted (base name: "PassesCompleted")', function() {
      // uncomment below and update the code to test the property passesCompleted
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property penaltiesConceded (base name: "PenaltiesConceded")', function() {
      // uncomment below and update the code to test the property penaltiesConceded
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property penaltiesWon (base name: "PenaltiesWon")', function() {
      // uncomment below and update the code to test the property penaltiesWon
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property penaltyKickGoals (base name: "PenaltyKickGoals")', function() {
      // uncomment below and update the code to test the property penaltyKickGoals
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property penaltyKickMisses (base name: "PenaltyKickMisses")', function() {
      // uncomment below and update the code to test the property penaltyKickMisses
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property penaltyKickSaves (base name: "PenaltyKickSaves")', function() {
      // uncomment below and update the code to test the property penaltyKickSaves
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property possession (base name: "Possession")', function() {
      // uncomment below and update the code to test the property possession
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property redCards (base name: "RedCards")', function() {
      // uncomment below and update the code to test the property redCards
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property roundId (base name: "RoundId")', function() {
      // uncomment below and update the code to test the property roundId
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property score (base name: "Score")', function() {
      // uncomment below and update the code to test the property score
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property season (base name: "Season")', function() {
      // uncomment below and update the code to test the property season
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property seasonType (base name: "SeasonType")', function() {
      // uncomment below and update the code to test the property seasonType
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property shots (base name: "Shots")', function() {
      // uncomment below and update the code to test the property shots
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property shotsOnGoal (base name: "ShotsOnGoal")', function() {
      // uncomment below and update the code to test the property shotsOnGoal
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property statId (base name: "StatId")', function() {
      // uncomment below and update the code to test the property statId
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property tackles (base name: "Tackles")', function() {
      // uncomment below and update the code to test the property tackles
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property tacklesWon (base name: "TacklesWon")', function() {
      // uncomment below and update the code to test the property tacklesWon
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property team (base name: "Team")', function() {
      // uncomment below and update the code to test the property team
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property teamId (base name: "TeamId")', function() {
      // uncomment below and update the code to test the property teamId
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property touches (base name: "Touches")', function() {
      // uncomment below and update the code to test the property touches
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property updated (base name: "Updated")', function() {
      // uncomment below and update the code to test the property updated
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property updatedUtc (base name: "UpdatedUtc")', function() {
      // uncomment below and update the code to test the property updatedUtc
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property yellowCards (base name: "YellowCards")', function() {
      // uncomment below and update the code to test the property yellowCards
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

    it('should have the property yellowRedCards (base name: "YellowRedCards")', function() {
      // uncomment below and update the code to test the property yellowRedCards
      //var instance = new SoccerV3Stats.TeamSeason();
      //expect(instance).to.be();
    });

  });

}));
