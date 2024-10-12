/**
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-09-30
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
    factory(root.expect, root.AzureMachineLearningModelManagementService);
  }
}(this, function(expect, AzureMachineLearningModelManagementService) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AzureMachineLearningModelManagementService.AKSVariantResponse();
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

  describe('AKSVariantResponse', function() {
    it('should create an instance of AKSVariantResponse', function() {
      // uncomment below and update the code to test AKSVariantResponse
      //var instance = new AzureMachineLearningModelManagementService.AKSVariantResponse();
      //expect(instance).to.be.a(AzureMachineLearningModelManagementService.AKSVariantResponse);
    });

    it('should have the property isDefault (base name: "isDefault")', function() {
      // uncomment below and update the code to test the property isDefault
      //var instance = new AzureMachineLearningModelManagementService.AKSVariantResponse();
      //expect(instance).to.be();
    });

    it('should have the property trafficPercentile (base name: "trafficPercentile")', function() {
      // uncomment below and update the code to test the property trafficPercentile
      //var instance = new AzureMachineLearningModelManagementService.AKSVariantResponse();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new AzureMachineLearningModelManagementService.AKSVariantResponse();
      //expect(instance).to.be();
    });

  });

}));
