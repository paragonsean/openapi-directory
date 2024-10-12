/**
 * Dataflow Kit Web Scraper
 * Render Javascript driven pages, while we internally manage Headless Chrome and proxies for you.   - Build a custom web scraper with our Visual point-and-click toolkit. - Scrape the most popular Search engines result pages (SERP). - Convert web pages to PDF and capture screenshots. *** ### Authentication Dataflow Kit API require you to sign up for an API key in order to use the API.   The API key can be found in the [DFK Dashboard](https://account.dataflowkit.com) after _free registration_.  Pass a secret API Key to all API requests to the server as the `api_key` query parameter.  
 *
 * The version of the OpenAPI document: 1.3
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
    factory(root.expect, root.DataflowKitWebScraper);
  }
}(this, function(expect, DataflowKitWebScraper) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new DataflowKitWebScraper.Click();
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

  describe('Click', function() {
    it('should create an instance of Click', function() {
      // uncomment below and update the code to test Click
      //var instance = new DataflowKitWebScraper.Click();
      //expect(instance).to.be.a(DataflowKitWebScraper.Click);
    });

    it('should have the property ignoreIfNotPresent (base name: "ignoreIfNotPresent")', function() {
      // uncomment below and update the code to test the property ignoreIfNotPresent
      //var instance = new DataflowKitWebScraper.Click();
      //expect(instance).to.be();
    });

    it('should have the property selector (base name: "selector")', function() {
      // uncomment below and update the code to test the property selector
      //var instance = new DataflowKitWebScraper.Click();
      //expect(instance).to.be();
    });

    it('should have the property skipLastIteration (base name: "skipLastIteration")', function() {
      // uncomment below and update the code to test the property skipLastIteration
      //var instance = new DataflowKitWebScraper.Click();
      //expect(instance).to.be();
    });

  });

}));
