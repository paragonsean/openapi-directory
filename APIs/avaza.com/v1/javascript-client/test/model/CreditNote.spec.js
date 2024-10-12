/**
 * Avaza API Documentation
 * Welcome to the autogenerated documentation & test tool for Avaza's API. <br/><br/><strong>API Security & Authentication</strong><br/>Authentication options include OAuth2 Implicit and Authorization Code flows, and Personal Access Token. All connections should be encrypted over SSL/TLS <br/><br/>You can set up and manage your api authentication credentials from within your Avaza account. (requires Administrator permissions on your Avaza account).<br/><br/> OAuth2 Authorization endpoint: https://any.avaza.com/oauth2/authorize  <br/>OAuth2 Token endpoint: https://any.avaza.com/oauth2/token<br/>Base URL for subsequent API Requests: https://api.avaza.com/ <br/><br/>Blogpost about authenticating with Avaza's API:  https://www.avaza.com/avaza-api-oauth2-authentication/ <br/>Blogpost on using Avaza's webhooks: https://www.avaza.com/avaza-api-webhook-notifications/<br/>The OAuth flow currently issues Access Tokens that last 1 day, and Refresh tokens that last 180 days<br/>The Api respects the security Roles assigned to the authenticating Avaza user and filters the data return appropriately. <br/><br><strong>Support</strong><br/>For API Support, and to request access please contact Avaza Support Team via our support chat. <br/><br/><strong>User Contributed Libraries:</strong><br/>Graciously contributed by 3rd party users like you. <br/>Note these are not tested or endorsesd by Avaza. We encourage you to review before use, and use at own risk.<br/> <ul><li> - <a target='blank' href='https://packagist.org/packages/debiprasad/oauth2-avaza'>PHP OAuth Client Package for Azava API (by Debiprasad Sahoo)</a></li></ul>
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
    factory(root.expect, root.AvazaApiDocumentation);
  }
}(this, function(expect, AvazaApiDocumentation) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AvazaApiDocumentation.CreditNote();
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

  describe('CreditNote', function() {
    it('should create an instance of CreditNote', function() {
      // uncomment below and update the code to test CreditNote
      //var instance = new AvazaApiDocumentation.CreditNote();
      //expect(instance).to.be.a(AvazaApiDocumentation.CreditNote);
    });

    it('should have the property balance (base name: "Balance")', function() {
      // uncomment below and update the code to test the property balance
      //var instance = new AvazaApiDocumentation.CreditNote();
      //expect(instance).to.be();
    });

    it('should have the property creditNoteAllocations (base name: "CreditNoteAllocations")', function() {
      // uncomment below and update the code to test the property creditNoteAllocations
      //var instance = new AvazaApiDocumentation.CreditNote();
      //expect(instance).to.be();
    });

    it('should have the property creditNoteLineItems (base name: "CreditNoteLineItems")', function() {
      // uncomment below and update the code to test the property creditNoteLineItems
      //var instance = new AvazaApiDocumentation.CreditNote();
      //expect(instance).to.be();
    });

    it('should have the property creditNoteNumber (base name: "CreditNoteNumber")', function() {
      // uncomment below and update the code to test the property creditNoteNumber
      //var instance = new AvazaApiDocumentation.CreditNote();
      //expect(instance).to.be();
    });

    it('should have the property currencyCode (base name: "CurrencyCode")', function() {
      // uncomment below and update the code to test the property currencyCode
      //var instance = new AvazaApiDocumentation.CreditNote();
      //expect(instance).to.be();
    });

    it('should have the property customerIDFK (base name: "CustomerIDFK")', function() {
      // uncomment below and update the code to test the property customerIDFK
      //var instance = new AvazaApiDocumentation.CreditNote();
      //expect(instance).to.be();
    });

    it('should have the property dateCreated (base name: "DateCreated")', function() {
      // uncomment below and update the code to test the property dateCreated
      //var instance = new AvazaApiDocumentation.CreditNote();
      //expect(instance).to.be();
    });

    it('should have the property dateIssued (base name: "DateIssued")', function() {
      // uncomment below and update the code to test the property dateIssued
      //var instance = new AvazaApiDocumentation.CreditNote();
      //expect(instance).to.be();
    });

    it('should have the property dateUpdated (base name: "DateUpdated")', function() {
      // uncomment below and update the code to test the property dateUpdated
      //var instance = new AvazaApiDocumentation.CreditNote();
      //expect(instance).to.be();
    });

    it('should have the property notes (base name: "Notes")', function() {
      // uncomment below and update the code to test the property notes
      //var instance = new AvazaApiDocumentation.CreditNote();
      //expect(instance).to.be();
    });

    it('should have the property totalAmount (base name: "TotalAmount")', function() {
      // uncomment below and update the code to test the property totalAmount
      //var instance = new AvazaApiDocumentation.CreditNote();
      //expect(instance).to.be();
    });

    it('should have the property transactionID (base name: "TransactionID")', function() {
      // uncomment below and update the code to test the property transactionID
      //var instance = new AvazaApiDocumentation.CreditNote();
      //expect(instance).to.be();
    });

    it('should have the property transactionPrefix (base name: "TransactionPrefix")', function() {
      // uncomment below and update the code to test the property transactionPrefix
      //var instance = new AvazaApiDocumentation.CreditNote();
      //expect(instance).to.be();
    });

    it('should have the property transactionStatusCode (base name: "TransactionStatusCode")', function() {
      // uncomment below and update the code to test the property transactionStatusCode
      //var instance = new AvazaApiDocumentation.CreditNote();
      //expect(instance).to.be();
    });

  });

}));
