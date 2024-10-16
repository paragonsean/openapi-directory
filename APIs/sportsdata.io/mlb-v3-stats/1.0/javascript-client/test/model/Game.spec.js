/**
 * MLB v3 Stats
 * MLB scores, stats, and news API.
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
    factory(root.expect, root.MlbV3Stats);
  }
}(this, function(expect, MlbV3Stats) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MlbV3Stats.Game();
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
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be.a(MlbV3Stats.Game);
    });

    it('should have the property attendance (base name: "Attendance")', function() {
      // uncomment below and update the code to test the property attendance
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property awayRotationNumber (base name: "AwayRotationNumber")', function() {
      // uncomment below and update the code to test the property awayRotationNumber
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property awayTeam (base name: "AwayTeam")', function() {
      // uncomment below and update the code to test the property awayTeam
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property awayTeamErrors (base name: "AwayTeamErrors")', function() {
      // uncomment below and update the code to test the property awayTeamErrors
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property awayTeamHits (base name: "AwayTeamHits")', function() {
      // uncomment below and update the code to test the property awayTeamHits
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property awayTeamID (base name: "AwayTeamID")', function() {
      // uncomment below and update the code to test the property awayTeamID
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property awayTeamMoneyLine (base name: "AwayTeamMoneyLine")', function() {
      // uncomment below and update the code to test the property awayTeamMoneyLine
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property awayTeamProbablePitcherID (base name: "AwayTeamProbablePitcherID")', function() {
      // uncomment below and update the code to test the property awayTeamProbablePitcherID
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property awayTeamRuns (base name: "AwayTeamRuns")', function() {
      // uncomment below and update the code to test the property awayTeamRuns
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property awayTeamStartingPitcher (base name: "AwayTeamStartingPitcher")', function() {
      // uncomment below and update the code to test the property awayTeamStartingPitcher
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property awayTeamStartingPitcherID (base name: "AwayTeamStartingPitcherID")', function() {
      // uncomment below and update the code to test the property awayTeamStartingPitcherID
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property balls (base name: "Balls")', function() {
      // uncomment below and update the code to test the property balls
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property channel (base name: "Channel")', function() {
      // uncomment below and update the code to test the property channel
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property currentHitter (base name: "CurrentHitter")', function() {
      // uncomment below and update the code to test the property currentHitter
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property currentHitterID (base name: "CurrentHitterID")', function() {
      // uncomment below and update the code to test the property currentHitterID
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property currentHittingTeamID (base name: "CurrentHittingTeamID")', function() {
      // uncomment below and update the code to test the property currentHittingTeamID
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property currentPitcher (base name: "CurrentPitcher")', function() {
      // uncomment below and update the code to test the property currentPitcher
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property currentPitcherID (base name: "CurrentPitcherID")', function() {
      // uncomment below and update the code to test the property currentPitcherID
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property currentPitchingTeamID (base name: "CurrentPitchingTeamID")', function() {
      // uncomment below and update the code to test the property currentPitchingTeamID
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property dateTime (base name: "DateTime")', function() {
      // uncomment below and update the code to test the property dateTime
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property dateTimeUTC (base name: "DateTimeUTC")', function() {
      // uncomment below and update the code to test the property dateTimeUTC
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property day (base name: "Day")', function() {
      // uncomment below and update the code to test the property day
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property dueUpHitterID1 (base name: "DueUpHitterID1")', function() {
      // uncomment below and update the code to test the property dueUpHitterID1
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property dueUpHitterID2 (base name: "DueUpHitterID2")', function() {
      // uncomment below and update the code to test the property dueUpHitterID2
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property dueUpHitterID3 (base name: "DueUpHitterID3")', function() {
      // uncomment below and update the code to test the property dueUpHitterID3
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property forecastDescription (base name: "ForecastDescription")', function() {
      // uncomment below and update the code to test the property forecastDescription
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property forecastTempHigh (base name: "ForecastTempHigh")', function() {
      // uncomment below and update the code to test the property forecastTempHigh
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property forecastTempLow (base name: "ForecastTempLow")', function() {
      // uncomment below and update the code to test the property forecastTempLow
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property forecastWindChill (base name: "ForecastWindChill")', function() {
      // uncomment below and update the code to test the property forecastWindChill
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property forecastWindDirection (base name: "ForecastWindDirection")', function() {
      // uncomment below and update the code to test the property forecastWindDirection
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property forecastWindSpeed (base name: "ForecastWindSpeed")', function() {
      // uncomment below and update the code to test the property forecastWindSpeed
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property gameEndDateTime (base name: "GameEndDateTime")', function() {
      // uncomment below and update the code to test the property gameEndDateTime
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property gameID (base name: "GameID")', function() {
      // uncomment below and update the code to test the property gameID
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property globalAwayTeamID (base name: "GlobalAwayTeamID")', function() {
      // uncomment below and update the code to test the property globalAwayTeamID
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property globalGameID (base name: "GlobalGameID")', function() {
      // uncomment below and update the code to test the property globalGameID
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property globalHomeTeamID (base name: "GlobalHomeTeamID")', function() {
      // uncomment below and update the code to test the property globalHomeTeamID
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property homeRotationNumber (base name: "HomeRotationNumber")', function() {
      // uncomment below and update the code to test the property homeRotationNumber
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property homeTeam (base name: "HomeTeam")', function() {
      // uncomment below and update the code to test the property homeTeam
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property homeTeamErrors (base name: "HomeTeamErrors")', function() {
      // uncomment below and update the code to test the property homeTeamErrors
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property homeTeamHits (base name: "HomeTeamHits")', function() {
      // uncomment below and update the code to test the property homeTeamHits
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property homeTeamID (base name: "HomeTeamID")', function() {
      // uncomment below and update the code to test the property homeTeamID
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property homeTeamMoneyLine (base name: "HomeTeamMoneyLine")', function() {
      // uncomment below and update the code to test the property homeTeamMoneyLine
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property homeTeamProbablePitcherID (base name: "HomeTeamProbablePitcherID")', function() {
      // uncomment below and update the code to test the property homeTeamProbablePitcherID
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property homeTeamRuns (base name: "HomeTeamRuns")', function() {
      // uncomment below and update the code to test the property homeTeamRuns
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property homeTeamStartingPitcher (base name: "HomeTeamStartingPitcher")', function() {
      // uncomment below and update the code to test the property homeTeamStartingPitcher
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property homeTeamStartingPitcherID (base name: "HomeTeamStartingPitcherID")', function() {
      // uncomment below and update the code to test the property homeTeamStartingPitcherID
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property inning (base name: "Inning")', function() {
      // uncomment below and update the code to test the property inning
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property inningDescription (base name: "InningDescription")', function() {
      // uncomment below and update the code to test the property inningDescription
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property inningHalf (base name: "InningHalf")', function() {
      // uncomment below and update the code to test the property inningHalf
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property innings (base name: "Innings")', function() {
      // uncomment below and update the code to test the property innings
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property isClosed (base name: "IsClosed")', function() {
      // uncomment below and update the code to test the property isClosed
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property lastPlay (base name: "LastPlay")', function() {
      // uncomment below and update the code to test the property lastPlay
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property losingPitcher (base name: "LosingPitcher")', function() {
      // uncomment below and update the code to test the property losingPitcher
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property losingPitcherID (base name: "LosingPitcherID")', function() {
      // uncomment below and update the code to test the property losingPitcherID
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property neutralVenue (base name: "NeutralVenue")', function() {
      // uncomment below and update the code to test the property neutralVenue
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property outs (base name: "Outs")', function() {
      // uncomment below and update the code to test the property outs
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property overPayout (base name: "OverPayout")', function() {
      // uncomment below and update the code to test the property overPayout
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property overUnder (base name: "OverUnder")', function() {
      // uncomment below and update the code to test the property overUnder
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property pointSpread (base name: "PointSpread")', function() {
      // uncomment below and update the code to test the property pointSpread
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property pointSpreadAwayTeamMoneyLine (base name: "PointSpreadAwayTeamMoneyLine")', function() {
      // uncomment below and update the code to test the property pointSpreadAwayTeamMoneyLine
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property pointSpreadHomeTeamMoneyLine (base name: "PointSpreadHomeTeamMoneyLine")', function() {
      // uncomment below and update the code to test the property pointSpreadHomeTeamMoneyLine
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property rescheduledFromGameID (base name: "RescheduledFromGameID")', function() {
      // uncomment below and update the code to test the property rescheduledFromGameID
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property rescheduledGameID (base name: "RescheduledGameID")', function() {
      // uncomment below and update the code to test the property rescheduledGameID
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property runnerOnFirst (base name: "RunnerOnFirst")', function() {
      // uncomment below and update the code to test the property runnerOnFirst
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property runnerOnSecond (base name: "RunnerOnSecond")', function() {
      // uncomment below and update the code to test the property runnerOnSecond
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property runnerOnThird (base name: "RunnerOnThird")', function() {
      // uncomment below and update the code to test the property runnerOnThird
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property savingPitcher (base name: "SavingPitcher")', function() {
      // uncomment below and update the code to test the property savingPitcher
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property savingPitcherID (base name: "SavingPitcherID")', function() {
      // uncomment below and update the code to test the property savingPitcherID
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property season (base name: "Season")', function() {
      // uncomment below and update the code to test the property season
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property seasonType (base name: "SeasonType")', function() {
      // uncomment below and update the code to test the property seasonType
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property seriesInfo (base name: "SeriesInfo")', function() {
      // uncomment below and update the code to test the property seriesInfo
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property stadiumID (base name: "StadiumID")', function() {
      // uncomment below and update the code to test the property stadiumID
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "Status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property strikes (base name: "Strikes")', function() {
      // uncomment below and update the code to test the property strikes
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property underPayout (base name: "UnderPayout")', function() {
      // uncomment below and update the code to test the property underPayout
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property updated (base name: "Updated")', function() {
      // uncomment below and update the code to test the property updated
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property winningPitcher (base name: "WinningPitcher")', function() {
      // uncomment below and update the code to test the property winningPitcher
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

    it('should have the property winningPitcherID (base name: "WinningPitcherID")', function() {
      // uncomment below and update the code to test the property winningPitcherID
      //var instance = new MlbV3Stats.Game();
      //expect(instance).to.be();
    });

  });

}));
