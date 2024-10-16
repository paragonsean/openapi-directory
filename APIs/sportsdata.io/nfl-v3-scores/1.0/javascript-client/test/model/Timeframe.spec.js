/**
 * NFL v3 Scores
 * NFL schedules, scores, odds, weather, and news API.
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
    factory(root.expect, root.NflV3Scores);
  }
}(this, function(expect, NflV3Scores) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NflV3Scores.Timeframe();
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

  describe('Timeframe', function() {
    it('should create an instance of Timeframe', function() {
      // uncomment below and update the code to test Timeframe
      //var instance = new NflV3Scores.Timeframe();
      //expect(instance).to.be.a(NflV3Scores.Timeframe);
    });

    it('should have the property apiSeason (base name: "ApiSeason")', function() {
      // uncomment below and update the code to test the property apiSeason
      //var instance = new NflV3Scores.Timeframe();
      //expect(instance).to.be();
    });

    it('should have the property apiWeek (base name: "ApiWeek")', function() {
      // uncomment below and update the code to test the property apiWeek
      //var instance = new NflV3Scores.Timeframe();
      //expect(instance).to.be();
    });

    it('should have the property endDate (base name: "EndDate")', function() {
      // uncomment below and update the code to test the property endDate
      //var instance = new NflV3Scores.Timeframe();
      //expect(instance).to.be();
    });

    it('should have the property firstGameEnd (base name: "FirstGameEnd")', function() {
      // uncomment below and update the code to test the property firstGameEnd
      //var instance = new NflV3Scores.Timeframe();
      //expect(instance).to.be();
    });

    it('should have the property firstGameStart (base name: "FirstGameStart")', function() {
      // uncomment below and update the code to test the property firstGameStart
      //var instance = new NflV3Scores.Timeframe();
      //expect(instance).to.be();
    });

    it('should have the property hasEnded (base name: "HasEnded")', function() {
      // uncomment below and update the code to test the property hasEnded
      //var instance = new NflV3Scores.Timeframe();
      //expect(instance).to.be();
    });

    it('should have the property hasFirstGameEnded (base name: "HasFirstGameEnded")', function() {
      // uncomment below and update the code to test the property hasFirstGameEnded
      //var instance = new NflV3Scores.Timeframe();
      //expect(instance).to.be();
    });

    it('should have the property hasFirstGameStarted (base name: "HasFirstGameStarted")', function() {
      // uncomment below and update the code to test the property hasFirstGameStarted
      //var instance = new NflV3Scores.Timeframe();
      //expect(instance).to.be();
    });

    it('should have the property hasGames (base name: "HasGames")', function() {
      // uncomment below and update the code to test the property hasGames
      //var instance = new NflV3Scores.Timeframe();
      //expect(instance).to.be();
    });

    it('should have the property hasLastGameEnded (base name: "HasLastGameEnded")', function() {
      // uncomment below and update the code to test the property hasLastGameEnded
      //var instance = new NflV3Scores.Timeframe();
      //expect(instance).to.be();
    });

    it('should have the property hasStarted (base name: "HasStarted")', function() {
      // uncomment below and update the code to test the property hasStarted
      //var instance = new NflV3Scores.Timeframe();
      //expect(instance).to.be();
    });

    it('should have the property lastGameEnd (base name: "LastGameEnd")', function() {
      // uncomment below and update the code to test the property lastGameEnd
      //var instance = new NflV3Scores.Timeframe();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "Name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new NflV3Scores.Timeframe();
      //expect(instance).to.be();
    });

    it('should have the property season (base name: "Season")', function() {
      // uncomment below and update the code to test the property season
      //var instance = new NflV3Scores.Timeframe();
      //expect(instance).to.be();
    });

    it('should have the property seasonType (base name: "SeasonType")', function() {
      // uncomment below and update the code to test the property seasonType
      //var instance = new NflV3Scores.Timeframe();
      //expect(instance).to.be();
    });

    it('should have the property shortName (base name: "ShortName")', function() {
      // uncomment below and update the code to test the property shortName
      //var instance = new NflV3Scores.Timeframe();
      //expect(instance).to.be();
    });

    it('should have the property startDate (base name: "StartDate")', function() {
      // uncomment below and update the code to test the property startDate
      //var instance = new NflV3Scores.Timeframe();
      //expect(instance).to.be();
    });

    it('should have the property week (base name: "Week")', function() {
      // uncomment below and update the code to test the property week
      //var instance = new NflV3Scores.Timeframe();
      //expect(instance).to.be();
    });

  });

}));
