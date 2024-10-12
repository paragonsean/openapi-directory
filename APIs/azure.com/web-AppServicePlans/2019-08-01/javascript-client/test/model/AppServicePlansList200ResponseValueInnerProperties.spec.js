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
    instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerProperties();
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

  describe('AppServicePlansList200ResponseValueInnerProperties', function() {
    it('should create an instance of AppServicePlansList200ResponseValueInnerProperties', function() {
      // uncomment below and update the code to test AppServicePlansList200ResponseValueInnerProperties
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerProperties();
      //expect(instance).to.be.a(AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerProperties);
    });

    it('should have the property freeOfferExpirationTime (base name: "freeOfferExpirationTime")', function() {
      // uncomment below and update the code to test the property freeOfferExpirationTime
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerProperties();
      //expect(instance).to.be();
    });

    it('should have the property geoRegion (base name: "geoRegion")', function() {
      // uncomment below and update the code to test the property geoRegion
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerProperties();
      //expect(instance).to.be();
    });

    it('should have the property hostingEnvironmentProfile (base name: "hostingEnvironmentProfile")', function() {
      // uncomment below and update the code to test the property hostingEnvironmentProfile
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerProperties();
      //expect(instance).to.be();
    });

    it('should have the property hyperV (base name: "hyperV")', function() {
      // uncomment below and update the code to test the property hyperV
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerProperties();
      //expect(instance).to.be();
    });

    it('should have the property isSpot (base name: "isSpot")', function() {
      // uncomment below and update the code to test the property isSpot
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerProperties();
      //expect(instance).to.be();
    });

    it('should have the property isXenon (base name: "isXenon")', function() {
      // uncomment below and update the code to test the property isXenon
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerProperties();
      //expect(instance).to.be();
    });

    it('should have the property maximumElasticWorkerCount (base name: "maximumElasticWorkerCount")', function() {
      // uncomment below and update the code to test the property maximumElasticWorkerCount
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerProperties();
      //expect(instance).to.be();
    });

    it('should have the property maximumNumberOfWorkers (base name: "maximumNumberOfWorkers")', function() {
      // uncomment below and update the code to test the property maximumNumberOfWorkers
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerProperties();
      //expect(instance).to.be();
    });

    it('should have the property numberOfSites (base name: "numberOfSites")', function() {
      // uncomment below and update the code to test the property numberOfSites
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerProperties();
      //expect(instance).to.be();
    });

    it('should have the property perSiteScaling (base name: "perSiteScaling")', function() {
      // uncomment below and update the code to test the property perSiteScaling
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerProperties();
      //expect(instance).to.be();
    });

    it('should have the property provisioningState (base name: "provisioningState")', function() {
      // uncomment below and update the code to test the property provisioningState
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerProperties();
      //expect(instance).to.be();
    });

    it('should have the property reserved (base name: "reserved")', function() {
      // uncomment below and update the code to test the property reserved
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerProperties();
      //expect(instance).to.be();
    });

    it('should have the property resourceGroup (base name: "resourceGroup")', function() {
      // uncomment below and update the code to test the property resourceGroup
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerProperties();
      //expect(instance).to.be();
    });

    it('should have the property spotExpirationTime (base name: "spotExpirationTime")', function() {
      // uncomment below and update the code to test the property spotExpirationTime
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerProperties();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerProperties();
      //expect(instance).to.be();
    });

    it('should have the property subscription (base name: "subscription")', function() {
      // uncomment below and update the code to test the property subscription
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerProperties();
      //expect(instance).to.be();
    });

    it('should have the property targetWorkerCount (base name: "targetWorkerCount")', function() {
      // uncomment below and update the code to test the property targetWorkerCount
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerProperties();
      //expect(instance).to.be();
    });

    it('should have the property targetWorkerSizeId (base name: "targetWorkerSizeId")', function() {
      // uncomment below and update the code to test the property targetWorkerSizeId
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerProperties();
      //expect(instance).to.be();
    });

    it('should have the property workerTierName (base name: "workerTierName")', function() {
      // uncomment below and update the code to test the property workerTierName
      //var instance = new AppServicePlansApiClient.AppServicePlansList200ResponseValueInnerProperties();
      //expect(instance).to.be();
    });

  });

}));
