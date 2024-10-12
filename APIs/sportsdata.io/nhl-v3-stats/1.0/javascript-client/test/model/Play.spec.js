/**
 * NHL v3 Stats
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
    factory(root.expect, root.NhlV3Stats);
  }
}(this, function(expect, NhlV3Stats) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NhlV3Stats.Play();
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

  describe('Play', function() {
    it('should create an instance of Play', function() {
      // uncomment below and update the code to test Play
      //var instance = new NhlV3Stats.Play();
      //expect(instance).to.be.a(NhlV3Stats.Play);
    });

    it('should have the property awayTeamScore (base name: "AwayTeamScore")', function() {
      // uncomment below and update the code to test the property awayTeamScore
      //var instance = new NhlV3Stats.Play();
      //expect(instance).to.be();
    });

    it('should have the property category (base name: "Category")', function() {
      // uncomment below and update the code to test the property category
      //var instance = new NhlV3Stats.Play();
      //expect(instance).to.be();
    });

    it('should have the property clockMinutes (base name: "ClockMinutes")', function() {
      // uncomment below and update the code to test the property clockMinutes
      //var instance = new NhlV3Stats.Play();
      //expect(instance).to.be();
    });

    it('should have the property clockSeconds (base name: "ClockSeconds")', function() {
      // uncomment below and update the code to test the property clockSeconds
      //var instance = new NhlV3Stats.Play();
      //expect(instance).to.be();
    });

    it('should have the property created (base name: "Created")', function() {
      // uncomment below and update the code to test the property created
      //var instance = new NhlV3Stats.Play();
      //expect(instance).to.be();
    });

    it('should have the property description (base name: "Description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new NhlV3Stats.Play();
      //expect(instance).to.be();
    });

    it('should have the property firstAssistedByPlayerID (base name: "FirstAssistedByPlayerID")', function() {
      // uncomment below and update the code to test the property firstAssistedByPlayerID
      //var instance = new NhlV3Stats.Play();
      //expect(instance).to.be();
    });

    it('should have the property homeTeamScore (base name: "HomeTeamScore")', function() {
      // uncomment below and update the code to test the property homeTeamScore
      //var instance = new NhlV3Stats.Play();
      //expect(instance).to.be();
    });

    it('should have the property opponent (base name: "Opponent")', function() {
      // uncomment below and update the code to test the property opponent
      //var instance = new NhlV3Stats.Play();
      //expect(instance).to.be();
    });

    it('should have the property opponentID (base name: "OpponentID")', function() {
      // uncomment below and update the code to test the property opponentID
      //var instance = new NhlV3Stats.Play();
      //expect(instance).to.be();
    });

    it('should have the property opposingPlayerID (base name: "OpposingPlayerID")', function() {
      // uncomment below and update the code to test the property opposingPlayerID
      //var instance = new NhlV3Stats.Play();
      //expect(instance).to.be();
    });

    it('should have the property periodID (base name: "PeriodID")', function() {
      // uncomment below and update the code to test the property periodID
      //var instance = new NhlV3Stats.Play();
      //expect(instance).to.be();
    });

    it('should have the property periodName (base name: "PeriodName")', function() {
      // uncomment below and update the code to test the property periodName
      //var instance = new NhlV3Stats.Play();
      //expect(instance).to.be();
    });

    it('should have the property playID (base name: "PlayID")', function() {
      // uncomment below and update the code to test the property playID
      //var instance = new NhlV3Stats.Play();
      //expect(instance).to.be();
    });

    it('should have the property playerID (base name: "PlayerID")', function() {
      // uncomment below and update the code to test the property playerID
      //var instance = new NhlV3Stats.Play();
      //expect(instance).to.be();
    });

    it('should have the property powerPlayTeam (base name: "PowerPlayTeam")', function() {
      // uncomment below and update the code to test the property powerPlayTeam
      //var instance = new NhlV3Stats.Play();
      //expect(instance).to.be();
    });

    it('should have the property powerPlayTeamID (base name: "PowerPlayTeamID")', function() {
      // uncomment below and update the code to test the property powerPlayTeamID
      //var instance = new NhlV3Stats.Play();
      //expect(instance).to.be();
    });

    it('should have the property secondAssistedByPlayerID (base name: "SecondAssistedByPlayerID")', function() {
      // uncomment below and update the code to test the property secondAssistedByPlayerID
      //var instance = new NhlV3Stats.Play();
      //expect(instance).to.be();
    });

    it('should have the property sequence (base name: "Sequence")', function() {
      // uncomment below and update the code to test the property sequence
      //var instance = new NhlV3Stats.Play();
      //expect(instance).to.be();
    });

    it('should have the property team (base name: "Team")', function() {
      // uncomment below and update the code to test the property team
      //var instance = new NhlV3Stats.Play();
      //expect(instance).to.be();
    });

    it('should have the property teamID (base name: "TeamID")', function() {
      // uncomment below and update the code to test the property teamID
      //var instance = new NhlV3Stats.Play();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "Type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new NhlV3Stats.Play();
      //expect(instance).to.be();
    });

    it('should have the property updated (base name: "Updated")', function() {
      // uncomment below and update the code to test the property updated
      //var instance = new NhlV3Stats.Play();
      //expect(instance).to.be();
    });

  });

}));
