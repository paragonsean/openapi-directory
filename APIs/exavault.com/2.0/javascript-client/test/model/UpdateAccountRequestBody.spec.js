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
    instance = new ExaVault.UpdateAccountRequestBody();
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

  describe('UpdateAccountRequestBody', function() {
    it('should create an instance of UpdateAccountRequestBody', function() {
      // uncomment below and update the code to test UpdateAccountRequestBody
      //var instance = new ExaVault.UpdateAccountRequestBody();
      //expect(instance).to.be.a(ExaVault.UpdateAccountRequestBody);
    });

    it('should have the property accountOnboarding (base name: "accountOnboarding")', function() {
      // uncomment below and update the code to test the property accountOnboarding
      //var instance = new ExaVault.UpdateAccountRequestBody();
      //expect(instance).to.be();
    });

    it('should have the property allowedIpRanges (base name: "allowedIpRanges")', function() {
      // uncomment below and update the code to test the property allowedIpRanges
      //var instance = new ExaVault.UpdateAccountRequestBody();
      //expect(instance).to.be();
    });

    it('should have the property brandingSettings (base name: "brandingSettings")', function() {
      // uncomment below and update the code to test the property brandingSettings
      //var instance = new ExaVault.UpdateAccountRequestBody();
      //expect(instance).to.be();
    });

    it('should have the property complexPasswords (base name: "complexPasswords")', function() {
      // uncomment below and update the code to test the property complexPasswords
      //var instance = new ExaVault.UpdateAccountRequestBody();
      //expect(instance).to.be();
    });

    it('should have the property customSignature (base name: "customSignature")', function() {
      // uncomment below and update the code to test the property customSignature
      //var instance = new ExaVault.UpdateAccountRequestBody();
      //expect(instance).to.be();
    });

    it('should have the property emailContent (base name: "emailContent")', function() {
      // uncomment below and update the code to test the property emailContent
      //var instance = new ExaVault.UpdateAccountRequestBody();
      //expect(instance).to.be();
    });

    it('should have the property emailSubject (base name: "emailSubject")', function() {
      // uncomment below and update the code to test the property emailSubject
      //var instance = new ExaVault.UpdateAccountRequestBody();
      //expect(instance).to.be();
    });

    it('should have the property externalDomain (base name: "externalDomain")', function() {
      // uncomment below and update the code to test the property externalDomain
      //var instance = new ExaVault.UpdateAccountRequestBody();
      //expect(instance).to.be();
    });

    it('should have the property quota (base name: "quota")', function() {
      // uncomment below and update the code to test the property quota
      //var instance = new ExaVault.UpdateAccountRequestBody();
      //expect(instance).to.be();
    });

    it('should have the property secureOnly (base name: "secureOnly")', function() {
      // uncomment below and update the code to test the property secureOnly
      //var instance = new ExaVault.UpdateAccountRequestBody();
      //expect(instance).to.be();
    });

    it('should have the property showReferralLinks (base name: "showReferralLinks")', function() {
      // uncomment below and update the code to test the property showReferralLinks
      //var instance = new ExaVault.UpdateAccountRequestBody();
      //expect(instance).to.be();
    });

  });

}));
