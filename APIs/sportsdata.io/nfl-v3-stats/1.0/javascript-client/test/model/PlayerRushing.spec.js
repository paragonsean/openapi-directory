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
    instance = new NflV3Stats.PlayerRushing();
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

  describe('PlayerRushing', function() {
    it('should create an instance of PlayerRushing', function() {
      // uncomment below and update the code to test PlayerRushing
      //var instance = new NflV3Stats.PlayerRushing();
      //expect(instance).to.be.a(NflV3Stats.PlayerRushing);
    });

    it('should have the property fantasyPoints (base name: "FantasyPoints")', function() {
      // uncomment below and update the code to test the property fantasyPoints
      //var instance = new NflV3Stats.PlayerRushing();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPosition (base name: "FantasyPosition")', function() {
      // uncomment below and update the code to test the property fantasyPosition
      //var instance = new NflV3Stats.PlayerRushing();
      //expect(instance).to.be();
    });

    it('should have the property fumblesLost (base name: "FumblesLost")', function() {
      // uncomment below and update the code to test the property fumblesLost
      //var instance = new NflV3Stats.PlayerRushing();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "Name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new NflV3Stats.PlayerRushing();
      //expect(instance).to.be();
    });

    it('should have the property number (base name: "Number")', function() {
      // uncomment below and update the code to test the property number
      //var instance = new NflV3Stats.PlayerRushing();
      //expect(instance).to.be();
    });

    it('should have the property playerGameID (base name: "PlayerGameID")', function() {
      // uncomment below and update the code to test the property playerGameID
      //var instance = new NflV3Stats.PlayerRushing();
      //expect(instance).to.be();
    });

    it('should have the property playerID (base name: "PlayerID")', function() {
      // uncomment below and update the code to test the property playerID
      //var instance = new NflV3Stats.PlayerRushing();
      //expect(instance).to.be();
    });

    it('should have the property position (base name: "Position")', function() {
      // uncomment below and update the code to test the property position
      //var instance = new NflV3Stats.PlayerRushing();
      //expect(instance).to.be();
    });

    it('should have the property positionCategory (base name: "PositionCategory")', function() {
      // uncomment below and update the code to test the property positionCategory
      //var instance = new NflV3Stats.PlayerRushing();
      //expect(instance).to.be();
    });

    it('should have the property rushingAttempts (base name: "RushingAttempts")', function() {
      // uncomment below and update the code to test the property rushingAttempts
      //var instance = new NflV3Stats.PlayerRushing();
      //expect(instance).to.be();
    });

    it('should have the property rushingLong (base name: "RushingLong")', function() {
      // uncomment below and update the code to test the property rushingLong
      //var instance = new NflV3Stats.PlayerRushing();
      //expect(instance).to.be();
    });

    it('should have the property rushingTouchdowns (base name: "RushingTouchdowns")', function() {
      // uncomment below and update the code to test the property rushingTouchdowns
      //var instance = new NflV3Stats.PlayerRushing();
      //expect(instance).to.be();
    });

    it('should have the property rushingYards (base name: "RushingYards")', function() {
      // uncomment below and update the code to test the property rushingYards
      //var instance = new NflV3Stats.PlayerRushing();
      //expect(instance).to.be();
    });

    it('should have the property rushingYardsPerAttempt (base name: "RushingYardsPerAttempt")', function() {
      // uncomment below and update the code to test the property rushingYardsPerAttempt
      //var instance = new NflV3Stats.PlayerRushing();
      //expect(instance).to.be();
    });

    it('should have the property shortName (base name: "ShortName")', function() {
      // uncomment below and update the code to test the property shortName
      //var instance = new NflV3Stats.PlayerRushing();
      //expect(instance).to.be();
    });

    it('should have the property team (base name: "Team")', function() {
      // uncomment below and update the code to test the property team
      //var instance = new NflV3Stats.PlayerRushing();
      //expect(instance).to.be();
    });

    it('should have the property twoPointConversionRuns (base name: "TwoPointConversionRuns")', function() {
      // uncomment below and update the code to test the property twoPointConversionRuns
      //var instance = new NflV3Stats.PlayerRushing();
      //expect(instance).to.be();
    });

    it('should have the property updated (base name: "Updated")', function() {
      // uncomment below and update the code to test the property updated
      //var instance = new NflV3Stats.PlayerRushing();
      //expect(instance).to.be();
    });

  });

}));
