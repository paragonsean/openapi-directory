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
    instance = new AzureMachineLearningModelManagementService.TargetRuntime();
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

  describe('TargetRuntime', function() {
    it('should create an instance of TargetRuntime', function() {
      // uncomment below and update the code to test TargetRuntime
      //var instance = new AzureMachineLearningModelManagementService.TargetRuntime();
      //expect(instance).to.be.a(AzureMachineLearningModelManagementService.TargetRuntime);
    });

    it('should have the property osType (base name: "osType")', function() {
      // uncomment below and update the code to test the property osType
      //var instance = new AzureMachineLearningModelManagementService.TargetRuntime();
      //expect(instance).to.be();
    });

    it('should have the property properties (base name: "properties")', function() {
      // uncomment below and update the code to test the property properties
      //var instance = new AzureMachineLearningModelManagementService.TargetRuntime();
      //expect(instance).to.be();
    });

    it('should have the property runtimeType (base name: "runtimeType")', function() {
      // uncomment below and update the code to test the property runtimeType
      //var instance = new AzureMachineLearningModelManagementService.TargetRuntime();
      //expect(instance).to.be();
    });

    it('should have the property targetArchitecture (base name: "targetArchitecture")', function() {
      // uncomment below and update the code to test the property targetArchitecture
      //var instance = new AzureMachineLearningModelManagementService.TargetRuntime();
      //expect(instance).to.be();
    });

  });

}));
