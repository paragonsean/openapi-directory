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
    instance = new AzureMachineLearningModelManagementService.IotServiceResponse();
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

  describe('IotServiceResponse', function() {
    it('should create an instance of IotServiceResponse', function() {
      // uncomment below and update the code to test IotServiceResponse
      //var instance = new AzureMachineLearningModelManagementService.IotServiceResponse();
      //expect(instance).to.be.a(AzureMachineLearningModelManagementService.IotServiceResponse);
    });

    it('should have the property authEnabled (base name: "authEnabled")', function() {
      // uncomment below and update the code to test the property authEnabled
      //var instance = new AzureMachineLearningModelManagementService.IotServiceResponse();
      //expect(instance).to.be();
    });

    it('should have the property computeName (base name: "computeName")', function() {
      // uncomment below and update the code to test the property computeName
      //var instance = new AzureMachineLearningModelManagementService.IotServiceResponse();
      //expect(instance).to.be();
    });

    it('should have the property imageDetails (base name: "imageDetails")', function() {
      // uncomment below and update the code to test the property imageDetails
      //var instance = new AzureMachineLearningModelManagementService.IotServiceResponse();
      //expect(instance).to.be();
    });

    it('should have the property imageId (base name: "imageId")', function() {
      // uncomment below and update the code to test the property imageId
      //var instance = new AzureMachineLearningModelManagementService.IotServiceResponse();
      //expect(instance).to.be();
    });

    it('should have the property iotDeviceId (base name: "iotDeviceId")', function() {
      // uncomment below and update the code to test the property iotDeviceId
      //var instance = new AzureMachineLearningModelManagementService.IotServiceResponse();
      //expect(instance).to.be();
    });

    it('should have the property iotEdgeModules (base name: "iotEdgeModules")', function() {
      // uncomment below and update the code to test the property iotEdgeModules
      //var instance = new AzureMachineLearningModelManagementService.IotServiceResponse();
      //expect(instance).to.be();
    });

    it('should have the property routes (base name: "routes")', function() {
      // uncomment below and update the code to test the property routes
      //var instance = new AzureMachineLearningModelManagementService.IotServiceResponse();
      //expect(instance).to.be();
    });

  });

}));
