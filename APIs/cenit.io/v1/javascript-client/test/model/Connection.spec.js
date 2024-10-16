/**
 * Cenit IO - REST API Specification
 * Cenit IO is an Open Platform for Data and Business Integration (iPaaS) 
 *
 * The version of the OpenAPI document: v1
 * Contact: support@cenit.io
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
    factory(root.expect, root.CenitIoRestApiSpecification);
  }
}(this, function(expect, CenitIoRestApiSpecification) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new CenitIoRestApiSpecification.Connection();
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

  describe('Connection', function() {
    it('should create an instance of Connection', function() {
      // uncomment below and update the code to test Connection
      //var instance = new CenitIoRestApiSpecification.Connection();
      //expect(instance).to.be.a(CenitIoRestApiSpecification.Connection);
    });

    it('should have the property headers (base name: "headers")', function() {
      // uncomment below and update the code to test the property headers
      //var instance = new CenitIoRestApiSpecification.Connection();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new CenitIoRestApiSpecification.Connection();
      //expect(instance).to.be();
    });

    it('should have the property key (base name: "key")', function() {
      // uncomment below and update the code to test the property key
      //var instance = new CenitIoRestApiSpecification.Connection();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new CenitIoRestApiSpecification.Connection();
      //expect(instance).to.be();
    });

    it('should have the property namespace (base name: "namespace")', function() {
      // uncomment below and update the code to test the property namespace
      //var instance = new CenitIoRestApiSpecification.Connection();
      //expect(instance).to.be();
    });

    it('should have the property parameters (base name: "parameters")', function() {
      // uncomment below and update the code to test the property parameters
      //var instance = new CenitIoRestApiSpecification.Connection();
      //expect(instance).to.be();
    });

    it('should have the property token (base name: "token")', function() {
      // uncomment below and update the code to test the property token
      //var instance = new CenitIoRestApiSpecification.Connection();
      //expect(instance).to.be();
    });

    it('should have the property url (base name: "url")', function() {
      // uncomment below and update the code to test the property url
      //var instance = new CenitIoRestApiSpecification.Connection();
      //expect(instance).to.be();
    });

  });

}));
