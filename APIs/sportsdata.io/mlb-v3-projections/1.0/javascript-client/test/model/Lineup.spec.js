/**
 * MLB v3 Projections
 * MLB projections API.
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
    factory(root.expect, root.MlbV3Projections);
  }
}(this, function(expect, MlbV3Projections) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MlbV3Projections.Lineup();
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

  describe('Lineup', function() {
    it('should create an instance of Lineup', function() {
      // uncomment below and update the code to test Lineup
      //var instance = new MlbV3Projections.Lineup();
      //expect(instance).to.be.a(MlbV3Projections.Lineup);
    });

    it('should have the property battingOrder (base name: "BattingOrder")', function() {
      // uncomment below and update the code to test the property battingOrder
      //var instance = new MlbV3Projections.Lineup();
      //expect(instance).to.be();
    });

    it('should have the property confirmed (base name: "Confirmed")', function() {
      // uncomment below and update the code to test the property confirmed
      //var instance = new MlbV3Projections.Lineup();
      //expect(instance).to.be();
    });

    it('should have the property firstName (base name: "FirstName")', function() {
      // uncomment below and update the code to test the property firstName
      //var instance = new MlbV3Projections.Lineup();
      //expect(instance).to.be();
    });

    it('should have the property lastName (base name: "LastName")', function() {
      // uncomment below and update the code to test the property lastName
      //var instance = new MlbV3Projections.Lineup();
      //expect(instance).to.be();
    });

    it('should have the property playerID (base name: "PlayerID")', function() {
      // uncomment below and update the code to test the property playerID
      //var instance = new MlbV3Projections.Lineup();
      //expect(instance).to.be();
    });

    it('should have the property position (base name: "Position")', function() {
      // uncomment below and update the code to test the property position
      //var instance = new MlbV3Projections.Lineup();
      //expect(instance).to.be();
    });

    it('should have the property starting (base name: "Starting")', function() {
      // uncomment below and update the code to test the property starting
      //var instance = new MlbV3Projections.Lineup();
      //expect(instance).to.be();
    });

    it('should have the property team (base name: "Team")', function() {
      // uncomment below and update the code to test the property team
      //var instance = new MlbV3Projections.Lineup();
      //expect(instance).to.be();
    });

    it('should have the property teamID (base name: "TeamID")', function() {
      // uncomment below and update the code to test the property teamID
      //var instance = new MlbV3Projections.Lineup();
      //expect(instance).to.be();
    });

  });

}));
