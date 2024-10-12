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
    instance = new AuthorizedPartnerApiSpecification.IssuerResponseIssuersInner();
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

  describe('IssuerResponseIssuersInner', function() {
    it('should create an instance of IssuerResponseIssuersInner', function() {
      // uncomment below and update the code to test IssuerResponseIssuersInner
      //var instance = new AuthorizedPartnerApiSpecification.IssuerResponseIssuersInner();
      //expect(instance).to.be.a(AuthorizedPartnerApiSpecification.IssuerResponseIssuersInner);
    });

    it('should have the property categories (base name: "categories")', function() {
      // uncomment below and update the code to test the property categories
      //var instance = new AuthorizedPartnerApiSpecification.IssuerResponseIssuersInner();
      //expect(instance).to.be();
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new AuthorizedPartnerApiSpecification.IssuerResponseIssuersInner();
      //expect(instance).to.be();
    });

    it('should have the property issuerid (base name: "issuerid")', function() {
      // uncomment below and update the code to test the property issuerid
      //var instance = new AuthorizedPartnerApiSpecification.IssuerResponseIssuersInner();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new AuthorizedPartnerApiSpecification.IssuerResponseIssuersInner();
      //expect(instance).to.be();
    });

    it('should have the property orgid (base name: "orgid")', function() {
      // uncomment below and update the code to test the property orgid
      //var instance = new AuthorizedPartnerApiSpecification.IssuerResponseIssuersInner();
      //expect(instance).to.be();
    });

  });

}));
