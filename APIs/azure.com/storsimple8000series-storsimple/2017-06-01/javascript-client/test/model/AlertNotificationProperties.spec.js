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
    instance = new StorSimple8000SeriesManagementClient.AlertNotificationProperties();
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

  describe('AlertNotificationProperties', function() {
    it('should create an instance of AlertNotificationProperties', function() {
      // uncomment below and update the code to test AlertNotificationProperties
      //var instance = new StorSimple8000SeriesManagementClient.AlertNotificationProperties();
      //expect(instance).to.be.a(StorSimple8000SeriesManagementClient.AlertNotificationProperties);
    });

    it('should have the property additionalRecipientEmailList (base name: "additionalRecipientEmailList")', function() {
      // uncomment below and update the code to test the property additionalRecipientEmailList
      //var instance = new StorSimple8000SeriesManagementClient.AlertNotificationProperties();
      //expect(instance).to.be();
    });

    it('should have the property alertNotificationCulture (base name: "alertNotificationCulture")', function() {
      // uncomment below and update the code to test the property alertNotificationCulture
      //var instance = new StorSimple8000SeriesManagementClient.AlertNotificationProperties();
      //expect(instance).to.be();
    });

    it('should have the property emailNotification (base name: "emailNotification")', function() {
      // uncomment below and update the code to test the property emailNotification
      //var instance = new StorSimple8000SeriesManagementClient.AlertNotificationProperties();
      //expect(instance).to.be();
    });

    it('should have the property notificationToServiceOwners (base name: "notificationToServiceOwners")', function() {
      // uncomment below and update the code to test the property notificationToServiceOwners
      //var instance = new StorSimple8000SeriesManagementClient.AlertNotificationProperties();
      //expect(instance).to.be();
    });

  });

}));
