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
    instance = new AppCenterClient.BranchConfigurationRevisionsInner();
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

  describe('BranchConfigurationRevisionsInner', function() {
    it('should create an instance of BranchConfigurationRevisionsInner', function() {
      // uncomment below and update the code to test BranchConfigurationRevisionsInner
      //var instance = new AppCenterClient.BranchConfigurationRevisionsInner();
      //expect(instance).to.be.a(AppCenterClient.BranchConfigurationRevisionsInner);
    });

    it('should have the property changeType (base name: "changeType")', function() {
      // uncomment below and update the code to test the property changeType
      //var instance = new AppCenterClient.BranchConfigurationRevisionsInner();
      //expect(instance).to.be();
    });

    it('should have the property changedBy (base name: "changedBy")', function() {
      // uncomment below and update the code to test the property changedBy
      //var instance = new AppCenterClient.BranchConfigurationRevisionsInner();
      //expect(instance).to.be();
    });

    it('should have the property changedDate (base name: "changedDate")', function() {
      // uncomment below and update the code to test the property changedDate
      //var instance = new AppCenterClient.BranchConfigurationRevisionsInner();
      //expect(instance).to.be();
    });

    it('should have the property definitionUrl (base name: "definitionUrl")', function() {
      // uncomment below and update the code to test the property definitionUrl
      //var instance = new AppCenterClient.BranchConfigurationRevisionsInner();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new AppCenterClient.BranchConfigurationRevisionsInner();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new AppCenterClient.BranchConfigurationRevisionsInner();
      //expect(instance).to.be();
    });

    it('should have the property revision (base name: "revision")', function() {
      // uncomment below and update the code to test the property revision
      //var instance = new AppCenterClient.BranchConfigurationRevisionsInner();
      //expect(instance).to.be();
    });

  });

}));
