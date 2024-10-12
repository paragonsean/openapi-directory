/**
 * API v1.0.0
 * [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/80638214aa04722c9203)  <span style='margin-left: 0.5em;'>or</span>  <a href='https://documenter.getpostman.com/view/3559821/TVeqcn2L' class='openapi-button' _ngcontent-c6>View Postman docs</a>    # Quickstart    Visit [github](https://github.com/EmitKnowledge/Envoice) to view the quickstart tutorial.    <div class='postman-tutorial'>    # Tutorial for running the API in postman    Click on \"\"Run in Postman\"\" button  <br /><br />  ![postman - tutorial - 1](/Assets/images/api/postman-tutorial/postman-tutorial-1.png)     ---     A new page will open.  Click the \"\"Postman for windows\"\" to run postman as a desktop app.  Make sure you have already [installed](https://www.getpostman.com/docs/postman/launching_postman/installation_and_updates) Postman.  <br /><br />  ![postman - tutorial - 2](/Assets/images/api/postman-tutorial/postman-tutorial-2.png)     ---     In chrome an alert might show up to set a default app for opening postman links. Click on \"\"Open Postman\"\".  <br /><br />  ![postman - tutorial - 3](/Assets/images/api/postman-tutorial/postman-tutorial-3.png)     ---     The OpenAPI specification will be imported in Postman as a new collection named \"\"Envoice api\"\"  <br /><br />  ![postman - tutorial - 4](/Assets/images/api/postman-tutorial/postman-tutorial-4.png)     ---     When testing be sure to check and modify the environment variables to suit your api key and secret. The domain is set to envoice's endpoint so you don't really need to change that.    <sub>\\*Eye button in top right corner </sub>  <br /><br />   ![postman - tutorial - 5](/Assets/images/api/postman-tutorial/postman-tutorial-5.png)  <br /><br />   ![postman - tutorial - 6](/Assets/images/api/postman-tutorial/postman-tutorial-6.png)     ---     You don't need to change the values of the header parameters, because they will be replaced automatically when you send a request with real values from the environment configured in the previous step.  <br /><br />  ![postman - tutorial - 7](/Assets/images/api/postman-tutorial/postman-tutorial-7.png)     ---     Modify the example data to suit your needs and send a request.  <br /><br />  ![postman - tutorial - 8](/Assets/images/api/postman-tutorial/postman-tutorial-8.png)  </div>    # Webhooks    Webhooks allow you to build or set up Envoice Apps which subscribe to invoice activities.   When one of those events is triggered, we'll send a HTTP POST payload to the webhook's configured URL.   Webhooks can be used to update an external invoice data storage.    In order to use webhooks visit [this link](/account/settings#api-tab) and add upto 10 webhook urls that will return status `200` in order to signal that the webhook is working.  All nonworking webhooks will be ignored after a certain period of time and several retry attempts.  If after several attempts the webhook starts to work, we will send you all activities, both past and present, in chronological order.    The payload of the webhook is in format:  ```  {      Signature: \"\"sha256 string\"\",      Timestamp: \"\"YYYY-MM-DDTHH:mm:ss.FFFFFFFZ\"\",      Activity: {          Message: \"string\",          Link: \"share url\",          Type: int,                  InvoiceNumber: \"string\",          InvoiceId: int,                  OrderNumber: \"string\",          OrderId: int,          Id: int,          CreatedOn: \"YYYY-MM-DDTHH:mm:ss.FFFFFFFZ\"      }  }  ```            
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
    factory(root.expect, root.ApiV100);
  }
}(this, function(expect, ApiV100) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new ApiV100.UserSettings();
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

  describe('UserSettings', function() {
    it('should create an instance of UserSettings', function() {
      // uncomment below and update the code to test UserSettings
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be.a(ApiV100.UserSettings);
    });

    it('should have the property accountantEmail (base name: "AccountantEmail")', function() {
      // uncomment below and update the code to test the property accountantEmail
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property address (base name: "Address")', function() {
      // uncomment below and update the code to test the property address
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property apiKey (base name: "ApiKey")', function() {
      // uncomment below and update the code to test the property apiKey
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property apiSecret (base name: "ApiSecret")', function() {
      // uncomment below and update the code to test the property apiSecret
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property backgroundImage (base name: "BackgroundImage")', function() {
      // uncomment below and update the code to test the property backgroundImage
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property bank (base name: "Bank")', function() {
      // uncomment below and update the code to test the property bank
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property bankAccount (base name: "BankAccount")', function() {
      // uncomment below and update the code to test the property bankAccount
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property cname (base name: "Cname")', function() {
      // uncomment below and update the code to test the property cname
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property companyRegistrationNumber (base name: "CompanyRegistrationNumber")', function() {
      // uncomment below and update the code to test the property companyRegistrationNumber
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property country (base name: "Country")', function() {
      // uncomment below and update the code to test the property country
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property countryId (base name: "CountryId")', function() {
      // uncomment below and update the code to test the property countryId
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property currency (base name: "Currency")', function() {
      // uncomment below and update the code to test the property currency
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property currencyId (base name: "CurrencyId")', function() {
      // uncomment below and update the code to test the property currencyId
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property currencySymbol (base name: "CurrencySymbol")', function() {
      // uncomment below and update the code to test the property currencySymbol
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property defaultDateFormat (base name: "DefaultDateFormat")', function() {
      // uncomment below and update the code to test the property defaultDateFormat
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property defaultDueDateInDays (base name: "DefaultDueDateInDays")', function() {
      // uncomment below and update the code to test the property defaultDueDateInDays
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property doNotTrack (base name: "DoNotTrack")', function() {
      // uncomment below and update the code to test the property doNotTrack
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property enableClientPortal (base name: "EnableClientPortal")', function() {
      // uncomment below and update the code to test the property enableClientPortal
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property enablePredictiveInvoicing (base name: "EnablePredictiveInvoicing")', function() {
      // uncomment below and update the code to test the property enablePredictiveInvoicing
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property enableRecurringInvoicing (base name: "EnableRecurringInvoicing")', function() {
      // uncomment below and update the code to test the property enableRecurringInvoicing
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property hasInvoiceLogo (base name: "HasInvoiceLogo")', function() {
      // uncomment below and update the code to test the property hasInvoiceLogo
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property iban (base name: "Iban")', function() {
      // uncomment below and update the code to test the property iban
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "Id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property invoiceTemplate (base name: "InvoiceTemplate")', function() {
      // uncomment below and update the code to test the property invoiceTemplate
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property invoiceTemplateColorHex (base name: "InvoiceTemplateColorHex")', function() {
      // uncomment below and update the code to test the property invoiceTemplateColorHex
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property phoneNumber (base name: "PhoneNumber")', function() {
      // uncomment below and update the code to test the property phoneNumber
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property profession (base name: "Profession")', function() {
      // uncomment below and update the code to test the property profession
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property receiveSmsNotifications (base name: "ReceiveSmsNotifications")', function() {
      // uncomment below and update the code to test the property receiveSmsNotifications
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property referralProgram (base name: "ReferralProgram")', function() {
      // uncomment below and update the code to test the property referralProgram
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property storeCheckoutFields (base name: "StoreCheckoutFields")', function() {
      // uncomment below and update the code to test the property storeCheckoutFields
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property storeColorHex (base name: "StoreColorHex")', function() {
      // uncomment below and update the code to test the property storeColorHex
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property storeCurrency (base name: "StoreCurrency")', function() {
      // uncomment below and update the code to test the property storeCurrency
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property storeCurrencyId (base name: "StoreCurrencyId")', function() {
      // uncomment below and update the code to test the property storeCurrencyId
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property storeCustomJavaScript (base name: "StoreCustomJavaScript")', function() {
      // uncomment below and update the code to test the property storeCustomJavaScript
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property storeDescription (base name: "StoreDescription")', function() {
      // uncomment below and update the code to test the property storeDescription
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property storeEmail (base name: "StoreEmail")', function() {
      // uncomment below and update the code to test the property storeEmail
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property storeLanguage (base name: "StoreLanguage")', function() {
      // uncomment below and update the code to test the property storeLanguage
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property storeLanguageId (base name: "StoreLanguageId")', function() {
      // uncomment below and update the code to test the property storeLanguageId
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property storeName (base name: "StoreName")', function() {
      // uncomment below and update the code to test the property storeName
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property storePurchaseEmailMessage (base name: "StorePurchaseEmailMessage")', function() {
      // uncomment below and update the code to test the property storePurchaseEmailMessage
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property storePurchaseThankYouMessage (base name: "StorePurchaseThankYouMessage")', function() {
      // uncomment below and update the code to test the property storePurchaseThankYouMessage
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property storeTextColorHex (base name: "StoreTextColorHex")', function() {
      // uncomment below and update the code to test the property storeTextColorHex
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property storeUrl (base name: "StoreUrl")', function() {
      // uncomment below and update the code to test the property storeUrl
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property subscribeToProductEmails (base name: "SubscribeToProductEmails")', function() {
      // uncomment below and update the code to test the property subscribeToProductEmails
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property swift (base name: "Swift")', function() {
      // uncomment below and update the code to test the property swift
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property terms (base name: "Terms")', function() {
      // uncomment below and update the code to test the property terms
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property userId (base name: "UserId")', function() {
      // uncomment below and update the code to test the property userId
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property userSignature (base name: "UserSignature")', function() {
      // uncomment below and update the code to test the property userSignature
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property vatNumber (base name: "VatNumber")', function() {
      // uncomment below and update the code to test the property vatNumber
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

    it('should have the property yearsOfExperience (base name: "YearsOfExperience")', function() {
      // uncomment below and update the code to test the property yearsOfExperience
      //var instance = new ApiV100.UserSettings();
      //expect(instance).to.be();
    });

  });

}));
