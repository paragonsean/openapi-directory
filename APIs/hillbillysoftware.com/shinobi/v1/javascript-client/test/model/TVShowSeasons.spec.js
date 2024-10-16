/**
 * shinobiapi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
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
    factory(root.expect, root.Shinobiapi);
  }
}(this, function(expect, Shinobiapi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new Shinobiapi.TVShowSeasons();
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

  describe('TVShowSeasons', function() {
    it('should create an instance of TVShowSeasons', function() {
      // uncomment below and update the code to test TVShowSeasons
      //var instance = new Shinobiapi.TVShowSeasons();
      //expect(instance).to.be.a(Shinobiapi.TVShowSeasons);
    });

    it('should have the property episodes (base name: "Episodes")', function() {
      // uncomment below and update the code to test the property episodes
      //var instance = new Shinobiapi.TVShowSeasons();
      //expect(instance).to.be();
    });

    it('should have the property externals (base name: "Externals")', function() {
      // uncomment below and update the code to test the property externals
      //var instance = new Shinobiapi.TVShowSeasons();
      //expect(instance).to.be();
    });

    it('should have the property seasons (base name: "Seasons")', function() {
      // uncomment below and update the code to test the property seasons
      //var instance = new Shinobiapi.TVShowSeasons();
      //expect(instance).to.be();
    });

    it('should have the property showname (base name: "Showname")', function() {
      // uncomment below and update the code to test the property showname
      //var instance = new Shinobiapi.TVShowSeasons();
      //expect(instance).to.be();
    });

  });

}));
