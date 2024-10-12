/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
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
    factory(root.expect, root.MagentoB2B);
  }
}(this, function(expect, MagentoB2B) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MagentoB2B.CompanyCreditDataHistorySearchResultsInterface();
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

  describe('CompanyCreditDataHistorySearchResultsInterface', function() {
    it('should create an instance of CompanyCreditDataHistorySearchResultsInterface', function() {
      // uncomment below and update the code to test CompanyCreditDataHistorySearchResultsInterface
      //var instance = new MagentoB2B.CompanyCreditDataHistorySearchResultsInterface();
      //expect(instance).to.be.a(MagentoB2B.CompanyCreditDataHistorySearchResultsInterface);
    });

    it('should have the property items (base name: "items")', function() {
      // uncomment below and update the code to test the property items
      //var instance = new MagentoB2B.CompanyCreditDataHistorySearchResultsInterface();
      //expect(instance).to.be();
    });

    it('should have the property searchCriteria (base name: "search_criteria")', function() {
      // uncomment below and update the code to test the property searchCriteria
      //var instance = new MagentoB2B.CompanyCreditDataHistorySearchResultsInterface();
      //expect(instance).to.be();
    });

    it('should have the property totalCount (base name: "total_count")', function() {
      // uncomment below and update the code to test the property totalCount
      //var instance = new MagentoB2B.CompanyCreditDataHistorySearchResultsInterface();
      //expect(instance).to.be();
    });

  });

}));
