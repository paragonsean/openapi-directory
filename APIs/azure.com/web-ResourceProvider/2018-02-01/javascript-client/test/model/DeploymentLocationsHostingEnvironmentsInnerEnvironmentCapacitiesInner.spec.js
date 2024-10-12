/**
 *  API Client
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
    factory(root.expect, root.ApiClient);
  }
}(this, function(expect, ApiClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new ApiClient.DeploymentLocationsHostingEnvironmentsInnerEnvironmentCapacitiesInner();
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

  describe('DeploymentLocationsHostingEnvironmentsInnerEnvironmentCapacitiesInner', function() {
    it('should create an instance of DeploymentLocationsHostingEnvironmentsInnerEnvironmentCapacitiesInner', function() {
      // uncomment below and update the code to test DeploymentLocationsHostingEnvironmentsInnerEnvironmentCapacitiesInner
      //var instance = new ApiClient.DeploymentLocationsHostingEnvironmentsInnerEnvironmentCapacitiesInner();
      //expect(instance).to.be.a(ApiClient.DeploymentLocationsHostingEnvironmentsInnerEnvironmentCapacitiesInner);
    });

    it('should have the property availableCapacity (base name: "availableCapacity")', function() {
      // uncomment below and update the code to test the property availableCapacity
      //var instance = new ApiClient.DeploymentLocationsHostingEnvironmentsInnerEnvironmentCapacitiesInner();
      //expect(instance).to.be();
    });

    it('should have the property computeMode (base name: "computeMode")', function() {
      // uncomment below and update the code to test the property computeMode
      //var instance = new ApiClient.DeploymentLocationsHostingEnvironmentsInnerEnvironmentCapacitiesInner();
      //expect(instance).to.be();
    });

    it('should have the property excludeFromCapacityAllocation (base name: "excludeFromCapacityAllocation")', function() {
      // uncomment below and update the code to test the property excludeFromCapacityAllocation
      //var instance = new ApiClient.DeploymentLocationsHostingEnvironmentsInnerEnvironmentCapacitiesInner();
      //expect(instance).to.be();
    });

    it('should have the property isApplicableForAllComputeModes (base name: "isApplicableForAllComputeModes")', function() {
      // uncomment below and update the code to test the property isApplicableForAllComputeModes
      //var instance = new ApiClient.DeploymentLocationsHostingEnvironmentsInnerEnvironmentCapacitiesInner();
      //expect(instance).to.be();
    });

    it('should have the property isLinux (base name: "isLinux")', function() {
      // uncomment below and update the code to test the property isLinux
      //var instance = new ApiClient.DeploymentLocationsHostingEnvironmentsInnerEnvironmentCapacitiesInner();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new ApiClient.DeploymentLocationsHostingEnvironmentsInnerEnvironmentCapacitiesInner();
      //expect(instance).to.be();
    });

    it('should have the property siteMode (base name: "siteMode")', function() {
      // uncomment below and update the code to test the property siteMode
      //var instance = new ApiClient.DeploymentLocationsHostingEnvironmentsInnerEnvironmentCapacitiesInner();
      //expect(instance).to.be();
    });

    it('should have the property totalCapacity (base name: "totalCapacity")', function() {
      // uncomment below and update the code to test the property totalCapacity
      //var instance = new ApiClient.DeploymentLocationsHostingEnvironmentsInnerEnvironmentCapacitiesInner();
      //expect(instance).to.be();
    });

    it('should have the property unit (base name: "unit")', function() {
      // uncomment below and update the code to test the property unit
      //var instance = new ApiClient.DeploymentLocationsHostingEnvironmentsInnerEnvironmentCapacitiesInner();
      //expect(instance).to.be();
    });

    it('should have the property workerSize (base name: "workerSize")', function() {
      // uncomment below and update the code to test the property workerSize
      //var instance = new ApiClient.DeploymentLocationsHostingEnvironmentsInnerEnvironmentCapacitiesInner();
      //expect(instance).to.be();
    });

    it('should have the property workerSizeId (base name: "workerSizeId")', function() {
      // uncomment below and update the code to test the property workerSizeId
      //var instance = new ApiClient.DeploymentLocationsHostingEnvironmentsInnerEnvironmentCapacitiesInner();
      //expect(instance).to.be();
    });

  });

}));
