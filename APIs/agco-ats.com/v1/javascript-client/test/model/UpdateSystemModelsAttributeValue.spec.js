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
    instance = new AgcoApi.UpdateSystemModelsAttributeValue();
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

  describe('UpdateSystemModelsAttributeValue', function() {
    it('should create an instance of UpdateSystemModelsAttributeValue', function() {
      // uncomment below and update the code to test UpdateSystemModelsAttributeValue
      //var instance = new AgcoApi.UpdateSystemModelsAttributeValue();
      //expect(instance).to.be.a(AgcoApi.UpdateSystemModelsAttributeValue);
    });

    it('should have the property key (base name: "Key")', function() {
      // uncomment below and update the code to test the property key
      //var instance = new AgcoApi.UpdateSystemModelsAttributeValue();
      //expect(instance).to.be();
    });

    it('should have the property timeStamp (base name: "TimeStamp")', function() {
      // uncomment below and update the code to test the property timeStamp
      //var instance = new AgcoApi.UpdateSystemModelsAttributeValue();
      //expect(instance).to.be();
    });

    it('should have the property value (base name: "Value")', function() {
      // uncomment below and update the code to test the property value
      //var instance = new AgcoApi.UpdateSystemModelsAttributeValue();
      //expect(instance).to.be();
    });

  });

}));
