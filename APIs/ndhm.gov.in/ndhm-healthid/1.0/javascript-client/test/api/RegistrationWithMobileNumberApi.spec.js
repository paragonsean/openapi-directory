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
    instance = new HealthIdService.RegistrationWithMobileNumberApi();
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

  describe('RegistrationWithMobileNumberApi', function() {
    describe('generateMobileOTPUsingPOST1', function() {
      it('should call generateMobileOTPUsingPOST1 successfully', function(done) {
        //uncomment below and update the code to test generateMobileOTPUsingPOST1
        //instance.generateMobileOTPUsingPOST1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('resentOtpUsingPOST', function() {
      it('should call resentOtpUsingPOST successfully', function(done) {
        //uncomment below and update the code to test resentOtpUsingPOST
        //instance.resentOtpUsingPOST(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('verifyMobileOTPUsingPOST', function() {
      it('should call verifyMobileOTPUsingPOST successfully', function(done) {
        //uncomment below and update the code to test verifyMobileOTPUsingPOST
        //instance.verifyMobileOTPUsingPOST(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('verifyUserViaMobileUsingPOST', function() {
      it('should call verifyUserViaMobileUsingPOST successfully', function(done) {
        //uncomment below and update the code to test verifyUserViaMobileUsingPOST
        //instance.verifyUserViaMobileUsingPOST(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
