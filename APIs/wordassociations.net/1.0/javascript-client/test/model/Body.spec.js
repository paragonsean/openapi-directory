/**
 * Word Associations API
 * The Word Associations Network API allows developers to embed the ability to find associations for a word or phrase into their mobile apps or web services. Words are grouped by semantics, meaning, and psychological perception. The Word Associations Network API currently supports English, French, Spanish, German, Italian, Portuguese, and Russian vocabulary. Please [register and subscribe](https://api.wordassociations.net/subscriptions/) to one of available tariff plans to get a valid API key.
 *
 * The version of the OpenAPI document: 1.0
 * Contact: contact@wordassociations.net
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
    factory(root.expect, root.WordAssociationsApi);
  }
}(this, function(expect, WordAssociationsApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new WordAssociationsApi.Body();
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

  describe('Body', function() {
    it('should create an instance of Body', function() {
      // uncomment below and update the code to test Body
      //var instance = new WordAssociationsApi.Body();
      //expect(instance).to.be.a(WordAssociationsApi.Body);
    });

    it('should have the property code (base name: "code")', function() {
      // uncomment below and update the code to test the property code
      //var instance = new WordAssociationsApi.Body();
      //expect(instance).to.be();
    });

    it('should have the property request (base name: "request")', function() {
      // uncomment below and update the code to test the property request
      //var instance = new WordAssociationsApi.Body();
      //expect(instance).to.be();
    });

    it('should have the property response (base name: "response")', function() {
      // uncomment below and update the code to test the property response
      //var instance = new WordAssociationsApi.Body();
      //expect(instance).to.be();
    });

    it('should have the property version (base name: "version")', function() {
      // uncomment below and update the code to test the property version
      //var instance = new WordAssociationsApi.Body();
      //expect(instance).to.be();
    });

  });

}));
