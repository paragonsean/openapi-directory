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
    instance = new StorSimple8000SeriesManagementClient.AccessControlRecordProperties();
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

  describe('AccessControlRecordProperties', function() {
    it('should create an instance of AccessControlRecordProperties', function() {
      // uncomment below and update the code to test AccessControlRecordProperties
      //var instance = new StorSimple8000SeriesManagementClient.AccessControlRecordProperties();
      //expect(instance).to.be.a(StorSimple8000SeriesManagementClient.AccessControlRecordProperties);
    });

    it('should have the property initiatorName (base name: "initiatorName")', function() {
      // uncomment below and update the code to test the property initiatorName
      //var instance = new StorSimple8000SeriesManagementClient.AccessControlRecordProperties();
      //expect(instance).to.be();
    });

    it('should have the property volumeCount (base name: "volumeCount")', function() {
      // uncomment below and update the code to test the property volumeCount
      //var instance = new StorSimple8000SeriesManagementClient.AccessControlRecordProperties();
      //expect(instance).to.be();
    });

  });

}));
