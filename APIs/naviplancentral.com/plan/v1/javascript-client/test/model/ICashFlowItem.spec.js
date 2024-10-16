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
    instance = new NaviPlanApi.ICashFlowItem();
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

  describe('ICashFlowItem', function() {
    it('should create an instance of ICashFlowItem', function() {
      // uncomment below and update the code to test ICashFlowItem
      //var instance = new NaviPlanApi.ICashFlowItem();
      //expect(instance).to.be.a(NaviPlanApi.ICashFlowItem);
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new NaviPlanApi.ICashFlowItem();
      //expect(instance).to.be();
    });

    it('should have the property descriptionWithOwner (base name: "descriptionWithOwner")', function() {
      // uncomment below and update the code to test the property descriptionWithOwner
      //var instance = new NaviPlanApi.ICashFlowItem();
      //expect(instance).to.be();
    });

    it('should have the property isCPP (base name: "isCPP")', function() {
      // uncomment below and update the code to test the property isCPP
      //var instance = new NaviPlanApi.ICashFlowItem();
      //expect(instance).to.be();
    });

    it('should have the property isOAS (base name: "isOAS")', function() {
      // uncomment below and update the code to test the property isOAS
      //var instance = new NaviPlanApi.ICashFlowItem();
      //expect(instance).to.be();
    });

    it('should have the property sourceId (base name: "sourceId")', function() {
      // uncomment below and update the code to test the property sourceId
      //var instance = new NaviPlanApi.ICashFlowItem();
      //expect(instance).to.be();
    });

    it('should have the property typeDescription (base name: "typeDescription")', function() {
      // uncomment below and update the code to test the property typeDescription
      //var instance = new NaviPlanApi.ICashFlowItem();
      //expect(instance).to.be();
    });

    it('should have the property value (base name: "value")', function() {
      // uncomment below and update the code to test the property value
      //var instance = new NaviPlanApi.ICashFlowItem();
      //expect(instance).to.be();
    });

  });

}));
