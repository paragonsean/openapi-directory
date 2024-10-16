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
    instance = new AgcoApi.GlobalResourcesSharedModelsFileDownload();
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

  describe('GlobalResourcesSharedModelsFileDownload', function() {
    it('should create an instance of GlobalResourcesSharedModelsFileDownload', function() {
      // uncomment below and update the code to test GlobalResourcesSharedModelsFileDownload
      //var instance = new AgcoApi.GlobalResourcesSharedModelsFileDownload();
      //expect(instance).to.be.a(AgcoApi.GlobalResourcesSharedModelsFileDownload);
    });

    it('should have the property CRC (base name: "CRC")', function() {
      // uncomment below and update the code to test the property CRC
      //var instance = new AgcoApi.GlobalResourcesSharedModelsFileDownload();
      //expect(instance).to.be();
    });

    it('should have the property contentType (base name: "ContentType")', function() {
      // uncomment below and update the code to test the property contentType
      //var instance = new AgcoApi.GlobalResourcesSharedModelsFileDownload();
      //expect(instance).to.be();
    });

    it('should have the property description (base name: "Description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new AgcoApi.GlobalResourcesSharedModelsFileDownload();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "Id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new AgcoApi.GlobalResourcesSharedModelsFileDownload();
      //expect(instance).to.be();
    });

    it('should have the property isPublic (base name: "IsPublic")', function() {
      // uncomment below and update the code to test the property isPublic
      //var instance = new AgcoApi.GlobalResourcesSharedModelsFileDownload();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "Name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new AgcoApi.GlobalResourcesSharedModelsFileDownload();
      //expect(instance).to.be();
    });

    it('should have the property path (base name: "Path")', function() {
      // uncomment below and update the code to test the property path
      //var instance = new AgcoApi.GlobalResourcesSharedModelsFileDownload();
      //expect(instance).to.be();
    });

    it('should have the property size (base name: "Size")', function() {
      // uncomment below and update the code to test the property size
      //var instance = new AgcoApi.GlobalResourcesSharedModelsFileDownload();
      //expect(instance).to.be();
    });

    it('should have the property state (base name: "State")', function() {
      // uncomment below and update the code to test the property state
      //var instance = new AgcoApi.GlobalResourcesSharedModelsFileDownload();
      //expect(instance).to.be();
    });

  });

}));
