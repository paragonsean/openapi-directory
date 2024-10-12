/**
 * Location Score
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.     Please also be aware that our test environment is based on a subset of the production, this API in test only returns a few selected cities. You can find the list in our **[data collection](https://github.com/amadeus4dev/data-collection)**.
 *
 * The version of the OpenAPI document: 1.0.2
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
    factory(root.expect, root.LocationScore);
  }
}(this, function(expect, LocationScore) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new LocationScore.CategoryRatedAreasAllOfCategoryScoresRestaurant();
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

  describe('CategoryRatedAreasAllOfCategoryScoresRestaurant', function() {
    it('should create an instance of CategoryRatedAreasAllOfCategoryScoresRestaurant', function() {
      // uncomment below and update the code to test CategoryRatedAreasAllOfCategoryScoresRestaurant
      //var instance = new LocationScore.CategoryRatedAreasAllOfCategoryScoresRestaurant();
      //expect(instance).to.be.a(LocationScore.CategoryRatedAreasAllOfCategoryScoresRestaurant);
    });

    it('should have the property overall (base name: "overall")', function() {
      // uncomment below and update the code to test the property overall
      //var instance = new LocationScore.CategoryRatedAreasAllOfCategoryScoresRestaurant();
      //expect(instance).to.be();
    });

    it('should have the property vegetarian (base name: "vegetarian")', function() {
      // uncomment below and update the code to test the property vegetarian
      //var instance = new LocationScore.CategoryRatedAreasAllOfCategoryScoresRestaurant();
      //expect(instance).to.be();
    });

  });

}));
