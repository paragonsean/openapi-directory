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
    instance = new AuthorizedPartnerApiSpecification.GetStatisticsResponseYearwiseAuthenticDocumentsDetails();
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

  describe('GetStatisticsResponseYearwiseAuthenticDocumentsDetails', function() {
    it('should create an instance of GetStatisticsResponseYearwiseAuthenticDocumentsDetails', function() {
      // uncomment below and update the code to test GetStatisticsResponseYearwiseAuthenticDocumentsDetails
      //var instance = new AuthorizedPartnerApiSpecification.GetStatisticsResponseYearwiseAuthenticDocumentsDetails();
      //expect(instance).to.be.a(AuthorizedPartnerApiSpecification.GetStatisticsResponseYearwiseAuthenticDocumentsDetails);
    });

    it('should have the property count (base name: "count")', function() {
      // uncomment below and update the code to test the property count
      //var instance = new AuthorizedPartnerApiSpecification.GetStatisticsResponseYearwiseAuthenticDocumentsDetails();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new AuthorizedPartnerApiSpecification.GetStatisticsResponseYearwiseAuthenticDocumentsDetails();
      //expect(instance).to.be();
    });

    it('should have the property year (base name: "year")', function() {
      // uncomment below and update the code to test the property year
      //var instance = new AuthorizedPartnerApiSpecification.GetStatisticsResponseYearwiseAuthenticDocumentsDetails();
      //expect(instance).to.be();
    });

  });

}));
