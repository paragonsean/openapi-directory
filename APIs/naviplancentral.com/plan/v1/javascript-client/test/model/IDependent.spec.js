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
    instance = new NaviPlanApi.IDependent();
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

  describe('IDependent', function() {
    it('should create an instance of IDependent', function() {
      // uncomment below and update the code to test IDependent
      //var instance = new NaviPlanApi.IDependent();
      //expect(instance).to.be.a(NaviPlanApi.IDependent);
    });

    it('should have the property address (base name: "address")', function() {
      // uncomment below and update the code to test the property address
      //var instance = new NaviPlanApi.IDependent();
      //expect(instance).to.be();
    });

    it('should have the property ageAsOfPlanDate (base name: "ageAsOfPlanDate")', function() {
      // uncomment below and update the code to test the property ageAsOfPlanDate
      //var instance = new NaviPlanApi.IDependent();
      //expect(instance).to.be();
    });

    it('should have the property birthdate (base name: "birthdate")', function() {
      // uncomment below and update the code to test the property birthdate
      //var instance = new NaviPlanApi.IDependent();
      //expect(instance).to.be();
    });

    it('should have the property citizenship (base name: "citizenship")', function() {
      // uncomment below and update the code to test the property citizenship
      //var instance = new NaviPlanApi.IDependent();
      //expect(instance).to.be();
    });

    it('should have the property dependentOf (base name: "dependentOf")', function() {
      // uncomment below and update the code to test the property dependentOf
      //var instance = new NaviPlanApi.IDependent();
      //expect(instance).to.be();
    });

    it('should have the property dependentOfId (base name: "dependentOfId")', function() {
      // uncomment below and update the code to test the property dependentOfId
      //var instance = new NaviPlanApi.IDependent();
      //expect(instance).to.be();
    });

    it('should have the property email (base name: "email")', function() {
      // uncomment below and update the code to test the property email
      //var instance = new NaviPlanApi.IDependent();
      //expect(instance).to.be();
    });

    it('should have the property employer (base name: "employer")', function() {
      // uncomment below and update the code to test the property employer
      //var instance = new NaviPlanApi.IDependent();
      //expect(instance).to.be();
    });

    it('should have the property gender (base name: "gender")', function() {
      // uncomment below and update the code to test the property gender
      //var instance = new NaviPlanApi.IDependent();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new NaviPlanApi.IDependent();
      //expect(instance).to.be();
    });

    it('should have the property ownershipId (base name: "ownershipId")', function() {
      // uncomment below and update the code to test the property ownershipId
      //var instance = new NaviPlanApi.IDependent();
      //expect(instance).to.be();
    });

    it('should have the property phone (base name: "phone")', function() {
      // uncomment below and update the code to test the property phone
      //var instance = new NaviPlanApi.IDependent();
      //expect(instance).to.be();
    });

    it('should have the property relationship (base name: "relationship")', function() {
      // uncomment below and update the code to test the property relationship
      //var instance = new NaviPlanApi.IDependent();
      //expect(instance).to.be();
    });

  });

}));
