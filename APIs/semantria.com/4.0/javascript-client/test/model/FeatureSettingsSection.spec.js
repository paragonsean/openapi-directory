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
    instance = new Semantria.FeatureSettingsSection();
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

  describe('FeatureSettingsSection', function() {
    it('should create an instance of FeatureSettingsSection', function() {
      // uncomment below and update the code to test FeatureSettingsSection
      //var instance = new Semantria.FeatureSettingsSection();
      //expect(instance).to.be.a(Semantria.FeatureSettingsSection);
    });

    it('should have the property blacklist (base name: "blacklist")', function() {
      // uncomment below and update the code to test the property blacklist
      //var instance = new Semantria.FeatureSettingsSection();
      //expect(instance).to.be();
    });

    it('should have the property queries (base name: "queries")', function() {
      // uncomment below and update the code to test the property queries
      //var instance = new Semantria.FeatureSettingsSection();
      //expect(instance).to.be();
    });

    it('should have the property sentimentPhrases (base name: "sentiment_phrases")', function() {
      // uncomment below and update the code to test the property sentimentPhrases
      //var instance = new Semantria.FeatureSettingsSection();
      //expect(instance).to.be();
    });

    it('should have the property taxonomy (base name: "taxonomy")', function() {
      // uncomment below and update the code to test the property taxonomy
      //var instance = new Semantria.FeatureSettingsSection();
      //expect(instance).to.be();
    });

    it('should have the property userCategories (base name: "user_categories")', function() {
      // uncomment below and update the code to test the property userCategories
      //var instance = new Semantria.FeatureSettingsSection();
      //expect(instance).to.be();
    });

    it('should have the property userEntities (base name: "user_entities")', function() {
      // uncomment below and update the code to test the property userEntities
      //var instance = new Semantria.FeatureSettingsSection();
      //expect(instance).to.be();
    });

  });

}));
