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
    instance = new Shinobiapi.ImdbImages();
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

  describe('ImdbImages', function() {
    it('should create an instance of ImdbImages', function() {
      // uncomment below and update the code to test ImdbImages
      //var instance = new Shinobiapi.ImdbImages();
      //expect(instance).to.be.a(Shinobiapi.ImdbImages);
    });

    it('should have the property backdrops (base name: "Backdrops")', function() {
      // uncomment below and update the code to test the property backdrops
      //var instance = new Shinobiapi.ImdbImages();
      //expect(instance).to.be();
    });

    it('should have the property posters (base name: "Posters")', function() {
      // uncomment below and update the code to test the property posters
      //var instance = new Shinobiapi.ImdbImages();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "Type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new Shinobiapi.ImdbImages();
      //expect(instance).to.be();
    });

    it('should have the property imdbID (base name: "imdbID")', function() {
      // uncomment below and update the code to test the property imdbID
      //var instance = new Shinobiapi.ImdbImages();
      //expect(instance).to.be();
    });

  });

}));
