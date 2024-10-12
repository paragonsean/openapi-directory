/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
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
    factory(root.expect, root.AppServicePlansApiClient);
  }
}(this, function(expect, AppServicePlansApiClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus();
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

  describe('AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus', function() {
    it('should create an instance of AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus', function() {
      // uncomment below and update the code to test AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus();
      //expect(instance).to.be.a(AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus);
    });

    it('should have the property destinationSlotName (base name: "destinationSlotName")', function() {
      // uncomment below and update the code to test the property destinationSlotName
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus();
      //expect(instance).to.be();
    });

    it('should have the property sourceSlotName (base name: "sourceSlotName")', function() {
      // uncomment below and update the code to test the property sourceSlotName
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus();
      //expect(instance).to.be();
    });

    it('should have the property timestampUtc (base name: "timestampUtc")', function() {
      // uncomment below and update the code to test the property timestampUtc
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus();
      //expect(instance).to.be();
    });

  });

}));
