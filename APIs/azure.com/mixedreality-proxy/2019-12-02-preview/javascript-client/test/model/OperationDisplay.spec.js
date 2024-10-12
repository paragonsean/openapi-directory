/**
 * Mixed Reality
 * Mixed Reality Resource Provider Proxy API
 *
 * The version of the OpenAPI document: 2019-12-02-preview
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
    factory(root.expect, root.MixedReality);
  }
}(this, function(expect, MixedReality) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MixedReality.OperationDisplay();
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

  describe('OperationDisplay', function() {
    it('should create an instance of OperationDisplay', function() {
      // uncomment below and update the code to test OperationDisplay
      //var instance = new MixedReality.OperationDisplay();
      //expect(instance).to.be.a(MixedReality.OperationDisplay);
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new MixedReality.OperationDisplay();
      //expect(instance).to.be();
    });

    it('should have the property operation (base name: "operation")', function() {
      // uncomment below and update the code to test the property operation
      //var instance = new MixedReality.OperationDisplay();
      //expect(instance).to.be();
    });

    it('should have the property provider (base name: "provider")', function() {
      // uncomment below and update the code to test the property provider
      //var instance = new MixedReality.OperationDisplay();
      //expect(instance).to.be();
    });

    it('should have the property resource (base name: "resource")', function() {
      // uncomment below and update the code to test the property resource
      //var instance = new MixedReality.OperationDisplay();
      //expect(instance).to.be();
    });

  });

}));
