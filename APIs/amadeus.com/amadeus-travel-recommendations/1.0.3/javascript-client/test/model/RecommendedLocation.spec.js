/**
 * Travel Recommendations API
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 1.0.3
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
    factory(root.expect, root.TravelRecommendationsApi);
  }
}(this, function(expect, TravelRecommendationsApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new TravelRecommendationsApi.RecommendedLocation();
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

  describe('RecommendedLocation', function() {
    it('should create an instance of RecommendedLocation', function() {
      // uncomment below and update the code to test RecommendedLocation
      //var instance = new TravelRecommendationsApi.RecommendedLocation();
      //expect(instance).to.be.a(TravelRecommendationsApi.RecommendedLocation);
    });

    it('should have the property geoCode (base name: "geoCode")', function() {
      // uncomment below and update the code to test the property geoCode
      //var instance = new TravelRecommendationsApi.RecommendedLocation();
      //expect(instance).to.be();
    });

    it('should have the property iataCode (base name: "iataCode")', function() {
      // uncomment below and update the code to test the property iataCode
      //var instance = new TravelRecommendationsApi.RecommendedLocation();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new TravelRecommendationsApi.RecommendedLocation();
      //expect(instance).to.be();
    });

    it('should have the property subtype (base name: "subtype")', function() {
      // uncomment below and update the code to test the property subtype
      //var instance = new TravelRecommendationsApi.RecommendedLocation();
      //expect(instance).to.be();
    });

    it('should have the property relevance (base name: "relevance")', function() {
      // uncomment below and update the code to test the property relevance
      //var instance = new TravelRecommendationsApi.RecommendedLocation();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new TravelRecommendationsApi.RecommendedLocation();
      //expect(instance).to.be();
    });

  });

}));
