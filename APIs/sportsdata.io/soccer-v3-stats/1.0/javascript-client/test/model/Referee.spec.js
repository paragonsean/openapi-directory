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
    instance = new SoccerV3Stats.Referee();
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

  describe('Referee', function() {
    it('should create an instance of Referee', function() {
      // uncomment below and update the code to test Referee
      //var instance = new SoccerV3Stats.Referee();
      //expect(instance).to.be.a(SoccerV3Stats.Referee);
    });

    it('should have the property firstName (base name: "FirstName")', function() {
      // uncomment below and update the code to test the property firstName
      //var instance = new SoccerV3Stats.Referee();
      //expect(instance).to.be();
    });

    it('should have the property lastName (base name: "LastName")', function() {
      // uncomment below and update the code to test the property lastName
      //var instance = new SoccerV3Stats.Referee();
      //expect(instance).to.be();
    });

    it('should have the property nationality (base name: "Nationality")', function() {
      // uncomment below and update the code to test the property nationality
      //var instance = new SoccerV3Stats.Referee();
      //expect(instance).to.be();
    });

    it('should have the property refereeId (base name: "RefereeId")', function() {
      // uncomment below and update the code to test the property refereeId
      //var instance = new SoccerV3Stats.Referee();
      //expect(instance).to.be();
    });

    it('should have the property shortName (base name: "ShortName")', function() {
      // uncomment below and update the code to test the property shortName
      //var instance = new SoccerV3Stats.Referee();
      //expect(instance).to.be();
    });

  });

}));
