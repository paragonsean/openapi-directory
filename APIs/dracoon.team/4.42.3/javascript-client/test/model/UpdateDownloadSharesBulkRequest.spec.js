/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
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
    factory(root.expect, root.DracoonApi);
  }
}(this, function(expect, DracoonApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new DracoonApi.UpdateDownloadSharesBulkRequest();
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

  describe('UpdateDownloadSharesBulkRequest', function() {
    it('should create an instance of UpdateDownloadSharesBulkRequest', function() {
      // uncomment below and update the code to test UpdateDownloadSharesBulkRequest
      //var instance = new DracoonApi.UpdateDownloadSharesBulkRequest();
      //expect(instance).to.be.a(DracoonApi.UpdateDownloadSharesBulkRequest);
    });

    it('should have the property expiration (base name: "expiration")', function() {
      // uncomment below and update the code to test the property expiration
      //var instance = new DracoonApi.UpdateDownloadSharesBulkRequest();
      //expect(instance).to.be();
    });

    it('should have the property maxDownloads (base name: "maxDownloads")', function() {
      // uncomment below and update the code to test the property maxDownloads
      //var instance = new DracoonApi.UpdateDownloadSharesBulkRequest();
      //expect(instance).to.be();
    });

    it('should have the property objectIds (base name: "objectIds")', function() {
      // uncomment below and update the code to test the property objectIds
      //var instance = new DracoonApi.UpdateDownloadSharesBulkRequest();
      //expect(instance).to.be();
    });

    it('should have the property resetMaxDownloads (base name: "resetMaxDownloads")', function() {
      // uncomment below and update the code to test the property resetMaxDownloads
      //var instance = new DracoonApi.UpdateDownloadSharesBulkRequest();
      //expect(instance).to.be();
    });

    it('should have the property showCreatorName (base name: "showCreatorName")', function() {
      // uncomment below and update the code to test the property showCreatorName
      //var instance = new DracoonApi.UpdateDownloadSharesBulkRequest();
      //expect(instance).to.be();
    });

    it('should have the property showCreatorUsername (base name: "showCreatorUsername")', function() {
      // uncomment below and update the code to test the property showCreatorUsername
      //var instance = new DracoonApi.UpdateDownloadSharesBulkRequest();
      //expect(instance).to.be();
    });

  });

}));
