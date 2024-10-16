/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
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
    factory(root.expect, root.AgcoApi);
  }
}(this, function(expect, AgcoApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AgcoApi.BuildSystemSharedDTOJobActivity();
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

  describe('BuildSystemSharedDTOJobActivity', function() {
    it('should create an instance of BuildSystemSharedDTOJobActivity', function() {
      // uncomment below and update the code to test BuildSystemSharedDTOJobActivity
      //var instance = new AgcoApi.BuildSystemSharedDTOJobActivity();
      //expect(instance).to.be.a(AgcoApi.BuildSystemSharedDTOJobActivity);
    });

    it('should have the property activityID (base name: "ActivityID")', function() {
      // uncomment below and update the code to test the property activityID
      //var instance = new AgcoApi.BuildSystemSharedDTOJobActivity();
      //expect(instance).to.be();
    });

    it('should have the property jobActivityID (base name: "JobActivityID")', function() {
      // uncomment below and update the code to test the property jobActivityID
      //var instance = new AgcoApi.BuildSystemSharedDTOJobActivity();
      //expect(instance).to.be();
    });

    it('should have the property jobID (base name: "JobID")', function() {
      // uncomment below and update the code to test the property jobID
      //var instance = new AgcoApi.BuildSystemSharedDTOJobActivity();
      //expect(instance).to.be();
    });

    it('should have the property parameterMappings (base name: "ParameterMappings")', function() {
      // uncomment below and update the code to test the property parameterMappings
      //var instance = new AgcoApi.BuildSystemSharedDTOJobActivity();
      //expect(instance).to.be();
    });

    it('should have the property runOrder (base name: "RunOrder")', function() {
      // uncomment below and update the code to test the property runOrder
      //var instance = new AgcoApi.BuildSystemSharedDTOJobActivity();
      //expect(instance).to.be();
    });

  });

}));
