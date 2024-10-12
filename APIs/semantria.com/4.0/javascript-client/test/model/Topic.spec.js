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
    instance = new Semantria.Topic();
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

  describe('Topic', function() {
    it('should create an instance of Topic', function() {
      // uncomment below and update the code to test Topic
      //var instance = new Semantria.Topic();
      //expect(instance).to.be.a(Semantria.Topic);
    });

    it('should have the property hitcount (base name: "hitcount")', function() {
      // uncomment below and update the code to test the property hitcount
      //var instance = new Semantria.Topic();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new Semantria.Topic();
      //expect(instance).to.be();
    });

    it('should have the property sentimentPolarity (base name: "sentiment_polarity")', function() {
      // uncomment below and update the code to test the property sentimentPolarity
      //var instance = new Semantria.Topic();
      //expect(instance).to.be();
    });

    it('should have the property sentimentScore (base name: "sentiment_score")', function() {
      // uncomment below and update the code to test the property sentimentScore
      //var instance = new Semantria.Topic();
      //expect(instance).to.be();
    });

    it('should have the property title (base name: "title")', function() {
      // uncomment below and update the code to test the property title
      //var instance = new Semantria.Topic();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new Semantria.Topic();
      //expect(instance).to.be();
    });

  });

}));
