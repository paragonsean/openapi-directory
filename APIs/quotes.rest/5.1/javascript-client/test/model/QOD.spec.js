/**
 * They Said So Quotes API
 *  They Said So Quotes API offers a complete feature rich REST API access to its quotes platform.  This is the documentation for the world famous [quotes API](https://theysaidso.com/api).  If you are a subscriber and you are trying this from a console you can use Bearer token with your api key as the token. You can test and play with the API right here on this web page. Please note recently we closed downs public access without api key to prevent abuse. The public routes are still available to use free of charge but requires a api token. You can get one for free at our website. For using the private end points and subscribing to the API please visit [https://theysaidso.com/api](https://theysaidso.com/api).
 *
 * The version of the OpenAPI document: 5.1
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
    factory(root.expect, root.TheySaidSoQuotesApi);
  }
}(this, function(expect, TheySaidSoQuotesApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new TheySaidSoQuotesApi.QOD();
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

  describe('QOD', function() {
    it('should create an instance of QOD', function() {
      // uncomment below and update the code to test QOD
      //var instance = new TheySaidSoQuotesApi.QOD();
      //expect(instance).to.be.a(TheySaidSoQuotesApi.QOD);
    });

    it('should have the property author (base name: "author")', function() {
      // uncomment below and update the code to test the property author
      //var instance = new TheySaidSoQuotesApi.QOD();
      //expect(instance).to.be();
    });

    it('should have the property quote (base name: "quote")', function() {
      // uncomment below and update the code to test the property quote
      //var instance = new TheySaidSoQuotesApi.QOD();
      //expect(instance).to.be();
    });

    it('should have the property tags (base name: "tags")', function() {
      // uncomment below and update the code to test the property tags
      //var instance = new TheySaidSoQuotesApi.QOD();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new TheySaidSoQuotesApi.QOD();
      //expect(instance).to.be();
    });

    it('should have the property image (base name: "image")', function() {
      // uncomment below and update the code to test the property image
      //var instance = new TheySaidSoQuotesApi.QOD();
      //expect(instance).to.be();
    });

    it('should have the property length (base name: "length")', function() {
      // uncomment below and update the code to test the property length
      //var instance = new TheySaidSoQuotesApi.QOD();
      //expect(instance).to.be();
    });

    it('should have the property date (base name: "date")', function() {
      // uncomment below and update the code to test the property date
      //var instance = new TheySaidSoQuotesApi.QOD();
      //expect(instance).to.be();
    });

    it('should have the property title (base name: "title")', function() {
      // uncomment below and update the code to test the property title
      //var instance = new TheySaidSoQuotesApi.QOD();
      //expect(instance).to.be();
    });

  });

}));
