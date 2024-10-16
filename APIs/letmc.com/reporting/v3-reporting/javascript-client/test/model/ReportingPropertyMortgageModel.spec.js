/**
 * LetMC Api V3, reporting
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v3-reporting
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
    factory(root.expect, root.LetMcApiV3Reporting);
  }
}(this, function(expect, LetMcApiV3Reporting) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new LetMcApiV3Reporting.ReportingPropertyMortgageModel();
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

  describe('ReportingPropertyMortgageModel', function() {
    it('should create an instance of ReportingPropertyMortgageModel', function() {
      // uncomment below and update the code to test ReportingPropertyMortgageModel
      //var instance = new LetMcApiV3Reporting.ReportingPropertyMortgageModel();
      //expect(instance).to.be.a(LetMcApiV3Reporting.ReportingPropertyMortgageModel);
    });

    it('should have the property amount (base name: "Amount")', function() {
      // uncomment below and update the code to test the property amount
      //var instance = new LetMcApiV3Reporting.ReportingPropertyMortgageModel();
      //expect(instance).to.be();
    });

    it('should have the property borrowersAccountName (base name: "BorrowersAccountName")', function() {
      // uncomment below and update the code to test the property borrowersAccountName
      //var instance = new LetMcApiV3Reporting.ReportingPropertyMortgageModel();
      //expect(instance).to.be();
    });

    it('should have the property createdAt (base name: "CreatedAt")', function() {
      // uncomment below and update the code to test the property createdAt
      //var instance = new LetMcApiV3Reporting.ReportingPropertyMortgageModel();
      //expect(instance).to.be();
    });

    it('should have the property displayType (base name: "DisplayType")', function() {
      // uncomment below and update the code to test the property displayType
      //var instance = new LetMcApiV3Reporting.ReportingPropertyMortgageModel();
      //expect(instance).to.be();
    });

    it('should have the property extraNotes (base name: "ExtraNotes")', function() {
      // uncomment below and update the code to test the property extraNotes
      //var instance = new LetMcApiV3Reporting.ReportingPropertyMortgageModel();
      //expect(instance).to.be();
    });

    it('should have the property from (base name: "From")', function() {
      // uncomment below and update the code to test the property from
      //var instance = new LetMcApiV3Reporting.ReportingPropertyMortgageModel();
      //expect(instance).to.be();
    });

    it('should have the property intrestRate (base name: "IntrestRate")', function() {
      // uncomment below and update the code to test the property intrestRate
      //var instance = new LetMcApiV3Reporting.ReportingPropertyMortgageModel();
      //expect(instance).to.be();
    });

    it('should have the property marketValue (base name: "MarketValue")', function() {
      // uncomment below and update the code to test the property marketValue
      //var instance = new LetMcApiV3Reporting.ReportingPropertyMortgageModel();
      //expect(instance).to.be();
    });

    it('should have the property monthlyPayment (base name: "MonthlyPayment")', function() {
      // uncomment below and update the code to test the property monthlyPayment
      //var instance = new LetMcApiV3Reporting.ReportingPropertyMortgageModel();
      //expect(instance).to.be();
    });

    it('should have the property mortgageAccountNumber (base name: "MortgageAccountNumber")', function() {
      // uncomment below and update the code to test the property mortgageAccountNumber
      //var instance = new LetMcApiV3Reporting.ReportingPropertyMortgageModel();
      //expect(instance).to.be();
    });

    it('should have the property mortgageProvider (base name: "MortgageProvider")', function() {
      // uncomment below and update the code to test the property mortgageProvider
      //var instance = new LetMcApiV3Reporting.ReportingPropertyMortgageModel();
      //expect(instance).to.be();
    });

    it('should have the property propertyOwnableID (base name: "PropertyOwnableID")', function() {
      // uncomment below and update the code to test the property propertyOwnableID
      //var instance = new LetMcApiV3Reporting.ReportingPropertyMortgageModel();
      //expect(instance).to.be();
    });

    it('should have the property salesInstructionID (base name: "SalesInstructionID")', function() {
      // uncomment below and update the code to test the property salesInstructionID
      //var instance = new LetMcApiV3Reporting.ReportingPropertyMortgageModel();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "Type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new LetMcApiV3Reporting.ReportingPropertyMortgageModel();
      //expect(instance).to.be();
    });

    it('should have the property valuationDate (base name: "ValuationDate")', function() {
      // uncomment below and update the code to test the property valuationDate
      //var instance = new LetMcApiV3Reporting.ReportingPropertyMortgageModel();
      //expect(instance).to.be();
    });

  });

}));
