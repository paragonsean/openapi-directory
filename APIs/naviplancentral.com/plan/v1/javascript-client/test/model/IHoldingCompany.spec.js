/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
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
    factory(root.expect, root.NaviPlanApi);
  }
}(this, function(expect, NaviPlanApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NaviPlanApi.IHoldingCompany();
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

  describe('IHoldingCompany', function() {
    it('should create an instance of IHoldingCompany', function() {
      // uncomment below and update the code to test IHoldingCompany
      //var instance = new NaviPlanApi.IHoldingCompany();
      //expect(instance).to.be.a(NaviPlanApi.IHoldingCompany);
    });

    it('should have the property annualDividendYield (base name: "annualDividendYield")', function() {
      // uncomment below and update the code to test the property annualDividendYield
      //var instance = new NaviPlanApi.IHoldingCompany();
      //expect(instance).to.be();
    });

    it('should have the property ccpc (base name: "ccpc")', function() {
      // uncomment below and update the code to test the property ccpc
      //var instance = new NaviPlanApi.IHoldingCompany();
      //expect(instance).to.be();
    });

    it('should have the property commonSharesOutstanding (base name: "commonSharesOutstanding")', function() {
      // uncomment below and update the code to test the property commonSharesOutstanding
      //var instance = new NaviPlanApi.IHoldingCompany();
      //expect(instance).to.be();
    });

    it('should have the property contributions (base name: "contributions")', function() {
      // uncomment below and update the code to test the property contributions
      //var instance = new NaviPlanApi.IHoldingCompany();
      //expect(instance).to.be();
    });

    it('should have the property corporateYearEnd (base name: "corporateYearEnd")', function() {
      // uncomment below and update the code to test the property corporateYearEnd
      //var instance = new NaviPlanApi.IHoldingCompany();
      //expect(instance).to.be();
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new NaviPlanApi.IHoldingCompany();
      //expect(instance).to.be();
    });

    it('should have the property dividendType (base name: "dividendType")', function() {
      // uncomment below and update the code to test the property dividendType
      //var instance = new NaviPlanApi.IHoldingCompany();
      //expect(instance).to.be();
    });

    it('should have the property dividendTypeFormatted (base name: "dividendTypeFormatted")', function() {
      // uncomment below and update the code to test the property dividendTypeFormatted
      //var instance = new NaviPlanApi.IHoldingCompany();
      //expect(instance).to.be();
    });

    it('should have the property estateDetails (base name: "estateDetails")', function() {
      // uncomment below and update the code to test the property estateDetails
      //var instance = new NaviPlanApi.IHoldingCompany();
      //expect(instance).to.be();
    });

    it('should have the property historicalData (base name: "historicalData")', function() {
      // uncomment below and update the code to test the property historicalData
      //var instance = new NaviPlanApi.IHoldingCompany();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new NaviPlanApi.IHoldingCompany();
      //expect(instance).to.be();
    });

    it('should have the property investmentAccounts (base name: "investmentAccounts")', function() {
      // uncomment below and update the code to test the property investmentAccounts
      //var instance = new NaviPlanApi.IHoldingCompany();
      //expect(instance).to.be();
    });

    it('should have the property liabilities (base name: "liabilities")', function() {
      // uncomment below and update the code to test the property liabilities
      //var instance = new NaviPlanApi.IHoldingCompany();
      //expect(instance).to.be();
    });

    it('should have the property lifeInsurancePolicies (base name: "lifeInsurancePolicies")', function() {
      // uncomment below and update the code to test the property lifeInsurancePolicies
      //var instance = new NaviPlanApi.IHoldingCompany();
      //expect(instance).to.be();
    });

    it('should have the property marketValue (base name: "marketValue")', function() {
      // uncomment below and update the code to test the property marketValue
      //var instance = new NaviPlanApi.IHoldingCompany();
      //expect(instance).to.be();
    });

    it('should have the property numPreferredShareClasses (base name: "numPreferredShareClasses")', function() {
      // uncomment below and update the code to test the property numPreferredShareClasses
      //var instance = new NaviPlanApi.IHoldingCompany();
      //expect(instance).to.be();
    });

    it('should have the property otherAssets (base name: "otherAssets")', function() {
      // uncomment below and update the code to test the property otherAssets
      //var instance = new NaviPlanApi.IHoldingCompany();
      //expect(instance).to.be();
    });

    it('should have the property ownershipAsOfDate (base name: "ownershipAsOfDate")', function() {
      // uncomment below and update the code to test the property ownershipAsOfDate
      //var instance = new NaviPlanApi.IHoldingCompany();
      //expect(instance).to.be();
    });

    it('should have the property ownershipDetails (base name: "ownershipDetails")', function() {
      // uncomment below and update the code to test the property ownershipDetails
      //var instance = new NaviPlanApi.IHoldingCompany();
      //expect(instance).to.be();
    });

    it('should have the property preferredSharesOutstanding (base name: "preferredSharesOutstanding")', function() {
      // uncomment below and update the code to test the property preferredSharesOutstanding
      //var instance = new NaviPlanApi.IHoldingCompany();
      //expect(instance).to.be();
    });

    it('should have the property provinceOfIncorporation (base name: "provinceOfIncorporation")', function() {
      // uncomment below and update the code to test the property provinceOfIncorporation
      //var instance = new NaviPlanApi.IHoldingCompany();
      //expect(instance).to.be();
    });

    it('should have the property provinceOfTaxation (base name: "provinceOfTaxation")', function() {
      // uncomment below and update the code to test the property provinceOfTaxation
      //var instance = new NaviPlanApi.IHoldingCompany();
      //expect(instance).to.be();
    });

    it('should have the property realEstateAssets (base name: "realEstateAssets")', function() {
      // uncomment below and update the code to test the property realEstateAssets
      //var instance = new NaviPlanApi.IHoldingCompany();
      //expect(instance).to.be();
    });

    it('should have the property valueOfAllCommonShares (base name: "valueOfAllCommonShares")', function() {
      // uncomment below and update the code to test the property valueOfAllCommonShares
      //var instance = new NaviPlanApi.IHoldingCompany();
      //expect(instance).to.be();
    });

    it('should have the property valueOfAllPreferredShares (base name: "valueOfAllPreferredShares")', function() {
      // uncomment below and update the code to test the property valueOfAllPreferredShares
      //var instance = new NaviPlanApi.IHoldingCompany();
      //expect(instance).to.be();
    });

    it('should have the property withdrawals (base name: "withdrawals")', function() {
      // uncomment below and update the code to test the property withdrawals
      //var instance = new NaviPlanApi.IHoldingCompany();
      //expect(instance).to.be();
    });

  });

}));
