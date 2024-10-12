/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on who is going to receive notifications associated with your Azure API Management deployment.
 *
 * The version of the OpenAPI document: 2018-01-01
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
    instance = new ApiManagementClient.NotificationRecipientUserApi();
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

  describe('NotificationRecipientUserApi', function() {
    describe('notificationRecipientUserCheckEntityExists', function() {
      it('should call notificationRecipientUserCheckEntityExists successfully', function(done) {
        //uncomment below and update the code to test notificationRecipientUserCheckEntityExists
        //instance.notificationRecipientUserCheckEntityExists(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('notificationRecipientUserCreateOrUpdate', function() {
      it('should call notificationRecipientUserCreateOrUpdate successfully', function(done) {
        //uncomment below and update the code to test notificationRecipientUserCreateOrUpdate
        //instance.notificationRecipientUserCreateOrUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('notificationRecipientUserDelete', function() {
      it('should call notificationRecipientUserDelete successfully', function(done) {
        //uncomment below and update the code to test notificationRecipientUserDelete
        //instance.notificationRecipientUserDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
