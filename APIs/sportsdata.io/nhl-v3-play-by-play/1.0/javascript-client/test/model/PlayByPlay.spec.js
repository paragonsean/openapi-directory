/**
 * NHL v3 Play-by-Play
 * NHL play-by-play API.
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
    factory(root.expect, root.NhlV3PlayByPlay);
  }
}(this, function(expect, NhlV3PlayByPlay) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NhlV3PlayByPlay.PlayByPlay();
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

  describe('PlayByPlay', function() {
    it('should create an instance of PlayByPlay', function() {
      // uncomment below and update the code to test PlayByPlay
      //var instance = new NhlV3PlayByPlay.PlayByPlay();
      //expect(instance).to.be.a(NhlV3PlayByPlay.PlayByPlay);
    });

    it('should have the property game (base name: "Game")', function() {
      // uncomment below and update the code to test the property game
      //var instance = new NhlV3PlayByPlay.PlayByPlay();
      //expect(instance).to.be();
    });

    it('should have the property plays (base name: "Plays")', function() {
      // uncomment below and update the code to test the property plays
      //var instance = new NhlV3PlayByPlay.PlayByPlay();
      //expect(instance).to.be();
    });

  });

}));
