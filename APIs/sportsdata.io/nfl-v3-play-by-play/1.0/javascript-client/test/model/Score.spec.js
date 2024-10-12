/**
 * NFL v3 Play-by-Play
 * NFL play-by-play API.
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
    factory(root.expect, root.NflV3PlayByPlay);
  }
}(this, function(expect, NflV3PlayByPlay) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NflV3PlayByPlay.Score();
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

  describe('Score', function() {
    it('should create an instance of Score', function() {
      // uncomment below and update the code to test Score
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be.a(NflV3PlayByPlay.Score);
    });

    it('should have the property attendance (base name: "Attendance")', function() {
      // uncomment below and update the code to test the property attendance
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property awayRotationNumber (base name: "AwayRotationNumber")', function() {
      // uncomment below and update the code to test the property awayRotationNumber
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property awayScore (base name: "AwayScore")', function() {
      // uncomment below and update the code to test the property awayScore
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property awayScoreOvertime (base name: "AwayScoreOvertime")', function() {
      // uncomment below and update the code to test the property awayScoreOvertime
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property awayScoreQuarter1 (base name: "AwayScoreQuarter1")', function() {
      // uncomment below and update the code to test the property awayScoreQuarter1
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property awayScoreQuarter2 (base name: "AwayScoreQuarter2")', function() {
      // uncomment below and update the code to test the property awayScoreQuarter2
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property awayScoreQuarter3 (base name: "AwayScoreQuarter3")', function() {
      // uncomment below and update the code to test the property awayScoreQuarter3
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property awayScoreQuarter4 (base name: "AwayScoreQuarter4")', function() {
      // uncomment below and update the code to test the property awayScoreQuarter4
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property awayTeam (base name: "AwayTeam")', function() {
      // uncomment below and update the code to test the property awayTeam
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property awayTeamID (base name: "AwayTeamID")', function() {
      // uncomment below and update the code to test the property awayTeamID
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property awayTeamMoneyLine (base name: "AwayTeamMoneyLine")', function() {
      // uncomment below and update the code to test the property awayTeamMoneyLine
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property awayTimeouts (base name: "AwayTimeouts")', function() {
      // uncomment below and update the code to test the property awayTimeouts
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property canceled (base name: "Canceled")', function() {
      // uncomment below and update the code to test the property canceled
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property channel (base name: "Channel")', function() {
      // uncomment below and update the code to test the property channel
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property closed (base name: "Closed")', function() {
      // uncomment below and update the code to test the property closed
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property date (base name: "Date")', function() {
      // uncomment below and update the code to test the property date
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property dateTime (base name: "DateTime")', function() {
      // uncomment below and update the code to test the property dateTime
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property dateTimeUTC (base name: "DateTimeUTC")', function() {
      // uncomment below and update the code to test the property dateTimeUTC
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property day (base name: "Day")', function() {
      // uncomment below and update the code to test the property day
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property distance (base name: "Distance")', function() {
      // uncomment below and update the code to test the property distance
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property down (base name: "Down")', function() {
      // uncomment below and update the code to test the property down
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property downAndDistance (base name: "DownAndDistance")', function() {
      // uncomment below and update the code to test the property downAndDistance
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property forecastDescription (base name: "ForecastDescription")', function() {
      // uncomment below and update the code to test the property forecastDescription
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property forecastTempHigh (base name: "ForecastTempHigh")', function() {
      // uncomment below and update the code to test the property forecastTempHigh
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property forecastTempLow (base name: "ForecastTempLow")', function() {
      // uncomment below and update the code to test the property forecastTempLow
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property forecastWindChill (base name: "ForecastWindChill")', function() {
      // uncomment below and update the code to test the property forecastWindChill
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property forecastWindSpeed (base name: "ForecastWindSpeed")', function() {
      // uncomment below and update the code to test the property forecastWindSpeed
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property gameEndDateTime (base name: "GameEndDateTime")', function() {
      // uncomment below and update the code to test the property gameEndDateTime
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property gameKey (base name: "GameKey")', function() {
      // uncomment below and update the code to test the property gameKey
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property geoLat (base name: "GeoLat")', function() {
      // uncomment below and update the code to test the property geoLat
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property geoLong (base name: "GeoLong")', function() {
      // uncomment below and update the code to test the property geoLong
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property globalAwayTeamID (base name: "GlobalAwayTeamID")', function() {
      // uncomment below and update the code to test the property globalAwayTeamID
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property globalGameID (base name: "GlobalGameID")', function() {
      // uncomment below and update the code to test the property globalGameID
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property globalHomeTeamID (base name: "GlobalHomeTeamID")', function() {
      // uncomment below and update the code to test the property globalHomeTeamID
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property has1stQuarterStarted (base name: "Has1stQuarterStarted")', function() {
      // uncomment below and update the code to test the property has1stQuarterStarted
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property has2ndQuarterStarted (base name: "Has2ndQuarterStarted")', function() {
      // uncomment below and update the code to test the property has2ndQuarterStarted
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property has3rdQuarterStarted (base name: "Has3rdQuarterStarted")', function() {
      // uncomment below and update the code to test the property has3rdQuarterStarted
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property has4thQuarterStarted (base name: "Has4thQuarterStarted")', function() {
      // uncomment below and update the code to test the property has4thQuarterStarted
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property hasStarted (base name: "HasStarted")', function() {
      // uncomment below and update the code to test the property hasStarted
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property homeRotationNumber (base name: "HomeRotationNumber")', function() {
      // uncomment below and update the code to test the property homeRotationNumber
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property homeScore (base name: "HomeScore")', function() {
      // uncomment below and update the code to test the property homeScore
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property homeScoreOvertime (base name: "HomeScoreOvertime")', function() {
      // uncomment below and update the code to test the property homeScoreOvertime
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property homeScoreQuarter1 (base name: "HomeScoreQuarter1")', function() {
      // uncomment below and update the code to test the property homeScoreQuarter1
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property homeScoreQuarter2 (base name: "HomeScoreQuarter2")', function() {
      // uncomment below and update the code to test the property homeScoreQuarter2
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property homeScoreQuarter3 (base name: "HomeScoreQuarter3")', function() {
      // uncomment below and update the code to test the property homeScoreQuarter3
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property homeScoreQuarter4 (base name: "HomeScoreQuarter4")', function() {
      // uncomment below and update the code to test the property homeScoreQuarter4
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property homeTeam (base name: "HomeTeam")', function() {
      // uncomment below and update the code to test the property homeTeam
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property homeTeamID (base name: "HomeTeamID")', function() {
      // uncomment below and update the code to test the property homeTeamID
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property homeTeamMoneyLine (base name: "HomeTeamMoneyLine")', function() {
      // uncomment below and update the code to test the property homeTeamMoneyLine
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property homeTimeouts (base name: "HomeTimeouts")', function() {
      // uncomment below and update the code to test the property homeTimeouts
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property isInProgress (base name: "IsInProgress")', function() {
      // uncomment below and update the code to test the property isInProgress
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property isOver (base name: "IsOver")', function() {
      // uncomment below and update the code to test the property isOver
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property isOvertime (base name: "IsOvertime")', function() {
      // uncomment below and update the code to test the property isOvertime
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property lastPlay (base name: "LastPlay")', function() {
      // uncomment below and update the code to test the property lastPlay
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property lastUpdated (base name: "LastUpdated")', function() {
      // uncomment below and update the code to test the property lastUpdated
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property neutralVenue (base name: "NeutralVenue")', function() {
      // uncomment below and update the code to test the property neutralVenue
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property overPayout (base name: "OverPayout")', function() {
      // uncomment below and update the code to test the property overPayout
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property overUnder (base name: "OverUnder")', function() {
      // uncomment below and update the code to test the property overUnder
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property pointSpread (base name: "PointSpread")', function() {
      // uncomment below and update the code to test the property pointSpread
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property pointSpreadAwayTeamMoneyLine (base name: "PointSpreadAwayTeamMoneyLine")', function() {
      // uncomment below and update the code to test the property pointSpreadAwayTeamMoneyLine
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property pointSpreadHomeTeamMoneyLine (base name: "PointSpreadHomeTeamMoneyLine")', function() {
      // uncomment below and update the code to test the property pointSpreadHomeTeamMoneyLine
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property possession (base name: "Possession")', function() {
      // uncomment below and update the code to test the property possession
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property quarter (base name: "Quarter")', function() {
      // uncomment below and update the code to test the property quarter
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property quarterDescription (base name: "QuarterDescription")', function() {
      // uncomment below and update the code to test the property quarterDescription
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property redZone (base name: "RedZone")', function() {
      // uncomment below and update the code to test the property redZone
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property refereeID (base name: "RefereeID")', function() {
      // uncomment below and update the code to test the property refereeID
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property scoreID (base name: "ScoreID")', function() {
      // uncomment below and update the code to test the property scoreID
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property season (base name: "Season")', function() {
      // uncomment below and update the code to test the property season
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property seasonType (base name: "SeasonType")', function() {
      // uncomment below and update the code to test the property seasonType
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property stadiumDetails (base name: "StadiumDetails")', function() {
      // uncomment below and update the code to test the property stadiumDetails
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property stadiumID (base name: "StadiumID")', function() {
      // uncomment below and update the code to test the property stadiumID
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "Status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property timeRemaining (base name: "TimeRemaining")', function() {
      // uncomment below and update the code to test the property timeRemaining
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property underPayout (base name: "UnderPayout")', function() {
      // uncomment below and update the code to test the property underPayout
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property week (base name: "Week")', function() {
      // uncomment below and update the code to test the property week
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property yardLine (base name: "YardLine")', function() {
      // uncomment below and update the code to test the property yardLine
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

    it('should have the property yardLineTerritory (base name: "YardLineTerritory")', function() {
      // uncomment below and update the code to test the property yardLineTerritory
      //var instance = new NflV3PlayByPlay.Score();
      //expect(instance).to.be();
    });

  });

}));
