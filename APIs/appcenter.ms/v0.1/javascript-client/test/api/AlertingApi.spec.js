/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
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
    factory(root.expect, root.AppCenterClient);
  }
}(this, function(expect, AppCenterClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AppCenterClient.AlertingApi();
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

  describe('AlertingApi', function() {
    describe('bugTrackerGetRepoIssueFromCrash', function() {
      it('should call bugTrackerGetRepoIssueFromCrash successfully', function(done) {
        //uncomment below and update the code to test bugTrackerGetRepoIssueFromCrash
        //instance.bugTrackerGetRepoIssueFromCrash(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('bugtrackerGetSettings', function() {
      it('should call bugtrackerGetSettings successfully', function(done) {
        //uncomment below and update the code to test bugtrackerGetSettings
        //instance.bugtrackerGetSettings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('notificationsGetAppEmailSettings', function() {
      it('should call notificationsGetAppEmailSettings successfully', function(done) {
        //uncomment below and update the code to test notificationsGetAppEmailSettings
        //instance.notificationsGetAppEmailSettings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('notificationsGetUserEmailSettings', function() {
      it('should call notificationsGetUserEmailSettings successfully', function(done) {
        //uncomment below and update the code to test notificationsGetUserEmailSettings
        //instance.notificationsGetUserEmailSettings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('webhooksList', function() {
      it('should call webhooksList successfully', function(done) {
        //uncomment below and update the code to test webhooksList
        //instance.webhooksList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
