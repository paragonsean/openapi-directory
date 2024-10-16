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
    instance = new CbbV3Scores.Player();
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

  describe('Player', function() {
    it('should create an instance of Player', function() {
      // uncomment below and update the code to test Player
      //var instance = new CbbV3Scores.Player();
      //expect(instance).to.be.a(CbbV3Scores.Player);
    });

    it('should have the property birthCity (base name: "BirthCity")', function() {
      // uncomment below and update the code to test the property birthCity
      //var instance = new CbbV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property birthState (base name: "BirthState")', function() {
      // uncomment below and update the code to test the property birthState
      //var instance = new CbbV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property _class (base name: "Class")', function() {
      // uncomment below and update the code to test the property _class
      //var instance = new CbbV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property fantasyAlarmPlayerID (base name: "FantasyAlarmPlayerID")', function() {
      // uncomment below and update the code to test the property fantasyAlarmPlayerID
      //var instance = new CbbV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property firstName (base name: "FirstName")', function() {
      // uncomment below and update the code to test the property firstName
      //var instance = new CbbV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property globalTeamID (base name: "GlobalTeamID")', function() {
      // uncomment below and update the code to test the property globalTeamID
      //var instance = new CbbV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property height (base name: "Height")', function() {
      // uncomment below and update the code to test the property height
      //var instance = new CbbV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property highSchool (base name: "HighSchool")', function() {
      // uncomment below and update the code to test the property highSchool
      //var instance = new CbbV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property injuryBodyPart (base name: "InjuryBodyPart")', function() {
      // uncomment below and update the code to test the property injuryBodyPart
      //var instance = new CbbV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property injuryNotes (base name: "InjuryNotes")', function() {
      // uncomment below and update the code to test the property injuryNotes
      //var instance = new CbbV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property injuryStartDate (base name: "InjuryStartDate")', function() {
      // uncomment below and update the code to test the property injuryStartDate
      //var instance = new CbbV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property injuryStatus (base name: "InjuryStatus")', function() {
      // uncomment below and update the code to test the property injuryStatus
      //var instance = new CbbV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property jersey (base name: "Jersey")', function() {
      // uncomment below and update the code to test the property jersey
      //var instance = new CbbV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property lastName (base name: "LastName")', function() {
      // uncomment below and update the code to test the property lastName
      //var instance = new CbbV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property playerID (base name: "PlayerID")', function() {
      // uncomment below and update the code to test the property playerID
      //var instance = new CbbV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property position (base name: "Position")', function() {
      // uncomment below and update the code to test the property position
      //var instance = new CbbV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property rotoWirePlayerID (base name: "RotoWirePlayerID")', function() {
      // uncomment below and update the code to test the property rotoWirePlayerID
      //var instance = new CbbV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property rotoworldPlayerID (base name: "RotoworldPlayerID")', function() {
      // uncomment below and update the code to test the property rotoworldPlayerID
      //var instance = new CbbV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property sportRadarPlayerID (base name: "SportRadarPlayerID")', function() {
      // uncomment below and update the code to test the property sportRadarPlayerID
      //var instance = new CbbV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property team (base name: "Team")', function() {
      // uncomment below and update the code to test the property team
      //var instance = new CbbV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property teamID (base name: "TeamID")', function() {
      // uncomment below and update the code to test the property teamID
      //var instance = new CbbV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property weight (base name: "Weight")', function() {
      // uncomment below and update the code to test the property weight
      //var instance = new CbbV3Scores.Player();
      //expect(instance).to.be();
    });

  });

}));
