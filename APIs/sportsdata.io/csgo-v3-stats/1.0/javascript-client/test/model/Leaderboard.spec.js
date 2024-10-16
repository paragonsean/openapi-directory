/**
 * CS:GO v3 Stats
 * CS:GO v3 Stats
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
    factory(root.expect, root.CsgoV3Stats);
  }
}(this, function(expect, CsgoV3Stats) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new CsgoV3Stats.Leaderboard();
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

  describe('Leaderboard', function() {
    it('should create an instance of Leaderboard', function() {
      // uncomment below and update the code to test Leaderboard
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be.a(CsgoV3Stats.Leaderboard);
    });

    it('should have the property aces (base name: "Aces")', function() {
      // uncomment below and update the code to test the property aces
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property assists (base name: "Assists")', function() {
      // uncomment below and update the code to test the property assists
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property averageDamagePerRound (base name: "AverageDamagePerRound")', function() {
      // uncomment below and update the code to test the property averageDamagePerRound
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property clutch1v2s (base name: "Clutch1v2s")', function() {
      // uncomment below and update the code to test the property clutch1v2s
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property clutch1v3s (base name: "Clutch1v3s")', function() {
      // uncomment below and update the code to test the property clutch1v3s
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property clutch1v4s (base name: "Clutch1v4s")', function() {
      // uncomment below and update the code to test the property clutch1v4s
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property clutch1v5s (base name: "Clutch1v5s")', function() {
      // uncomment below and update the code to test the property clutch1v5s
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property dateTime (base name: "DateTime")', function() {
      // uncomment below and update the code to test the property dateTime
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property day (base name: "Day")', function() {
      // uncomment below and update the code to test the property day
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property deaths (base name: "Deaths")', function() {
      // uncomment below and update the code to test the property deaths
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property entryKills (base name: "EntryKills")', function() {
      // uncomment below and update the code to test the property entryKills
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPoints (base name: "FantasyPoints")', function() {
      // uncomment below and update the code to test the property fantasyPoints
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property gameId (base name: "GameId")', function() {
      // uncomment below and update the code to test the property gameId
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property games (base name: "Games")', function() {
      // uncomment below and update the code to test the property games
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property headshots (base name: "Headshots")', function() {
      // uncomment below and update the code to test the property headshots
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property isClosed (base name: "IsClosed")', function() {
      // uncomment below and update the code to test the property isClosed
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property kast (base name: "Kast")', function() {
      // uncomment below and update the code to test the property kast
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property kills (base name: "Kills")', function() {
      // uncomment below and update the code to test the property kills
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property maps (base name: "Maps")', function() {
      // uncomment below and update the code to test the property maps
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property matchName (base name: "MatchName")', function() {
      // uncomment below and update the code to test the property matchName
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "Name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property opponent (base name: "Opponent")', function() {
      // uncomment below and update the code to test the property opponent
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property opponentId (base name: "OpponentId")', function() {
      // uncomment below and update the code to test the property opponentId
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property playerId (base name: "PlayerId")', function() {
      // uncomment below and update the code to test the property playerId
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property quadKills (base name: "QuadKills")', function() {
      // uncomment below and update the code to test the property quadKills
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property rating (base name: "Rating")', function() {
      // uncomment below and update the code to test the property rating
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property team (base name: "Team")', function() {
      // uncomment below and update the code to test the property team
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property teamId (base name: "TeamId")', function() {
      // uncomment below and update the code to test the property teamId
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property updated (base name: "Updated")', function() {
      // uncomment below and update the code to test the property updated
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

    it('should have the property updatedUtc (base name: "UpdatedUtc")', function() {
      // uncomment below and update the code to test the property updatedUtc
      //var instance = new CsgoV3Stats.Leaderboard();
      //expect(instance).to.be();
    });

  });

}));
