/**
 * Big Red Cloud API
 *   <div style='line-height: 30px;'>      <strong>Welcome to the Big Red Cloud API</strong><br/>      This API enables programmatic access to Big Red Cloud data.<br/>      We have used Swagger to auto generate the API documentation on this page, and it also enables direct interaction with the API in this page. <br/>      To get started, you will require an API Key - check out our guide at <a target='_blank' href='https://www.bigredcloud.com/support/generating-api-key-guide/'>https://www.bigredcloud.com/support/generating-api-key-guide/</a> for information on how to get one. <br/>      Use the  'Enter API Key' button below to enter your API key and start interacting with your Big Red Cloud data right on this page. <br/>      The API key will be stored in your browsers local storage for convenience, but you will be able to delete it at any time if you wish. <br/>      For additional information on the API, check out our support article at <a target='_blank' href='https://www.bigredcloud.com/support/api/'>https://www.bigredcloud.com/support/api/</a><br/>  </div>
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
    factory(root.expect, root.BigRedCloudApi);
  }
}(this, function(expect, BigRedCloudApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new BigRedCloudApi.CashReceiptQueryDto();
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

  describe('CashReceiptQueryDto', function() {
    it('should create an instance of CashReceiptQueryDto', function() {
      // uncomment below and update the code to test CashReceiptQueryDto
      //var instance = new BigRedCloudApi.CashReceiptQueryDto();
      //expect(instance).to.be.a(BigRedCloudApi.CashReceiptQueryDto);
    });

    it('should have the property acCode (base name: "acCode")', function() {
      // uncomment below and update the code to test the property acCode
      //var instance = new BigRedCloudApi.CashReceiptQueryDto();
      //expect(instance).to.be();
    });

    it('should have the property acEntries (base name: "acEntries")', function() {
      // uncomment below and update the code to test the property acEntries
      //var instance = new BigRedCloudApi.CashReceiptQueryDto();
      //expect(instance).to.be();
    });

    it('should have the property bookTranTypeId (base name: "bookTranTypeId")', function() {
      // uncomment below and update the code to test the property bookTranTypeId
      //var instance = new BigRedCloudApi.CashReceiptQueryDto();
      //expect(instance).to.be();
    });

    it('should have the property customFields (base name: "customFields")', function() {
      // uncomment below and update the code to test the property customFields
      //var instance = new BigRedCloudApi.CashReceiptQueryDto();
      //expect(instance).to.be();
    });

    it('should have the property customerId (base name: "customerId")', function() {
      // uncomment below and update the code to test the property customerId
      //var instance = new BigRedCloudApi.CashReceiptQueryDto();
      //expect(instance).to.be();
    });

    it('should have the property detailCollection (base name: "detailCollection")', function() {
      // uncomment below and update the code to test the property detailCollection
      //var instance = new BigRedCloudApi.CashReceiptQueryDto();
      //expect(instance).to.be();
    });

    it('should have the property discount (base name: "discount")', function() {
      // uncomment below and update the code to test the property discount
      //var instance = new BigRedCloudApi.CashReceiptQueryDto();
      //expect(instance).to.be();
    });

    it('should have the property entryDate (base name: "entryDate")', function() {
      // uncomment below and update the code to test the property entryDate
      //var instance = new BigRedCloudApi.CashReceiptQueryDto();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new BigRedCloudApi.CashReceiptQueryDto();
      //expect(instance).to.be();
    });

    it('should have the property ledger (base name: "ledger")', function() {
      // uncomment below and update the code to test the property ledger
      //var instance = new BigRedCloudApi.CashReceiptQueryDto();
      //expect(instance).to.be();
    });

    it('should have the property note (base name: "note")', function() {
      // uncomment below and update the code to test the property note
      //var instance = new BigRedCloudApi.CashReceiptQueryDto();
      //expect(instance).to.be();
    });

    it('should have the property plaidTransactionId (base name: "plaidTransactionId")', function() {
      // uncomment below and update the code to test the property plaidTransactionId
      //var instance = new BigRedCloudApi.CashReceiptQueryDto();
      //expect(instance).to.be();
    });

    it('should have the property procDate (base name: "procDate")', function() {
      // uncomment below and update the code to test the property procDate
      //var instance = new BigRedCloudApi.CashReceiptQueryDto();
      //expect(instance).to.be();
    });

    it('should have the property timestamp (base name: "timestamp")', function() {
      // uncomment below and update the code to test the property timestamp
      //var instance = new BigRedCloudApi.CashReceiptQueryDto();
      //expect(instance).to.be();
    });

    it('should have the property total (base name: "total")', function() {
      // uncomment below and update the code to test the property total
      //var instance = new BigRedCloudApi.CashReceiptQueryDto();
      //expect(instance).to.be();
    });

    it('should have the property unallocated (base name: "unallocated")', function() {
      // uncomment below and update the code to test the property unallocated
      //var instance = new BigRedCloudApi.CashReceiptQueryDto();
      //expect(instance).to.be();
    });

    it('should have the property vatEntries (base name: "vatEntries")', function() {
      // uncomment below and update the code to test the property vatEntries
      //var instance = new BigRedCloudApi.CashReceiptQueryDto();
      //expect(instance).to.be();
    });

    it('should have the property vatTypeId (base name: "vatTypeId")', function() {
      // uncomment below and update the code to test the property vatTypeId
      //var instance = new BigRedCloudApi.CashReceiptQueryDto();
      //expect(instance).to.be();
    });

  });

}));
