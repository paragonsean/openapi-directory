/**
 * DaniWeb Connect API
 * User Recommendation Engine and Chat Network
 *
 * The version of the OpenAPI document: 4
 * Contact: dani@daniwebmail.com
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
    factory(root.expect, root.DaniWebConnectApi);
  }
}(this, function(expect, DaniWebConnectApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new DaniWebConnectApi.MessagesApi();
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

  describe('MessagesApi', function() {
    describe('messagesIDGet', function() {
      it('should call messagesIDGet successfully', function(done) {
        //uncomment below and update the code to test messagesIDGet
        //instance.messagesIDGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('messagesIDMetadataCollectionsGet', function() {
      it('should call messagesIDMetadataCollectionsGet successfully', function(done) {
        //uncomment below and update the code to test messagesIDMetadataCollectionsGet
        //instance.messagesIDMetadataCollectionsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('messagesIDMetadataGet', function() {
      it('should call messagesIDMetadataGet successfully', function(done) {
        //uncomment below and update the code to test messagesIDMetadataGet
        //instance.messagesIDMetadataGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('messagesIDMetadataPost', function() {
      it('should call messagesIDMetadataPost successfully', function(done) {
        //uncomment below and update the code to test messagesIDMetadataPost
        //instance.messagesIDMetadataPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('messagesMetadataFiltersPost', function() {
      it('should call messagesMetadataFiltersPost successfully', function(done) {
        //uncomment below and update the code to test messagesMetadataFiltersPost
        //instance.messagesMetadataFiltersPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
