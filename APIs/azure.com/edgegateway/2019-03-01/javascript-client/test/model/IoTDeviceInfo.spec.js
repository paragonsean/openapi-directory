/**
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
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
    factory(root.expect, root.DataBoxEdgeManagementClient);
  }
}(this, function(expect, DataBoxEdgeManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new DataBoxEdgeManagementClient.IoTDeviceInfo();
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

  describe('IoTDeviceInfo', function() {
    it('should create an instance of IoTDeviceInfo', function() {
      // uncomment below and update the code to test IoTDeviceInfo
      //var instance = new DataBoxEdgeManagementClient.IoTDeviceInfo();
      //expect(instance).to.be.a(DataBoxEdgeManagementClient.IoTDeviceInfo);
    });

    it('should have the property authentication (base name: "authentication")', function() {
      // uncomment below and update the code to test the property authentication
      //var instance = new DataBoxEdgeManagementClient.IoTDeviceInfo();
      //expect(instance).to.be();
    });

    it('should have the property deviceId (base name: "deviceId")', function() {
      // uncomment below and update the code to test the property deviceId
      //var instance = new DataBoxEdgeManagementClient.IoTDeviceInfo();
      //expect(instance).to.be();
    });

    it('should have the property ioTHostHub (base name: "ioTHostHub")', function() {
      // uncomment below and update the code to test the property ioTHostHub
      //var instance = new DataBoxEdgeManagementClient.IoTDeviceInfo();
      //expect(instance).to.be();
    });

  });

}));
