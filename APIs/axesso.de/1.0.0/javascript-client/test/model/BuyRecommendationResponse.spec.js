/**
 * Axesso Api
 * Use this api to fetch information to Amazon products and more.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@axesso.de
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
    factory(root.expect, root.AxessoApi);
  }
}(this, function(expect, AxessoApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AxessoApi.BuyRecommendationResponse();
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

  describe('BuyRecommendationResponse', function() {
    it('should create an instance of BuyRecommendationResponse', function() {
      // uncomment below and update the code to test BuyRecommendationResponse
      //var instance = new AxessoApi.BuyRecommendationResponse();
      //expect(instance).to.be.a(AxessoApi.BuyRecommendationResponse);
    });

    it('should have the property buyRecommendations (base name: "buyRecommendations")', function() {
      // uncomment below and update the code to test the property buyRecommendations
      //var instance = new AxessoApi.BuyRecommendationResponse();
      //expect(instance).to.be();
    });

    it('should have the property numberOfProducts (base name: "numberOfProducts")', function() {
      // uncomment below and update the code to test the property numberOfProducts
      //var instance = new AxessoApi.BuyRecommendationResponse();
      //expect(instance).to.be();
    });

    it('should have the property responseMessage (base name: "responseMessage")', function() {
      // uncomment below and update the code to test the property responseMessage
      //var instance = new AxessoApi.BuyRecommendationResponse();
      //expect(instance).to.be();
    });

    it('should have the property responseStatus (base name: "responseStatus")', function() {
      // uncomment below and update the code to test the property responseStatus
      //var instance = new AxessoApi.BuyRecommendationResponse();
      //expect(instance).to.be();
    });

  });

}));
