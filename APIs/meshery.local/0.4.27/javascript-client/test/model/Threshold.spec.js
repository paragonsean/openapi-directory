/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
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
    factory(root.expect, root.MesheryApi);
  }
}(this, function(expect, MesheryApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MesheryApi.Threshold();
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

  describe('Threshold', function() {
    it('should create an instance of Threshold', function() {
      // uncomment below and update the code to test Threshold
      //var instance = new MesheryApi.Threshold();
      //expect(instance).to.be.a(MesheryApi.Threshold);
    });

    it('should have the property colorMode (base name: "colorMode")', function() {
      // uncomment below and update the code to test the property colorMode
      //var instance = new MesheryApi.Threshold();
      //expect(instance).to.be();
    });

    it('should have the property fill (base name: "fill")', function() {
      // uncomment below and update the code to test the property fill
      //var instance = new MesheryApi.Threshold();
      //expect(instance).to.be();
    });

    it('should have the property fillColor (base name: "fillColor")', function() {
      // uncomment below and update the code to test the property fillColor
      //var instance = new MesheryApi.Threshold();
      //expect(instance).to.be();
    });

    it('should have the property line (base name: "line")', function() {
      // uncomment below and update the code to test the property line
      //var instance = new MesheryApi.Threshold();
      //expect(instance).to.be();
    });

    it('should have the property lineColor (base name: "lineColor")', function() {
      // uncomment below and update the code to test the property lineColor
      //var instance = new MesheryApi.Threshold();
      //expect(instance).to.be();
    });

    it('should have the property op (base name: "op")', function() {
      // uncomment below and update the code to test the property op
      //var instance = new MesheryApi.Threshold();
      //expect(instance).to.be();
    });

    it('should have the property value (base name: "value")', function() {
      // uncomment below and update the code to test the property value
      //var instance = new MesheryApi.Threshold();
      //expect(instance).to.be();
    });

    it('should have the property yaxis (base name: "yaxis")', function() {
      // uncomment below and update the code to test the property yaxis
      //var instance = new MesheryApi.Threshold();
      //expect(instance).to.be();
    });

  });

}));
