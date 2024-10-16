/**
 * Football Prediction API
 * The Football Prediction API allows developers to get predictions for upcoming football (soccer) matches, results for past matches, and performance monitoring for statistical models.
 *
 * The version of the OpenAPI document: 2
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
    factory(root.expect, root.FootballPredictionApi);
  }
}(this, function(expect, FootballPredictionApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new FootballPredictionApi.ApiV2PredictionsIdGet200Response();
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

  describe('ApiV2PredictionsIdGet200Response', function() {
    it('should create an instance of ApiV2PredictionsIdGet200Response', function() {
      // uncomment below and update the code to test ApiV2PredictionsIdGet200Response
      //var instance = new FootballPredictionApi.ApiV2PredictionsIdGet200Response();
      //expect(instance).to.be.a(FootballPredictionApi.ApiV2PredictionsIdGet200Response);
    });

    it('should have the property data (base name: "data")', function() {
      // uncomment below and update the code to test the property data
      //var instance = new FootballPredictionApi.ApiV2PredictionsIdGet200Response();
      //expect(instance).to.be();
    });

  });

}));
