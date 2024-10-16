/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
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
    factory(root.expect, root.AppCenterClient);
  }
}(this, function(expect, AppCenterClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AppCenterClient.AggregatedBillingInformation();
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

  describe('AggregatedBillingInformation', function() {
    it('should create an instance of AggregatedBillingInformation', function() {
      // uncomment below and update the code to test AggregatedBillingInformation
      //var instance = new AppCenterClient.AggregatedBillingInformation();
      //expect(instance).to.be.a(AppCenterClient.AggregatedBillingInformation);
    });

    it('should have the property azureSubscriptionId (base name: "azureSubscriptionId")', function() {
      // uncomment below and update the code to test the property azureSubscriptionId
      //var instance = new AppCenterClient.AggregatedBillingInformation();
      //expect(instance).to.be();
    });

    it('should have the property azureSubscriptionState (base name: "azureSubscriptionState")', function() {
      // uncomment below and update the code to test the property azureSubscriptionState
      //var instance = new AppCenterClient.AggregatedBillingInformation();
      //expect(instance).to.be();
    });

    it('should have the property billingPlans (base name: "billingPlans")', function() {
      // uncomment below and update the code to test the property billingPlans
      //var instance = new AppCenterClient.AggregatedBillingInformation();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new AppCenterClient.AggregatedBillingInformation();
      //expect(instance).to.be();
    });

    it('should have the property timestamp (base name: "timestamp")', function() {
      // uncomment below and update the code to test the property timestamp
      //var instance = new AppCenterClient.AggregatedBillingInformation();
      //expect(instance).to.be();
    });

    it('should have the property usage (base name: "usage")', function() {
      // uncomment below and update the code to test the property usage
      //var instance = new AppCenterClient.AggregatedBillingInformation();
      //expect(instance).to.be();
    });

    it('should have the property version (base name: "version")', function() {
      // uncomment below and update the code to test the property version
      //var instance = new AppCenterClient.AggregatedBillingInformation();
      //expect(instance).to.be();
    });

  });

}));
