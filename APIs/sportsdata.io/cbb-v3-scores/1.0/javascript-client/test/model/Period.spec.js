/**
 * CBB v3 Scores
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
    factory(root.expect, root.CbbV3Scores);
  }
}(this, function(expect, CbbV3Scores) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new CbbV3Scores.Period();
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

  describe('Period', function() {
    it('should create an instance of Period', function() {
      // uncomment below and update the code to test Period
      //var instance = new CbbV3Scores.Period();
      //expect(instance).to.be.a(CbbV3Scores.Period);
    });

    it('should have the property awayScore (base name: "AwayScore")', function() {
      // uncomment below and update the code to test the property awayScore
      //var instance = new CbbV3Scores.Period();
      //expect(instance).to.be();
    });

    it('should have the property gameID (base name: "GameID")', function() {
      // uncomment below and update the code to test the property gameID
      //var instance = new CbbV3Scores.Period();
      //expect(instance).to.be();
    });

    it('should have the property homeScore (base name: "HomeScore")', function() {
      // uncomment below and update the code to test the property homeScore
      //var instance = new CbbV3Scores.Period();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "Name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new CbbV3Scores.Period();
      //expect(instance).to.be();
    });

    it('should have the property number (base name: "Number")', function() {
      // uncomment below and update the code to test the property number
      //var instance = new CbbV3Scores.Period();
      //expect(instance).to.be();
    });

    it('should have the property periodID (base name: "PeriodID")', function() {
      // uncomment below and update the code to test the property periodID
      //var instance = new CbbV3Scores.Period();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "Type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new CbbV3Scores.Period();
      //expect(instance).to.be();
    });

  });

}));
