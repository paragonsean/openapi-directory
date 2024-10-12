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
    instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits();
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

  describe('AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits', function() {
    it('should create an instance of AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits', function() {
      // uncomment below and update the code to test AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits();
      //expect(instance).to.be.a(AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits);
    });

    it('should have the property maxDiskSizeInMb (base name: "maxDiskSizeInMb")', function() {
      // uncomment below and update the code to test the property maxDiskSizeInMb
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits();
      //expect(instance).to.be();
    });

    it('should have the property maxMemoryInMb (base name: "maxMemoryInMb")', function() {
      // uncomment below and update the code to test the property maxMemoryInMb
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits();
      //expect(instance).to.be();
    });

    it('should have the property maxPercentageCpu (base name: "maxPercentageCpu")', function() {
      // uncomment below and update the code to test the property maxPercentageCpu
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits();
      //expect(instance).to.be();
    });

  });

}));
