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
    instance = new NaviPlanApi.AdvisorModel();
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

  describe('AdvisorModel', function() {
    it('should create an instance of AdvisorModel', function() {
      // uncomment below and update the code to test AdvisorModel
      //var instance = new NaviPlanApi.AdvisorModel();
      //expect(instance).to.be.a(NaviPlanApi.AdvisorModel);
    });

    it('should have the property addressLine1 (base name: "addressLine1")', function() {
      // uncomment below and update the code to test the property addressLine1
      //var instance = new NaviPlanApi.AdvisorModel();
      //expect(instance).to.be();
    });

    it('should have the property addressLine2 (base name: "addressLine2")', function() {
      // uncomment below and update the code to test the property addressLine2
      //var instance = new NaviPlanApi.AdvisorModel();
      //expect(instance).to.be();
    });

    it('should have the property advisorId (base name: "advisorId")', function() {
      // uncomment below and update the code to test the property advisorId
      //var instance = new NaviPlanApi.AdvisorModel();
      //expect(instance).to.be();
    });

    it('should have the property advisorTitle (base name: "advisorTitle")', function() {
      // uncomment below and update the code to test the property advisorTitle
      //var instance = new NaviPlanApi.AdvisorModel();
      //expect(instance).to.be();
    });

    it('should have the property businessPhone (base name: "businessPhone")', function() {
      // uncomment below and update the code to test the property businessPhone
      //var instance = new NaviPlanApi.AdvisorModel();
      //expect(instance).to.be();
    });

    it('should have the property cellPhone (base name: "cellPhone")', function() {
      // uncomment below and update the code to test the property cellPhone
      //var instance = new NaviPlanApi.AdvisorModel();
      //expect(instance).to.be();
    });

    it('should have the property city (base name: "city")', function() {
      // uncomment below and update the code to test the property city
      //var instance = new NaviPlanApi.AdvisorModel();
      //expect(instance).to.be();
    });

    it('should have the property emailAddress (base name: "emailAddress")', function() {
      // uncomment below and update the code to test the property emailAddress
      //var instance = new NaviPlanApi.AdvisorModel();
      //expect(instance).to.be();
    });

    it('should have the property faxPhone (base name: "faxPhone")', function() {
      // uncomment below and update the code to test the property faxPhone
      //var instance = new NaviPlanApi.AdvisorModel();
      //expect(instance).to.be();
    });

    it('should have the property firstName (base name: "firstName")', function() {
      // uncomment below and update the code to test the property firstName
      //var instance = new NaviPlanApi.AdvisorModel();
      //expect(instance).to.be();
    });

    it('should have the property homePhone (base name: "homePhone")', function() {
      // uncomment below and update the code to test the property homePhone
      //var instance = new NaviPlanApi.AdvisorModel();
      //expect(instance).to.be();
    });

    it('should have the property lastName (base name: "lastName")', function() {
      // uncomment below and update the code to test the property lastName
      //var instance = new NaviPlanApi.AdvisorModel();
      //expect(instance).to.be();
    });

    it('should have the property links (base name: "links")', function() {
      // uncomment below and update the code to test the property links
      //var instance = new NaviPlanApi.AdvisorModel();
      //expect(instance).to.be();
    });

    it('should have the property middleName (base name: "middleName")', function() {
      // uncomment below and update the code to test the property middleName
      //var instance = new NaviPlanApi.AdvisorModel();
      //expect(instance).to.be();
    });

    it('should have the property officeName (base name: "officeName")', function() {
      // uncomment below and update the code to test the property officeName
      //var instance = new NaviPlanApi.AdvisorModel();
      //expect(instance).to.be();
    });

    it('should have the property officeWebsite (base name: "officeWebsite")', function() {
      // uncomment below and update the code to test the property officeWebsite
      //var instance = new NaviPlanApi.AdvisorModel();
      //expect(instance).to.be();
    });

    it('should have the property pagerNumber (base name: "pagerNumber")', function() {
      // uncomment below and update the code to test the property pagerNumber
      //var instance = new NaviPlanApi.AdvisorModel();
      //expect(instance).to.be();
    });

    it('should have the property postalCode (base name: "postalCode")', function() {
      // uncomment below and update the code to test the property postalCode
      //var instance = new NaviPlanApi.AdvisorModel();
      //expect(instance).to.be();
    });

    it('should have the property stateProvince (base name: "stateProvince")', function() {
      // uncomment below and update the code to test the property stateProvince
      //var instance = new NaviPlanApi.AdvisorModel();
      //expect(instance).to.be();
    });

  });

}));
