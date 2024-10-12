/**
 * Azure SQL Database
 * Provides create, read, update and delete functionality for Azure SQL Database resources including recommendations and operations.
 *
 * The version of the OpenAPI document: 2014-04-01
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
    factory(root.expect, root.AzureSqlDatabase);
  }
}(this, function(expect, AzureSqlDatabase) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AzureSqlDatabase.ServiceTierAdvisorListResult();
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

  describe('ServiceTierAdvisorListResult', function() {
    it('should create an instance of ServiceTierAdvisorListResult', function() {
      // uncomment below and update the code to test ServiceTierAdvisorListResult
      //var instance = new AzureSqlDatabase.ServiceTierAdvisorListResult();
      //expect(instance).to.be.a(AzureSqlDatabase.ServiceTierAdvisorListResult);
    });

    it('should have the property value (base name: "value")', function() {
      // uncomment below and update the code to test the property value
      //var instance = new AzureSqlDatabase.ServiceTierAdvisorListResult();
      //expect(instance).to.be();
    });

  });

}));
