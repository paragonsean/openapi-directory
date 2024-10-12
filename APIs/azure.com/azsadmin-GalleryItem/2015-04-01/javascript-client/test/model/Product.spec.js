/**
 * GalleryManagementClient
 * The Admin Gallery Management Client.
 *
 * The version of the OpenAPI document: 2015-04-01
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
    factory(root.expect, root.GalleryManagementClient);
  }
}(this, function(expect, GalleryManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new GalleryManagementClient.Product();
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

  describe('Product', function() {
    it('should create an instance of Product', function() {
      // uncomment below and update the code to test Product
      //var instance = new GalleryManagementClient.Product();
      //expect(instance).to.be.a(GalleryManagementClient.Product);
    });

    it('should have the property displayName (base name: "displayName")', function() {
      // uncomment below and update the code to test the property displayName
      //var instance = new GalleryManagementClient.Product();
      //expect(instance).to.be();
    });

    it('should have the property legalTerms (base name: "legalTerms")', function() {
      // uncomment below and update the code to test the property legalTerms
      //var instance = new GalleryManagementClient.Product();
      //expect(instance).to.be();
    });

    it('should have the property legalTermsUri (base name: "legalTermsUri")', function() {
      // uncomment below and update the code to test the property legalTermsUri
      //var instance = new GalleryManagementClient.Product();
      //expect(instance).to.be();
    });

    it('should have the property offerDetails (base name: "offerDetails")', function() {
      // uncomment below and update the code to test the property offerDetails
      //var instance = new GalleryManagementClient.Product();
      //expect(instance).to.be();
    });

    it('should have the property pricingDetailsUri (base name: "pricingDetailsUri")', function() {
      // uncomment below and update the code to test the property pricingDetailsUri
      //var instance = new GalleryManagementClient.Product();
      //expect(instance).to.be();
    });

    it('should have the property privacyPolicy (base name: "privacyPolicy")', function() {
      // uncomment below and update the code to test the property privacyPolicy
      //var instance = new GalleryManagementClient.Product();
      //expect(instance).to.be();
    });

    it('should have the property privacyPolicyUri (base name: "privacyPolicyUri")', function() {
      // uncomment below and update the code to test the property privacyPolicyUri
      //var instance = new GalleryManagementClient.Product();
      //expect(instance).to.be();
    });

    it('should have the property publisherDisplayName (base name: "publisherDisplayName")', function() {
      // uncomment below and update the code to test the property publisherDisplayName
      //var instance = new GalleryManagementClient.Product();
      //expect(instance).to.be();
    });

  });

}));
