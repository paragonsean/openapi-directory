/**
 * Flight Choice Prediction
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 2.0.2
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
    factory(root.expect, root.FlightChoicePrediction);
  }
}(this, function(expect, FlightChoicePrediction) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new FlightChoicePrediction.AdditionalService();
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

  describe('AdditionalService', function() {
    it('should create an instance of AdditionalService', function() {
      // uncomment below and update the code to test AdditionalService
      //var instance = new FlightChoicePrediction.AdditionalService();
      //expect(instance).to.be.a(FlightChoicePrediction.AdditionalService);
    });

    it('should have the property amount (base name: "amount")', function() {
      // uncomment below and update the code to test the property amount
      //var instance = new FlightChoicePrediction.AdditionalService();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new FlightChoicePrediction.AdditionalService();
      //expect(instance).to.be();
    });

  });

}));
