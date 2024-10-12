/**
 * Health ID Service
 * It is important to standardize the process of identification of an individual across healthcare providers, to ensure that the created medical records are issued to the right individual or accessed by a Health Information User through appropriate consent.  In order to issue a Health ID to an individual, one only needs basic demographic details like Name, Year of Birth, Gender. In addition, citizens should be able to update contact information easily.
 *
 * The version of the OpenAPI document: 1.0
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
    factory(root.expect, root.HealthIdService);
  }
}(this, function(expect, HealthIdService) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new HealthIdService.VerifyAadhaarOtp();
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

  describe('VerifyAadhaarOtp', function() {
    it('should create an instance of VerifyAadhaarOtp', function() {
      // uncomment below and update the code to test VerifyAadhaarOtp
      //var instance = new HealthIdService.VerifyAadhaarOtp();
      //expect(instance).to.be.a(HealthIdService.VerifyAadhaarOtp);
    });

    it('should have the property otp (base name: "otp")', function() {
      // uncomment below and update the code to test the property otp
      //var instance = new HealthIdService.VerifyAadhaarOtp();
      //expect(instance).to.be();
    });

    it('should have the property restrictions (base name: "restrictions")', function() {
      // uncomment below and update the code to test the property restrictions
      //var instance = new HealthIdService.VerifyAadhaarOtp();
      //expect(instance).to.be();
    });

    it('should have the property txnId (base name: "txnId")', function() {
      // uncomment below and update the code to test the property txnId
      //var instance = new HealthIdService.VerifyAadhaarOtp();
      //expect(instance).to.be();
    });

  });

}));
