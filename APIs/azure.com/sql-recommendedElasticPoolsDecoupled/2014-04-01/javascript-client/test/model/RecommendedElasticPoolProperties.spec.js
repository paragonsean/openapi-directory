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
    instance = new AzureSqlDatabase.RecommendedElasticPoolProperties();
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

  describe('RecommendedElasticPoolProperties', function() {
    it('should create an instance of RecommendedElasticPoolProperties', function() {
      // uncomment below and update the code to test RecommendedElasticPoolProperties
      //var instance = new AzureSqlDatabase.RecommendedElasticPoolProperties();
      //expect(instance).to.be.a(AzureSqlDatabase.RecommendedElasticPoolProperties);
    });

    it('should have the property databaseDtuMax (base name: "databaseDtuMax")', function() {
      // uncomment below and update the code to test the property databaseDtuMax
      //var instance = new AzureSqlDatabase.RecommendedElasticPoolProperties();
      //expect(instance).to.be();
    });

    it('should have the property databaseDtuMin (base name: "databaseDtuMin")', function() {
      // uncomment below and update the code to test the property databaseDtuMin
      //var instance = new AzureSqlDatabase.RecommendedElasticPoolProperties();
      //expect(instance).to.be();
    });

    it('should have the property databaseEdition (base name: "databaseEdition")', function() {
      // uncomment below and update the code to test the property databaseEdition
      //var instance = new AzureSqlDatabase.RecommendedElasticPoolProperties();
      //expect(instance).to.be();
    });

    it('should have the property databases (base name: "databases")', function() {
      // uncomment below and update the code to test the property databases
      //var instance = new AzureSqlDatabase.RecommendedElasticPoolProperties();
      //expect(instance).to.be();
    });

    it('should have the property dtu (base name: "dtu")', function() {
      // uncomment below and update the code to test the property dtu
      //var instance = new AzureSqlDatabase.RecommendedElasticPoolProperties();
      //expect(instance).to.be();
    });

    it('should have the property maxObservedDtu (base name: "maxObservedDtu")', function() {
      // uncomment below and update the code to test the property maxObservedDtu
      //var instance = new AzureSqlDatabase.RecommendedElasticPoolProperties();
      //expect(instance).to.be();
    });

    it('should have the property maxObservedStorageMB (base name: "maxObservedStorageMB")', function() {
      // uncomment below and update the code to test the property maxObservedStorageMB
      //var instance = new AzureSqlDatabase.RecommendedElasticPoolProperties();
      //expect(instance).to.be();
    });

    it('should have the property metrics (base name: "metrics")', function() {
      // uncomment below and update the code to test the property metrics
      //var instance = new AzureSqlDatabase.RecommendedElasticPoolProperties();
      //expect(instance).to.be();
    });

    it('should have the property observationPeriodEnd (base name: "observationPeriodEnd")', function() {
      // uncomment below and update the code to test the property observationPeriodEnd
      //var instance = new AzureSqlDatabase.RecommendedElasticPoolProperties();
      //expect(instance).to.be();
    });

    it('should have the property observationPeriodStart (base name: "observationPeriodStart")', function() {
      // uncomment below and update the code to test the property observationPeriodStart
      //var instance = new AzureSqlDatabase.RecommendedElasticPoolProperties();
      //expect(instance).to.be();
    });

    it('should have the property storageMB (base name: "storageMB")', function() {
      // uncomment below and update the code to test the property storageMB
      //var instance = new AzureSqlDatabase.RecommendedElasticPoolProperties();
      //expect(instance).to.be();
    });

  });

}));
