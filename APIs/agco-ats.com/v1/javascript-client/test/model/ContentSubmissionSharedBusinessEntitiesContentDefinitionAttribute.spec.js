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
    instance = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute();
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

  describe('ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute', function() {
    it('should create an instance of ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute', function() {
      // uncomment below and update the code to test ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute
      //var instance = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute();
      //expect(instance).to.be.a(AgcoApi.ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute);
    });

    it('should have the property contentDefinitionID (base name: "ContentDefinitionID")', function() {
      // uncomment below and update the code to test the property contentDefinitionID
      //var instance = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute();
      //expect(instance).to.be();
    });

    it('should have the property ID (base name: "ID")', function() {
      // uncomment below and update the code to test the property ID
      //var instance = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "Name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute();
      //expect(instance).to.be();
    });

    it('should have the property value (base name: "Value")', function() {
      // uncomment below and update the code to test the property value
      //var instance = new AgcoApi.ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute();
      //expect(instance).to.be();
    });

  });

}));
