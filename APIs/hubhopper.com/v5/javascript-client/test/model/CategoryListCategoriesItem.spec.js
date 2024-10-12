/**
 * Hubhopper Partner Integration API(s) - Production
 * This is an interactive document explaining the API(s) that could be used to fetch data from [Hubhopper](https://hubhopper.com). Use the api key provided to authorize `x-api-key` and test the API(s). The output data models are also available for reference.
 *
 * The version of the OpenAPI document: v5
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
    factory(root.expect, root.HubhopperPartnerIntegrationApiSProduction);
  }
}(this, function(expect, HubhopperPartnerIntegrationApiSProduction) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new HubhopperPartnerIntegrationApiSProduction.CategoryListCategoriesItem();
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

  describe('CategoryListCategoriesItem', function() {
    it('should create an instance of CategoryListCategoriesItem', function() {
      // uncomment below and update the code to test CategoryListCategoriesItem
      //var instance = new HubhopperPartnerIntegrationApiSProduction.CategoryListCategoriesItem();
      //expect(instance).to.be.a(HubhopperPartnerIntegrationApiSProduction.CategoryListCategoriesItem);
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new HubhopperPartnerIntegrationApiSProduction.CategoryListCategoriesItem();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new HubhopperPartnerIntegrationApiSProduction.CategoryListCategoriesItem();
      //expect(instance).to.be();
    });

    it('should have the property url (base name: "url")', function() {
      // uncomment below and update the code to test the property url
      //var instance = new HubhopperPartnerIntegrationApiSProduction.CategoryListCategoriesItem();
      //expect(instance).to.be();
    });

  });

}));
