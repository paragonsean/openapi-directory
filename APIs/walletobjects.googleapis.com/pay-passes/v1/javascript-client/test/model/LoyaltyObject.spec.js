/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
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
    factory(root.expect, root.GooglePayPassesApi);
  }
}(this, function(expect, GooglePayPassesApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new GooglePayPassesApi.LoyaltyObject();
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

  describe('LoyaltyObject', function() {
    it('should create an instance of LoyaltyObject', function() {
      // uncomment below and update the code to test LoyaltyObject
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be.a(GooglePayPassesApi.LoyaltyObject);
    });

    it('should have the property accountId (base name: "accountId")', function() {
      // uncomment below and update the code to test the property accountId
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

    it('should have the property accountName (base name: "accountName")', function() {
      // uncomment below and update the code to test the property accountName
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

    it('should have the property appLinkData (base name: "appLinkData")', function() {
      // uncomment below and update the code to test the property appLinkData
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

    it('should have the property barcode (base name: "barcode")', function() {
      // uncomment below and update the code to test the property barcode
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

    it('should have the property classId (base name: "classId")', function() {
      // uncomment below and update the code to test the property classId
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

    it('should have the property classReference (base name: "classReference")', function() {
      // uncomment below and update the code to test the property classReference
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

    it('should have the property disableExpirationNotification (base name: "disableExpirationNotification")', function() {
      // uncomment below and update the code to test the property disableExpirationNotification
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

    it('should have the property groupingInfo (base name: "groupingInfo")', function() {
      // uncomment below and update the code to test the property groupingInfo
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

    it('should have the property hasLinkedDevice (base name: "hasLinkedDevice")', function() {
      // uncomment below and update the code to test the property hasLinkedDevice
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

    it('should have the property hasUsers (base name: "hasUsers")', function() {
      // uncomment below and update the code to test the property hasUsers
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

    it('should have the property heroImage (base name: "heroImage")', function() {
      // uncomment below and update the code to test the property heroImage
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

    it('should have the property imageModulesData (base name: "imageModulesData")', function() {
      // uncomment below and update the code to test the property imageModulesData
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

    it('should have the property infoModuleData (base name: "infoModuleData")', function() {
      // uncomment below and update the code to test the property infoModuleData
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

    it('should have the property kind (base name: "kind")', function() {
      // uncomment below and update the code to test the property kind
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

    it('should have the property linkedOfferIds (base name: "linkedOfferIds")', function() {
      // uncomment below and update the code to test the property linkedOfferIds
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

    it('should have the property linksModuleData (base name: "linksModuleData")', function() {
      // uncomment below and update the code to test the property linksModuleData
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

    it('should have the property locations (base name: "locations")', function() {
      // uncomment below and update the code to test the property locations
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

    it('should have the property loyaltyPoints (base name: "loyaltyPoints")', function() {
      // uncomment below and update the code to test the property loyaltyPoints
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

    it('should have the property messages (base name: "messages")', function() {
      // uncomment below and update the code to test the property messages
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

    it('should have the property passConstraints (base name: "passConstraints")', function() {
      // uncomment below and update the code to test the property passConstraints
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

    it('should have the property rotatingBarcode (base name: "rotatingBarcode")', function() {
      // uncomment below and update the code to test the property rotatingBarcode
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

    it('should have the property secondaryLoyaltyPoints (base name: "secondaryLoyaltyPoints")', function() {
      // uncomment below and update the code to test the property secondaryLoyaltyPoints
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

    it('should have the property smartTapRedemptionValue (base name: "smartTapRedemptionValue")', function() {
      // uncomment below and update the code to test the property smartTapRedemptionValue
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

    it('should have the property state (base name: "state")', function() {
      // uncomment below and update the code to test the property state
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

    it('should have the property textModulesData (base name: "textModulesData")', function() {
      // uncomment below and update the code to test the property textModulesData
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

    it('should have the property validTimeInterval (base name: "validTimeInterval")', function() {
      // uncomment below and update the code to test the property validTimeInterval
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

    it('should have the property version (base name: "version")', function() {
      // uncomment below and update the code to test the property version
      //var instance = new GooglePayPassesApi.LoyaltyObject();
      //expect(instance).to.be();
    });

  });

}));
