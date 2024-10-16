/**
 * NFL v3 RotoBaller Articles
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
    factory(root.expect, root.NflV3RotoBallerArticles);
  }
}(this, function(expect, NflV3RotoBallerArticles) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NflV3RotoBallerArticles.Article();
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

  describe('Article', function() {
    it('should create an instance of Article', function() {
      // uncomment below and update the code to test Article
      //var instance = new NflV3RotoBallerArticles.Article();
      //expect(instance).to.be.a(NflV3RotoBallerArticles.Article);
    });

    it('should have the property articleID (base name: "ArticleID")', function() {
      // uncomment below and update the code to test the property articleID
      //var instance = new NflV3RotoBallerArticles.Article();
      //expect(instance).to.be();
    });

    it('should have the property author (base name: "Author")', function() {
      // uncomment below and update the code to test the property author
      //var instance = new NflV3RotoBallerArticles.Article();
      //expect(instance).to.be();
    });

    it('should have the property content (base name: "Content")', function() {
      // uncomment below and update the code to test the property content
      //var instance = new NflV3RotoBallerArticles.Article();
      //expect(instance).to.be();
    });

    it('should have the property players (base name: "Players")', function() {
      // uncomment below and update the code to test the property players
      //var instance = new NflV3RotoBallerArticles.Article();
      //expect(instance).to.be();
    });

    it('should have the property source (base name: "Source")', function() {
      // uncomment below and update the code to test the property source
      //var instance = new NflV3RotoBallerArticles.Article();
      //expect(instance).to.be();
    });

    it('should have the property termsOfUse (base name: "TermsOfUse")', function() {
      // uncomment below and update the code to test the property termsOfUse
      //var instance = new NflV3RotoBallerArticles.Article();
      //expect(instance).to.be();
    });

    it('should have the property title (base name: "Title")', function() {
      // uncomment below and update the code to test the property title
      //var instance = new NflV3RotoBallerArticles.Article();
      //expect(instance).to.be();
    });

    it('should have the property updated (base name: "Updated")', function() {
      // uncomment below and update the code to test the property updated
      //var instance = new NflV3RotoBallerArticles.Article();
      //expect(instance).to.be();
    });

    it('should have the property url (base name: "Url")', function() {
      // uncomment below and update the code to test the property url
      //var instance = new NflV3RotoBallerArticles.Article();
      //expect(instance).to.be();
    });

  });

}));
