/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
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
    factory(root.expect, root.GooglePayPassesApi);
  }
}(this, function(expect, GooglePayPassesApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new GooglePayPassesApi.PurchaseDetails();
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

  describe('PurchaseDetails', function() {
    it('should create an instance of PurchaseDetails', function() {
      // uncomment below and update the code to test PurchaseDetails
      //var instance = new GooglePayPassesApi.PurchaseDetails();
      //expect(instance).to.be.a(GooglePayPassesApi.PurchaseDetails);
    });

    it('should have the property accountId (base name: "accountId")', function() {
      // uncomment below and update the code to test the property accountId
      //var instance = new GooglePayPassesApi.PurchaseDetails();
      //expect(instance).to.be();
    });

    it('should have the property confirmationCode (base name: "confirmationCode")', function() {
      // uncomment below and update the code to test the property confirmationCode
      //var instance = new GooglePayPassesApi.PurchaseDetails();
      //expect(instance).to.be();
    });

    it('should have the property purchaseDateTime (base name: "purchaseDateTime")', function() {
      // uncomment below and update the code to test the property purchaseDateTime
      //var instance = new GooglePayPassesApi.PurchaseDetails();
      //expect(instance).to.be();
    });

    it('should have the property purchaseReceiptNumber (base name: "purchaseReceiptNumber")', function() {
      // uncomment below and update the code to test the property purchaseReceiptNumber
      //var instance = new GooglePayPassesApi.PurchaseDetails();
      //expect(instance).to.be();
    });

    it('should have the property ticketCost (base name: "ticketCost")', function() {
      // uncomment below and update the code to test the property ticketCost
      //var instance = new GooglePayPassesApi.PurchaseDetails();
      //expect(instance).to.be();
    });

  });

}));
