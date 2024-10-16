/**
 * NBA v3 Scores
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
    factory(root.expect, root.NbaV3Scores);
  }
}(this, function(expect, NbaV3Scores) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NbaV3Scores.Player();
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
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be.a(NbaV3Scores.Player);
    });

    it('should have the property birthCity (base name: "BirthCity")', function() {
      // uncomment below and update the code to test the property birthCity
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property birthCountry (base name: "BirthCountry")', function() {
      // uncomment below and update the code to test the property birthCountry
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property birthDate (base name: "BirthDate")', function() {
      // uncomment below and update the code to test the property birthDate
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property birthState (base name: "BirthState")', function() {
      // uncomment below and update the code to test the property birthState
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property college (base name: "College")', function() {
      // uncomment below and update the code to test the property college
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property depthChartOrder (base name: "DepthChartOrder")', function() {
      // uncomment below and update the code to test the property depthChartOrder
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property depthChartPosition (base name: "DepthChartPosition")', function() {
      // uncomment below and update the code to test the property depthChartPosition
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property draftKingsName (base name: "DraftKingsName")', function() {
      // uncomment below and update the code to test the property draftKingsName
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property draftKingsPlayerID (base name: "DraftKingsPlayerID")', function() {
      // uncomment below and update the code to test the property draftKingsPlayerID
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property experience (base name: "Experience")', function() {
      // uncomment below and update the code to test the property experience
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property fanDuelName (base name: "FanDuelName")', function() {
      // uncomment below and update the code to test the property fanDuelName
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property fanDuelPlayerID (base name: "FanDuelPlayerID")', function() {
      // uncomment below and update the code to test the property fanDuelPlayerID
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property fantasyAlarmPlayerID (base name: "FantasyAlarmPlayerID")', function() {
      // uncomment below and update the code to test the property fantasyAlarmPlayerID
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property fantasyDraftName (base name: "FantasyDraftName")', function() {
      // uncomment below and update the code to test the property fantasyDraftName
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property fantasyDraftPlayerID (base name: "FantasyDraftPlayerID")', function() {
      // uncomment below and update the code to test the property fantasyDraftPlayerID
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property firstName (base name: "FirstName")', function() {
      // uncomment below and update the code to test the property firstName
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property globalTeamID (base name: "GlobalTeamID")', function() {
      // uncomment below and update the code to test the property globalTeamID
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property height (base name: "Height")', function() {
      // uncomment below and update the code to test the property height
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property highSchool (base name: "HighSchool")', function() {
      // uncomment below and update the code to test the property highSchool
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property injuryBodyPart (base name: "InjuryBodyPart")', function() {
      // uncomment below and update the code to test the property injuryBodyPart
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property injuryNotes (base name: "InjuryNotes")', function() {
      // uncomment below and update the code to test the property injuryNotes
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property injuryStartDate (base name: "InjuryStartDate")', function() {
      // uncomment below and update the code to test the property injuryStartDate
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property injuryStatus (base name: "InjuryStatus")', function() {
      // uncomment below and update the code to test the property injuryStatus
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property jersey (base name: "Jersey")', function() {
      // uncomment below and update the code to test the property jersey
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property lastName (base name: "LastName")', function() {
      // uncomment below and update the code to test the property lastName
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property nbaDotComPlayerID (base name: "NbaDotComPlayerID")', function() {
      // uncomment below and update the code to test the property nbaDotComPlayerID
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property photoUrl (base name: "PhotoUrl")', function() {
      // uncomment below and update the code to test the property photoUrl
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property playerID (base name: "PlayerID")', function() {
      // uncomment below and update the code to test the property playerID
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property position (base name: "Position")', function() {
      // uncomment below and update the code to test the property position
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property positionCategory (base name: "PositionCategory")', function() {
      // uncomment below and update the code to test the property positionCategory
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property rotoWirePlayerID (base name: "RotoWirePlayerID")', function() {
      // uncomment below and update the code to test the property rotoWirePlayerID
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property rotoworldPlayerID (base name: "RotoworldPlayerID")', function() {
      // uncomment below and update the code to test the property rotoworldPlayerID
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property salary (base name: "Salary")', function() {
      // uncomment below and update the code to test the property salary
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property sportRadarPlayerID (base name: "SportRadarPlayerID")', function() {
      // uncomment below and update the code to test the property sportRadarPlayerID
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property sportsDataID (base name: "SportsDataID")', function() {
      // uncomment below and update the code to test the property sportsDataID
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property sportsDirectPlayerID (base name: "SportsDirectPlayerID")', function() {
      // uncomment below and update the code to test the property sportsDirectPlayerID
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property statsPlayerID (base name: "StatsPlayerID")', function() {
      // uncomment below and update the code to test the property statsPlayerID
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "Status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property team (base name: "Team")', function() {
      // uncomment below and update the code to test the property team
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property teamID (base name: "TeamID")', function() {
      // uncomment below and update the code to test the property teamID
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property usaTodayHeadshotNoBackgroundUpdated (base name: "UsaTodayHeadshotNoBackgroundUpdated")', function() {
      // uncomment below and update the code to test the property usaTodayHeadshotNoBackgroundUpdated
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property usaTodayHeadshotNoBackgroundUrl (base name: "UsaTodayHeadshotNoBackgroundUrl")', function() {
      // uncomment below and update the code to test the property usaTodayHeadshotNoBackgroundUrl
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property usaTodayHeadshotUpdated (base name: "UsaTodayHeadshotUpdated")', function() {
      // uncomment below and update the code to test the property usaTodayHeadshotUpdated
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property usaTodayHeadshotUrl (base name: "UsaTodayHeadshotUrl")', function() {
      // uncomment below and update the code to test the property usaTodayHeadshotUrl
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property usaTodayPlayerID (base name: "UsaTodayPlayerID")', function() {
      // uncomment below and update the code to test the property usaTodayPlayerID
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property weight (base name: "Weight")', function() {
      // uncomment below and update the code to test the property weight
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property xmlTeamPlayerID (base name: "XmlTeamPlayerID")', function() {
      // uncomment below and update the code to test the property xmlTeamPlayerID
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property yahooName (base name: "YahooName")', function() {
      // uncomment below and update the code to test the property yahooName
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

    it('should have the property yahooPlayerID (base name: "YahooPlayerID")', function() {
      // uncomment below and update the code to test the property yahooPlayerID
      //var instance = new NbaV3Scores.Player();
      //expect(instance).to.be();
    });

  });

}));
