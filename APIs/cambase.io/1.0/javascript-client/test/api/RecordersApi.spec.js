/**
 * Cambase.io
 * Cambase.io is a project by Evercam.io in order to make it easier for software developers to have a reliable, up to date source of model hardware information available via a public API.
 *
 * The version of the OpenAPI document: 1.0
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
    factory(root.expect, root.CambaseIo);
  }
}(this, function(expect, CambaseIo) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new CambaseIo.RecordersApi();
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

  describe('RecordersApi', function() {
    describe('apiV1RecordersCreate', function() {
      it('should call apiV1RecordersCreate successfully', function(done) {
        //uncomment below and update the code to test apiV1RecordersCreate
        //instance.apiV1RecordersCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('apiV1RecordersIdJsonPatch', function() {
      it('should call apiV1RecordersIdJsonPatch successfully', function(done) {
        //uncomment below and update the code to test apiV1RecordersIdJsonPatch
        //instance.apiV1RecordersIdJsonPatch(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('apiV1RecordersIdJsonPut', function() {
      it('should call apiV1RecordersIdJsonPut successfully', function(done) {
        //uncomment below and update the code to test apiV1RecordersIdJsonPut
        //instance.apiV1RecordersIdJsonPut(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('apiV1RecordersIndex', function() {
      it('should call apiV1RecordersIndex successfully', function(done) {
        //uncomment below and update the code to test apiV1RecordersIndex
        //instance.apiV1RecordersIndex(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('apiV1RecordersSearch', function() {
      it('should call apiV1RecordersSearch successfully', function(done) {
        //uncomment below and update the code to test apiV1RecordersSearch
        //instance.apiV1RecordersSearch(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('apiV1RecordersShow', function() {
      it('should call apiV1RecordersShow successfully', function(done) {
        //uncomment below and update the code to test apiV1RecordersShow
        //instance.apiV1RecordersShow(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
