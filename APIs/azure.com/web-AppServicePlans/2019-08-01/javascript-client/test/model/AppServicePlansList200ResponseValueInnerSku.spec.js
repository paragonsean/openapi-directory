/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
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
    instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerSku();
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

  describe('AppServicePlansList200ResponseValueInnerSku', function() {
    it('should create an instance of AppServicePlansList200ResponseValueInnerSku', function() {
      // uncomment below and update the code to test AppServicePlansList200ResponseValueInnerSku
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerSku();
      //expect(instance).to.be.a(AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerSku);
    });

    it('should have the property capabilities (base name: "capabilities")', function() {
      // uncomment below and update the code to test the property capabilities
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerSku();
      //expect(instance).to.be();
    });

    it('should have the property capacity (base name: "capacity")', function() {
      // uncomment below and update the code to test the property capacity
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerSku();
      //expect(instance).to.be();
    });

    it('should have the property family (base name: "family")', function() {
      // uncomment below and update the code to test the property family
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerSku();
      //expect(instance).to.be();
    });

    it('should have the property locations (base name: "locations")', function() {
      // uncomment below and update the code to test the property locations
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerSku();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerSku();
      //expect(instance).to.be();
    });

    it('should have the property size (base name: "size")', function() {
      // uncomment below and update the code to test the property size
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerSku();
      //expect(instance).to.be();
    });

    it('should have the property skuCapacity (base name: "skuCapacity")', function() {
      // uncomment below and update the code to test the property skuCapacity
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerSku();
      //expect(instance).to.be();
    });

    it('should have the property tier (base name: "tier")', function() {
      // uncomment below and update the code to test the property tier
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerSku();
      //expect(instance).to.be();
    });

  });

}));
