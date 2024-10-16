/**
 * Contribly
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
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
    factory(root.expect, root.Contribly);
  }
}(this, function(expect, Contribly) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new Contribly.Contribution();
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

  describe('Contribution', function() {
    it('should create an instance of Contribution', function() {
      // uncomment below and update the code to test Contribution
      //var instance = new Contribly.Contribution();
      //expect(instance).to.be.a(Contribly.Contribution);
    });

    it('should have the property assignment (base name: "assignment")', function() {
      // uncomment below and update the code to test the property assignment
      //var instance = new Contribly.Contribution();
      //expect(instance).to.be();
    });

    it('should have the property attribution (base name: "attribution")', function() {
      // uncomment below and update the code to test the property attribution
      //var instance = new Contribly.Contribution();
      //expect(instance).to.be();
    });

    it('should have the property body (base name: "body")', function() {
      // uncomment below and update the code to test the property body
      //var instance = new Contribly.Contribution();
      //expect(instance).to.be();
    });

    it('should have the property created (base name: "created")', function() {
      // uncomment below and update the code to test the property created
      //var instance = new Contribly.Contribution();
      //expect(instance).to.be();
    });

    it('should have the property headline (base name: "headline")', function() {
      // uncomment below and update the code to test the property headline
      //var instance = new Contribly.Contribution();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new Contribly.Contribution();
      //expect(instance).to.be();
    });

    it('should have the property mediaUsages (base name: "mediaUsages")', function() {
      // uncomment below and update the code to test the property mediaUsages
      //var instance = new Contribly.Contribution();
      //expect(instance).to.be();
    });

    it('should have the property moderationHistory (base name: "moderationHistory")', function() {
      // uncomment below and update the code to test the property moderationHistory
      //var instance = new Contribly.Contribution();
      //expect(instance).to.be();
    });

    it('should have the property place (base name: "place")', function() {
      // uncomment below and update the code to test the property place
      //var instance = new Contribly.Contribution();
      //expect(instance).to.be();
    });

    it('should have the property urlWords (base name: "urlWords")', function() {
      // uncomment below and update the code to test the property urlWords
      //var instance = new Contribly.Contribution();
      //expect(instance).to.be();
    });

    it('should have the property via (base name: "via")', function() {
      // uncomment below and update the code to test the property via
      //var instance = new Contribly.Contribution();
      //expect(instance).to.be();
    });

  });

}));
