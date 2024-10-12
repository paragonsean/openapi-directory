/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2016-03-01
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
    factory(root.expect, root.ApiClient);
  }
}(this, function(expect, ApiClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new ApiClient.ValidateProperties();
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

  describe('ValidateProperties', function() {
    it('should create an instance of ValidateProperties', function() {
      // uncomment below and update the code to test ValidateProperties
      //var instance = new ApiClient.ValidateProperties();
      //expect(instance).to.be.a(ApiClient.ValidateProperties);
    });

    it('should have the property capacity (base name: "capacity")', function() {
      // uncomment below and update the code to test the property capacity
      //var instance = new ApiClient.ValidateProperties();
      //expect(instance).to.be();
    });

    it('should have the property hostingEnvironment (base name: "hostingEnvironment")', function() {
      // uncomment below and update the code to test the property hostingEnvironment
      //var instance = new ApiClient.ValidateProperties();
      //expect(instance).to.be();
    });

    it('should have the property isSpot (base name: "isSpot")', function() {
      // uncomment below and update the code to test the property isSpot
      //var instance = new ApiClient.ValidateProperties();
      //expect(instance).to.be();
    });

    it('should have the property needLinuxWorkers (base name: "needLinuxWorkers")', function() {
      // uncomment below and update the code to test the property needLinuxWorkers
      //var instance = new ApiClient.ValidateProperties();
      //expect(instance).to.be();
    });

    it('should have the property serverFarmId (base name: "serverFarmId")', function() {
      // uncomment below and update the code to test the property serverFarmId
      //var instance = new ApiClient.ValidateProperties();
      //expect(instance).to.be();
    });

    it('should have the property skuName (base name: "skuName")', function() {
      // uncomment below and update the code to test the property skuName
      //var instance = new ApiClient.ValidateProperties();
      //expect(instance).to.be();
    });

  });

}));
