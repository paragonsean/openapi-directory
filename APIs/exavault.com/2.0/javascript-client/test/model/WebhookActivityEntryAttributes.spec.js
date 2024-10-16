/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
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
    factory(root.expect, root.ExaVault);
  }
}(this, function(expect, ExaVault) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new ExaVault.WebhookActivityEntryAttributes();
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

  describe('WebhookActivityEntryAttributes', function() {
    it('should create an instance of WebhookActivityEntryAttributes', function() {
      // uncomment below and update the code to test WebhookActivityEntryAttributes
      //var instance = new ExaVault.WebhookActivityEntryAttributes();
      //expect(instance).to.be.a(ExaVault.WebhookActivityEntryAttributes);
    });

    it('should have the property accountId (base name: "accountId")', function() {
      // uncomment below and update the code to test the property accountId
      //var instance = new ExaVault.WebhookActivityEntryAttributes();
      //expect(instance).to.be();
    });

    it('should have the property attemptId (base name: "attemptId")', function() {
      // uncomment below and update the code to test the property attemptId
      //var instance = new ExaVault.WebhookActivityEntryAttributes();
      //expect(instance).to.be();
    });

    it('should have the property created (base name: "created")', function() {
      // uncomment below and update the code to test the property created
      //var instance = new ExaVault.WebhookActivityEntryAttributes();
      //expect(instance).to.be();
    });

    it('should have the property details (base name: "details")', function() {
      // uncomment below and update the code to test the property details
      //var instance = new ExaVault.WebhookActivityEntryAttributes();
      //expect(instance).to.be();
    });

    it('should have the property endpointUrl (base name: "endpointUrl")', function() {
      // uncomment below and update the code to test the property endpointUrl
      //var instance = new ExaVault.WebhookActivityEntryAttributes();
      //expect(instance).to.be();
    });

    it('should have the property event (base name: "event")', function() {
      // uncomment below and update the code to test the property event
      //var instance = new ExaVault.WebhookActivityEntryAttributes();
      //expect(instance).to.be();
    });

    it('should have the property ipAddress (base name: "ipAddress")', function() {
      // uncomment below and update the code to test the property ipAddress
      //var instance = new ExaVault.WebhookActivityEntryAttributes();
      //expect(instance).to.be();
    });

    it('should have the property resend (base name: "resend")', function() {
      // uncomment below and update the code to test the property resend
      //var instance = new ExaVault.WebhookActivityEntryAttributes();
      //expect(instance).to.be();
    });

    it('should have the property resourcePath (base name: "resourcePath")', function() {
      // uncomment below and update the code to test the property resourcePath
      //var instance = new ExaVault.WebhookActivityEntryAttributes();
      //expect(instance).to.be();
    });

    it('should have the property response (base name: "response")', function() {
      // uncomment below and update the code to test the property response
      //var instance = new ExaVault.WebhookActivityEntryAttributes();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new ExaVault.WebhookActivityEntryAttributes();
      //expect(instance).to.be();
    });

    it('should have the property username (base name: "username")', function() {
      // uncomment below and update the code to test the property username
      //var instance = new ExaVault.WebhookActivityEntryAttributes();
      //expect(instance).to.be();
    });

    it('should have the property webhookFormat (base name: "webhookFormat")', function() {
      // uncomment below and update the code to test the property webhookFormat
      //var instance = new ExaVault.WebhookActivityEntryAttributes();
      //expect(instance).to.be();
    });

    it('should have the property webhookId (base name: "webhookId")', function() {
      // uncomment below and update the code to test the property webhookId
      //var instance = new ExaVault.WebhookActivityEntryAttributes();
      //expect(instance).to.be();
    });

    it('should have the property webhookPath (base name: "webhookPath")', function() {
      // uncomment below and update the code to test the property webhookPath
      //var instance = new ExaVault.WebhookActivityEntryAttributes();
      //expect(instance).to.be();
    });

  });

}));
