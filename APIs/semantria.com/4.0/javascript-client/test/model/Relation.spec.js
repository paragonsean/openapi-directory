/**
 * Semantria
 * Semantria applies Text and Sentiment Analysis to tweets, facebook posts, surveys, reviews or enterprise content.
 *
 * The version of the OpenAPI document: 4.0
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
    factory(root.expect, root.Semantria);
  }
}(this, function(expect, Semantria) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new Semantria.Relation();
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

  describe('Relation', function() {
    it('should create an instance of Relation', function() {
      // uncomment below and update the code to test Relation
      //var instance = new Semantria.Relation();
      //expect(instance).to.be.a(Semantria.Relation);
    });

    it('should have the property confidenceScore (base name: "confidence_score")', function() {
      // uncomment below and update the code to test the property confidenceScore
      //var instance = new Semantria.Relation();
      //expect(instance).to.be();
    });

    it('should have the property entities (base name: "entities")', function() {
      // uncomment below and update the code to test the property entities
      //var instance = new Semantria.Relation();
      //expect(instance).to.be();
    });

    it('should have the property extra (base name: "extra")', function() {
      // uncomment below and update the code to test the property extra
      //var instance = new Semantria.Relation();
      //expect(instance).to.be();
    });

    it('should have the property relationType (base name: "relation_type")', function() {
      // uncomment below and update the code to test the property relationType
      //var instance = new Semantria.Relation();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new Semantria.Relation();
      //expect(instance).to.be();
    });

  });

}));
