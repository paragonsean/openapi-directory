/**
 * Flight Delay Prediction
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 1.0.6
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
    factory(root.expect, root.FlightDelayPrediction);
  }
}(this, function(expect, FlightDelayPrediction) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new FlightDelayPrediction.DelayPrediction();
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

  describe('DelayPrediction', function() {
    it('should create an instance of DelayPrediction', function() {
      // uncomment below and update the code to test DelayPrediction
      //var instance = new FlightDelayPrediction.DelayPrediction();
      //expect(instance).to.be.a(FlightDelayPrediction.DelayPrediction);
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new FlightDelayPrediction.DelayPrediction();
      //expect(instance).to.be();
    });

    it('should have the property probability (base name: "probability")', function() {
      // uncomment below and update the code to test the property probability
      //var instance = new FlightDelayPrediction.DelayPrediction();
      //expect(instance).to.be();
    });

    it('should have the property result (base name: "result")', function() {
      // uncomment below and update the code to test the property result
      //var instance = new FlightDelayPrediction.DelayPrediction();
      //expect(instance).to.be();
    });

    it('should have the property subType (base name: "subType")', function() {
      // uncomment below and update the code to test the property subType
      //var instance = new FlightDelayPrediction.DelayPrediction();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new FlightDelayPrediction.DelayPrediction();
      //expect(instance).to.be();
    });

  });

}));
