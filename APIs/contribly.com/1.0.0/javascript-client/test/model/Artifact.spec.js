/**
 * Contribly
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
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
    factory(root.expect, root.Contribly);
  }
}(this, function(expect, Contribly) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new Contribly.Artifact();
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

  describe('Artifact', function() {
    it('should create an instance of Artifact', function() {
      // uncomment below and update the code to test Artifact
      //var instance = new Contribly.Artifact();
      //expect(instance).to.be.a(Contribly.Artifact);
    });

    it('should have the property contentLength (base name: "contentLength")', function() {
      // uncomment below and update the code to test the property contentLength
      //var instance = new Contribly.Artifact();
      //expect(instance).to.be();
    });

    it('should have the property contentType (base name: "contentType")', function() {
      // uncomment below and update the code to test the property contentType
      //var instance = new Contribly.Artifact();
      //expect(instance).to.be();
    });

    it('should have the property height (base name: "height")', function() {
      // uncomment below and update the code to test the property height
      //var instance = new Contribly.Artifact();
      //expect(instance).to.be();
    });

    it('should have the property label (base name: "label")', function() {
      // uncomment below and update the code to test the property label
      //var instance = new Contribly.Artifact();
      //expect(instance).to.be();
    });

    it('should have the property url (base name: "url")', function() {
      // uncomment below and update the code to test the property url
      //var instance = new Contribly.Artifact();
      //expect(instance).to.be();
    });

    it('should have the property width (base name: "width")', function() {
      // uncomment below and update the code to test the property width
      //var instance = new Contribly.Artifact();
      //expect(instance).to.be();
    });

  });

}));
