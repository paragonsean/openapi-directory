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
    instance = new ApiManagementClient.NotificationRecipientEmailApi();
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

  describe('NotificationRecipientEmailApi', function() {
    describe('notificationRecipientEmailCheckEntityExists', function() {
      it('should call notificationRecipientEmailCheckEntityExists successfully', function(done) {
        //uncomment below and update the code to test notificationRecipientEmailCheckEntityExists
        //instance.notificationRecipientEmailCheckEntityExists(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('notificationRecipientEmailCreateOrUpdate', function() {
      it('should call notificationRecipientEmailCreateOrUpdate successfully', function(done) {
        //uncomment below and update the code to test notificationRecipientEmailCreateOrUpdate
        //instance.notificationRecipientEmailCreateOrUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('notificationRecipientEmailDelete', function() {
      it('should call notificationRecipientEmailDelete successfully', function(done) {
        //uncomment below and update the code to test notificationRecipientEmailDelete
        //instance.notificationRecipientEmailDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('notificationRecipientEmailListByNotification', function() {
      it('should call notificationRecipientEmailListByNotification successfully', function(done) {
        //uncomment below and update the code to test notificationRecipientEmailListByNotification
        //instance.notificationRecipientEmailListByNotification(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
