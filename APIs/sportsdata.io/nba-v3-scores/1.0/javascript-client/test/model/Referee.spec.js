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
    instance = new NbaV3Scores.Referee();
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
      //var instance = new NbaV3Scores.Referee();
      //expect(instance).to.be.a(NbaV3Scores.Referee);
    });

    it('should have the property college (base name: "College")', function() {
      // uncomment below and update the code to test the property college
      //var instance = new NbaV3Scores.Referee();
      //expect(instance).to.be();
    });

    it('should have the property experience (base name: "Experience")', function() {
      // uncomment below and update the code to test the property experience
      //var instance = new NbaV3Scores.Referee();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "Name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new NbaV3Scores.Referee();
      //expect(instance).to.be();
    });

    it('should have the property number (base name: "Number")', function() {
      // uncomment below and update the code to test the property number
      //var instance = new NbaV3Scores.Referee();
      //expect(instance).to.be();
    });

    it('should have the property position (base name: "Position")', function() {
      // uncomment below and update the code to test the property position
      //var instance = new NbaV3Scores.Referee();
      //expect(instance).to.be();
    });

    it('should have the property refereeID (base name: "RefereeID")', function() {
      // uncomment below and update the code to test the property refereeID
      //var instance = new NbaV3Scores.Referee();
      //expect(instance).to.be();
    });

  });

}));
