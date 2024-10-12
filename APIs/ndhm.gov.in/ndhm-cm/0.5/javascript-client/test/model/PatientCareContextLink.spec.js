/**
 * Health Data Consent Manager
 * Entity which provides health information aggregation services to customers of health care services. It enables customers to fetch their health information from one or more Health Information Providers (e.g., Hospitals, Diagnostic Labs, Medical Device Companies), based on their explicit Consent and to share such aggregated information with Health Information Users i.e. entities in need of such data (e.g., Insurers, Doctors, Medical Researchers).  # Specifications 1. This document maintains only the Health Information Gateway relevant APIs.  
 *
 * The version of the OpenAPI document: 0.5
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
    factory(root.expect, root.HealthDataConsentManager);
  }
}(this, function(expect, HealthDataConsentManager) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new HealthDataConsentManager.PatientCareContextLink();
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

  describe('PatientCareContextLink', function() {
    it('should create an instance of PatientCareContextLink', function() {
      // uncomment below and update the code to test PatientCareContextLink
      //var instance = new HealthDataConsentManager.PatientCareContextLink();
      //expect(instance).to.be.a(HealthDataConsentManager.PatientCareContextLink);
    });

    it('should have the property accessToken (base name: "accessToken")', function() {
      // uncomment below and update the code to test the property accessToken
      //var instance = new HealthDataConsentManager.PatientCareContextLink();
      //expect(instance).to.be();
    });

    it('should have the property patient (base name: "patient")', function() {
      // uncomment below and update the code to test the property patient
      //var instance = new HealthDataConsentManager.PatientCareContextLink();
      //expect(instance).to.be();
    });

  });

}));
