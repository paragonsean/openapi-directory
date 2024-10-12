/**
 * Azure Media Services
 * This Swagger was generated by the API Framework.
 *
 * The version of the OpenAPI document: 2018-07-01
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
    factory(root.expect, root.AzureMediaServices);
  }
}(this, function(expect, AzureMediaServices) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AzureMediaServices.PresentationTimeRange();
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

  describe('PresentationTimeRange', function() {
    it('should create an instance of PresentationTimeRange', function() {
      // uncomment below and update the code to test PresentationTimeRange
      //var instance = new AzureMediaServices.PresentationTimeRange();
      //expect(instance).to.be.a(AzureMediaServices.PresentationTimeRange);
    });

    it('should have the property endTimestamp (base name: "endTimestamp")', function() {
      // uncomment below and update the code to test the property endTimestamp
      //var instance = new AzureMediaServices.PresentationTimeRange();
      //expect(instance).to.be();
    });

    it('should have the property forceEndTimestamp (base name: "forceEndTimestamp")', function() {
      // uncomment below and update the code to test the property forceEndTimestamp
      //var instance = new AzureMediaServices.PresentationTimeRange();
      //expect(instance).to.be();
    });

    it('should have the property liveBackoffDuration (base name: "liveBackoffDuration")', function() {
      // uncomment below and update the code to test the property liveBackoffDuration
      //var instance = new AzureMediaServices.PresentationTimeRange();
      //expect(instance).to.be();
    });

    it('should have the property presentationWindowDuration (base name: "presentationWindowDuration")', function() {
      // uncomment below and update the code to test the property presentationWindowDuration
      //var instance = new AzureMediaServices.PresentationTimeRange();
      //expect(instance).to.be();
    });

    it('should have the property startTimestamp (base name: "startTimestamp")', function() {
      // uncomment below and update the code to test the property startTimestamp
      //var instance = new AzureMediaServices.PresentationTimeRange();
      //expect(instance).to.be();
    });

    it('should have the property timescale (base name: "timescale")', function() {
      // uncomment below and update the code to test the property timescale
      //var instance = new AzureMediaServices.PresentationTimeRange();
      //expect(instance).to.be();
    });

  });

}));
