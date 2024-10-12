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
    instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
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

  describe('AddCoupons200ResponseItemsInner', function() {
    it('should create an instance of AddCoupons200ResponseItemsInner', function() {
      // uncomment below and update the code to test AddCoupons200ResponseItemsInner
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be.a(CheckoutApi.AddCoupons200ResponseItemsInner);
    });

    it('should have the property additionalInfo (base name: "additionalInfo")', function() {
      // uncomment below and update the code to test the property additionalInfo
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property attachments (base name: "attachments")', function() {
      // uncomment below and update the code to test the property attachments
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property availability (base name: "availability")', function() {
      // uncomment below and update the code to test the property availability
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property bundleItems (base name: "bundleItems")', function() {
      // uncomment below and update the code to test the property bundleItems
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property detailUrl (base name: "detailUrl")', function() {
      // uncomment below and update the code to test the property detailUrl
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property ean (base name: "ean")', function() {
      // uncomment below and update the code to test the property ean
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property imageUrl (base name: "imageUrl")', function() {
      // uncomment below and update the code to test the property imageUrl
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property isGift (base name: "isGift")', function() {
      // uncomment below and update the code to test the property isGift
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property listPrice (base name: "listPrice")', function() {
      // uncomment below and update the code to test the property listPrice
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property manualPrice (base name: "manualPrice")', function() {
      // uncomment below and update the code to test the property manualPrice
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property manualPriceAppliedBy (base name: "manualPriceAppliedBy")', function() {
      // uncomment below and update the code to test the property manualPriceAppliedBy
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property manufacturerCode (base name: "manufacturerCode")', function() {
      // uncomment below and update the code to test the property manufacturerCode
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property measurementUnit (base name: "measurementUnit")', function() {
      // uncomment below and update the code to test the property measurementUnit
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property modalType (base name: "modalType")', function() {
      // uncomment below and update the code to test the property modalType
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property parentAssemblyBinding (base name: "parentAssemblyBinding")', function() {
      // uncomment below and update the code to test the property parentAssemblyBinding
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property parentItemIndex (base name: "parentItemIndex")', function() {
      // uncomment below and update the code to test the property parentItemIndex
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property preSaleDate (base name: "preSaleDate")', function() {
      // uncomment below and update the code to test the property preSaleDate
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property price (base name: "price")', function() {
      // uncomment below and update the code to test the property price
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property priceDefinition (base name: "priceDefinition")', function() {
      // uncomment below and update the code to test the property priceDefinition
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property priceTags (base name: "priceTags")', function() {
      // uncomment below and update the code to test the property priceTags
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property priceValidUntil (base name: "priceValidUntil")', function() {
      // uncomment below and update the code to test the property priceValidUntil
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property productCategories (base name: "productCategories")', function() {
      // uncomment below and update the code to test the property productCategories
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property productCategoryIds (base name: "productCategoryIds")', function() {
      // uncomment below and update the code to test the property productCategoryIds
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property productId (base name: "productId")', function() {
      // uncomment below and update the code to test the property productId
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property productRefId (base name: "productRefId")', function() {
      // uncomment below and update the code to test the property productRefId
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property quantity (base name: "quantity")', function() {
      // uncomment below and update the code to test the property quantity
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property refId (base name: "refId")', function() {
      // uncomment below and update the code to test the property refId
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property rewardValue (base name: "rewardValue")', function() {
      // uncomment below and update the code to test the property rewardValue
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property seller (base name: "seller")', function() {
      // uncomment below and update the code to test the property seller
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property sellerChain (base name: "sellerChain")', function() {
      // uncomment below and update the code to test the property sellerChain
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property sellingPrice (base name: "sellingPrice")', function() {
      // uncomment below and update the code to test the property sellingPrice
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property skuName (base name: "skuName")', function() {
      // uncomment below and update the code to test the property skuName
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property tax (base name: "tax")', function() {
      // uncomment below and update the code to test the property tax
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property uniqueId (base name: "uniqueId")', function() {
      // uncomment below and update the code to test the property uniqueId
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property unitMultiplier (base name: "unitMultiplier")', function() {
      // uncomment below and update the code to test the property unitMultiplier
      //var instance = new CheckoutApi.AddCoupons200ResponseItemsInner();
      //expect(instance).to.be();
    });

  });

}));
