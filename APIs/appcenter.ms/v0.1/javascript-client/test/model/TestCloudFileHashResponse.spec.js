/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
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
    factory(root.expect, root.AppCenterClient);
  }
}(this, function(expect, AppCenterClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AppCenterClient.TestCloudFileHashResponse();
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

  describe('TestCloudFileHashResponse', function() {
    it('should create an instance of TestCloudFileHashResponse', function() {
      // uncomment below and update the code to test TestCloudFileHashResponse
      //var instance = new AppCenterClient.TestCloudFileHashResponse();
      //expect(instance).to.be.a(AppCenterClient.TestCloudFileHashResponse);
    });

    it('should have the property checksum (base name: "checksum")', function() {
      // uncomment below and update the code to test the property checksum
      //var instance = new AppCenterClient.TestCloudFileHashResponse();
      //expect(instance).to.be();
    });

    it('should have the property fileType (base name: "fileType")', function() {
      // uncomment below and update the code to test the property fileType
      //var instance = new AppCenterClient.TestCloudFileHashResponse();
      //expect(instance).to.be();
    });

    it('should have the property relativePath (base name: "relativePath")', function() {
      // uncomment below and update the code to test the property relativePath
      //var instance = new AppCenterClient.TestCloudFileHashResponse();
      //expect(instance).to.be();
    });

    it('should have the property uploadStatus (base name: "uploadStatus")', function() {
      // uncomment below and update the code to test the property uploadStatus
      //var instance = new AppCenterClient.TestCloudFileHashResponse();
      //expect(instance).to.be();
    });

  });

}));
