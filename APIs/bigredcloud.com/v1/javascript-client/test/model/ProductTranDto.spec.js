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
    instance = new BigRedCloudApi.ProductTranDto();
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

  describe('ProductTranDto', function() {
    it('should create an instance of ProductTranDto', function() {
      // uncomment below and update the code to test ProductTranDto
      //var instance = new BigRedCloudApi.ProductTranDto();
      //expect(instance).to.be.a(BigRedCloudApi.ProductTranDto);
    });

    it('should have the property acEntries (base name: "acEntries")', function() {
      // uncomment below and update the code to test the property acEntries
      //var instance = new BigRedCloudApi.ProductTranDto();
      //expect(instance).to.be();
    });

    it('should have the property amount (base name: "amount")', function() {
      // uncomment below and update the code to test the property amount
      //var instance = new BigRedCloudApi.ProductTranDto();
      //expect(instance).to.be();
    });

    it('should have the property amountNet (base name: "amountNet")', function() {
      // uncomment below and update the code to test the property amountNet
      //var instance = new BigRedCloudApi.ProductTranDto();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new BigRedCloudApi.ProductTranDto();
      //expect(instance).to.be();
    });

    it('should have the property percentage (base name: "percentage")', function() {
      // uncomment below and update the code to test the property percentage
      //var instance = new BigRedCloudApi.ProductTranDto();
      //expect(instance).to.be();
    });

    it('should have the property productCode (base name: "productCode")', function() {
      // uncomment below and update the code to test the property productCode
      //var instance = new BigRedCloudApi.ProductTranDto();
      //expect(instance).to.be();
    });

    it('should have the property productId (base name: "productId")', function() {
      // uncomment below and update the code to test the property productId
      //var instance = new BigRedCloudApi.ProductTranDto();
      //expect(instance).to.be();
    });

    it('should have the property quantity (base name: "quantity")', function() {
      // uncomment below and update the code to test the property quantity
      //var instance = new BigRedCloudApi.ProductTranDto();
      //expect(instance).to.be();
    });

    it('should have the property tranNotes (base name: "tranNotes")', function() {
      // uncomment below and update the code to test the property tranNotes
      //var instance = new BigRedCloudApi.ProductTranDto();
      //expect(instance).to.be();
    });

    it('should have the property unitPrice (base name: "unitPrice")', function() {
      // uncomment below and update the code to test the property unitPrice
      //var instance = new BigRedCloudApi.ProductTranDto();
      //expect(instance).to.be();
    });

    it('should have the property vat (base name: "vat")', function() {
      // uncomment below and update the code to test the property vat
      //var instance = new BigRedCloudApi.ProductTranDto();
      //expect(instance).to.be();
    });

    it('should have the property vatAnalysisTypeId (base name: "vatAnalysisTypeId")', function() {
      // uncomment below and update the code to test the property vatAnalysisTypeId
      //var instance = new BigRedCloudApi.ProductTranDto();
      //expect(instance).to.be();
    });

    it('should have the property vatRateId (base name: "vatRateId")', function() {
      // uncomment below and update the code to test the property vatRateId
      //var instance = new BigRedCloudApi.ProductTranDto();
      //expect(instance).to.be();
    });

  });

}));
