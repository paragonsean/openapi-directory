/**
 * agentOS Api V2, Customer Login Call Group
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-customer
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
    factory(root.expect, root.AgentOsApiV2CustomerLoginCallGroup);
  }
}(this, function(expect, AgentOsApiV2CustomerLoginCallGroup) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AgentOsApiV2CustomerLoginCallGroup.LandlordRentArrearsModel();
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

  describe('LandlordRentArrearsModel', function() {
    it('should create an instance of LandlordRentArrearsModel', function() {
      // uncomment below and update the code to test LandlordRentArrearsModel
      //var instance = new AgentOsApiV2CustomerLoginCallGroup.LandlordRentArrearsModel();
      //expect(instance).to.be.a(AgentOsApiV2CustomerLoginCallGroup.LandlordRentArrearsModel);
    });

    it('should have the property chaseNotes (base name: "ChaseNotes")', function() {
      // uncomment below and update the code to test the property chaseNotes
      //var instance = new AgentOsApiV2CustomerLoginCallGroup.LandlordRentArrearsModel();
      //expect(instance).to.be();
    });

    it('should have the property rentCollected (base name: "RentCollected")', function() {
      // uncomment below and update the code to test the property rentCollected
      //var instance = new AgentOsApiV2CustomerLoginCallGroup.LandlordRentArrearsModel();
      //expect(instance).to.be();
    });

    it('should have the property rentOutstanding (base name: "RentOutstanding")', function() {
      // uncomment below and update the code to test the property rentOutstanding
      //var instance = new AgentOsApiV2CustomerLoginCallGroup.LandlordRentArrearsModel();
      //expect(instance).to.be();
    });

    it('should have the property totalRentArrears (base name: "TotalRentArrears")', function() {
      // uncomment below and update the code to test the property totalRentArrears
      //var instance = new AgentOsApiV2CustomerLoginCallGroup.LandlordRentArrearsModel();
      //expect(instance).to.be();
    });

  });

}));
