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
    instance = new NaviPlanApi.AssumptionsModel();
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

  describe('AssumptionsModel', function() {
    it('should create an instance of AssumptionsModel', function() {
      // uncomment below and update the code to test AssumptionsModel
      //var instance = new NaviPlanApi.AssumptionsModel();
      //expect(instance).to.be.a(NaviPlanApi.AssumptionsModel);
    });

    it('should have the property assumptions (base name: "assumptions")', function() {
      // uncomment below and update the code to test the property assumptions
      //var instance = new NaviPlanApi.AssumptionsModel();
      //expect(instance).to.be();
    });

    it('should have the property links (base name: "links")', function() {
      // uncomment below and update the code to test the property links
      //var instance = new NaviPlanApi.AssumptionsModel();
      //expect(instance).to.be();
    });

  });

}));
