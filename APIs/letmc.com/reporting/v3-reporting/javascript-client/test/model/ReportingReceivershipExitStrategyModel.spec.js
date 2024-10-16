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
    instance = new LetMcApiV3Reporting.ReportingReceivershipExitStrategyModel();
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

  describe('ReportingReceivershipExitStrategyModel', function() {
    it('should create an instance of ReportingReceivershipExitStrategyModel', function() {
      // uncomment below and update the code to test ReportingReceivershipExitStrategyModel
      //var instance = new LetMcApiV3Reporting.ReportingReceivershipExitStrategyModel();
      //expect(instance).to.be.a(LetMcApiV3Reporting.ReportingReceivershipExitStrategyModel);
    });

    it('should have the property compiled (base name: "Compiled")', function() {
      // uncomment below and update the code to test the property compiled
      //var instance = new LetMcApiV3Reporting.ReportingReceivershipExitStrategyModel();
      //expect(instance).to.be();
    });

    it('should have the property compiledByID (base name: "CompiledByID")', function() {
      // uncomment below and update the code to test the property compiledByID
      //var instance = new LetMcApiV3Reporting.ReportingReceivershipExitStrategyModel();
      //expect(instance).to.be();
    });

    it('should have the property displayCompiledByID (base name: "DisplayCompiledByID")', function() {
      // uncomment below and update the code to test the property displayCompiledByID
      //var instance = new LetMcApiV3Reporting.ReportingReceivershipExitStrategyModel();
      //expect(instance).to.be();
    });

    it('should have the property extraNotes (base name: "ExtraNotes")', function() {
      // uncomment below and update the code to test the property extraNotes
      //var instance = new LetMcApiV3Reporting.ReportingReceivershipExitStrategyModel();
      //expect(instance).to.be();
    });

    it('should have the property lenderResponse (base name: "LenderResponse")', function() {
      // uncomment below and update the code to test the property lenderResponse
      //var instance = new LetMcApiV3Reporting.ReportingReceivershipExitStrategyModel();
      //expect(instance).to.be();
    });

    it('should have the property lenderResponseDate (base name: "LenderResponseDate")', function() {
      // uncomment below and update the code to test the property lenderResponseDate
      //var instance = new LetMcApiV3Reporting.ReportingReceivershipExitStrategyModel();
      //expect(instance).to.be();
    });

    it('should have the property lockChanged (base name: "LockChanged")', function() {
      // uncomment below and update the code to test the property lockChanged
      //var instance = new LetMcApiV3Reporting.ReportingReceivershipExitStrategyModel();
      //expect(instance).to.be();
    });

    it('should have the property mortgageArrears (base name: "MortgageArrears")', function() {
      // uncomment below and update the code to test the property mortgageArrears
      //var instance = new LetMcApiV3Reporting.ReportingReceivershipExitStrategyModel();
      //expect(instance).to.be();
    });

    it('should have the property mortgageBalance (base name: "MortgageBalance")', function() {
      // uncomment below and update the code to test the property mortgageBalance
      //var instance = new LetMcApiV3Reporting.ReportingReceivershipExitStrategyModel();
      //expect(instance).to.be();
    });

    it('should have the property mortgageCMI (base name: "MortgageCMI")', function() {
      // uncomment below and update the code to test the property mortgageCMI
      //var instance = new LetMcApiV3Reporting.ReportingReceivershipExitStrategyModel();
      //expect(instance).to.be();
    });

    it('should have the property recommendation (base name: "Recommendation")', function() {
      // uncomment below and update the code to test the property recommendation
      //var instance = new LetMcApiV3Reporting.ReportingReceivershipExitStrategyModel();
      //expect(instance).to.be();
    });

    it('should have the property reviewDate (base name: "ReviewDate")', function() {
      // uncomment below and update the code to test the property reviewDate
      //var instance = new LetMcApiV3Reporting.ReportingReceivershipExitStrategyModel();
      //expect(instance).to.be();
    });

    it('should have the property sentToLender (base name: "SentToLender")', function() {
      // uncomment below and update the code to test the property sentToLender
      //var instance = new LetMcApiV3Reporting.ReportingReceivershipExitStrategyModel();
      //expect(instance).to.be();
    });

  });

}));
