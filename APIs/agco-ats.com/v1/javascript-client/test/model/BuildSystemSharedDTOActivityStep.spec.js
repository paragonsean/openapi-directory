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
    instance = new AgcoApi.BuildSystemSharedDTOActivityStep();
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

  describe('BuildSystemSharedDTOActivityStep', function() {
    it('should create an instance of BuildSystemSharedDTOActivityStep', function() {
      // uncomment below and update the code to test BuildSystemSharedDTOActivityStep
      //var instance = new AgcoApi.BuildSystemSharedDTOActivityStep();
      //expect(instance).to.be.a(AgcoApi.BuildSystemSharedDTOActivityStep);
    });

    it('should have the property activityID (base name: "ActivityID")', function() {
      // uncomment below and update the code to test the property activityID
      //var instance = new AgcoApi.BuildSystemSharedDTOActivityStep();
      //expect(instance).to.be();
    });

    it('should have the property activityStepID (base name: "ActivityStepID")', function() {
      // uncomment below and update the code to test the property activityStepID
      //var instance = new AgcoApi.BuildSystemSharedDTOActivityStep();
      //expect(instance).to.be();
    });

    it('should have the property implementationID (base name: "ImplementationID")', function() {
      // uncomment below and update the code to test the property implementationID
      //var instance = new AgcoApi.BuildSystemSharedDTOActivityStep();
      //expect(instance).to.be();
    });

    it('should have the property parameterMappings (base name: "ParameterMappings")', function() {
      // uncomment below and update the code to test the property parameterMappings
      //var instance = new AgcoApi.BuildSystemSharedDTOActivityStep();
      //expect(instance).to.be();
    });

    it('should have the property runOrder (base name: "RunOrder")', function() {
      // uncomment below and update the code to test the property runOrder
      //var instance = new AgcoApi.BuildSystemSharedDTOActivityStep();
      //expect(instance).to.be();
    });

    it('should have the property stepID (base name: "StepID")', function() {
      // uncomment below and update the code to test the property stepID
      //var instance = new AgcoApi.BuildSystemSharedDTOActivityStep();
      //expect(instance).to.be();
    });

    it('should have the property stepName (base name: "StepName")', function() {
      // uncomment below and update the code to test the property stepName
      //var instance = new AgcoApi.BuildSystemSharedDTOActivityStep();
      //expect(instance).to.be();
    });

    it('should have the property useConfig (base name: "UseConfig")', function() {
      // uncomment below and update the code to test the property useConfig
      //var instance = new AgcoApi.BuildSystemSharedDTOActivityStep();
      //expect(instance).to.be();
    });

  });

}));
