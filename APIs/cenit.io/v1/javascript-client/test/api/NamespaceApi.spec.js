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
    instance = new CenitIoRestApiSpecification.NamespaceApi();
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

  describe('NamespaceApi', function() {
    describe('setupNamespaceGet', function() {
      it('should call setupNamespaceGet successfully', function(done) {
        //uncomment below and update the code to test setupNamespaceGet
        //instance.setupNamespaceGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('setupNamespaceIdDelete', function() {
      it('should call setupNamespaceIdDelete successfully', function(done) {
        //uncomment below and update the code to test setupNamespaceIdDelete
        //instance.setupNamespaceIdDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('setupNamespaceIdGet', function() {
      it('should call setupNamespaceIdGet successfully', function(done) {
        //uncomment below and update the code to test setupNamespaceIdGet
        //instance.setupNamespaceIdGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('setupNamespacePost', function() {
      it('should call setupNamespacePost successfully', function(done) {
        //uncomment below and update the code to test setupNamespacePost
        //instance.setupNamespacePost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
