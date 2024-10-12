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
    instance = new NhlV3Stats.Game();
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
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be.a(NhlV3Stats.Game);
    });

    it('should have the property attendance (base name: "Attendance")', function() {
      // uncomment below and update the code to test the property attendance
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property awayRotationNumber (base name: "AwayRotationNumber")', function() {
      // uncomment below and update the code to test the property awayRotationNumber
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property awayTeam (base name: "AwayTeam")', function() {
      // uncomment below and update the code to test the property awayTeam
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property awayTeamID (base name: "AwayTeamID")', function() {
      // uncomment below and update the code to test the property awayTeamID
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property awayTeamMoneyLine (base name: "AwayTeamMoneyLine")', function() {
      // uncomment below and update the code to test the property awayTeamMoneyLine
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property awayTeamScore (base name: "AwayTeamScore")', function() {
      // uncomment below and update the code to test the property awayTeamScore
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property channel (base name: "Channel")', function() {
      // uncomment below and update the code to test the property channel
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property dateTime (base name: "DateTime")', function() {
      // uncomment below and update the code to test the property dateTime
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property dateTimeUTC (base name: "DateTimeUTC")', function() {
      // uncomment below and update the code to test the property dateTimeUTC
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property day (base name: "Day")', function() {
      // uncomment below and update the code to test the property day
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property gameEndDateTime (base name: "GameEndDateTime")', function() {
      // uncomment below and update the code to test the property gameEndDateTime
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property gameID (base name: "GameID")', function() {
      // uncomment below and update the code to test the property gameID
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property globalAwayTeamID (base name: "GlobalAwayTeamID")', function() {
      // uncomment below and update the code to test the property globalAwayTeamID
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property globalGameID (base name: "GlobalGameID")', function() {
      // uncomment below and update the code to test the property globalGameID
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property globalHomeTeamID (base name: "GlobalHomeTeamID")', function() {
      // uncomment below and update the code to test the property globalHomeTeamID
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property homeRotationNumber (base name: "HomeRotationNumber")', function() {
      // uncomment below and update the code to test the property homeRotationNumber
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property homeTeam (base name: "HomeTeam")', function() {
      // uncomment below and update the code to test the property homeTeam
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property homeTeamID (base name: "HomeTeamID")', function() {
      // uncomment below and update the code to test the property homeTeamID
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property homeTeamMoneyLine (base name: "HomeTeamMoneyLine")', function() {
      // uncomment below and update the code to test the property homeTeamMoneyLine
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property homeTeamScore (base name: "HomeTeamScore")', function() {
      // uncomment below and update the code to test the property homeTeamScore
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property isClosed (base name: "IsClosed")', function() {
      // uncomment below and update the code to test the property isClosed
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property lastPlay (base name: "LastPlay")', function() {
      // uncomment below and update the code to test the property lastPlay
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property neutralVenue (base name: "NeutralVenue")', function() {
      // uncomment below and update the code to test the property neutralVenue
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property overPayout (base name: "OverPayout")', function() {
      // uncomment below and update the code to test the property overPayout
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property overUnder (base name: "OverUnder")', function() {
      // uncomment below and update the code to test the property overUnder
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property period (base name: "Period")', function() {
      // uncomment below and update the code to test the property period
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property periods (base name: "Periods")', function() {
      // uncomment below and update the code to test the property periods
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property pointSpread (base name: "PointSpread")', function() {
      // uncomment below and update the code to test the property pointSpread
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property pointSpreadAwayTeamMoneyLine (base name: "PointSpreadAwayTeamMoneyLine")', function() {
      // uncomment below and update the code to test the property pointSpreadAwayTeamMoneyLine
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property pointSpreadHomeTeamMoneyLine (base name: "PointSpreadHomeTeamMoneyLine")', function() {
      // uncomment below and update the code to test the property pointSpreadHomeTeamMoneyLine
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property season (base name: "Season")', function() {
      // uncomment below and update the code to test the property season
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property seasonType (base name: "SeasonType")', function() {
      // uncomment below and update the code to test the property seasonType
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property seriesInfo (base name: "SeriesInfo")', function() {
      // uncomment below and update the code to test the property seriesInfo
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property stadiumID (base name: "StadiumID")', function() {
      // uncomment below and update the code to test the property stadiumID
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "Status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property timeRemainingMinutes (base name: "TimeRemainingMinutes")', function() {
      // uncomment below and update the code to test the property timeRemainingMinutes
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property timeRemainingSeconds (base name: "TimeRemainingSeconds")', function() {
      // uncomment below and update the code to test the property timeRemainingSeconds
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property underPayout (base name: "UnderPayout")', function() {
      // uncomment below and update the code to test the property underPayout
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property updated (base name: "Updated")', function() {
      // uncomment below and update the code to test the property updated
      //var instance = new NhlV3Stats.Game();
      //expect(instance).to.be();
    });

  });

}));
