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
    instance = new GolfV2.DfsSlatePlayer();
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

  describe('DfsSlatePlayer', function() {
    it('should create an instance of DfsSlatePlayer', function() {
      // uncomment below and update the code to test DfsSlatePlayer
      //var instance = new GolfV2.DfsSlatePlayer();
      //expect(instance).to.be.a(GolfV2.DfsSlatePlayer);
    });

    it('should have the property operatorPlayerID (base name: "OperatorPlayerID")', function() {
      // uncomment below and update the code to test the property operatorPlayerID
      //var instance = new GolfV2.DfsSlatePlayer();
      //expect(instance).to.be();
    });

    it('should have the property operatorPlayerName (base name: "OperatorPlayerName")', function() {
      // uncomment below and update the code to test the property operatorPlayerName
      //var instance = new GolfV2.DfsSlatePlayer();
      //expect(instance).to.be();
    });

    it('should have the property operatorPosition (base name: "OperatorPosition")', function() {
      // uncomment below and update the code to test the property operatorPosition
      //var instance = new GolfV2.DfsSlatePlayer();
      //expect(instance).to.be();
    });

    it('should have the property operatorRosterSlots (base name: "OperatorRosterSlots")', function() {
      // uncomment below and update the code to test the property operatorRosterSlots
      //var instance = new GolfV2.DfsSlatePlayer();
      //expect(instance).to.be();
    });

    it('should have the property operatorSalary (base name: "OperatorSalary")', function() {
      // uncomment below and update the code to test the property operatorSalary
      //var instance = new GolfV2.DfsSlatePlayer();
      //expect(instance).to.be();
    });

    it('should have the property operatorSlatePlayerID (base name: "OperatorSlatePlayerID")', function() {
      // uncomment below and update the code to test the property operatorSlatePlayerID
      //var instance = new GolfV2.DfsSlatePlayer();
      //expect(instance).to.be();
    });

    it('should have the property playerID (base name: "PlayerID")', function() {
      // uncomment below and update the code to test the property playerID
      //var instance = new GolfV2.DfsSlatePlayer();
      //expect(instance).to.be();
    });

    it('should have the property playerTournamentProjectionID (base name: "PlayerTournamentProjectionID")', function() {
      // uncomment below and update the code to test the property playerTournamentProjectionID
      //var instance = new GolfV2.DfsSlatePlayer();
      //expect(instance).to.be();
    });

    it('should have the property removedByOperator (base name: "RemovedByOperator")', function() {
      // uncomment below and update the code to test the property removedByOperator
      //var instance = new GolfV2.DfsSlatePlayer();
      //expect(instance).to.be();
    });

    it('should have the property slateID (base name: "SlateID")', function() {
      // uncomment below and update the code to test the property slateID
      //var instance = new GolfV2.DfsSlatePlayer();
      //expect(instance).to.be();
    });

    it('should have the property slatePlayerID (base name: "SlatePlayerID")', function() {
      // uncomment below and update the code to test the property slatePlayerID
      //var instance = new GolfV2.DfsSlatePlayer();
      //expect(instance).to.be();
    });

    it('should have the property slateTournamentID (base name: "SlateTournamentID")', function() {
      // uncomment below and update the code to test the property slateTournamentID
      //var instance = new GolfV2.DfsSlatePlayer();
      //expect(instance).to.be();
    });

  });

}));
