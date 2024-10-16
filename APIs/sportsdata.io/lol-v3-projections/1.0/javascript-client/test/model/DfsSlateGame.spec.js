/**
 * LoL v3 Projections
 * LoL v3 Projections
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
    factory(root.expect, root.LoLV3Projections);
  }
}(this, function(expect, LoLV3Projections) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new LoLV3Projections.DfsSlateGame();
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

  describe('DfsSlateGame', function() {
    it('should create an instance of DfsSlateGame', function() {
      // uncomment below and update the code to test DfsSlateGame
      //var instance = new LoLV3Projections.DfsSlateGame();
      //expect(instance).to.be.a(LoLV3Projections.DfsSlateGame);
    });

    it('should have the property game (base name: "Game")', function() {
      // uncomment below and update the code to test the property game
      //var instance = new LoLV3Projections.DfsSlateGame();
      //expect(instance).to.be();
    });

    it('should have the property gameID (base name: "GameID")', function() {
      // uncomment below and update the code to test the property gameID
      //var instance = new LoLV3Projections.DfsSlateGame();
      //expect(instance).to.be();
    });

    it('should have the property operatorGameID (base name: "OperatorGameID")', function() {
      // uncomment below and update the code to test the property operatorGameID
      //var instance = new LoLV3Projections.DfsSlateGame();
      //expect(instance).to.be();
    });

    it('should have the property removedByOperator (base name: "RemovedByOperator")', function() {
      // uncomment below and update the code to test the property removedByOperator
      //var instance = new LoLV3Projections.DfsSlateGame();
      //expect(instance).to.be();
    });

    it('should have the property slateGameID (base name: "SlateGameID")', function() {
      // uncomment below and update the code to test the property slateGameID
      //var instance = new LoLV3Projections.DfsSlateGame();
      //expect(instance).to.be();
    });

    it('should have the property slateID (base name: "SlateID")', function() {
      // uncomment below and update the code to test the property slateID
      //var instance = new LoLV3Projections.DfsSlateGame();
      //expect(instance).to.be();
    });

  });

}));
