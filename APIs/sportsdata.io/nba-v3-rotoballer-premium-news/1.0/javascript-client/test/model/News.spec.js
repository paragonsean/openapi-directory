/**
 * NBA v3 RotoBaller Premium News
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
    factory(root.expect, root.NbaV3RotoBallerPremiumNews);
  }
}(this, function(expect, NbaV3RotoBallerPremiumNews) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NbaV3RotoBallerPremiumNews.News();
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
      //var instance = new NbaV3RotoBallerPremiumNews.News();
      //expect(instance).to.be.a(NbaV3RotoBallerPremiumNews.News);
    });

    it('should have the property author (base name: "Author")', function() {
      // uncomment below and update the code to test the property author
      //var instance = new NbaV3RotoBallerPremiumNews.News();
      //expect(instance).to.be();
    });

    it('should have the property categories (base name: "Categories")', function() {
      // uncomment below and update the code to test the property categories
      //var instance = new NbaV3RotoBallerPremiumNews.News();
      //expect(instance).to.be();
    });

    it('should have the property content (base name: "Content")', function() {
      // uncomment below and update the code to test the property content
      //var instance = new NbaV3RotoBallerPremiumNews.News();
      //expect(instance).to.be();
    });

    it('should have the property newsID (base name: "NewsID")', function() {
      // uncomment below and update the code to test the property newsID
      //var instance = new NbaV3RotoBallerPremiumNews.News();
      //expect(instance).to.be();
    });

    it('should have the property originalSource (base name: "OriginalSource")', function() {
      // uncomment below and update the code to test the property originalSource
      //var instance = new NbaV3RotoBallerPremiumNews.News();
      //expect(instance).to.be();
    });

    it('should have the property originalSourceUrl (base name: "OriginalSourceUrl")', function() {
      // uncomment below and update the code to test the property originalSourceUrl
      //var instance = new NbaV3RotoBallerPremiumNews.News();
      //expect(instance).to.be();
    });

    it('should have the property playerID (base name: "PlayerID")', function() {
      // uncomment below and update the code to test the property playerID
      //var instance = new NbaV3RotoBallerPremiumNews.News();
      //expect(instance).to.be();
    });

    it('should have the property playerID2 (base name: "PlayerID2")', function() {
      // uncomment below and update the code to test the property playerID2
      //var instance = new NbaV3RotoBallerPremiumNews.News();
      //expect(instance).to.be();
    });

    it('should have the property source (base name: "Source")', function() {
      // uncomment below and update the code to test the property source
      //var instance = new NbaV3RotoBallerPremiumNews.News();
      //expect(instance).to.be();
    });

    it('should have the property team (base name: "Team")', function() {
      // uncomment below and update the code to test the property team
      //var instance = new NbaV3RotoBallerPremiumNews.News();
      //expect(instance).to.be();
    });

    it('should have the property team2 (base name: "Team2")', function() {
      // uncomment below and update the code to test the property team2
      //var instance = new NbaV3RotoBallerPremiumNews.News();
      //expect(instance).to.be();
    });

    it('should have the property teamID (base name: "TeamID")', function() {
      // uncomment below and update the code to test the property teamID
      //var instance = new NbaV3RotoBallerPremiumNews.News();
      //expect(instance).to.be();
    });

    it('should have the property teamID2 (base name: "TeamID2")', function() {
      // uncomment below and update the code to test the property teamID2
      //var instance = new NbaV3RotoBallerPremiumNews.News();
      //expect(instance).to.be();
    });

    it('should have the property termsOfUse (base name: "TermsOfUse")', function() {
      // uncomment below and update the code to test the property termsOfUse
      //var instance = new NbaV3RotoBallerPremiumNews.News();
      //expect(instance).to.be();
    });

    it('should have the property timeAgo (base name: "TimeAgo")', function() {
      // uncomment below and update the code to test the property timeAgo
      //var instance = new NbaV3RotoBallerPremiumNews.News();
      //expect(instance).to.be();
    });

    it('should have the property title (base name: "Title")', function() {
      // uncomment below and update the code to test the property title
      //var instance = new NbaV3RotoBallerPremiumNews.News();
      //expect(instance).to.be();
    });

    it('should have the property updated (base name: "Updated")', function() {
      // uncomment below and update the code to test the property updated
      //var instance = new NbaV3RotoBallerPremiumNews.News();
      //expect(instance).to.be();
    });

    it('should have the property url (base name: "Url")', function() {
      // uncomment below and update the code to test the property url
      //var instance = new NbaV3RotoBallerPremiumNews.News();
      //expect(instance).to.be();
    });

  });

}));
