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
    instance = new FireFinancialServicesBusinessApi.DirectDebit();
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

  describe('DirectDebit', function() {
    it('should create an instance of DirectDebit', function() {
      // uncomment below and update the code to test DirectDebit
      //var instance = new FireFinancialServicesBusinessApi.DirectDebit();
      //expect(instance).to.be.a(FireFinancialServicesBusinessApi.DirectDebit);
    });

    it('should have the property amount (base name: "amount")', function() {
      // uncomment below and update the code to test the property amount
      //var instance = new FireFinancialServicesBusinessApi.DirectDebit();
      //expect(instance).to.be();
    });

    it('should have the property currency (base name: "currency")', function() {
      // uncomment below and update the code to test the property currency
      //var instance = new FireFinancialServicesBusinessApi.DirectDebit();
      //expect(instance).to.be();
    });

    it('should have the property dateCreated (base name: "dateCreated")', function() {
      // uncomment below and update the code to test the property dateCreated
      //var instance = new FireFinancialServicesBusinessApi.DirectDebit();
      //expect(instance).to.be();
    });

    it('should have the property directDebitReference (base name: "directDebitReference")', function() {
      // uncomment below and update the code to test the property directDebitReference
      //var instance = new FireFinancialServicesBusinessApi.DirectDebit();
      //expect(instance).to.be();
    });

    it('should have the property directDebitUuid (base name: "directDebitUuid")', function() {
      // uncomment below and update the code to test the property directDebitUuid
      //var instance = new FireFinancialServicesBusinessApi.DirectDebit();
      //expect(instance).to.be();
    });

    it('should have the property isDDIC (base name: "isDDIC")', function() {
      // uncomment below and update the code to test the property isDDIC
      //var instance = new FireFinancialServicesBusinessApi.DirectDebit();
      //expect(instance).to.be();
    });

    it('should have the property lastUpdated (base name: "lastUpdated")', function() {
      // uncomment below and update the code to test the property lastUpdated
      //var instance = new FireFinancialServicesBusinessApi.DirectDebit();
      //expect(instance).to.be();
    });

    it('should have the property mandateUUid (base name: "mandateUUid")', function() {
      // uncomment below and update the code to test the property mandateUUid
      //var instance = new FireFinancialServicesBusinessApi.DirectDebit();
      //expect(instance).to.be();
    });

    it('should have the property originatorAlias (base name: "originatorAlias")', function() {
      // uncomment below and update the code to test the property originatorAlias
      //var instance = new FireFinancialServicesBusinessApi.DirectDebit();
      //expect(instance).to.be();
    });

    it('should have the property originatorName (base name: "originatorName")', function() {
      // uncomment below and update the code to test the property originatorName
      //var instance = new FireFinancialServicesBusinessApi.DirectDebit();
      //expect(instance).to.be();
    });

    it('should have the property originatorReference (base name: "originatorReference")', function() {
      // uncomment below and update the code to test the property originatorReference
      //var instance = new FireFinancialServicesBusinessApi.DirectDebit();
      //expect(instance).to.be();
    });

    it('should have the property schemeRejectReason (base name: "schemeRejectReason")', function() {
      // uncomment below and update the code to test the property schemeRejectReason
      //var instance = new FireFinancialServicesBusinessApi.DirectDebit();
      //expect(instance).to.be();
    });

    it('should have the property schemeRejectReasonCode (base name: "schemeRejectReasonCode")', function() {
      // uncomment below and update the code to test the property schemeRejectReasonCode
      //var instance = new FireFinancialServicesBusinessApi.DirectDebit();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new FireFinancialServicesBusinessApi.DirectDebit();
      //expect(instance).to.be();
    });

    it('should have the property targetIcan (base name: "targetIcan")', function() {
      // uncomment below and update the code to test the property targetIcan
      //var instance = new FireFinancialServicesBusinessApi.DirectDebit();
      //expect(instance).to.be();
    });

    it('should have the property targetPayeeId (base name: "targetPayeeId")', function() {
      // uncomment below and update the code to test the property targetPayeeId
      //var instance = new FireFinancialServicesBusinessApi.DirectDebit();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new FireFinancialServicesBusinessApi.DirectDebit();
      //expect(instance).to.be();
    });

  });

}));
