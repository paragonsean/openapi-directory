/**
 * Authorized Partner API Specification
 * To access files in user’s DigiLocker account from your application, you must first obtain user’s authorization.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@digitallocker.gov.in
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
    factory(root.expect, root.AuthorizedPartnerApiSpecification);
  }
}(this, function(expect, AuthorizedPartnerApiSpecification) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AuthorizedPartnerApiSpecification.AccessResponse();
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

  describe('AccessResponse', function() {
    it('should create an instance of AccessResponse', function() {
      // uncomment below and update the code to test AccessResponse
      //var instance = new AuthorizedPartnerApiSpecification.AccessResponse();
      //expect(instance).to.be.a(AuthorizedPartnerApiSpecification.AccessResponse);
    });

    it('should have the property accessToken (base name: "access_token")', function() {
      // uncomment below and update the code to test the property accessToken
      //var instance = new AuthorizedPartnerApiSpecification.AccessResponse();
      //expect(instance).to.be();
    });

    it('should have the property digilockerId (base name: "digilocker_id")', function() {
      // uncomment below and update the code to test the property digilockerId
      //var instance = new AuthorizedPartnerApiSpecification.AccessResponse();
      //expect(instance).to.be();
    });

    it('should have the property dob (base name: "dob")', function() {
      // uncomment below and update the code to test the property dob
      //var instance = new AuthorizedPartnerApiSpecification.AccessResponse();
      //expect(instance).to.be();
    });

    it('should have the property eaadhar (base name: "eaadhar")', function() {
      // uncomment below and update the code to test the property eaadhar
      //var instance = new AuthorizedPartnerApiSpecification.AccessResponse();
      //expect(instance).to.be();
    });

    it('should have the property expiresIn (base name: "expires_in")', function() {
      // uncomment below and update the code to test the property expiresIn
      //var instance = new AuthorizedPartnerApiSpecification.AccessResponse();
      //expect(instance).to.be();
    });

    it('should have the property gender (base name: "gender")', function() {
      // uncomment below and update the code to test the property gender
      //var instance = new AuthorizedPartnerApiSpecification.AccessResponse();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new AuthorizedPartnerApiSpecification.AccessResponse();
      //expect(instance).to.be();
    });

    it('should have the property referenceKey (base name: "reference_key")', function() {
      // uncomment below and update the code to test the property referenceKey
      //var instance = new AuthorizedPartnerApiSpecification.AccessResponse();
      //expect(instance).to.be();
    });

    it('should have the property refreshToken (base name: "refresh_token")', function() {
      // uncomment below and update the code to test the property refreshToken
      //var instance = new AuthorizedPartnerApiSpecification.AccessResponse();
      //expect(instance).to.be();
    });

    it('should have the property scope (base name: "scope")', function() {
      // uncomment below and update the code to test the property scope
      //var instance = new AuthorizedPartnerApiSpecification.AccessResponse();
      //expect(instance).to.be();
    });

    it('should have the property tokenType (base name: "token_type")', function() {
      // uncomment below and update the code to test the property tokenType
      //var instance = new AuthorizedPartnerApiSpecification.AccessResponse();
      //expect(instance).to.be();
    });

  });

}));
