/**
 * NHL v3 Scores
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
    factory(root.expect, root.NhlV3Scores);
  }
}(this, function(expect, NhlV3Scores) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NhlV3Scores.PlayerBasic();
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

  describe('PlayerBasic', function() {
    it('should create an instance of PlayerBasic', function() {
      // uncomment below and update the code to test PlayerBasic
      //var instance = new NhlV3Scores.PlayerBasic();
      //expect(instance).to.be.a(NhlV3Scores.PlayerBasic);
    });

    it('should have the property birthCity (base name: "BirthCity")', function() {
      // uncomment below and update the code to test the property birthCity
      //var instance = new NhlV3Scores.PlayerBasic();
      //expect(instance).to.be();
    });

    it('should have the property birthDate (base name: "BirthDate")', function() {
      // uncomment below and update the code to test the property birthDate
      //var instance = new NhlV3Scores.PlayerBasic();
      //expect(instance).to.be();
    });

    it('should have the property birthState (base name: "BirthState")', function() {
      // uncomment below and update the code to test the property birthState
      //var instance = new NhlV3Scores.PlayerBasic();
      //expect(instance).to.be();
    });

    it('should have the property firstName (base name: "FirstName")', function() {
      // uncomment below and update the code to test the property firstName
      //var instance = new NhlV3Scores.PlayerBasic();
      //expect(instance).to.be();
    });

    it('should have the property globalTeamID (base name: "GlobalTeamID")', function() {
      // uncomment below and update the code to test the property globalTeamID
      //var instance = new NhlV3Scores.PlayerBasic();
      //expect(instance).to.be();
    });

    it('should have the property height (base name: "Height")', function() {
      // uncomment below and update the code to test the property height
      //var instance = new NhlV3Scores.PlayerBasic();
      //expect(instance).to.be();
    });

    it('should have the property jersey (base name: "Jersey")', function() {
      // uncomment below and update the code to test the property jersey
      //var instance = new NhlV3Scores.PlayerBasic();
      //expect(instance).to.be();
    });

    it('should have the property lastName (base name: "LastName")', function() {
      // uncomment below and update the code to test the property lastName
      //var instance = new NhlV3Scores.PlayerBasic();
      //expect(instance).to.be();
    });

    it('should have the property playerID (base name: "PlayerID")', function() {
      // uncomment below and update the code to test the property playerID
      //var instance = new NhlV3Scores.PlayerBasic();
      //expect(instance).to.be();
    });

    it('should have the property position (base name: "Position")', function() {
      // uncomment below and update the code to test the property position
      //var instance = new NhlV3Scores.PlayerBasic();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "Status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new NhlV3Scores.PlayerBasic();
      //expect(instance).to.be();
    });

    it('should have the property team (base name: "Team")', function() {
      // uncomment below and update the code to test the property team
      //var instance = new NhlV3Scores.PlayerBasic();
      //expect(instance).to.be();
    });

    it('should have the property teamID (base name: "TeamID")', function() {
      // uncomment below and update the code to test the property teamID
      //var instance = new NhlV3Scores.PlayerBasic();
      //expect(instance).to.be();
    });

    it('should have the property weight (base name: "Weight")', function() {
      // uncomment below and update the code to test the property weight
      //var instance = new NhlV3Scores.PlayerBasic();
      //expect(instance).to.be();
    });

  });

}));
