/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
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
    factory(root.expect, root.StorSimple8000SeriesManagementClient);
  }
}(this, function(expect, StorSimple8000SeriesManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new StorSimple8000SeriesManagementClient.AccessControlRecordsApi();
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

  describe('AccessControlRecordsApi', function() {
    describe('accessControlRecordsCreateOrUpdate', function() {
      it('should call accessControlRecordsCreateOrUpdate successfully', function(done) {
        //uncomment below and update the code to test accessControlRecordsCreateOrUpdate
        //instance.accessControlRecordsCreateOrUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('accessControlRecordsDelete', function() {
      it('should call accessControlRecordsDelete successfully', function(done) {
        //uncomment below and update the code to test accessControlRecordsDelete
        //instance.accessControlRecordsDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('accessControlRecordsGet', function() {
      it('should call accessControlRecordsGet successfully', function(done) {
        //uncomment below and update the code to test accessControlRecordsGet
        //instance.accessControlRecordsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('accessControlRecordsListByManager', function() {
      it('should call accessControlRecordsListByManager successfully', function(done) {
        //uncomment below and update the code to test accessControlRecordsListByManager
        //instance.accessControlRecordsListByManager(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
