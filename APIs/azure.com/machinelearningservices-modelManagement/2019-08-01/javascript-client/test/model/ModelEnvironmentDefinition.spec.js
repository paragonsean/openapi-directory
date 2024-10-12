/**
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-08-01
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
    instance = new AzureMachineLearningModelManagementService.ModelEnvironmentDefinition();
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

  describe('ModelEnvironmentDefinition', function() {
    it('should create an instance of ModelEnvironmentDefinition', function() {
      // uncomment below and update the code to test ModelEnvironmentDefinition
      //var instance = new AzureMachineLearningModelManagementService.ModelEnvironmentDefinition();
      //expect(instance).to.be.a(AzureMachineLearningModelManagementService.ModelEnvironmentDefinition);
    });

    it('should have the property docker (base name: "docker")', function() {
      // uncomment below and update the code to test the property docker
      //var instance = new AzureMachineLearningModelManagementService.ModelEnvironmentDefinition();
      //expect(instance).to.be();
    });

    it('should have the property environmentVariables (base name: "environmentVariables")', function() {
      // uncomment below and update the code to test the property environmentVariables
      //var instance = new AzureMachineLearningModelManagementService.ModelEnvironmentDefinition();
      //expect(instance).to.be();
    });

    it('should have the property inferencingStackVersion (base name: "inferencingStackVersion")', function() {
      // uncomment below and update the code to test the property inferencingStackVersion
      //var instance = new AzureMachineLearningModelManagementService.ModelEnvironmentDefinition();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new AzureMachineLearningModelManagementService.ModelEnvironmentDefinition();
      //expect(instance).to.be();
    });

    it('should have the property python (base name: "python")', function() {
      // uncomment below and update the code to test the property python
      //var instance = new AzureMachineLearningModelManagementService.ModelEnvironmentDefinition();
      //expect(instance).to.be();
    });

    it('should have the property spark (base name: "spark")', function() {
      // uncomment below and update the code to test the property spark
      //var instance = new AzureMachineLearningModelManagementService.ModelEnvironmentDefinition();
      //expect(instance).to.be();
    });

    it('should have the property version (base name: "version")', function() {
      // uncomment below and update the code to test the property version
      //var instance = new AzureMachineLearningModelManagementService.ModelEnvironmentDefinition();
      //expect(instance).to.be();
    });

  });

}));
