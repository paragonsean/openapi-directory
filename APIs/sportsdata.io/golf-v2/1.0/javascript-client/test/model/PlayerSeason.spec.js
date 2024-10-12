/**
 * Golf v2
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
    factory(root.expect, root.GolfV2);
  }
}(this, function(expect, GolfV2) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new GolfV2.PlayerSeason();
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

  describe('PlayerSeason', function() {
    it('should create an instance of PlayerSeason', function() {
      // uncomment below and update the code to test PlayerSeason
      //var instance = new GolfV2.PlayerSeason();
      //expect(instance).to.be.a(GolfV2.PlayerSeason);
    });

    it('should have the property averagePoints (base name: "AveragePoints")', function() {
      // uncomment below and update the code to test the property averagePoints
      //var instance = new GolfV2.PlayerSeason();
      //expect(instance).to.be();
    });

    it('should have the property events (base name: "Events")', function() {
      // uncomment below and update the code to test the property events
      //var instance = new GolfV2.PlayerSeason();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "Name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new GolfV2.PlayerSeason();
      //expect(instance).to.be();
    });

    it('should have the property playerID (base name: "PlayerID")', function() {
      // uncomment below and update the code to test the property playerID
      //var instance = new GolfV2.PlayerSeason();
      //expect(instance).to.be();
    });

    it('should have the property playerSeasonID (base name: "PlayerSeasonID")', function() {
      // uncomment below and update the code to test the property playerSeasonID
      //var instance = new GolfV2.PlayerSeason();
      //expect(instance).to.be();
    });

    it('should have the property pointsGained (base name: "PointsGained")', function() {
      // uncomment below and update the code to test the property pointsGained
      //var instance = new GolfV2.PlayerSeason();
      //expect(instance).to.be();
    });

    it('should have the property pointsLost (base name: "PointsLost")', function() {
      // uncomment below and update the code to test the property pointsLost
      //var instance = new GolfV2.PlayerSeason();
      //expect(instance).to.be();
    });

    it('should have the property season (base name: "Season")', function() {
      // uncomment below and update the code to test the property season
      //var instance = new GolfV2.PlayerSeason();
      //expect(instance).to.be();
    });

    it('should have the property totalPoints (base name: "TotalPoints")', function() {
      // uncomment below and update the code to test the property totalPoints
      //var instance = new GolfV2.PlayerSeason();
      //expect(instance).to.be();
    });

    it('should have the property worldGolfRank (base name: "WorldGolfRank")', function() {
      // uncomment below and update the code to test the property worldGolfRank
      //var instance = new GolfV2.PlayerSeason();
      //expect(instance).to.be();
    });

    it('should have the property worldGolfRankLastWeek (base name: "WorldGolfRankLastWeek")', function() {
      // uncomment below and update the code to test the property worldGolfRankLastWeek
      //var instance = new GolfV2.PlayerSeason();
      //expect(instance).to.be();
    });

  });

}));
