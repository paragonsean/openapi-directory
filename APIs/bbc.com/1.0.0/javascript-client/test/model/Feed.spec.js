/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
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
    factory(root.expect, root.BbcNitroApi);
  }
}(this, function(expect, BbcNitroApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new BbcNitroApi.Feed();
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

  describe('Feed', function() {
    it('should create an instance of Feed', function() {
      // uncomment below and update the code to test Feed
      //var instance = new BbcNitroApi.Feed();
      //expect(instance).to.be.a(BbcNitroApi.Feed);
    });

    it('should have the property deprecations (base name: "deprecations")', function() {
      // uncomment below and update the code to test the property deprecations
      //var instance = new BbcNitroApi.Feed();
      //expect(instance).to.be();
    });

    it('should have the property filters (base name: "filters")', function() {
      // uncomment below and update the code to test the property filters
      //var instance = new BbcNitroApi.Feed();
      //expect(instance).to.be();
    });

    it('should have the property href (base name: "href")', function() {
      // uncomment below and update the code to test the property href
      //var instance = new BbcNitroApi.Feed();
      //expect(instance).to.be();
    });

    it('should have the property mixins (base name: "mixins")', function() {
      // uncomment below and update the code to test the property mixins
      //var instance = new BbcNitroApi.Feed();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new BbcNitroApi.Feed();
      //expect(instance).to.be();
    });

    it('should have the property rel (base name: "rel")', function() {
      // uncomment below and update the code to test the property rel
      //var instance = new BbcNitroApi.Feed();
      //expect(instance).to.be();
    });

    it('should have the property releaseStatus (base name: "release_status")', function() {
      // uncomment below and update the code to test the property releaseStatus
      //var instance = new BbcNitroApi.Feed();
      //expect(instance).to.be();
    });

    it('should have the property sorts (base name: "sorts")', function() {
      // uncomment below and update the code to test the property sorts
      //var instance = new BbcNitroApi.Feed();
      //expect(instance).to.be();
    });

    it('should have the property title (base name: "title")', function() {
      // uncomment below and update the code to test the property title
      //var instance = new BbcNitroApi.Feed();
      //expect(instance).to.be();
    });

  });

}));
