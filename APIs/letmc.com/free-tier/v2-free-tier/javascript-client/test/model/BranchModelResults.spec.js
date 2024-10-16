/**
 * LetMC Api V2, Free (Tier 1)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-free-tier
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
    factory(root.expect, root.LetMcApiV2FreeTier1);
  }
}(this, function(expect, LetMcApiV2FreeTier1) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new LetMcApiV2FreeTier1.BranchModelResults();
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

  describe('BranchModelResults', function() {
    it('should create an instance of BranchModelResults', function() {
      // uncomment below and update the code to test BranchModelResults
      //var instance = new LetMcApiV2FreeTier1.BranchModelResults();
      //expect(instance).to.be.a(LetMcApiV2FreeTier1.BranchModelResults);
    });

    it('should have the property count (base name: "Count")', function() {
      // uncomment below and update the code to test the property count
      //var instance = new LetMcApiV2FreeTier1.BranchModelResults();
      //expect(instance).to.be();
    });

    it('should have the property data (base name: "Data")', function() {
      // uncomment below and update the code to test the property data
      //var instance = new LetMcApiV2FreeTier1.BranchModelResults();
      //expect(instance).to.be();
    });

  });

}));
