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
    instance = new Contribly.ArtifactFormats();
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

  describe('ArtifactFormats', function() {
    it('should create an instance of ArtifactFormats', function() {
      // uncomment below and update the code to test ArtifactFormats
      //var instance = new Contribly.ArtifactFormats();
      //expect(instance).to.be.a(Contribly.ArtifactFormats);
    });

    it('should have the property contribution (base name: "contribution")', function() {
      // uncomment below and update the code to test the property contribution
      //var instance = new Contribly.ArtifactFormats();
      //expect(instance).to.be();
    });

    it('should have the property cover (base name: "cover")', function() {
      // uncomment below and update the code to test the property cover
      //var instance = new Contribly.ArtifactFormats();
      //expect(instance).to.be();
    });

    it('should have the property profileImage (base name: "profileImage")', function() {
      // uncomment below and update the code to test the property profileImage
      //var instance = new Contribly.ArtifactFormats();
      //expect(instance).to.be();
    });

  });

}));
