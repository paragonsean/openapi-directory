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
    instance = new AzureMachineLearningModelManagementService.RegenerateServiceKeysRequest();
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

  describe('RegenerateServiceKeysRequest', function() {
    it('should create an instance of RegenerateServiceKeysRequest', function() {
      // uncomment below and update the code to test RegenerateServiceKeysRequest
      //var instance = new AzureMachineLearningModelManagementService.RegenerateServiceKeysRequest();
      //expect(instance).to.be.a(AzureMachineLearningModelManagementService.RegenerateServiceKeysRequest);
    });

    it('should have the property keyType (base name: "keyType")', function() {
      // uncomment below and update the code to test the property keyType
      //var instance = new AzureMachineLearningModelManagementService.RegenerateServiceKeysRequest();
      //expect(instance).to.be();
    });

    it('should have the property keyValue (base name: "keyValue")', function() {
      // uncomment below and update the code to test the property keyValue
      //var instance = new AzureMachineLearningModelManagementService.RegenerateServiceKeysRequest();
      //expect(instance).to.be();
    });

  });

}));
