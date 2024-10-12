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
    instance = new AzureMachineLearningModelManagementService.EnvironmentImageAsset();
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

  describe('EnvironmentImageAsset', function() {
    it('should create an instance of EnvironmentImageAsset', function() {
      // uncomment below and update the code to test EnvironmentImageAsset
      //var instance = new AzureMachineLearningModelManagementService.EnvironmentImageAsset();
      //expect(instance).to.be.a(AzureMachineLearningModelManagementService.EnvironmentImageAsset);
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new AzureMachineLearningModelManagementService.EnvironmentImageAsset();
      //expect(instance).to.be();
    });

    it('should have the property mimeType (base name: "mimeType")', function() {
      // uncomment below and update the code to test the property mimeType
      //var instance = new AzureMachineLearningModelManagementService.EnvironmentImageAsset();
      //expect(instance).to.be();
    });

    it('should have the property unpack (base name: "unpack")', function() {
      // uncomment below and update the code to test the property unpack
      //var instance = new AzureMachineLearningModelManagementService.EnvironmentImageAsset();
      //expect(instance).to.be();
    });

    it('should have the property url (base name: "url")', function() {
      // uncomment below and update the code to test the property url
      //var instance = new AzureMachineLearningModelManagementService.EnvironmentImageAsset();
      //expect(instance).to.be();
    });

  });

}));
