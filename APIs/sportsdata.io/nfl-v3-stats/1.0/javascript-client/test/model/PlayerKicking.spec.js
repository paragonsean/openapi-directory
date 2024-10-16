/**
 * NFL v3 Stats
 * NFL rosters, player stats, team stats, and fantasy stats API.
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
    factory(root.expect, root.NflV3Stats);
  }
}(this, function(expect, NflV3Stats) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NflV3Stats.PlayerKicking();
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

  describe('PlayerKicking', function() {
    it('should create an instance of PlayerKicking', function() {
      // uncomment below and update the code to test PlayerKicking
      //var instance = new NflV3Stats.PlayerKicking();
      //expect(instance).to.be.a(NflV3Stats.PlayerKicking);
    });

    it('should have the property extraPointsAttempted (base name: "ExtraPointsAttempted")', function() {
      // uncomment below and update the code to test the property extraPointsAttempted
      //var instance = new NflV3Stats.PlayerKicking();
      //expect(instance).to.be();
    });

    it('should have the property extraPointsMade (base name: "ExtraPointsMade")', function() {
      // uncomment below and update the code to test the property extraPointsMade
      //var instance = new NflV3Stats.PlayerKicking();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPoints (base name: "FantasyPoints")', function() {
      // uncomment below and update the code to test the property fantasyPoints
      //var instance = new NflV3Stats.PlayerKicking();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPosition (base name: "FantasyPosition")', function() {
      // uncomment below and update the code to test the property fantasyPosition
      //var instance = new NflV3Stats.PlayerKicking();
      //expect(instance).to.be();
    });

    it('should have the property fieldGoalPercentage (base name: "FieldGoalPercentage")', function() {
      // uncomment below and update the code to test the property fieldGoalPercentage
      //var instance = new NflV3Stats.PlayerKicking();
      //expect(instance).to.be();
    });

    it('should have the property fieldGoalsAttempted (base name: "FieldGoalsAttempted")', function() {
      // uncomment below and update the code to test the property fieldGoalsAttempted
      //var instance = new NflV3Stats.PlayerKicking();
      //expect(instance).to.be();
    });

    it('should have the property fieldGoalsLongestMade (base name: "FieldGoalsLongestMade")', function() {
      // uncomment below and update the code to test the property fieldGoalsLongestMade
      //var instance = new NflV3Stats.PlayerKicking();
      //expect(instance).to.be();
    });

    it('should have the property fieldGoalsMade (base name: "FieldGoalsMade")', function() {
      // uncomment below and update the code to test the property fieldGoalsMade
      //var instance = new NflV3Stats.PlayerKicking();
      //expect(instance).to.be();
    });

    it('should have the property fieldGoalsMade0to19 (base name: "FieldGoalsMade0to19")', function() {
      // uncomment below and update the code to test the property fieldGoalsMade0to19
      //var instance = new NflV3Stats.PlayerKicking();
      //expect(instance).to.be();
    });

    it('should have the property fieldGoalsMade20to29 (base name: "FieldGoalsMade20to29")', function() {
      // uncomment below and update the code to test the property fieldGoalsMade20to29
      //var instance = new NflV3Stats.PlayerKicking();
      //expect(instance).to.be();
    });

    it('should have the property fieldGoalsMade30to39 (base name: "FieldGoalsMade30to39")', function() {
      // uncomment below and update the code to test the property fieldGoalsMade30to39
      //var instance = new NflV3Stats.PlayerKicking();
      //expect(instance).to.be();
    });

    it('should have the property fieldGoalsMade40to49 (base name: "FieldGoalsMade40to49")', function() {
      // uncomment below and update the code to test the property fieldGoalsMade40to49
      //var instance = new NflV3Stats.PlayerKicking();
      //expect(instance).to.be();
    });

    it('should have the property fieldGoalsMade50Plus (base name: "FieldGoalsMade50Plus")', function() {
      // uncomment below and update the code to test the property fieldGoalsMade50Plus
      //var instance = new NflV3Stats.PlayerKicking();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "Name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new NflV3Stats.PlayerKicking();
      //expect(instance).to.be();
    });

    it('should have the property number (base name: "Number")', function() {
      // uncomment below and update the code to test the property number
      //var instance = new NflV3Stats.PlayerKicking();
      //expect(instance).to.be();
    });

    it('should have the property playerGameID (base name: "PlayerGameID")', function() {
      // uncomment below and update the code to test the property playerGameID
      //var instance = new NflV3Stats.PlayerKicking();
      //expect(instance).to.be();
    });

    it('should have the property playerID (base name: "PlayerID")', function() {
      // uncomment below and update the code to test the property playerID
      //var instance = new NflV3Stats.PlayerKicking();
      //expect(instance).to.be();
    });

    it('should have the property position (base name: "Position")', function() {
      // uncomment below and update the code to test the property position
      //var instance = new NflV3Stats.PlayerKicking();
      //expect(instance).to.be();
    });

    it('should have the property positionCategory (base name: "PositionCategory")', function() {
      // uncomment below and update the code to test the property positionCategory
      //var instance = new NflV3Stats.PlayerKicking();
      //expect(instance).to.be();
    });

    it('should have the property shortName (base name: "ShortName")', function() {
      // uncomment below and update the code to test the property shortName
      //var instance = new NflV3Stats.PlayerKicking();
      //expect(instance).to.be();
    });

    it('should have the property team (base name: "Team")', function() {
      // uncomment below and update the code to test the property team
      //var instance = new NflV3Stats.PlayerKicking();
      //expect(instance).to.be();
    });

    it('should have the property updated (base name: "Updated")', function() {
      // uncomment below and update the code to test the property updated
      //var instance = new NflV3Stats.PlayerKicking();
      //expect(instance).to.be();
    });

  });

}));
