/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
 *
 * The version of the OpenAPI document: v1
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
    factory(root.expect, root.NaviPlanApi);
  }
}(this, function(expect, NaviPlanApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NaviPlanApi.INetWorthAtDate();
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

  describe('INetWorthAtDate', function() {
    it('should create an instance of INetWorthAtDate', function() {
      // uncomment below and update the code to test INetWorthAtDate
      //var instance = new NaviPlanApi.INetWorthAtDate();
      //expect(instance).to.be.a(NaviPlanApi.INetWorthAtDate);
    });

    it('should have the property assets (base name: "assets")', function() {
      // uncomment below and update the code to test the property assets
      //var instance = new NaviPlanApi.INetWorthAtDate();
      //expect(instance).to.be();
    });

    it('should have the property assetsFundingRetirement (base name: "assetsFundingRetirement")', function() {
      // uncomment below and update the code to test the property assetsFundingRetirement
      //var instance = new NaviPlanApi.INetWorthAtDate();
      //expect(instance).to.be();
    });

    it('should have the property clientNetWorth (base name: "clientNetWorth")', function() {
      // uncomment below and update the code to test the property clientNetWorth
      //var instance = new NaviPlanApi.INetWorthAtDate();
      //expect(instance).to.be();
    });

    it('should have the property coClientNetWorth (base name: "coClientNetWorth")', function() {
      // uncomment below and update the code to test the property coClientNetWorth
      //var instance = new NaviPlanApi.INetWorthAtDate();
      //expect(instance).to.be();
    });

    it('should have the property communityPropertyNetWorth (base name: "communityPropertyNetWorth")', function() {
      // uncomment below and update the code to test the property communityPropertyNetWorth
      //var instance = new NaviPlanApi.INetWorthAtDate();
      //expect(instance).to.be();
    });

    it('should have the property jointNetWorth (base name: "jointNetWorth")', function() {
      // uncomment below and update the code to test the property jointNetWorth
      //var instance = new NaviPlanApi.INetWorthAtDate();
      //expect(instance).to.be();
    });

    it('should have the property liabilities (base name: "liabilities")', function() {
      // uncomment below and update the code to test the property liabilities
      //var instance = new NaviPlanApi.INetWorthAtDate();
      //expect(instance).to.be();
    });

    it('should have the property totalNetWorth (base name: "totalNetWorth")', function() {
      // uncomment below and update the code to test the property totalNetWorth
      //var instance = new NaviPlanApi.INetWorthAtDate();
      //expect(instance).to.be();
    });

  });

}));
