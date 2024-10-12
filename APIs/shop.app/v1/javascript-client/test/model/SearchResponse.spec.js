/**
 * Shop
 * Search for millions of products from the world's greatest brands.
 *
 * The version of the OpenAPI document: v1
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
    factory(root.expect, root.Shop);
  }
}(this, function(expect, Shop) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new Shop.SearchResponse();
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

  describe('SearchResponse', function() {
    it('should create an instance of SearchResponse', function() {
      // uncomment below and update the code to test SearchResponse
      //var instance = new Shop.SearchResponse();
      //expect(instance).to.be.a(Shop.SearchResponse);
    });

    it('should have the property results (base name: "results")', function() {
      // uncomment below and update the code to test the property results
      //var instance = new Shop.SearchResponse();
      //expect(instance).to.be();
    });

  });

}));
