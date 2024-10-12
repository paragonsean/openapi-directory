/**
 * CS:GO v3 Stats
 * CS:GO v3 Stats
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
    factory(root.expect, root.CsgoV3Stats);
  }
}(this, function(expect, CsgoV3Stats) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new CsgoV3Stats.Season();
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

  describe('Season', function() {
    it('should create an instance of Season', function() {
      // uncomment below and update the code to test Season
      //var instance = new CsgoV3Stats.Season();
      //expect(instance).to.be.a(CsgoV3Stats.Season);
    });

    it('should have the property competitionId (base name: "CompetitionId")', function() {
      // uncomment below and update the code to test the property competitionId
      //var instance = new CsgoV3Stats.Season();
      //expect(instance).to.be();
    });

    it('should have the property competitionName (base name: "CompetitionName")', function() {
      // uncomment below and update the code to test the property competitionName
      //var instance = new CsgoV3Stats.Season();
      //expect(instance).to.be();
    });

    it('should have the property currentSeason (base name: "CurrentSeason")', function() {
      // uncomment below and update the code to test the property currentSeason
      //var instance = new CsgoV3Stats.Season();
      //expect(instance).to.be();
    });

    it('should have the property endDate (base name: "EndDate")', function() {
      // uncomment below and update the code to test the property endDate
      //var instance = new CsgoV3Stats.Season();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "Name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new CsgoV3Stats.Season();
      //expect(instance).to.be();
    });

    it('should have the property rounds (base name: "Rounds")', function() {
      // uncomment below and update the code to test the property rounds
      //var instance = new CsgoV3Stats.Season();
      //expect(instance).to.be();
    });

    it('should have the property season (base name: "Season")', function() {
      // uncomment below and update the code to test the property season
      //var instance = new CsgoV3Stats.Season();
      //expect(instance).to.be();
    });

    it('should have the property seasonId (base name: "SeasonId")', function() {
      // uncomment below and update the code to test the property seasonId
      //var instance = new CsgoV3Stats.Season();
      //expect(instance).to.be();
    });

    it('should have the property startDate (base name: "StartDate")', function() {
      // uncomment below and update the code to test the property startDate
      //var instance = new CsgoV3Stats.Season();
      //expect(instance).to.be();
    });

  });

}));
