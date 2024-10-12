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
    instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
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

  describe('PlaceOrder200ResponseOrdersInner', function() {
    it('should create an instance of PlaceOrder200ResponseOrdersInner', function() {
      // uncomment below and update the code to test PlaceOrder200ResponseOrdersInner
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be.a(CheckoutApi.PlaceOrder200ResponseOrdersInner);
    });

    it('should have the property allowCancelation (base name: "allowCancelation")', function() {
      // uncomment below and update the code to test the property allowCancelation
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property allowChangeSeller (base name: "allowChangeSeller")', function() {
      // uncomment below and update the code to test the property allowChangeSeller
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property allowEdition (base name: "allowEdition")', function() {
      // uncomment below and update the code to test the property allowEdition
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property checkedInPickupPointId (base name: "checkedInPickupPointId")', function() {
      // uncomment below and update the code to test the property checkedInPickupPointId
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property clientProfileData (base name: "clientProfileData")', function() {
      // uncomment below and update the code to test the property clientProfileData
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property creationDate (base name: "creationDate")', function() {
      // uncomment below and update the code to test the property creationDate
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property followUpEmail (base name: "followUpEmail")', function() {
      // uncomment below and update the code to test the property followUpEmail
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property hostName (base name: "hostName")', function() {
      // uncomment below and update the code to test the property hostName
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property isCheckedIn (base name: "isCheckedIn")', function() {
      // uncomment below and update the code to test the property isCheckedIn
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property isCompleted (base name: "isCompleted")', function() {
      // uncomment below and update the code to test the property isCompleted
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property isUserDataVisible (base name: "isUserDataVisible")', function() {
      // uncomment below and update the code to test the property isUserDataVisible
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property itemMetadata (base name: "itemMetadata")', function() {
      // uncomment below and update the code to test the property itemMetadata
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property items (base name: "items")', function() {
      // uncomment below and update the code to test the property items
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property lastChange (base name: "lastChange")', function() {
      // uncomment below and update the code to test the property lastChange
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property merchantName (base name: "merchantName")', function() {
      // uncomment below and update the code to test the property merchantName
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property orderFormCreationDate (base name: "orderFormCreationDate")', function() {
      // uncomment below and update the code to test the property orderFormCreationDate
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property orderGroup (base name: "orderGroup")', function() {
      // uncomment below and update the code to test the property orderGroup
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property orderId (base name: "orderId")', function() {
      // uncomment below and update the code to test the property orderId
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property paymentData (base name: "paymentData")', function() {
      // uncomment below and update the code to test the property paymentData
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property ratesAndBenefitsData (base name: "ratesAndBenefitsData")', function() {
      // uncomment below and update the code to test the property ratesAndBenefitsData
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property roundingError (base name: "roundingError")', function() {
      // uncomment below and update the code to test the property roundingError
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property salesAssociateId (base name: "salesAssociateId")', function() {
      // uncomment below and update the code to test the property salesAssociateId
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property salesChannel (base name: "salesChannel")', function() {
      // uncomment below and update the code to test the property salesChannel
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property sellerOrderId (base name: "sellerOrderId")', function() {
      // uncomment below and update the code to test the property sellerOrderId
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property sellers (base name: "sellers")', function() {
      // uncomment below and update the code to test the property sellers
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property shippingData (base name: "shippingData")', function() {
      // uncomment below and update the code to test the property shippingData
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property state (base name: "state")', function() {
      // uncomment below and update the code to test the property state
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property storeId (base name: "storeId")', function() {
      // uncomment below and update the code to test the property storeId
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property timeZoneCreationDate (base name: "timeZoneCreationDate")', function() {
      // uncomment below and update the code to test the property timeZoneCreationDate
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property timeZoneLastChange (base name: "timeZoneLastChange")', function() {
      // uncomment below and update the code to test the property timeZoneLastChange
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property totals (base name: "totals")', function() {
      // uncomment below and update the code to test the property totals
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property userType (base name: "userType")', function() {
      // uncomment below and update the code to test the property userType
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

    it('should have the property value (base name: "value")', function() {
      // uncomment below and update the code to test the property value
      //var instance = new CheckoutApi.PlaceOrder200ResponseOrdersInner();
      //expect(instance).to.be();
    });

  });

}));
