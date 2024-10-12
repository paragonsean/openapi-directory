/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on the ApiVersionSet entity associated with your Azure API Management deployment. Using this entity you create and manage API Version Sets that are used to group APIs for consistent versioning.
 *
 * The version of the OpenAPI document: 2018-06-01-preview
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
    factory(root.expect, root.ApiManagementClient);
  }
}(this, function(expect, ApiManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new ApiManagementClient.ApiVersionSetsApi();
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

  describe('ApiVersionSetsApi', function() {
    describe('apiVersionSetCreateOrUpdate', function() {
      it('should call apiVersionSetCreateOrUpdate successfully', function(done) {
        //uncomment below and update the code to test apiVersionSetCreateOrUpdate
        //instance.apiVersionSetCreateOrUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('apiVersionSetDelete', function() {
      it('should call apiVersionSetDelete successfully', function(done) {
        //uncomment below and update the code to test apiVersionSetDelete
        //instance.apiVersionSetDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('apiVersionSetGet', function() {
      it('should call apiVersionSetGet successfully', function(done) {
        //uncomment below and update the code to test apiVersionSetGet
        //instance.apiVersionSetGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('apiVersionSetGetEntityTag', function() {
      it('should call apiVersionSetGetEntityTag successfully', function(done) {
        //uncomment below and update the code to test apiVersionSetGetEntityTag
        //instance.apiVersionSetGetEntityTag(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('apiVersionSetListByService', function() {
      it('should call apiVersionSetListByService successfully', function(done) {
        //uncomment below and update the code to test apiVersionSetListByService
        //instance.apiVersionSetListByService(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('apiVersionSetUpdate', function() {
      it('should call apiVersionSetUpdate successfully', function(done) {
        //uncomment below and update the code to test apiVersionSetUpdate
        //instance.apiVersionSetUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
