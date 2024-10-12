/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2016-09-01
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
    instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerPropertiesHostingEnvironmentProfile();
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

  describe('AppServicePlansList200ResponseValueInnerPropertiesHostingEnvironmentProfile', function() {
    it('should create an instance of AppServicePlansList200ResponseValueInnerPropertiesHostingEnvironmentProfile', function() {
      // uncomment below and update the code to test AppServicePlansList200ResponseValueInnerPropertiesHostingEnvironmentProfile
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerPropertiesHostingEnvironmentProfile();
      //expect(instance).to.be.a(AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerPropertiesHostingEnvironmentProfile);
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerPropertiesHostingEnvironmentProfile();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerPropertiesHostingEnvironmentProfile();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerPropertiesHostingEnvironmentProfile();
      //expect(instance).to.be();
    });

  });

}));
