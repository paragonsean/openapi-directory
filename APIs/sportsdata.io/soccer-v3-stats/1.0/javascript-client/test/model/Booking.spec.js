/**
 * Soccer v3 Stats
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
    factory(root.expect, root.SoccerV3Stats);
  }
}(this, function(expect, SoccerV3Stats) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new SoccerV3Stats.Booking();
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

  describe('Booking', function() {
    it('should create an instance of Booking', function() {
      // uncomment below and update the code to test Booking
      //var instance = new SoccerV3Stats.Booking();
      //expect(instance).to.be.a(SoccerV3Stats.Booking);
    });

    it('should have the property bookingId (base name: "BookingId")', function() {
      // uncomment below and update the code to test the property bookingId
      //var instance = new SoccerV3Stats.Booking();
      //expect(instance).to.be();
    });

    it('should have the property gameId (base name: "GameId")', function() {
      // uncomment below and update the code to test the property gameId
      //var instance = new SoccerV3Stats.Booking();
      //expect(instance).to.be();
    });

    it('should have the property gameMinute (base name: "GameMinute")', function() {
      // uncomment below and update the code to test the property gameMinute
      //var instance = new SoccerV3Stats.Booking();
      //expect(instance).to.be();
    });

    it('should have the property gameMinuteExtra (base name: "GameMinuteExtra")', function() {
      // uncomment below and update the code to test the property gameMinuteExtra
      //var instance = new SoccerV3Stats.Booking();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "Name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new SoccerV3Stats.Booking();
      //expect(instance).to.be();
    });

    it('should have the property playerId (base name: "PlayerId")', function() {
      // uncomment below and update the code to test the property playerId
      //var instance = new SoccerV3Stats.Booking();
      //expect(instance).to.be();
    });

    it('should have the property teamId (base name: "TeamId")', function() {
      // uncomment below and update the code to test the property teamId
      //var instance = new SoccerV3Stats.Booking();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "Type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new SoccerV3Stats.Booking();
      //expect(instance).to.be();
    });

  });

}));
