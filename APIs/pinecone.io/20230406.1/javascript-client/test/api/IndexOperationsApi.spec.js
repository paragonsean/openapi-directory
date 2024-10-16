/**
 * Pinecone API
 * Pinecone is a vector database. This is an unofficial, community-managed OpenAPI spec that (should) accurately model the Pinecone API. This project was developed independent of and is unaffiliated with Pinecone Systems. Users should switch to the official API spec, if and when Pinecone releases it.
 *
 * The version of the OpenAPI document: 20230406.1
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
    factory(root.expect, root.PineconeApi);
  }
}(this, function(expect, PineconeApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new PineconeApi.IndexOperationsApi();
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

  describe('IndexOperationsApi', function() {
    describe('configureIndex', function() {
      it('should call configureIndex successfully', function(done) {
        //uncomment below and update the code to test configureIndex
        //instance.configureIndex(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createCollection', function() {
      it('should call createCollection successfully', function(done) {
        //uncomment below and update the code to test createCollection
        //instance.createCollection(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createIndex', function() {
      it('should call createIndex successfully', function(done) {
        //uncomment below and update the code to test createIndex
        //instance.createIndex(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteCollection', function() {
      it('should call deleteCollection successfully', function(done) {
        //uncomment below and update the code to test deleteCollection
        //instance.deleteCollection(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteIndex', function() {
      it('should call deleteIndex successfully', function(done) {
        //uncomment below and update the code to test deleteIndex
        //instance.deleteIndex(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('describeCollection', function() {
      it('should call describeCollection successfully', function(done) {
        //uncomment below and update the code to test describeCollection
        //instance.describeCollection(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('describeIndex', function() {
      it('should call describeIndex successfully', function(done) {
        //uncomment below and update the code to test describeIndex
        //instance.describeIndex(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listCollections', function() {
      it('should call listCollections successfully', function(done) {
        //uncomment below and update the code to test listCollections
        //instance.listCollections(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('listIndexes', function() {
      it('should call listIndexes successfully', function(done) {
        //uncomment below and update the code to test listIndexes
        //instance.listIndexes(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
