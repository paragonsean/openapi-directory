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
    instance = new MesheryApi.Link();
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

  describe('Link', function() {
    it('should create an instance of Link', function() {
      // uncomment below and update the code to test Link
      //var instance = new MesheryApi.Link();
      //expect(instance).to.be.a(MesheryApi.Link);
    });

    it('should have the property asDropdown (base name: "asDropdown")', function() {
      // uncomment below and update the code to test the property asDropdown
      //var instance = new MesheryApi.Link();
      //expect(instance).to.be();
    });

    it('should have the property dashUri (base name: "dashUri")', function() {
      // uncomment below and update the code to test the property dashUri
      //var instance = new MesheryApi.Link();
      //expect(instance).to.be();
    });

    it('should have the property dashboard (base name: "dashboard")', function() {
      // uncomment below and update the code to test the property dashboard
      //var instance = new MesheryApi.Link();
      //expect(instance).to.be();
    });

    it('should have the property icon (base name: "icon")', function() {
      // uncomment below and update the code to test the property icon
      //var instance = new MesheryApi.Link();
      //expect(instance).to.be();
    });

    it('should have the property includeVars (base name: "includeVars")', function() {
      // uncomment below and update the code to test the property includeVars
      //var instance = new MesheryApi.Link();
      //expect(instance).to.be();
    });

    it('should have the property keepTime (base name: "keepTime")', function() {
      // uncomment below and update the code to test the property keepTime
      //var instance = new MesheryApi.Link();
      //expect(instance).to.be();
    });

    it('should have the property params (base name: "params")', function() {
      // uncomment below and update the code to test the property params
      //var instance = new MesheryApi.Link();
      //expect(instance).to.be();
    });

    it('should have the property tags (base name: "tags")', function() {
      // uncomment below and update the code to test the property tags
      //var instance = new MesheryApi.Link();
      //expect(instance).to.be();
    });

    it('should have the property targetBlank (base name: "targetBlank")', function() {
      // uncomment below and update the code to test the property targetBlank
      //var instance = new MesheryApi.Link();
      //expect(instance).to.be();
    });

    it('should have the property title (base name: "title")', function() {
      // uncomment below and update the code to test the property title
      //var instance = new MesheryApi.Link();
      //expect(instance).to.be();
    });

    it('should have the property tooltip (base name: "tooltip")', function() {
      // uncomment below and update the code to test the property tooltip
      //var instance = new MesheryApi.Link();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new MesheryApi.Link();
      //expect(instance).to.be();
    });

    it('should have the property url (base name: "url")', function() {
      // uncomment below and update the code to test the property url
      //var instance = new MesheryApi.Link();
      //expect(instance).to.be();
    });

  });

}));
