/**
 * Advicent.FactFinderService
 * An API for accessing the NaviPlan Fact Finder.
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
    factory(root.expect, root.AdvicentFactFinderService);
  }
}(this, function(expect, AdvicentFactFinderService) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AdvicentFactFinderService.LifestyleAssetModel();
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

  describe('LifestyleAssetModel', function() {
    it('should create an instance of LifestyleAssetModel', function() {
      // uncomment below and update the code to test LifestyleAssetModel
      //var instance = new AdvicentFactFinderService.LifestyleAssetModel();
      //expect(instance).to.be.a(AdvicentFactFinderService.LifestyleAssetModel);
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new AdvicentFactFinderService.LifestyleAssetModel();
      //expect(instance).to.be();
    });

    it('should have the property externalDestinationId (base name: "externalDestinationId")', function() {
      // uncomment below and update the code to test the property externalDestinationId
      //var instance = new AdvicentFactFinderService.LifestyleAssetModel();
      //expect(instance).to.be();
    });

    it('should have the property factFinderId (base name: "factFinderId")', function() {
      // uncomment below and update the code to test the property factFinderId
      //var instance = new AdvicentFactFinderService.LifestyleAssetModel();
      //expect(instance).to.be();
    });

    it('should have the property marketValue (base name: "marketValue")', function() {
      // uncomment below and update the code to test the property marketValue
      //var instance = new AdvicentFactFinderService.LifestyleAssetModel();
      //expect(instance).to.be();
    });

    it('should have the property owner (base name: "owner")', function() {
      // uncomment below and update the code to test the property owner
      //var instance = new AdvicentFactFinderService.LifestyleAssetModel();
      //expect(instance).to.be();
    });

    it('should have the property purchaseAmount (base name: "purchaseAmount")', function() {
      // uncomment below and update the code to test the property purchaseAmount
      //var instance = new AdvicentFactFinderService.LifestyleAssetModel();
      //expect(instance).to.be();
    });

    it('should have the property purchaseDate (base name: "purchaseDate")', function() {
      // uncomment below and update the code to test the property purchaseDate
      //var instance = new AdvicentFactFinderService.LifestyleAssetModel();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new AdvicentFactFinderService.LifestyleAssetModel();
      //expect(instance).to.be();
    });

  });

}));
