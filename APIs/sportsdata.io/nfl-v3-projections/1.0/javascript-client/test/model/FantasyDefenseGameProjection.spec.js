/**
 * NFL v3 Projections
 * NFL projected stats API.
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
    factory(root.expect, root.NflV3Projections);
  }
}(this, function(expect, NflV3Projections) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NflV3Projections.FantasyDefenseGameProjection();
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

  describe('FantasyDefenseGameProjection', function() {
    it('should create an instance of FantasyDefenseGameProjection', function() {
      // uncomment below and update the code to test FantasyDefenseGameProjection
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be.a(NflV3Projections.FantasyDefenseGameProjection);
    });

    it('should have the property assistedTackles (base name: "AssistedTackles")', function() {
      // uncomment below and update the code to test the property assistedTackles
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property blockedKickReturnTouchdowns (base name: "BlockedKickReturnTouchdowns")', function() {
      // uncomment below and update the code to test the property blockedKickReturnTouchdowns
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property blockedKickReturnYards (base name: "BlockedKickReturnYards")', function() {
      // uncomment below and update the code to test the property blockedKickReturnYards
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property blockedKicks (base name: "BlockedKicks")', function() {
      // uncomment below and update the code to test the property blockedKicks
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property date (base name: "Date")', function() {
      // uncomment below and update the code to test the property date
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property dateTime (base name: "DateTime")', function() {
      // uncomment below and update the code to test the property dateTime
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property day (base name: "Day")', function() {
      // uncomment below and update the code to test the property day
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property defensiveTouchdowns (base name: "DefensiveTouchdowns")', function() {
      // uncomment below and update the code to test the property defensiveTouchdowns
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property draftKingsFantasyPointsAllowed (base name: "DraftKingsFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property draftKingsFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property draftKingsKickerFantasyPointsAllowed (base name: "DraftKingsKickerFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property draftKingsKickerFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property draftKingsPosition (base name: "DraftKingsPosition")', function() {
      // uncomment below and update the code to test the property draftKingsPosition
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property draftKingsQuarterbackFantasyPointsAllowed (base name: "DraftKingsQuarterbackFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property draftKingsQuarterbackFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property draftKingsRunningbackFantasyPointsAllowed (base name: "DraftKingsRunningbackFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property draftKingsRunningbackFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property draftKingsSalary (base name: "DraftKingsSalary")', function() {
      // uncomment below and update the code to test the property draftKingsSalary
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property draftKingsTightEndFantasyPointsAllowed (base name: "DraftKingsTightEndFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property draftKingsTightEndFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property draftKingsWideReceiverFantasyPointsAllowed (base name: "DraftKingsWideReceiverFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property draftKingsWideReceiverFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fanDuelFantasyPointsAllowed (base name: "FanDuelFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property fanDuelFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fanDuelKickerFantasyPointsAllowed (base name: "FanDuelKickerFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property fanDuelKickerFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fanDuelPosition (base name: "FanDuelPosition")', function() {
      // uncomment below and update the code to test the property fanDuelPosition
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fanDuelQuarterbackFantasyPointsAllowed (base name: "FanDuelQuarterbackFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property fanDuelQuarterbackFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fanDuelRunningbackFantasyPointsAllowed (base name: "FanDuelRunningbackFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property fanDuelRunningbackFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fanDuelSalary (base name: "FanDuelSalary")', function() {
      // uncomment below and update the code to test the property fanDuelSalary
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fanDuelTightEndFantasyPointsAllowed (base name: "FanDuelTightEndFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property fanDuelTightEndFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fanDuelWideReceiverFantasyPointsAllowed (base name: "FanDuelWideReceiverFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property fanDuelWideReceiverFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fantasyDataSalary (base name: "FantasyDataSalary")', function() {
      // uncomment below and update the code to test the property fantasyDataSalary
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fantasyDefenseID (base name: "FantasyDefenseID")', function() {
      // uncomment below and update the code to test the property fantasyDefenseID
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fantasyDraftFantasyPointsAllowed (base name: "FantasyDraftFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property fantasyDraftFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fantasyDraftKickerFantasyPointsAllowed (base name: "FantasyDraftKickerFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property fantasyDraftKickerFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fantasyDraftPosition (base name: "FantasyDraftPosition")', function() {
      // uncomment below and update the code to test the property fantasyDraftPosition
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fantasyDraftQuarterbackFantasyPointsAllowed (base name: "FantasyDraftQuarterbackFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property fantasyDraftQuarterbackFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fantasyDraftRunningbackFantasyPointsAllowed (base name: "FantasyDraftRunningbackFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property fantasyDraftRunningbackFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fantasyDraftSalary (base name: "FantasyDraftSalary")', function() {
      // uncomment below and update the code to test the property fantasyDraftSalary
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fantasyDraftTightEndFantasyPointsAllowed (base name: "FantasyDraftTightEndFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property fantasyDraftTightEndFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fantasyDraftWideReceiverFantasyPointsAllowed (base name: "FantasyDraftWideReceiverFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property fantasyDraftWideReceiverFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPoints (base name: "FantasyPoints")', function() {
      // uncomment below and update the code to test the property fantasyPoints
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPointsAllowed (base name: "FantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property fantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPointsDraftKings (base name: "FantasyPointsDraftKings")', function() {
      // uncomment below and update the code to test the property fantasyPointsDraftKings
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPointsFanDuel (base name: "FantasyPointsFanDuel")', function() {
      // uncomment below and update the code to test the property fantasyPointsFanDuel
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPointsFantasyDraft (base name: "FantasyPointsFantasyDraft")', function() {
      // uncomment below and update the code to test the property fantasyPointsFantasyDraft
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPointsYahoo (base name: "FantasyPointsYahoo")', function() {
      // uncomment below and update the code to test the property fantasyPointsYahoo
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fieldGoalReturnTouchdowns (base name: "FieldGoalReturnTouchdowns")', function() {
      // uncomment below and update the code to test the property fieldGoalReturnTouchdowns
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fieldGoalReturnYards (base name: "FieldGoalReturnYards")', function() {
      // uncomment below and update the code to test the property fieldGoalReturnYards
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fourthDownAttempts (base name: "FourthDownAttempts")', function() {
      // uncomment below and update the code to test the property fourthDownAttempts
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fourthDownConversions (base name: "FourthDownConversions")', function() {
      // uncomment below and update the code to test the property fourthDownConversions
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fumbleReturnTouchdowns (base name: "FumbleReturnTouchdowns")', function() {
      // uncomment below and update the code to test the property fumbleReturnTouchdowns
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fumbleReturnYards (base name: "FumbleReturnYards")', function() {
      // uncomment below and update the code to test the property fumbleReturnYards
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fumblesForced (base name: "FumblesForced")', function() {
      // uncomment below and update the code to test the property fumblesForced
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property fumblesRecovered (base name: "FumblesRecovered")', function() {
      // uncomment below and update the code to test the property fumblesRecovered
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property gameKey (base name: "GameKey")', function() {
      // uncomment below and update the code to test the property gameKey
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property globalGameID (base name: "GlobalGameID")', function() {
      // uncomment below and update the code to test the property globalGameID
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property globalOpponentID (base name: "GlobalOpponentID")', function() {
      // uncomment below and update the code to test the property globalOpponentID
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property globalTeamID (base name: "GlobalTeamID")', function() {
      // uncomment below and update the code to test the property globalTeamID
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property homeOrAway (base name: "HomeOrAway")', function() {
      // uncomment below and update the code to test the property homeOrAway
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property humidity (base name: "Humidity")', function() {
      // uncomment below and update the code to test the property humidity
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property interceptionReturnTouchdowns (base name: "InterceptionReturnTouchdowns")', function() {
      // uncomment below and update the code to test the property interceptionReturnTouchdowns
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property interceptionReturnYards (base name: "InterceptionReturnYards")', function() {
      // uncomment below and update the code to test the property interceptionReturnYards
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property interceptions (base name: "Interceptions")', function() {
      // uncomment below and update the code to test the property interceptions
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property isGameOver (base name: "IsGameOver")', function() {
      // uncomment below and update the code to test the property isGameOver
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property kickReturnLong (base name: "KickReturnLong")', function() {
      // uncomment below and update the code to test the property kickReturnLong
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property kickReturnTouchdowns (base name: "KickReturnTouchdowns")', function() {
      // uncomment below and update the code to test the property kickReturnTouchdowns
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property kickReturnYards (base name: "KickReturnYards")', function() {
      // uncomment below and update the code to test the property kickReturnYards
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property kickReturns (base name: "KickReturns")', function() {
      // uncomment below and update the code to test the property kickReturns
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property kickerFantasyPointsAllowed (base name: "KickerFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property kickerFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property offensiveYardsAllowed (base name: "OffensiveYardsAllowed")', function() {
      // uncomment below and update the code to test the property offensiveYardsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property opponent (base name: "Opponent")', function() {
      // uncomment below and update the code to test the property opponent
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property opponentID (base name: "OpponentID")', function() {
      // uncomment below and update the code to test the property opponentID
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property opponentPositionRank (base name: "OpponentPositionRank")', function() {
      // uncomment below and update the code to test the property opponentPositionRank
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property opponentRank (base name: "OpponentRank")', function() {
      // uncomment below and update the code to test the property opponentRank
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property passesDefended (base name: "PassesDefended")', function() {
      // uncomment below and update the code to test the property passesDefended
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property playerID (base name: "PlayerID")', function() {
      // uncomment below and update the code to test the property playerID
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property pointsAllowed (base name: "PointsAllowed")', function() {
      // uncomment below and update the code to test the property pointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property pointsAllowedByDefenseSpecialTeams (base name: "PointsAllowedByDefenseSpecialTeams")', function() {
      // uncomment below and update the code to test the property pointsAllowedByDefenseSpecialTeams
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property puntReturnLong (base name: "PuntReturnLong")', function() {
      // uncomment below and update the code to test the property puntReturnLong
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property puntReturnTouchdowns (base name: "PuntReturnTouchdowns")', function() {
      // uncomment below and update the code to test the property puntReturnTouchdowns
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property puntReturnYards (base name: "PuntReturnYards")', function() {
      // uncomment below and update the code to test the property puntReturnYards
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property puntReturns (base name: "PuntReturns")', function() {
      // uncomment below and update the code to test the property puntReturns
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property quarterbackFantasyPointsAllowed (base name: "QuarterbackFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property quarterbackFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property quarterbackHits (base name: "QuarterbackHits")', function() {
      // uncomment below and update the code to test the property quarterbackHits
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property runningbackFantasyPointsAllowed (base name: "RunningbackFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property runningbackFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property sackYards (base name: "SackYards")', function() {
      // uncomment below and update the code to test the property sackYards
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property sacks (base name: "Sacks")', function() {
      // uncomment below and update the code to test the property sacks
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property safeties (base name: "Safeties")', function() {
      // uncomment below and update the code to test the property safeties
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property scoreID (base name: "ScoreID")', function() {
      // uncomment below and update the code to test the property scoreID
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property scoringDetails (base name: "ScoringDetails")', function() {
      // uncomment below and update the code to test the property scoringDetails
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property season (base name: "Season")', function() {
      // uncomment below and update the code to test the property season
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property seasonType (base name: "SeasonType")', function() {
      // uncomment below and update the code to test the property seasonType
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property soloTackles (base name: "SoloTackles")', function() {
      // uncomment below and update the code to test the property soloTackles
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property specialTeamsTouchdowns (base name: "SpecialTeamsTouchdowns")', function() {
      // uncomment below and update the code to test the property specialTeamsTouchdowns
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property stadium (base name: "Stadium")', function() {
      // uncomment below and update the code to test the property stadium
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property tacklesForLoss (base name: "TacklesForLoss")', function() {
      // uncomment below and update the code to test the property tacklesForLoss
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property team (base name: "Team")', function() {
      // uncomment below and update the code to test the property team
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property teamID (base name: "TeamID")', function() {
      // uncomment below and update the code to test the property teamID
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property temperature (base name: "Temperature")', function() {
      // uncomment below and update the code to test the property temperature
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property thirdDownAttempts (base name: "ThirdDownAttempts")', function() {
      // uncomment below and update the code to test the property thirdDownAttempts
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property thirdDownConversions (base name: "ThirdDownConversions")', function() {
      // uncomment below and update the code to test the property thirdDownConversions
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property tightEndFantasyPointsAllowed (base name: "TightEndFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property tightEndFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property touchdownsScored (base name: "TouchdownsScored")', function() {
      // uncomment below and update the code to test the property touchdownsScored
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property twoPointConversionReturns (base name: "TwoPointConversionReturns")', function() {
      // uncomment below and update the code to test the property twoPointConversionReturns
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property victivSalary (base name: "VictivSalary")', function() {
      // uncomment below and update the code to test the property victivSalary
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property week (base name: "Week")', function() {
      // uncomment below and update the code to test the property week
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property wideReceiverFantasyPointsAllowed (base name: "WideReceiverFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property wideReceiverFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property windSpeed (base name: "WindSpeed")', function() {
      // uncomment below and update the code to test the property windSpeed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property yahooFantasyPointsAllowed (base name: "YahooFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property yahooFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property yahooKickerFantasyPointsAllowed (base name: "YahooKickerFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property yahooKickerFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property yahooPosition (base name: "YahooPosition")', function() {
      // uncomment below and update the code to test the property yahooPosition
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property yahooQuarterbackFantasyPointsAllowed (base name: "YahooQuarterbackFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property yahooQuarterbackFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property yahooRunningbackFantasyPointsAllowed (base name: "YahooRunningbackFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property yahooRunningbackFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property yahooSalary (base name: "YahooSalary")', function() {
      // uncomment below and update the code to test the property yahooSalary
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property yahooTightEndFantasyPointsAllowed (base name: "YahooTightEndFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property yahooTightEndFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

    it('should have the property yahooWideReceiverFantasyPointsAllowed (base name: "YahooWideReceiverFantasyPointsAllowed")', function() {
      // uncomment below and update the code to test the property yahooWideReceiverFantasyPointsAllowed
      //var instance = new NflV3Projections.FantasyDefenseGameProjection();
      //expect(instance).to.be();
    });

  });

}));
