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
    instance = new BigRedCloudApi.CompanyOptionViewModel();
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

  describe('CompanyOptionViewModel', function() {
    it('should create an instance of CompanyOptionViewModel', function() {
      // uncomment below and update the code to test CompanyOptionViewModel
      //var instance = new BigRedCloudApi.CompanyOptionViewModel();
      //expect(instance).to.be.a(BigRedCloudApi.CompanyOptionViewModel);
    });

    it('should have the property allowEntryOfGrossPriceInInvoicing (base name: "allowEntryOfGrossPriceInInvoicing")', function() {
      // uncomment below and update the code to test the property allowEntryOfGrossPriceInInvoicing
      //var instance = new BigRedCloudApi.CompanyOptionViewModel();
      //expect(instance).to.be();
    });

    it('should have the property creditInputForReverseChargeVAT (base name: "creditInputForReverseChargeVAT")', function() {
      // uncomment below and update the code to test the property creditInputForReverseChargeVAT
      //var instance = new BigRedCloudApi.CompanyOptionViewModel();
      //expect(instance).to.be();
    });

    it('should have the property creditNoteJournalAgeingName (base name: "creditNoteJournalAgeingName")', function() {
      // uncomment below and update the code to test the property creditNoteJournalAgeingName
      //var instance = new BigRedCloudApi.CompanyOptionViewModel();
      //expect(instance).to.be();
    });

    it('should have the property creditNoteJournalAgeingValue (base name: "creditNoteJournalAgeingValue")', function() {
      // uncomment below and update the code to test the property creditNoteJournalAgeingValue
      //var instance = new BigRedCloudApi.CompanyOptionViewModel();
      //expect(instance).to.be();
    });

    it('should have the property discrepancyAllowed (base name: "discrepancyAllowed")', function() {
      // uncomment below and update the code to test the property discrepancyAllowed
      //var instance = new BigRedCloudApi.CompanyOptionViewModel();
      //expect(instance).to.be();
    });

    it('should have the property enableVOCRReporting (base name: "enableVOCRReporting")', function() {
      // uncomment below and update the code to test the property enableVOCRReporting
      //var instance = new BigRedCloudApi.CompanyOptionViewModel();
      //expect(instance).to.be();
    });

    it('should have the property marginVatScheme (base name: "marginVatScheme")', function() {
      // uncomment below and update the code to test the property marginVatScheme
      //var instance = new BigRedCloudApi.CompanyOptionViewModel();
      //expect(instance).to.be();
    });

    it('should have the property printOSItemsOnly (base name: "printOSItemsOnly")', function() {
      // uncomment below and update the code to test the property printOSItemsOnly
      //var instance = new BigRedCloudApi.CompanyOptionViewModel();
      //expect(instance).to.be();
    });

    it('should have the property purchasesVatAnalysisType (base name: "purchasesVatAnalysisType")', function() {
      // uncomment below and update the code to test the property purchasesVatAnalysisType
      //var instance = new BigRedCloudApi.CompanyOptionViewModel();
      //expect(instance).to.be();
    });

    it('should have the property salesVatAnalysisType (base name: "salesVatAnalysisType")', function() {
      // uncomment below and update the code to test the property salesVatAnalysisType
      //var instance = new BigRedCloudApi.CompanyOptionViewModel();
      //expect(instance).to.be();
    });

    it('should have the property useAllocations (base name: "useAllocations")', function() {
      // uncomment below and update the code to test the property useAllocations
      //var instance = new BigRedCloudApi.CompanyOptionViewModel();
      //expect(instance).to.be();
    });

    it('should have the property useNominal (base name: "useNominal")', function() {
      // uncomment below and update the code to test the property useNominal
      //var instance = new BigRedCloudApi.CompanyOptionViewModel();
      //expect(instance).to.be();
    });

    it('should have the property useNominalCode (base name: "useNominalCode")', function() {
      // uncomment below and update the code to test the property useNominalCode
      //var instance = new BigRedCloudApi.CompanyOptionViewModel();
      //expect(instance).to.be();
    });

    it('should have the property vocrSettingValue (base name: "vocrSettingValue")', function() {
      // uncomment below and update the code to test the property vocrSettingValue
      //var instance = new BigRedCloudApi.CompanyOptionViewModel();
      //expect(instance).to.be();
    });

  });

}));
