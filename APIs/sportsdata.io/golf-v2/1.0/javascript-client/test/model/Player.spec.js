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
    instance = new GolfV2.Player();
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
      //var instance = new GolfV2.Player();
      //expect(instance).to.be.a(GolfV2.Player);
    });

    it('should have the property birthCity (base name: "BirthCity")', function() {
      // uncomment below and update the code to test the property birthCity
      //var instance = new GolfV2.Player();
      //expect(instance).to.be();
    });

    it('should have the property birthDate (base name: "BirthDate")', function() {
      // uncomment below and update the code to test the property birthDate
      //var instance = new GolfV2.Player();
      //expect(instance).to.be();
    });

    it('should have the property birthState (base name: "BirthState")', function() {
      // uncomment below and update the code to test the property birthState
      //var instance = new GolfV2.Player();
      //expect(instance).to.be();
    });

    it('should have the property college (base name: "College")', function() {
      // uncomment below and update the code to test the property college
      //var instance = new GolfV2.Player();
      //expect(instance).to.be();
    });

    it('should have the property country (base name: "Country")', function() {
      // uncomment below and update the code to test the property country
      //var instance = new GolfV2.Player();
      //expect(instance).to.be();
    });

    it('should have the property draftKingsName (base name: "DraftKingsName")', function() {
      // uncomment below and update the code to test the property draftKingsName
      //var instance = new GolfV2.Player();
      //expect(instance).to.be();
    });

    it('should have the property draftKingsPlayerID (base name: "DraftKingsPlayerID")', function() {
      // uncomment below and update the code to test the property draftKingsPlayerID
      //var instance = new GolfV2.Player();
      //expect(instance).to.be();
    });

    it('should have the property fanDuelName (base name: "FanDuelName")', function() {
      // uncomment below and update the code to test the property fanDuelName
      //var instance = new GolfV2.Player();
      //expect(instance).to.be();
    });

    it('should have the property fanDuelPlayerID (base name: "FanDuelPlayerID")', function() {
      // uncomment below and update the code to test the property fanDuelPlayerID
      //var instance = new GolfV2.Player();
      //expect(instance).to.be();
    });

    it('should have the property fantasyAlarmPlayerID (base name: "FantasyAlarmPlayerID")', function() {
      // uncomment below and update the code to test the property fantasyAlarmPlayerID
      //var instance = new GolfV2.Player();
      //expect(instance).to.be();
    });

    it('should have the property fantasyDraftName (base name: "FantasyDraftName")', function() {
      // uncomment below and update the code to test the property fantasyDraftName
      //var instance = new GolfV2.Player();
      //expect(instance).to.be();
    });

    it('should have the property fantasyDraftPlayerID (base name: "FantasyDraftPlayerID")', function() {
      // uncomment below and update the code to test the property fantasyDraftPlayerID
      //var instance = new GolfV2.Player();
      //expect(instance).to.be();
    });

    it('should have the property firstName (base name: "FirstName")', function() {
      // uncomment below and update the code to test the property firstName
      //var instance = new GolfV2.Player();
      //expect(instance).to.be();
    });

    it('should have the property lastName (base name: "LastName")', function() {
      // uncomment below and update the code to test the property lastName
      //var instance = new GolfV2.Player();
      //expect(instance).to.be();
    });

    it('should have the property pgaDebut (base name: "PgaDebut")', function() {
      // uncomment below and update the code to test the property pgaDebut
      //var instance = new GolfV2.Player();
      //expect(instance).to.be();
    });

    it('should have the property pgaTourPlayerID (base name: "PgaTourPlayerID")', function() {
      // uncomment below and update the code to test the property pgaTourPlayerID
      //var instance = new GolfV2.Player();
      //expect(instance).to.be();
    });

    it('should have the property photoUrl (base name: "PhotoUrl")', function() {
      // uncomment below and update the code to test the property photoUrl
      //var instance = new GolfV2.Player();
      //expect(instance).to.be();
    });

    it('should have the property playerID (base name: "PlayerID")', function() {
      // uncomment below and update the code to test the property playerID
      //var instance = new GolfV2.Player();
      //expect(instance).to.be();
    });

    it('should have the property rotoWirePlayerID (base name: "RotoWirePlayerID")', function() {
      // uncomment below and update the code to test the property rotoWirePlayerID
      //var instance = new GolfV2.Player();
      //expect(instance).to.be();
    });

    it('should have the property rotoworldPlayerID (base name: "RotoworldPlayerID")', function() {
      // uncomment below and update the code to test the property rotoworldPlayerID
      //var instance = new GolfV2.Player();
      //expect(instance).to.be();
    });

    it('should have the property sportRadarPlayerID (base name: "SportRadarPlayerID")', function() {
      // uncomment below and update the code to test the property sportRadarPlayerID
      //var instance = new GolfV2.Player();
      //expect(instance).to.be();
    });

    it('should have the property swings (base name: "Swings")', function() {
      // uncomment below and update the code to test the property swings
      //var instance = new GolfV2.Player();
      //expect(instance).to.be();
    });

    it('should have the property weight (base name: "Weight")', function() {
      // uncomment below and update the code to test the property weight
      //var instance = new GolfV2.Player();
      //expect(instance).to.be();
    });

    it('should have the property yahooPlayerID (base name: "YahooPlayerID")', function() {
      // uncomment below and update the code to test the property yahooPlayerID
      //var instance = new GolfV2.Player();
      //expect(instance).to.be();
    });

  });

}));
