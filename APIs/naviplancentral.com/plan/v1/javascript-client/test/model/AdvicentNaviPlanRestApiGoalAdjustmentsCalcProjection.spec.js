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
    instance = new NaviPlanApi.AdvicentNaviPlanRestApiGoalAdjustmentsCalcProjection();
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

  describe('AdvicentNaviPlanRestApiGoalAdjustmentsCalcProjection', function() {
    it('should create an instance of AdvicentNaviPlanRestApiGoalAdjustmentsCalcProjection', function() {
      // uncomment below and update the code to test AdvicentNaviPlanRestApiGoalAdjustmentsCalcProjection
      //var instance = new NaviPlanApi.AdvicentNaviPlanRestApiGoalAdjustmentsCalcProjection();
      //expect(instance).to.be.a(NaviPlanApi.AdvicentNaviPlanRestApiGoalAdjustmentsCalcProjection);
    });

    it('should have the property projectedAbilities (base name: "projectedAbilities")', function() {
      // uncomment below and update the code to test the property projectedAbilities
      //var instance = new NaviPlanApi.AdvicentNaviPlanRestApiGoalAdjustmentsCalcProjection();
      //expect(instance).to.be();
    });

    it('should have the property projectedNeed (base name: "projectedNeed")', function() {
      // uncomment below and update the code to test the property projectedNeed
      //var instance = new NaviPlanApi.AdvicentNaviPlanRestApiGoalAdjustmentsCalcProjection();
      //expect(instance).to.be();
    });

    it('should have the property projectedRetirementAssetValues (base name: "projectedRetirementAssetValues")', function() {
      // uncomment below and update the code to test the property projectedRetirementAssetValues
      //var instance = new NaviPlanApi.AdvicentNaviPlanRestApiGoalAdjustmentsCalcProjection();
      //expect(instance).to.be();
    });

    it('should have the property year (base name: "year")', function() {
      // uncomment below and update the code to test the property year
      //var instance = new NaviPlanApi.AdvicentNaviPlanRestApiGoalAdjustmentsCalcProjection();
      //expect(instance).to.be();
    });

  });

}));
