/**
 * Checkout API
 * >ℹ️ Check the new [Checkout onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/checkout-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about the Checkout and is organized by focusing on the developer's journey.    The Checkout API allows you to obtain and configure information about the shopping cart and its attachments, personalization of custom fields, orderForm structure, fulfillment data, order management, and identification of the sellers delivery region.    >ℹ️ Data modification operations (`POST`, `PATCH`, `PUT` or `DELETE` endpoints) shall not be performed in parallel in the Checkout APIs. They need to be enqueued by the client/requester. Otherwise, old values ​​can be overwritten incorrectly or competition errors may occur.    >⚠️ All endpoints that consult or edit the orderForm can change the authentication depending on the customer context. If you are handling information from a customer with a complete profile on the store, authentication will be required. You can only access or modify the customer data for these profiles with an authenticated request.    ## Shopping cart    Allows merchants to simulate, configure and customize shopping cart information.    - [POST - Cart Simulation](https://developers.vtex.com/vtex-rest-api/reference/cartsimulation)  - [GET - Get current or create a new cart](https://developers.vtex.com/vtex-rest-api/reference/createanewcart)  - [GET - Get cart information by ID](https://developers.vtex.com/vtex-rest-api/reference/getcartinformationbyid)  - [POST - Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems)  - [GET - Remove all personal data](https://developers.vtex.com/vtex-rest-api/reference/removeallpersonaldata)  - [POST - Update cart items](https://developers.vtex.com/vtex-rest-api/reference/itemsupdate)  - [POST - Add cart items](https://developers.vtex.com/vtex-rest-api/reference/items)  - [PUT - Change price](https://developers.vtex.com/vtex-rest-api/reference/pricechange)  - [PATCH - Ignore profile data](https://developers.vtex.com/vtex-rest-api/reference/ignoreprofiledata)  - [GET - Cart installments](https://developers.vtex.com/vtex-rest-api/reference/getcartinstallments)  - [POST - Add coupons to the cart](https://developers.vtex.com/vtex-rest-api/reference/addcoupons)      ## Cart attachments    Allows merchants to obtain client profiles and add information to a given shopping cart.    - [GET - Get client profile by email](https://developers.vtex.com/vtex-rest-api/reference/getclientprofilebyemail)  - [POST - Add client profile](https://developers.vtex.com/vtex-rest-api/reference/addclientprofile)  - [POST - Add shipping address and select delivery option](https://developers.vtex.com/vtex-rest-api/reference/addshippingaddress)  - [POST - Add client preferences](https://developers.vtex.com/vtex-rest-api/reference/addclientpreferences)  - [POST - Add marketing data](https://developers.vtex.com/vtex-rest-api/reference/addmarketingdata)  - [POST - Add payment data](https://developers.vtex.com/vtex-rest-api/reference/addpaymentdata)  - [POST - Add merchant context data](https://developers.vtex.com/vtex-rest-api/reference/addmerchantcontextdata)      ## Custom data    Allows merchants to manage custom fields that were created by an app in their account.    - [PUT - Set multiple custom field values](https://developers.vtex.com/vtex-rest-api/reference/setmultiplecustomfieldvalues)  - [PUT - Set single custom field value](https://developers.vtex.com/vtex-rest-api/reference/setsinglecustomfieldvalue)  - [DELETE - Remove single custom field value](https://developers.vtex.com/vtex-rest-api/reference/removesinglecustomfieldvalue)      ## Configuration    Allows merchants to configure orderForm in the account and seller exchange on a given order.    - [GET - Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/getorderformconfiguration)  - [POST - Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration)  - [GET - Get window to change seller](https://developers.vtex.com/vtex-rest-api/reference/getwindowtochangeseller)  - [POST - Update window to change seller](https://developers.vtex.com/vtex-rest-api/reference/updatewindowtochangeseller)  - [POST - Clear orderForm messages](https://developers.vtex.com/vtex-rest-api/reference/clearorderformmessages)      ## Fulfillment    Allows merchants to obtain pickup points and address information.    - [GET - List pickup points by location](https://developers.vtex.com/vtex-rest-api/reference/listpickupppointsbylocation)  - [GET - Get address by postal code](https://developers.vtex.com/vtex-rest-api/reference/getaddressbypostalcode)      ## Order placement    Allows merchants to place and process orders by creating a new cart or using an existing cart.    - [POST - Place order from an existing cart](https://developers.vtex.com/vtex-rest-api/reference/placeorderfromexistingorderform)  - [PUT - Place order](https://developers.vtex.com/vtex-rest-api/reference/placeorder)  - [POST - Process order](https://developers.vtex.com/vtex-rest-api/reference/processorder)      ## Region    Allows merchants to obtain a list of sellers serving a specific delivery region.    - [GET - Get sellers by region or address](https://developers.vtex.com/vtex-rest-api/reference/getsellersbyregion)
 *
 * The version of the OpenAPI document: 1.0
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
    factory(root.expect, root.CheckoutApi);
  }
}(this, function(expect, CheckoutApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new CheckoutApi.ItemsUpdate200Response();
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

  describe('ItemsUpdate200Response', function() {
    it('should create an instance of ItemsUpdate200Response', function() {
      // uncomment below and update the code to test ItemsUpdate200Response
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be.a(CheckoutApi.ItemsUpdate200Response);
    });

    it('should have the property allowManualPrice (base name: "allowManualPrice")', function() {
      // uncomment below and update the code to test the property allowManualPrice
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property availableAccounts (base name: "availableAccounts")', function() {
      // uncomment below and update the code to test the property availableAccounts
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property availableAddresses (base name: "availableAddresses")', function() {
      // uncomment below and update the code to test the property availableAddresses
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property canEditData (base name: "canEditData")', function() {
      // uncomment below and update the code to test the property canEditData
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property clientPreferencesData (base name: "clientPreferencesData")', function() {
      // uncomment below and update the code to test the property clientPreferencesData
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property clientProfileData (base name: "clientProfileData")', function() {
      // uncomment below and update the code to test the property clientProfileData
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property commercialConditionData (base name: "commercialConditionData")', function() {
      // uncomment below and update the code to test the property commercialConditionData
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property customData (base name: "customData")', function() {
      // uncomment below and update the code to test the property customData
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property giftRegistryData (base name: "giftRegistryData")', function() {
      // uncomment below and update the code to test the property giftRegistryData
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property hooksData (base name: "hooksData")', function() {
      // uncomment below and update the code to test the property hooksData
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property ignoreProfileData (base name: "ignoreProfileData")', function() {
      // uncomment below and update the code to test the property ignoreProfileData
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property invoiceData (base name: "invoiceData")', function() {
      // uncomment below and update the code to test the property invoiceData
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property isCheckedIn (base name: "isCheckedIn")', function() {
      // uncomment below and update the code to test the property isCheckedIn
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property itemMetadata (base name: "itemMetadata")', function() {
      // uncomment below and update the code to test the property itemMetadata
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property items (base name: "items")', function() {
      // uncomment below and update the code to test the property items
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property itemsOrdination (base name: "itemsOrdination")', function() {
      // uncomment below and update the code to test the property itemsOrdination
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property loggedIn (base name: "loggedIn")', function() {
      // uncomment below and update the code to test the property loggedIn
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property marketingData (base name: "marketingData")', function() {
      // uncomment below and update the code to test the property marketingData
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property messages (base name: "messages")', function() {
      // uncomment below and update the code to test the property messages
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property openTextField (base name: "openTextField")', function() {
      // uncomment below and update the code to test the property openTextField
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property orderFormId (base name: "orderFormId")', function() {
      // uncomment below and update the code to test the property orderFormId
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property paymentData (base name: "paymentData")', function() {
      // uncomment below and update the code to test the property paymentData
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property profileProvider (base name: "profileProvider")', function() {
      // uncomment below and update the code to test the property profileProvider
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property ratesAndBenefitsData (base name: "ratesAndBenefitsData")', function() {
      // uncomment below and update the code to test the property ratesAndBenefitsData
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property salesChannel (base name: "salesChannel")', function() {
      // uncomment below and update the code to test the property salesChannel
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property selectableGifts (base name: "selectableGifts")', function() {
      // uncomment below and update the code to test the property selectableGifts
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property sellers (base name: "sellers")', function() {
      // uncomment below and update the code to test the property sellers
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property shippingData (base name: "shippingData")', function() {
      // uncomment below and update the code to test the property shippingData
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property storeId (base name: "storeId")', function() {
      // uncomment below and update the code to test the property storeId
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property storePreferencesData (base name: "storePreferencesData")', function() {
      // uncomment below and update the code to test the property storePreferencesData
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property subscriptionData (base name: "subscriptionData")', function() {
      // uncomment below and update the code to test the property subscriptionData
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property totalizers (base name: "totalizers")', function() {
      // uncomment below and update the code to test the property totalizers
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property userProfileId (base name: "userProfileId")', function() {
      // uncomment below and update the code to test the property userProfileId
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property userType (base name: "userType")', function() {
      // uncomment below and update the code to test the property userType
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

    it('should have the property value (base name: "value")', function() {
      // uncomment below and update the code to test the property value
      //var instance = new CheckoutApi.ItemsUpdate200Response();
      //expect(instance).to.be();
    });

  });

}));
