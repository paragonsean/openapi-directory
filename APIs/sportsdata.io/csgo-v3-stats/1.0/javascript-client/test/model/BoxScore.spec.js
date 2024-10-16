/**
 * CS:GO v3 Stats
 * CS:GO v3 Stats
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
    factory(root.expect, root.CsgoV3Stats);
  }
}(this, function(expect, CsgoV3Stats) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new CsgoV3Stats.BoxScore();
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

  describe('BoxScore', function() {
    it('should create an instance of BoxScore', function() {
      // uncomment below and update the code to test BoxScore
      //var instance = new CsgoV3Stats.BoxScore();
      //expect(instance).to.be.a(CsgoV3Stats.BoxScore);
    });

    it('should have the property game (base name: "Game")', function() {
      // uncomment below and update the code to test the property game
      //var instance = new CsgoV3Stats.BoxScore();
      //expect(instance).to.be();
    });

    it('should have the property maps (base name: "Maps")', function() {
      // uncomment below and update the code to test the property maps
      //var instance = new CsgoV3Stats.BoxScore();
      //expect(instance).to.be();
    });

  });

}));
