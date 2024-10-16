/**
 * LoL v3 Projections
 * LoL v3 Projections
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
    factory(root.expect, root.LoLV3Projections);
  }
}(this, function(expect, LoLV3Projections) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new LoLV3Projections.Game();
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

  describe('Game', function() {
    it('should create an instance of Game', function() {
      // uncomment below and update the code to test Game
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be.a(LoLV3Projections.Game);
    });

    it('should have the property bestOf (base name: "BestOf")', function() {
      // uncomment below and update the code to test the property bestOf
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property dateTime (base name: "DateTime")', function() {
      // uncomment below and update the code to test the property dateTime
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property day (base name: "Day")', function() {
      // uncomment below and update the code to test the property day
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property drawMoneyLine (base name: "DrawMoneyLine")', function() {
      // uncomment below and update the code to test the property drawMoneyLine
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property gameId (base name: "GameId")', function() {
      // uncomment below and update the code to test the property gameId
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property group (base name: "Group")', function() {
      // uncomment below and update the code to test the property group
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property isClosed (base name: "IsClosed")', function() {
      // uncomment below and update the code to test the property isClosed
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property pointSpread (base name: "PointSpread")', function() {
      // uncomment below and update the code to test the property pointSpread
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property roundId (base name: "RoundId")', function() {
      // uncomment below and update the code to test the property roundId
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property season (base name: "Season")', function() {
      // uncomment below and update the code to test the property season
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property seasonType (base name: "SeasonType")', function() {
      // uncomment below and update the code to test the property seasonType
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "Status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property teamAId (base name: "TeamAId")', function() {
      // uncomment below and update the code to test the property teamAId
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property teamAKey (base name: "TeamAKey")', function() {
      // uncomment below and update the code to test the property teamAKey
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property teamAMoneyLine (base name: "TeamAMoneyLine")', function() {
      // uncomment below and update the code to test the property teamAMoneyLine
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property teamAName (base name: "TeamAName")', function() {
      // uncomment below and update the code to test the property teamAName
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property teamAPointSpreadPayout (base name: "TeamAPointSpreadPayout")', function() {
      // uncomment below and update the code to test the property teamAPointSpreadPayout
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property teamAScore (base name: "TeamAScore")', function() {
      // uncomment below and update the code to test the property teamAScore
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property teamBId (base name: "TeamBId")', function() {
      // uncomment below and update the code to test the property teamBId
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property teamBKey (base name: "TeamBKey")', function() {
      // uncomment below and update the code to test the property teamBKey
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property teamBMoneyLine (base name: "TeamBMoneyLine")', function() {
      // uncomment below and update the code to test the property teamBMoneyLine
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property teamBName (base name: "TeamBName")', function() {
      // uncomment below and update the code to test the property teamBName
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property teamBPointSpreadPayout (base name: "TeamBPointSpreadPayout")', function() {
      // uncomment below and update the code to test the property teamBPointSpreadPayout
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property teamBScore (base name: "TeamBScore")', function() {
      // uncomment below and update the code to test the property teamBScore
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property updated (base name: "Updated")', function() {
      // uncomment below and update the code to test the property updated
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property updatedUtc (base name: "UpdatedUtc")', function() {
      // uncomment below and update the code to test the property updatedUtc
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property venueId (base name: "VenueId")', function() {
      // uncomment below and update the code to test the property venueId
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property venueType (base name: "VenueType")', function() {
      // uncomment below and update the code to test the property venueType
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property week (base name: "Week")', function() {
      // uncomment below and update the code to test the property week
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

    it('should have the property winner (base name: "Winner")', function() {
      // uncomment below and update the code to test the property winner
      //var instance = new LoLV3Projections.Game();
      //expect(instance).to.be();
    });

  });

}));
