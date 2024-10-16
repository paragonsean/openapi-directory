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
    instance = new FireFinancialServicesBusinessApi.NewBatch();
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

  describe('NewBatch', function() {
    it('should create an instance of NewBatch', function() {
      // uncomment below and update the code to test NewBatch
      //var instance = new FireFinancialServicesBusinessApi.NewBatch();
      //expect(instance).to.be.a(FireFinancialServicesBusinessApi.NewBatch);
    });

    it('should have the property batchName (base name: "batchName")', function() {
      // uncomment below and update the code to test the property batchName
      //var instance = new FireFinancialServicesBusinessApi.NewBatch();
      //expect(instance).to.be();
    });

    it('should have the property callbackUrl (base name: "callbackUrl")', function() {
      // uncomment below and update the code to test the property callbackUrl
      //var instance = new FireFinancialServicesBusinessApi.NewBatch();
      //expect(instance).to.be();
    });

    it('should have the property currency (base name: "currency")', function() {
      // uncomment below and update the code to test the property currency
      //var instance = new FireFinancialServicesBusinessApi.NewBatch();
      //expect(instance).to.be();
    });

    it('should have the property jobNumber (base name: "jobNumber")', function() {
      // uncomment below and update the code to test the property jobNumber
      //var instance = new FireFinancialServicesBusinessApi.NewBatch();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new FireFinancialServicesBusinessApi.NewBatch();
      //expect(instance).to.be();
    });

  });

}));
