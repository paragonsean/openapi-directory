/**
 * Semantria
 * Semantria applies Text and Sentiment Analysis to tweets, facebook posts, surveys, reviews or enterprise content.
 *
 * The version of the OpenAPI document: 4.0
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
    factory(root.expect, root.Semantria);
  }
}(this, function(expect, Semantria) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new Semantria.ProcessingDocumentsApi();
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

  describe('ProcessingDocumentsApi', function() {
    describe('cancelDocument', function() {
      it('should call cancelDocument successfully', function(done) {
        //uncomment below and update the code to test cancelDocument
        //instance.cancelDocument(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('queueBatchOfDocuments', function() {
      it('should call queueBatchOfDocuments successfully', function(done) {
        //uncomment below and update the code to test queueBatchOfDocuments
        //instance.queueBatchOfDocuments(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('queueDocument', function() {
      it('should call queueDocument successfully', function(done) {
        //uncomment below and update the code to test queueDocument
        //instance.queueDocument(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('receiveDocumentAnalyticData', function() {
      it('should call receiveDocumentAnalyticData successfully', function(done) {
        //uncomment below and update the code to test receiveDocumentAnalyticData
        //instance.receiveDocumentAnalyticData(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('retrieveProcessedDocuments', function() {
      it('should call retrieveProcessedDocuments successfully', function(done) {
        //uncomment below and update the code to test retrieveProcessedDocuments
        //instance.retrieveProcessedDocuments(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
