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
    instance = new GooglePayPassesApi.GiftCardClass();
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

  describe('GiftCardClass', function() {
    it('should create an instance of GiftCardClass', function() {
      // uncomment below and update the code to test GiftCardClass
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be.a(GooglePayPassesApi.GiftCardClass);
    });

    it('should have the property allowBarcodeRedemption (base name: "allowBarcodeRedemption")', function() {
      // uncomment below and update the code to test the property allowBarcodeRedemption
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property allowMultipleUsersPerObject (base name: "allowMultipleUsersPerObject")', function() {
      // uncomment below and update the code to test the property allowMultipleUsersPerObject
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property callbackOptions (base name: "callbackOptions")', function() {
      // uncomment below and update the code to test the property callbackOptions
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property cardNumberLabel (base name: "cardNumberLabel")', function() {
      // uncomment below and update the code to test the property cardNumberLabel
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property classTemplateInfo (base name: "classTemplateInfo")', function() {
      // uncomment below and update the code to test the property classTemplateInfo
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property countryCode (base name: "countryCode")', function() {
      // uncomment below and update the code to test the property countryCode
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property enableSmartTap (base name: "enableSmartTap")', function() {
      // uncomment below and update the code to test the property enableSmartTap
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property eventNumberLabel (base name: "eventNumberLabel")', function() {
      // uncomment below and update the code to test the property eventNumberLabel
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property heroImage (base name: "heroImage")', function() {
      // uncomment below and update the code to test the property heroImage
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property hexBackgroundColor (base name: "hexBackgroundColor")', function() {
      // uncomment below and update the code to test the property hexBackgroundColor
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property homepageUri (base name: "homepageUri")', function() {
      // uncomment below and update the code to test the property homepageUri
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property imageModulesData (base name: "imageModulesData")', function() {
      // uncomment below and update the code to test the property imageModulesData
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property infoModuleData (base name: "infoModuleData")', function() {
      // uncomment below and update the code to test the property infoModuleData
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property issuerName (base name: "issuerName")', function() {
      // uncomment below and update the code to test the property issuerName
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property kind (base name: "kind")', function() {
      // uncomment below and update the code to test the property kind
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property linksModuleData (base name: "linksModuleData")', function() {
      // uncomment below and update the code to test the property linksModuleData
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property localizedCardNumberLabel (base name: "localizedCardNumberLabel")', function() {
      // uncomment below and update the code to test the property localizedCardNumberLabel
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property localizedEventNumberLabel (base name: "localizedEventNumberLabel")', function() {
      // uncomment below and update the code to test the property localizedEventNumberLabel
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property localizedIssuerName (base name: "localizedIssuerName")', function() {
      // uncomment below and update the code to test the property localizedIssuerName
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property localizedMerchantName (base name: "localizedMerchantName")', function() {
      // uncomment below and update the code to test the property localizedMerchantName
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property localizedPinLabel (base name: "localizedPinLabel")', function() {
      // uncomment below and update the code to test the property localizedPinLabel
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property locations (base name: "locations")', function() {
      // uncomment below and update the code to test the property locations
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property merchantName (base name: "merchantName")', function() {
      // uncomment below and update the code to test the property merchantName
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property messages (base name: "messages")', function() {
      // uncomment below and update the code to test the property messages
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property multipleDevicesAndHoldersAllowedStatus (base name: "multipleDevicesAndHoldersAllowedStatus")', function() {
      // uncomment below and update the code to test the property multipleDevicesAndHoldersAllowedStatus
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property pinLabel (base name: "pinLabel")', function() {
      // uncomment below and update the code to test the property pinLabel
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property programLogo (base name: "programLogo")', function() {
      // uncomment below and update the code to test the property programLogo
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property redemptionIssuers (base name: "redemptionIssuers")', function() {
      // uncomment below and update the code to test the property redemptionIssuers
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property review (base name: "review")', function() {
      // uncomment below and update the code to test the property review
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property reviewStatus (base name: "reviewStatus")', function() {
      // uncomment below and update the code to test the property reviewStatus
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property securityAnimation (base name: "securityAnimation")', function() {
      // uncomment below and update the code to test the property securityAnimation
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property textModulesData (base name: "textModulesData")', function() {
      // uncomment below and update the code to test the property textModulesData
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property version (base name: "version")', function() {
      // uncomment below and update the code to test the property version
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property viewUnlockRequirement (base name: "viewUnlockRequirement")', function() {
      // uncomment below and update the code to test the property viewUnlockRequirement
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

    it('should have the property wordMark (base name: "wordMark")', function() {
      // uncomment below and update the code to test the property wordMark
      //var instance = new GooglePayPassesApi.GiftCardClass();
      //expect(instance).to.be();
    });

  });

}));
