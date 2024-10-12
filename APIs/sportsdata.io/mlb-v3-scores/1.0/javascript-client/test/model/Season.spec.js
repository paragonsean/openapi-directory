/**
 * MLB v3 Scores
 * MLB scores API.
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
    factory(root.expect, root.MlbV3Scores);
  }
}(this, function(expect, MlbV3Scores) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MlbV3Scores.Season();
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
      //var instance = new MlbV3Scores.Season();
      //expect(instance).to.be.a(MlbV3Scores.Season);
    });

    it('should have the property apiSeason (base name: "ApiSeason")', function() {
      // uncomment below and update the code to test the property apiSeason
      //var instance = new MlbV3Scores.Season();
      //expect(instance).to.be();
    });

    it('should have the property postSeasonStartDate (base name: "PostSeasonStartDate")', function() {
      // uncomment below and update the code to test the property postSeasonStartDate
      //var instance = new MlbV3Scores.Season();
      //expect(instance).to.be();
    });

    it('should have the property regularSeasonStartDate (base name: "RegularSeasonStartDate")', function() {
      // uncomment below and update the code to test the property regularSeasonStartDate
      //var instance = new MlbV3Scores.Season();
      //expect(instance).to.be();
    });

    it('should have the property season (base name: "Season")', function() {
      // uncomment below and update the code to test the property season
      //var instance = new MlbV3Scores.Season();
      //expect(instance).to.be();
    });

    it('should have the property seasonType (base name: "SeasonType")', function() {
      // uncomment below and update the code to test the property seasonType
      //var instance = new MlbV3Scores.Season();
      //expect(instance).to.be();
    });

  });

}));
