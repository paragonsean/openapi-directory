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
    instance = new NaviPlanApi.AdvicentNaviPlanRestApiNetWorthModelsAccountModel();
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

  describe('AdvicentNaviPlanRestApiNetWorthModelsAccountModel', function() {
    it('should create an instance of AdvicentNaviPlanRestApiNetWorthModelsAccountModel', function() {
      // uncomment below and update the code to test AdvicentNaviPlanRestApiNetWorthModelsAccountModel
      //var instance = new NaviPlanApi.AdvicentNaviPlanRestApiNetWorthModelsAccountModel();
      //expect(instance).to.be.a(NaviPlanApi.AdvicentNaviPlanRestApiNetWorthModelsAccountModel);
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new NaviPlanApi.AdvicentNaviPlanRestApiNetWorthModelsAccountModel();
      //expect(instance).to.be();
    });

    it('should have the property holdings (base name: "holdings")', function() {
      // uncomment below and update the code to test the property holdings
      //var instance = new NaviPlanApi.AdvicentNaviPlanRestApiNetWorthModelsAccountModel();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new NaviPlanApi.AdvicentNaviPlanRestApiNetWorthModelsAccountModel();
      //expect(instance).to.be();
    });

    it('should have the property legacyId (base name: "legacyId")', function() {
      // uncomment below and update the code to test the property legacyId
      //var instance = new NaviPlanApi.AdvicentNaviPlanRestApiNetWorthModelsAccountModel();
      //expect(instance).to.be();
    });

    it('should have the property owner (base name: "owner")', function() {
      // uncomment below and update the code to test the property owner
      //var instance = new NaviPlanApi.AdvicentNaviPlanRestApiNetWorthModelsAccountModel();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new NaviPlanApi.AdvicentNaviPlanRestApiNetWorthModelsAccountModel();
      //expect(instance).to.be();
    });

  });

}));
