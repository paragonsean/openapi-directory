/**
 * LoL v3 Stats
 * LoL v3 Stats
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
    factory(root.expect, root.LoLV3Stats);
  }
}(this, function(expect, LoLV3Stats) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new LoLV3Stats.TeamGame();
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

  describe('TeamGame', function() {
    it('should create an instance of TeamGame', function() {
      // uncomment below and update the code to test TeamGame
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be.a(LoLV3Stats.TeamGame);
    });

    it('should have the property assists (base name: "Assists")', function() {
      // uncomment below and update the code to test the property assists
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property combatPlayerScore (base name: "CombatPlayerScore")', function() {
      // uncomment below and update the code to test the property combatPlayerScore
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property dateTime (base name: "DateTime")', function() {
      // uncomment below and update the code to test the property dateTime
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property day (base name: "Day")', function() {
      // uncomment below and update the code to test the property day
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property deaths (base name: "Deaths")', function() {
      // uncomment below and update the code to test the property deaths
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property doubleKills (base name: "DoubleKills")', function() {
      // uncomment below and update the code to test the property doubleKills
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPoints (base name: "FantasyPoints")', function() {
      // uncomment below and update the code to test the property fantasyPoints
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property firstBaron (base name: "FirstBaron")', function() {
      // uncomment below and update the code to test the property firstBaron
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property firstBlood (base name: "FirstBlood")', function() {
      // uncomment below and update the code to test the property firstBlood
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property firstDragon (base name: "FirstDragon")', function() {
      // uncomment below and update the code to test the property firstDragon
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property firstInhibitor (base name: "FirstInhibitor")', function() {
      // uncomment below and update the code to test the property firstInhibitor
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property firstRiftHerald (base name: "FirstRiftHerald")', function() {
      // uncomment below and update the code to test the property firstRiftHerald
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property firstTower (base name: "FirstTower")', function() {
      // uncomment below and update the code to test the property firstTower
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property gameId (base name: "GameId")', function() {
      // uncomment below and update the code to test the property gameId
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property games (base name: "Games")', function() {
      // uncomment below and update the code to test the property games
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property goldEarned (base name: "GoldEarned")', function() {
      // uncomment below and update the code to test the property goldEarned
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property goldSpent (base name: "GoldSpent")', function() {
      // uncomment below and update the code to test the property goldSpent
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property inhibitorKills (base name: "InhibitorKills")', function() {
      // uncomment below and update the code to test the property inhibitorKills
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property isClosed (base name: "IsClosed")', function() {
      // uncomment below and update the code to test the property isClosed
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property killingSpree (base name: "KillingSpree")', function() {
      // uncomment below and update the code to test the property killingSpree
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property kills (base name: "Kills")', function() {
      // uncomment below and update the code to test the property kills
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property largestCriticalStrike (base name: "LargestCriticalStrike")', function() {
      // uncomment below and update the code to test the property largestCriticalStrike
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property largestKillingSpree (base name: "LargestKillingSpree")', function() {
      // uncomment below and update the code to test the property largestKillingSpree
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property largestMultiKill (base name: "LargestMultiKill")', function() {
      // uncomment below and update the code to test the property largestMultiKill
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property longestTimeSpentLiving (base name: "LongestTimeSpentLiving")', function() {
      // uncomment below and update the code to test the property longestTimeSpentLiving
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property magicDamageDealt (base name: "MagicDamageDealt")', function() {
      // uncomment below and update the code to test the property magicDamageDealt
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property magicDamageDealtToChampions (base name: "MagicDamageDealtToChampions")', function() {
      // uncomment below and update the code to test the property magicDamageDealtToChampions
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property magicDamageTaken (base name: "MagicDamageTaken")', function() {
      // uncomment below and update the code to test the property magicDamageTaken
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property matchName (base name: "MatchName")', function() {
      // uncomment below and update the code to test the property matchName
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property matches (base name: "Matches")', function() {
      // uncomment below and update the code to test the property matches
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "Name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property neutralMinionsKIlled (base name: "NeutralMinionsKIlled")', function() {
      // uncomment below and update the code to test the property neutralMinionsKIlled
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property neutralMinionsKIlledTeamJungle (base name: "NeutralMinionsKIlledTeamJungle")', function() {
      // uncomment below and update the code to test the property neutralMinionsKIlledTeamJungle
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property neutralMinionsKilledEnemyJungle (base name: "NeutralMinionsKilledEnemyJungle")', function() {
      // uncomment below and update the code to test the property neutralMinionsKilledEnemyJungle
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property objectivePlayerScore (base name: "ObjectivePlayerScore")', function() {
      // uncomment below and update the code to test the property objectivePlayerScore
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property opponent (base name: "Opponent")', function() {
      // uncomment below and update the code to test the property opponent
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property opponentId (base name: "OpponentId")', function() {
      // uncomment below and update the code to test the property opponentId
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property pentaKills (base name: "PentaKills")', function() {
      // uncomment below and update the code to test the property pentaKills
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property physicalDamageDealt (base name: "PhysicalDamageDealt")', function() {
      // uncomment below and update the code to test the property physicalDamageDealt
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property physicalDamageDealtToChampions (base name: "PhysicalDamageDealtToChampions")', function() {
      // uncomment below and update the code to test the property physicalDamageDealtToChampions
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property physicalDamageTaken (base name: "PhysicalDamageTaken")', function() {
      // uncomment below and update the code to test the property physicalDamageTaken
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property playerId (base name: "PlayerId")', function() {
      // uncomment below and update the code to test the property playerId
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property position (base name: "Position")', function() {
      // uncomment below and update the code to test the property position
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property quadraKills (base name: "QuadraKills")', function() {
      // uncomment below and update the code to test the property quadraKills
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property sightWardsBoughtInGame (base name: "SightWardsBoughtInGame")', function() {
      // uncomment below and update the code to test the property sightWardsBoughtInGame
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property team (base name: "Team")', function() {
      // uncomment below and update the code to test the property team
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property teamId (base name: "TeamId")', function() {
      // uncomment below and update the code to test the property teamId
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property tenKillsOrAssists (base name: "TenKillsOrAssists")', function() {
      // uncomment below and update the code to test the property tenKillsOrAssists
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property totalDamageDealt (base name: "TotalDamageDealt")', function() {
      // uncomment below and update the code to test the property totalDamageDealt
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property totalDamageDealtToChampions (base name: "TotalDamageDealtToChampions")', function() {
      // uncomment below and update the code to test the property totalDamageDealtToChampions
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property totalDamageTaken (base name: "TotalDamageTaken")', function() {
      // uncomment below and update the code to test the property totalDamageTaken
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property totalHeal (base name: "TotalHeal")', function() {
      // uncomment below and update the code to test the property totalHeal
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property totalMinionsKilled (base name: "TotalMinionsKilled")', function() {
      // uncomment below and update the code to test the property totalMinionsKilled
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property totalPlayerScore (base name: "TotalPlayerScore")', function() {
      // uncomment below and update the code to test the property totalPlayerScore
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property totalTimeCrowdControlDealt (base name: "TotalTimeCrowdControlDealt")', function() {
      // uncomment below and update the code to test the property totalTimeCrowdControlDealt
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property totalUnitsHealed (base name: "TotalUnitsHealed")', function() {
      // uncomment below and update the code to test the property totalUnitsHealed
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property tripleKills (base name: "TripleKills")', function() {
      // uncomment below and update the code to test the property tripleKills
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property trueDamageDealt (base name: "TrueDamageDealt")', function() {
      // uncomment below and update the code to test the property trueDamageDealt
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property trueDamageDealtToChampions (base name: "TrueDamageDealtToChampions")', function() {
      // uncomment below and update the code to test the property trueDamageDealtToChampions
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property trueDamageTaken (base name: "TrueDamageTaken")', function() {
      // uncomment below and update the code to test the property trueDamageTaken
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property turretKills (base name: "TurretKills")', function() {
      // uncomment below and update the code to test the property turretKills
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property unrealKills (base name: "UnrealKills")', function() {
      // uncomment below and update the code to test the property unrealKills
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property updated (base name: "Updated")', function() {
      // uncomment below and update the code to test the property updated
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property visionWardsBoughtInGame (base name: "VisionWardsBoughtInGame")', function() {
      // uncomment below and update the code to test the property visionWardsBoughtInGame
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property wardsKilled (base name: "WardsKilled")', function() {
      // uncomment below and update the code to test the property wardsKilled
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

    it('should have the property wardsPlaced (base name: "WardsPlaced")', function() {
      // uncomment below and update the code to test the property wardsPlaced
      //var instance = new LoLV3Stats.TeamGame();
      //expect(instance).to.be();
    });

  });

}));
