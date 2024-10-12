/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on who is going to receive notifications associated with your Azure API Management deployment.
 *
 * The version of the OpenAPI document: 2019-12-01-preview
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
    instance = new ApiManagementClient.NotificationRecipientUserListByNotification200Response();
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

  describe('NotificationRecipientUserListByNotification200Response', function() {
    it('should create an instance of NotificationRecipientUserListByNotification200Response', function() {
      // uncomment below and update the code to test NotificationRecipientUserListByNotification200Response
      //var instance = new ApiManagementClient.NotificationRecipientUserListByNotification200Response();
      //expect(instance).to.be.a(ApiManagementClient.NotificationRecipientUserListByNotification200Response);
    });

    it('should have the property nextLink (base name: "nextLink")', function() {
      // uncomment below and update the code to test the property nextLink
      //var instance = new ApiManagementClient.NotificationRecipientUserListByNotification200Response();
      //expect(instance).to.be();
    });

    it('should have the property value (base name: "value")', function() {
      // uncomment below and update the code to test the property value
      //var instance = new ApiManagementClient.NotificationRecipientUserListByNotification200Response();
      //expect(instance).to.be();
    });

  });

}));
