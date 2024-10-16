/**
 * NHL v3 Scores
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
    factory(root.expect, root.NhlV3Scores);
  }
}(this, function(expect, NhlV3Scores) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NhlV3Scores.News();
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

  describe('News', function() {
    it('should create an instance of News', function() {
      // uncomment below and update the code to test News
      //var instance = new NhlV3Scores.News();
      //expect(instance).to.be.a(NhlV3Scores.News);
    });

    it('should have the property content (base name: "Content")', function() {
      // uncomment below and update the code to test the property content
      //var instance = new NhlV3Scores.News();
      //expect(instance).to.be();
    });

    it('should have the property newsID (base name: "NewsID")', function() {
      // uncomment below and update the code to test the property newsID
      //var instance = new NhlV3Scores.News();
      //expect(instance).to.be();
    });

    it('should have the property playerID (base name: "PlayerID")', function() {
      // uncomment below and update the code to test the property playerID
      //var instance = new NhlV3Scores.News();
      //expect(instance).to.be();
    });

    it('should have the property source (base name: "Source")', function() {
      // uncomment below and update the code to test the property source
      //var instance = new NhlV3Scores.News();
      //expect(instance).to.be();
    });

    it('should have the property team (base name: "Team")', function() {
      // uncomment below and update the code to test the property team
      //var instance = new NhlV3Scores.News();
      //expect(instance).to.be();
    });

    it('should have the property teamID (base name: "TeamID")', function() {
      // uncomment below and update the code to test the property teamID
      //var instance = new NhlV3Scores.News();
      //expect(instance).to.be();
    });

    it('should have the property termsOfUse (base name: "TermsOfUse")', function() {
      // uncomment below and update the code to test the property termsOfUse
      //var instance = new NhlV3Scores.News();
      //expect(instance).to.be();
    });

    it('should have the property title (base name: "Title")', function() {
      // uncomment below and update the code to test the property title
      //var instance = new NhlV3Scores.News();
      //expect(instance).to.be();
    });

    it('should have the property updated (base name: "Updated")', function() {
      // uncomment below and update the code to test the property updated
      //var instance = new NhlV3Scores.News();
      //expect(instance).to.be();
    });

    it('should have the property url (base name: "Url")', function() {
      // uncomment below and update the code to test the property url
      //var instance = new NhlV3Scores.News();
      //expect(instance).to.be();
    });

  });

}));
