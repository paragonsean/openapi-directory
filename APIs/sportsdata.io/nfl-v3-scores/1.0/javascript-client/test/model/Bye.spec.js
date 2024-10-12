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
    instance = new NflV3Scores.Bye();
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

  describe('Bye', function() {
    it('should create an instance of Bye', function() {
      // uncomment below and update the code to test Bye
      //var instance = new NflV3Scores.Bye();
      //expect(instance).to.be.a(NflV3Scores.Bye);
    });

    it('should have the property season (base name: "Season")', function() {
      // uncomment below and update the code to test the property season
      //var instance = new NflV3Scores.Bye();
      //expect(instance).to.be();
    });

    it('should have the property team (base name: "Team")', function() {
      // uncomment below and update the code to test the property team
      //var instance = new NflV3Scores.Bye();
      //expect(instance).to.be();
    });

    it('should have the property week (base name: "Week")', function() {
      // uncomment below and update the code to test the property week
      //var instance = new NflV3Scores.Bye();
      //expect(instance).to.be();
    });

  });

}));
