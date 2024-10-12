/**
 * NBA v3 Play-by-Play
 * NBA play-by-play API.
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
    factory(root.expect, root.NbaV3PlayByPlay);
  }
}(this, function(expect, NbaV3PlayByPlay) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NbaV3PlayByPlay.Quarter();
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

  describe('Quarter', function() {
    it('should create an instance of Quarter', function() {
      // uncomment below and update the code to test Quarter
      //var instance = new NbaV3PlayByPlay.Quarter();
      //expect(instance).to.be.a(NbaV3PlayByPlay.Quarter);
    });

    it('should have the property awayScore (base name: "AwayScore")', function() {
      // uncomment below and update the code to test the property awayScore
      //var instance = new NbaV3PlayByPlay.Quarter();
      //expect(instance).to.be();
    });

    it('should have the property gameID (base name: "GameID")', function() {
      // uncomment below and update the code to test the property gameID
      //var instance = new NbaV3PlayByPlay.Quarter();
      //expect(instance).to.be();
    });

    it('should have the property homeScore (base name: "HomeScore")', function() {
      // uncomment below and update the code to test the property homeScore
      //var instance = new NbaV3PlayByPlay.Quarter();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "Name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new NbaV3PlayByPlay.Quarter();
      //expect(instance).to.be();
    });

    it('should have the property number (base name: "Number")', function() {
      // uncomment below and update the code to test the property number
      //var instance = new NbaV3PlayByPlay.Quarter();
      //expect(instance).to.be();
    });

    it('should have the property quarterID (base name: "QuarterID")', function() {
      // uncomment below and update the code to test the property quarterID
      //var instance = new NbaV3PlayByPlay.Quarter();
      //expect(instance).to.be();
    });

  });

}));
