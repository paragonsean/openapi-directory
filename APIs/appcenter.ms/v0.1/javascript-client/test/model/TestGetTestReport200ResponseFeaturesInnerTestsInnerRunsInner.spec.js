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
    instance = new AppCenterClient.TestGetTestReport200ResponseFeaturesInnerTestsInnerRunsInner();
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

  describe('TestGetTestReport200ResponseFeaturesInnerTestsInnerRunsInner', function() {
    it('should create an instance of TestGetTestReport200ResponseFeaturesInnerTestsInnerRunsInner', function() {
      // uncomment below and update the code to test TestGetTestReport200ResponseFeaturesInnerTestsInnerRunsInner
      //var instance = new AppCenterClient.TestGetTestReport200ResponseFeaturesInnerTestsInnerRunsInner();
      //expect(instance).to.be.a(AppCenterClient.TestGetTestReport200ResponseFeaturesInnerTestsInnerRunsInner);
    });

    it('should have the property failed (base name: "failed")', function() {
      // uncomment below and update the code to test the property failed
      //var instance = new AppCenterClient.TestGetTestReport200ResponseFeaturesInnerTestsInnerRunsInner();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new AppCenterClient.TestGetTestReport200ResponseFeaturesInnerTestsInnerRunsInner();
      //expect(instance).to.be();
    });

    it('should have the property number (base name: "number")', function() {
      // uncomment below and update the code to test the property number
      //var instance = new AppCenterClient.TestGetTestReport200ResponseFeaturesInnerTestsInnerRunsInner();
      //expect(instance).to.be();
    });

    it('should have the property reportUrl (base name: "report_url")', function() {
      // uncomment below and update the code to test the property reportUrl
      //var instance = new AppCenterClient.TestGetTestReport200ResponseFeaturesInnerTestsInnerRunsInner();
      //expect(instance).to.be();
    });

    it('should have the property skipped (base name: "skipped")', function() {
      // uncomment below and update the code to test the property skipped
      //var instance = new AppCenterClient.TestGetTestReport200ResponseFeaturesInnerTestsInnerRunsInner();
      //expect(instance).to.be();
    });

    it('should have the property steps (base name: "steps")', function() {
      // uncomment below and update the code to test the property steps
      //var instance = new AppCenterClient.TestGetTestReport200ResponseFeaturesInnerTestsInnerRunsInner();
      //expect(instance).to.be();
    });

  });

}));
