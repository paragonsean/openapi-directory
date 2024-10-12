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
    instance = new NflV3Stats.PlayerDefense();
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

  describe('PlayerDefense', function() {
    it('should create an instance of PlayerDefense', function() {
      // uncomment below and update the code to test PlayerDefense
      //var instance = new NflV3Stats.PlayerDefense();
      //expect(instance).to.be.a(NflV3Stats.PlayerDefense);
    });

    it('should have the property assistedTackles (base name: "AssistedTackles")', function() {
      // uncomment below and update the code to test the property assistedTackles
      //var instance = new NflV3Stats.PlayerDefense();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPoints (base name: "FantasyPoints")', function() {
      // uncomment below and update the code to test the property fantasyPoints
      //var instance = new NflV3Stats.PlayerDefense();
      //expect(instance).to.be();
    });

    it('should have the property fantasyPosition (base name: "FantasyPosition")', function() {
      // uncomment below and update the code to test the property fantasyPosition
      //var instance = new NflV3Stats.PlayerDefense();
      //expect(instance).to.be();
    });

    it('should have the property fumbleReturnTouchdowns (base name: "FumbleReturnTouchdowns")', function() {
      // uncomment below and update the code to test the property fumbleReturnTouchdowns
      //var instance = new NflV3Stats.PlayerDefense();
      //expect(instance).to.be();
    });

    it('should have the property fumblesForced (base name: "FumblesForced")', function() {
      // uncomment below and update the code to test the property fumblesForced
      //var instance = new NflV3Stats.PlayerDefense();
      //expect(instance).to.be();
    });

    it('should have the property fumblesRecovered (base name: "FumblesRecovered")', function() {
      // uncomment below and update the code to test the property fumblesRecovered
      //var instance = new NflV3Stats.PlayerDefense();
      //expect(instance).to.be();
    });

    it('should have the property interceptionReturnTouchdowns (base name: "InterceptionReturnTouchdowns")', function() {
      // uncomment below and update the code to test the property interceptionReturnTouchdowns
      //var instance = new NflV3Stats.PlayerDefense();
      //expect(instance).to.be();
    });

    it('should have the property interceptionReturnYards (base name: "InterceptionReturnYards")', function() {
      // uncomment below and update the code to test the property interceptionReturnYards
      //var instance = new NflV3Stats.PlayerDefense();
      //expect(instance).to.be();
    });

    it('should have the property interceptions (base name: "Interceptions")', function() {
      // uncomment below and update the code to test the property interceptions
      //var instance = new NflV3Stats.PlayerDefense();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "Name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new NflV3Stats.PlayerDefense();
      //expect(instance).to.be();
    });

    it('should have the property number (base name: "Number")', function() {
      // uncomment below and update the code to test the property number
      //var instance = new NflV3Stats.PlayerDefense();
      //expect(instance).to.be();
    });

    it('should have the property passesDefended (base name: "PassesDefended")', function() {
      // uncomment below and update the code to test the property passesDefended
      //var instance = new NflV3Stats.PlayerDefense();
      //expect(instance).to.be();
    });

    it('should have the property playerGameID (base name: "PlayerGameID")', function() {
      // uncomment below and update the code to test the property playerGameID
      //var instance = new NflV3Stats.PlayerDefense();
      //expect(instance).to.be();
    });

    it('should have the property playerID (base name: "PlayerID")', function() {
      // uncomment below and update the code to test the property playerID
      //var instance = new NflV3Stats.PlayerDefense();
      //expect(instance).to.be();
    });

    it('should have the property position (base name: "Position")', function() {
      // uncomment below and update the code to test the property position
      //var instance = new NflV3Stats.PlayerDefense();
      //expect(instance).to.be();
    });

    it('should have the property positionCategory (base name: "PositionCategory")', function() {
      // uncomment below and update the code to test the property positionCategory
      //var instance = new NflV3Stats.PlayerDefense();
      //expect(instance).to.be();
    });

    it('should have the property quarterbackHits (base name: "QuarterbackHits")', function() {
      // uncomment below and update the code to test the property quarterbackHits
      //var instance = new NflV3Stats.PlayerDefense();
      //expect(instance).to.be();
    });

    it('should have the property sackYards (base name: "SackYards")', function() {
      // uncomment below and update the code to test the property sackYards
      //var instance = new NflV3Stats.PlayerDefense();
      //expect(instance).to.be();
    });

    it('should have the property sacks (base name: "Sacks")', function() {
      // uncomment below and update the code to test the property sacks
      //var instance = new NflV3Stats.PlayerDefense();
      //expect(instance).to.be();
    });

    it('should have the property safeties (base name: "Safeties")', function() {
      // uncomment below and update the code to test the property safeties
      //var instance = new NflV3Stats.PlayerDefense();
      //expect(instance).to.be();
    });

    it('should have the property shortName (base name: "ShortName")', function() {
      // uncomment below and update the code to test the property shortName
      //var instance = new NflV3Stats.PlayerDefense();
      //expect(instance).to.be();
    });

    it('should have the property soloTackles (base name: "SoloTackles")', function() {
      // uncomment below and update the code to test the property soloTackles
      //var instance = new NflV3Stats.PlayerDefense();
      //expect(instance).to.be();
    });

    it('should have the property tackles (base name: "Tackles")', function() {
      // uncomment below and update the code to test the property tackles
      //var instance = new NflV3Stats.PlayerDefense();
      //expect(instance).to.be();
    });

    it('should have the property tacklesForLoss (base name: "TacklesForLoss")', function() {
      // uncomment below and update the code to test the property tacklesForLoss
      //var instance = new NflV3Stats.PlayerDefense();
      //expect(instance).to.be();
    });

    it('should have the property team (base name: "Team")', function() {
      // uncomment below and update the code to test the property team
      //var instance = new NflV3Stats.PlayerDefense();
      //expect(instance).to.be();
    });

    it('should have the property updated (base name: "Updated")', function() {
      // uncomment below and update the code to test the property updated
      //var instance = new NflV3Stats.PlayerDefense();
      //expect(instance).to.be();
    });

  });

}));
