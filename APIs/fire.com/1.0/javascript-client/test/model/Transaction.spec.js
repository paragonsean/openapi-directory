/**
 * Fire Financial Services Business API
 * The fire.com API allows you to deeply integrate Business Account features into your application or back-office systems.  The API provides read access to your profile, accounts and transactions, event-driven notifications of activity on the account and payment initiation via batches. Each feature has its own HTTP endpoint and every endpoint has its own permission.   The API exposes 3 main areas of functionality: financial functions, service information and service configuration. ## Financial Functions These functions provide access to your account details, transactions, payee accounts, payment initiation etc. ## Service Functions These provide information about the fees and limits applied to your account. ## Service configuration These provide information about your service configs - applications, webhooks, API tokens, etc. 
 *
 * The version of the OpenAPI document: 1.0
 * Contact: api@fire.com
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
    factory(root.expect, root.FireFinancialServicesBusinessApi);
  }
}(this, function(expect, FireFinancialServicesBusinessApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new FireFinancialServicesBusinessApi.Transaction();
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

  describe('Transaction', function() {
    it('should create an instance of Transaction', function() {
      // uncomment below and update the code to test Transaction
      //var instance = new FireFinancialServicesBusinessApi.Transaction();
      //expect(instance).to.be.a(FireFinancialServicesBusinessApi.Transaction);
    });

    it('should have the property amountAfterCharges (base name: "amountAfterCharges")', function() {
      // uncomment below and update the code to test the property amountAfterCharges
      //var instance = new FireFinancialServicesBusinessApi.Transaction();
      //expect(instance).to.be();
    });

    it('should have the property amountBeforeCharges (base name: "amountBeforeCharges")', function() {
      // uncomment below and update the code to test the property amountBeforeCharges
      //var instance = new FireFinancialServicesBusinessApi.Transaction();
      //expect(instance).to.be();
    });

    it('should have the property balance (base name: "balance")', function() {
      // uncomment below and update the code to test the property balance
      //var instance = new FireFinancialServicesBusinessApi.Transaction();
      //expect(instance).to.be();
    });

    it('should have the property batchItemDetails (base name: "batchItemDetails")', function() {
      // uncomment below and update the code to test the property batchItemDetails
      //var instance = new FireFinancialServicesBusinessApi.Transaction();
      //expect(instance).to.be();
    });

    it('should have the property card (base name: "card")', function() {
      // uncomment below and update the code to test the property card
      //var instance = new FireFinancialServicesBusinessApi.Transaction();
      //expect(instance).to.be();
    });

    it('should have the property currency (base name: "currency")', function() {
      // uncomment below and update the code to test the property currency
      //var instance = new FireFinancialServicesBusinessApi.Transaction();
      //expect(instance).to.be();
    });

    it('should have the property date (base name: "date")', function() {
      // uncomment below and update the code to test the property date
      //var instance = new FireFinancialServicesBusinessApi.Transaction();
      //expect(instance).to.be();
    });

    it('should have the property dateAcknowledged (base name: "dateAcknowledged")', function() {
      // uncomment below and update the code to test the property dateAcknowledged
      //var instance = new FireFinancialServicesBusinessApi.Transaction();
      //expect(instance).to.be();
    });

    it('should have the property directDebitDetails (base name: "directDebitDetails")', function() {
      // uncomment below and update the code to test the property directDebitDetails
      //var instance = new FireFinancialServicesBusinessApi.Transaction();
      //expect(instance).to.be();
    });

    it('should have the property eventUuid (base name: "eventUuid")', function() {
      // uncomment below and update the code to test the property eventUuid
      //var instance = new FireFinancialServicesBusinessApi.Transaction();
      //expect(instance).to.be();
    });

    it('should have the property feeAmount (base name: "feeAmount")', function() {
      // uncomment below and update the code to test the property feeAmount
      //var instance = new FireFinancialServicesBusinessApi.Transaction();
      //expect(instance).to.be();
    });

    it('should have the property fxTradeDetails (base name: "fxTradeDetails")', function() {
      // uncomment below and update the code to test the property fxTradeDetails
      //var instance = new FireFinancialServicesBusinessApi.Transaction();
      //expect(instance).to.be();
    });

    it('should have the property ican (base name: "ican")', function() {
      // uncomment below and update the code to test the property ican
      //var instance = new FireFinancialServicesBusinessApi.Transaction();
      //expect(instance).to.be();
    });

    it('should have the property myRef (base name: "myRef")', function() {
      // uncomment below and update the code to test the property myRef
      //var instance = new FireFinancialServicesBusinessApi.Transaction();
      //expect(instance).to.be();
    });

    it('should have the property paymentRequestPublicCode (base name: "paymentRequestPublicCode")', function() {
      // uncomment below and update the code to test the property paymentRequestPublicCode
      //var instance = new FireFinancialServicesBusinessApi.Transaction();
      //expect(instance).to.be();
    });

    it('should have the property proprietarySchemeDetails (base name: "proprietarySchemeDetails")', function() {
      // uncomment below and update the code to test the property proprietarySchemeDetails
      //var instance = new FireFinancialServicesBusinessApi.Transaction();
      //expect(instance).to.be();
    });

    it('should have the property refId (base name: "refId")', function() {
      // uncomment below and update the code to test the property refId
      //var instance = new FireFinancialServicesBusinessApi.Transaction();
      //expect(instance).to.be();
    });

    it('should have the property relatedParty (base name: "relatedParty")', function() {
      // uncomment below and update the code to test the property relatedParty
      //var instance = new FireFinancialServicesBusinessApi.Transaction();
      //expect(instance).to.be();
    });

    it('should have the property taxAmount (base name: "taxAmount")', function() {
      // uncomment below and update the code to test the property taxAmount
      //var instance = new FireFinancialServicesBusinessApi.Transaction();
      //expect(instance).to.be();
    });

    it('should have the property txnId (base name: "txnId")', function() {
      // uncomment below and update the code to test the property txnId
      //var instance = new FireFinancialServicesBusinessApi.Transaction();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new FireFinancialServicesBusinessApi.Transaction();
      //expect(instance).to.be();
    });

    it('should have the property yourRef (base name: "yourRef")', function() {
      // uncomment below and update the code to test the property yourRef
      //var instance = new FireFinancialServicesBusinessApi.Transaction();
      //expect(instance).to.be();
    });

  });

}));
