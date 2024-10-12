/**
 * Storage Cache Mgmt Client
 * A Storage Cache provides scalable caching service for NAS clients, serving data from either NFSv3 or Blob at-rest storage (referred to as \"Storage Targets\"). These operations allow you to manage caches.
 *
 * The version of the OpenAPI document: 2019-08-01-preview
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
    instance = new StorageCacheMgmtClient.ResourceSku();
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

  describe('ResourceSku', function() {
    it('should create an instance of ResourceSku', function() {
      // uncomment below and update the code to test ResourceSku
      //var instance = new StorageCacheMgmtClient.ResourceSku();
      //expect(instance).to.be.a(StorageCacheMgmtClient.ResourceSku);
    });

    it('should have the property capabilities (base name: "capabilities")', function() {
      // uncomment below and update the code to test the property capabilities
      //var instance = new StorageCacheMgmtClient.ResourceSku();
      //expect(instance).to.be();
    });

    it('should have the property locationInfo (base name: "locationInfo")', function() {
      // uncomment below and update the code to test the property locationInfo
      //var instance = new StorageCacheMgmtClient.ResourceSku();
      //expect(instance).to.be();
    });

    it('should have the property locations (base name: "locations")', function() {
      // uncomment below and update the code to test the property locations
      //var instance = new StorageCacheMgmtClient.ResourceSku();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new StorageCacheMgmtClient.ResourceSku();
      //expect(instance).to.be();
    });

    it('should have the property resourceType (base name: "resourceType")', function() {
      // uncomment below and update the code to test the property resourceType
      //var instance = new StorageCacheMgmtClient.ResourceSku();
      //expect(instance).to.be();
    });

    it('should have the property restrictions (base name: "restrictions")', function() {
      // uncomment below and update the code to test the property restrictions
      //var instance = new StorageCacheMgmtClient.ResourceSku();
      //expect(instance).to.be();
    });

  });

}));
