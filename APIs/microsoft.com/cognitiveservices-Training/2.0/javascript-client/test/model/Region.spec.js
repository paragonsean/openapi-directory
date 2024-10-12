/**
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.0
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
    factory(root.expect, root.TrainingApi);
  }
}(this, function(expect, TrainingApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new TrainingApi.Region();
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

  describe('Region', function() {
    it('should create an instance of Region', function() {
      // uncomment below and update the code to test Region
      //var instance = new TrainingApi.Region();
      //expect(instance).to.be.a(TrainingApi.Region);
    });

    it('should have the property height (base name: "height")', function() {
      // uncomment below and update the code to test the property height
      //var instance = new TrainingApi.Region();
      //expect(instance).to.be();
    });

    it('should have the property left (base name: "left")', function() {
      // uncomment below and update the code to test the property left
      //var instance = new TrainingApi.Region();
      //expect(instance).to.be();
    });

    it('should have the property tagId (base name: "tagId")', function() {
      // uncomment below and update the code to test the property tagId
      //var instance = new TrainingApi.Region();
      //expect(instance).to.be();
    });

    it('should have the property top (base name: "top")', function() {
      // uncomment below and update the code to test the property top
      //var instance = new TrainingApi.Region();
      //expect(instance).to.be();
    });

    it('should have the property width (base name: "width")', function() {
      // uncomment below and update the code to test the property width
      //var instance = new TrainingApi.Region();
      //expect(instance).to.be();
    });

  });

}));
