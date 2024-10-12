/**
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
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
    factory(root.expect, root.DataBoxEdgeManagementClient);
  }
}(this, function(expect, DataBoxEdgeManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new DataBoxEdgeManagementClient.SharesApi();
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

  describe('SharesApi', function() {
    describe('sharesCreateOrUpdate', function() {
      it('should call sharesCreateOrUpdate successfully', function(done) {
        //uncomment below and update the code to test sharesCreateOrUpdate
        //instance.sharesCreateOrUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('sharesDelete', function() {
      it('should call sharesDelete successfully', function(done) {
        //uncomment below and update the code to test sharesDelete
        //instance.sharesDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('sharesGet', function() {
      it('should call sharesGet successfully', function(done) {
        //uncomment below and update the code to test sharesGet
        //instance.sharesGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('sharesListByDataBoxEdgeDevice', function() {
      it('should call sharesListByDataBoxEdgeDevice successfully', function(done) {
        //uncomment below and update the code to test sharesListByDataBoxEdgeDevice
        //instance.sharesListByDataBoxEdgeDevice(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('sharesRefresh', function() {
      it('should call sharesRefresh successfully', function(done) {
        //uncomment below and update the code to test sharesRefresh
        //instance.sharesRefresh(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
