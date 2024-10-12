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
    instance = new AppCenterClient.BranchConfigurationsGet200ResponseAllOfToolsetsXamarin();
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

  describe('BranchConfigurationsGet200ResponseAllOfToolsetsXamarin', function() {
    it('should create an instance of BranchConfigurationsGet200ResponseAllOfToolsetsXamarin', function() {
      // uncomment below and update the code to test BranchConfigurationsGet200ResponseAllOfToolsetsXamarin
      //var instance = new AppCenterClient.BranchConfigurationsGet200ResponseAllOfToolsetsXamarin();
      //expect(instance).to.be.a(AppCenterClient.BranchConfigurationsGet200ResponseAllOfToolsetsXamarin);
    });

    it('should have the property args (base name: "args")', function() {
      // uncomment below and update the code to test the property args
      //var instance = new AppCenterClient.BranchConfigurationsGet200ResponseAllOfToolsetsXamarin();
      //expect(instance).to.be();
    });

    it('should have the property configuration (base name: "configuration")', function() {
      // uncomment below and update the code to test the property configuration
      //var instance = new AppCenterClient.BranchConfigurationsGet200ResponseAllOfToolsetsXamarin();
      //expect(instance).to.be();
    });

    it('should have the property isSimBuild (base name: "isSimBuild")', function() {
      // uncomment below and update the code to test the property isSimBuild
      //var instance = new AppCenterClient.BranchConfigurationsGet200ResponseAllOfToolsetsXamarin();
      //expect(instance).to.be();
    });

    it('should have the property monoVersion (base name: "monoVersion")', function() {
      // uncomment below and update the code to test the property monoVersion
      //var instance = new AppCenterClient.BranchConfigurationsGet200ResponseAllOfToolsetsXamarin();
      //expect(instance).to.be();
    });

    it('should have the property p12File (base name: "p12File")', function() {
      // uncomment below and update the code to test the property p12File
      //var instance = new AppCenterClient.BranchConfigurationsGet200ResponseAllOfToolsetsXamarin();
      //expect(instance).to.be();
    });

    it('should have the property p12Pwd (base name: "p12Pwd")', function() {
      // uncomment below and update the code to test the property p12Pwd
      //var instance = new AppCenterClient.BranchConfigurationsGet200ResponseAllOfToolsetsXamarin();
      //expect(instance).to.be();
    });

    it('should have the property provProfile (base name: "provProfile")', function() {
      // uncomment below and update the code to test the property provProfile
      //var instance = new AppCenterClient.BranchConfigurationsGet200ResponseAllOfToolsetsXamarin();
      //expect(instance).to.be();
    });

    it('should have the property sdkBundle (base name: "sdkBundle")', function() {
      // uncomment below and update the code to test the property sdkBundle
      //var instance = new AppCenterClient.BranchConfigurationsGet200ResponseAllOfToolsetsXamarin();
      //expect(instance).to.be();
    });

    it('should have the property slnPath (base name: "slnPath")', function() {
      // uncomment below and update the code to test the property slnPath
      //var instance = new AppCenterClient.BranchConfigurationsGet200ResponseAllOfToolsetsXamarin();
      //expect(instance).to.be();
    });

    it('should have the property symlink (base name: "symlink")', function() {
      // uncomment below and update the code to test the property symlink
      //var instance = new AppCenterClient.BranchConfigurationsGet200ResponseAllOfToolsetsXamarin();
      //expect(instance).to.be();
    });

  });

}));
