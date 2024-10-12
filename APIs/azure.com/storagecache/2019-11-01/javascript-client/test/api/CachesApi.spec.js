/**
 * Storage Cache Mgmt Client
 * A Storage Cache provides scalable caching service for NAS clients, serving data from either NFSv3 or Blob at-rest storage (referred to as \"Storage Targets\"). These operations allow you to manage Caches.
 *
 * The version of the OpenAPI document: 2019-11-01
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
    factory(root.expect, root.StorageCacheMgmtClient);
  }
}(this, function(expect, StorageCacheMgmtClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new StorageCacheMgmtClient.CachesApi();
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

  describe('CachesApi', function() {
    describe('cachesCreateOrUpdate', function() {
      it('should call cachesCreateOrUpdate successfully', function(done) {
        //uncomment below and update the code to test cachesCreateOrUpdate
        //instance.cachesCreateOrUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('cachesDelete', function() {
      it('should call cachesDelete successfully', function(done) {
        //uncomment below and update the code to test cachesDelete
        //instance.cachesDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('cachesFlush', function() {
      it('should call cachesFlush successfully', function(done) {
        //uncomment below and update the code to test cachesFlush
        //instance.cachesFlush(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('cachesGet', function() {
      it('should call cachesGet successfully', function(done) {
        //uncomment below and update the code to test cachesGet
        //instance.cachesGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('cachesList', function() {
      it('should call cachesList successfully', function(done) {
        //uncomment below and update the code to test cachesList
        //instance.cachesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('cachesListByResourceGroup', function() {
      it('should call cachesListByResourceGroup successfully', function(done) {
        //uncomment below and update the code to test cachesListByResourceGroup
        //instance.cachesListByResourceGroup(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('cachesStart', function() {
      it('should call cachesStart successfully', function(done) {
        //uncomment below and update the code to test cachesStart
        //instance.cachesStart(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('cachesStop', function() {
      it('should call cachesStop successfully', function(done) {
        //uncomment below and update the code to test cachesStop
        //instance.cachesStop(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('cachesUpdate', function() {
      it('should call cachesUpdate successfully', function(done) {
        //uncomment below and update the code to test cachesUpdate
        //instance.cachesUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('cachesUpgradeFirmware', function() {
      it('should call cachesUpgradeFirmware successfully', function(done) {
        //uncomment below and update the code to test cachesUpgradeFirmware
        //instance.cachesUpgradeFirmware(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
