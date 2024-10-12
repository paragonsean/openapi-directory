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
    instance = new HealthIdService.HidUpdateAccountRequest();
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

  describe('HidUpdateAccountRequest', function() {
    it('should create an instance of HidUpdateAccountRequest', function() {
      // uncomment below and update the code to test HidUpdateAccountRequest
      //var instance = new HealthIdService.HidUpdateAccountRequest();
      //expect(instance).to.be.a(HealthIdService.HidUpdateAccountRequest);
    });

    it('should have the property address (base name: "address")', function() {
      // uncomment below and update the code to test the property address
      //var instance = new HealthIdService.HidUpdateAccountRequest();
      //expect(instance).to.be();
    });

    it('should have the property dayOfBirth (base name: "dayOfBirth")', function() {
      // uncomment below and update the code to test the property dayOfBirth
      //var instance = new HealthIdService.HidUpdateAccountRequest();
      //expect(instance).to.be();
    });

    it('should have the property districtCode (base name: "districtCode")', function() {
      // uncomment below and update the code to test the property districtCode
      //var instance = new HealthIdService.HidUpdateAccountRequest();
      //expect(instance).to.be();
    });

    it('should have the property email (base name: "email")', function() {
      // uncomment below and update the code to test the property email
      //var instance = new HealthIdService.HidUpdateAccountRequest();
      //expect(instance).to.be();
    });

    it('should have the property firstName (base name: "firstName")', function() {
      // uncomment below and update the code to test the property firstName
      //var instance = new HealthIdService.HidUpdateAccountRequest();
      //expect(instance).to.be();
    });

    it('should have the property healthId (base name: "healthId")', function() {
      // uncomment below and update the code to test the property healthId
      //var instance = new HealthIdService.HidUpdateAccountRequest();
      //expect(instance).to.be();
    });

    it('should have the property healthIdNumber (base name: "healthIdNumber")', function() {
      // uncomment below and update the code to test the property healthIdNumber
      //var instance = new HealthIdService.HidUpdateAccountRequest();
      //expect(instance).to.be();
    });

    it('should have the property lastName (base name: "lastName")', function() {
      // uncomment below and update the code to test the property lastName
      //var instance = new HealthIdService.HidUpdateAccountRequest();
      //expect(instance).to.be();
    });

    it('should have the property middleName (base name: "middleName")', function() {
      // uncomment below and update the code to test the property middleName
      //var instance = new HealthIdService.HidUpdateAccountRequest();
      //expect(instance).to.be();
    });

    it('should have the property monthOfBirth (base name: "monthOfBirth")', function() {
      // uncomment below and update the code to test the property monthOfBirth
      //var instance = new HealthIdService.HidUpdateAccountRequest();
      //expect(instance).to.be();
    });

    it('should have the property password (base name: "password")', function() {
      // uncomment below and update the code to test the property password
      //var instance = new HealthIdService.HidUpdateAccountRequest();
      //expect(instance).to.be();
    });

    it('should have the property pincode (base name: "pincode")', function() {
      // uncomment below and update the code to test the property pincode
      //var instance = new HealthIdService.HidUpdateAccountRequest();
      //expect(instance).to.be();
    });

    it('should have the property profilePhoto (base name: "profilePhoto")', function() {
      // uncomment below and update the code to test the property profilePhoto
      //var instance = new HealthIdService.HidUpdateAccountRequest();
      //expect(instance).to.be();
    });

    it('should have the property stateCode (base name: "stateCode")', function() {
      // uncomment below and update the code to test the property stateCode
      //var instance = new HealthIdService.HidUpdateAccountRequest();
      //expect(instance).to.be();
    });

    it('should have the property subdistrictCode (base name: "subdistrictCode")', function() {
      // uncomment below and update the code to test the property subdistrictCode
      //var instance = new HealthIdService.HidUpdateAccountRequest();
      //expect(instance).to.be();
    });

    it('should have the property townCode (base name: "townCode")', function() {
      // uncomment below and update the code to test the property townCode
      //var instance = new HealthIdService.HidUpdateAccountRequest();
      //expect(instance).to.be();
    });

    it('should have the property villageCode (base name: "villageCode")', function() {
      // uncomment below and update the code to test the property villageCode
      //var instance = new HealthIdService.HidUpdateAccountRequest();
      //expect(instance).to.be();
    });

    it('should have the property wardCode (base name: "wardCode")', function() {
      // uncomment below and update the code to test the property wardCode
      //var instance = new HealthIdService.HidUpdateAccountRequest();
      //expect(instance).to.be();
    });

    it('should have the property yearOfBirth (base name: "yearOfBirth")', function() {
      // uncomment below and update the code to test the property yearOfBirth
      //var instance = new HealthIdService.HidUpdateAccountRequest();
      //expect(instance).to.be();
    });

  });

}));
