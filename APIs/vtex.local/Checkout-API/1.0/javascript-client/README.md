# checkout_api

CheckoutApi - JavaScript client for checkout_api
>ℹ️ Check the new [Checkout onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/checkout-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about the Checkout and is organized by focusing on the developer's journey.

The Checkout API allows you to obtain and configure information about the shopping cart and its attachments, personalization of custom fields, orderForm structure, fulfillment data, order management, and identification of the sellers delivery region.

>ℹ️ Data modification operations (`POST`, `PATCH`, `PUT` or `DELETE` endpoints) shall not be performed in parallel in the Checkout APIs. They need to be enqueued by the client/requester. Otherwise, old values ​​can be overwritten incorrectly or competition errors may occur.

>⚠️ All endpoints that consult or edit the orderForm can change the authentication depending on the customer context. If you are handling information from a customer with a complete profile on the store, authentication will be required. You can only access or modify the customer data for these profiles with an authenticated request.

## Shopping cart

Allows merchants to simulate, configure and customize shopping cart information.

- [POST - Cart Simulation](https://developers.vtex.com/vtex-rest-api/reference/cartsimulation)
- [GET - Get current or create a new cart](https://developers.vtex.com/vtex-rest-api/reference/createanewcart)
- [GET - Get cart information by ID](https://developers.vtex.com/vtex-rest-api/reference/getcartinformationbyid)
- [POST - Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems)
- [GET - Remove all personal data](https://developers.vtex.com/vtex-rest-api/reference/removeallpersonaldata)
- [POST - Update cart items](https://developers.vtex.com/vtex-rest-api/reference/itemsupdate)
- [POST - Add cart items](https://developers.vtex.com/vtex-rest-api/reference/items)
- [PUT - Change price](https://developers.vtex.com/vtex-rest-api/reference/pricechange)
- [PATCH - Ignore profile data](https://developers.vtex.com/vtex-rest-api/reference/ignoreprofiledata)
- [GET - Cart installments](https://developers.vtex.com/vtex-rest-api/reference/getcartinstallments)
- [POST - Add coupons to the cart](https://developers.vtex.com/vtex-rest-api/reference/addcoupons)


## Cart attachments

Allows merchants to obtain client profiles and add information to a given shopping cart.

- [GET - Get client profile by email](https://developers.vtex.com/vtex-rest-api/reference/getclientprofilebyemail)
- [POST - Add client profile](https://developers.vtex.com/vtex-rest-api/reference/addclientprofile)
- [POST - Add shipping address and select delivery option](https://developers.vtex.com/vtex-rest-api/reference/addshippingaddress)
- [POST - Add client preferences](https://developers.vtex.com/vtex-rest-api/reference/addclientpreferences)
- [POST - Add marketing data](https://developers.vtex.com/vtex-rest-api/reference/addmarketingdata)
- [POST - Add payment data](https://developers.vtex.com/vtex-rest-api/reference/addpaymentdata)
- [POST - Add merchant context data](https://developers.vtex.com/vtex-rest-api/reference/addmerchantcontextdata)


## Custom data

Allows merchants to manage custom fields that were created by an app in their account.

- [PUT - Set multiple custom field values](https://developers.vtex.com/vtex-rest-api/reference/setmultiplecustomfieldvalues)
- [PUT - Set single custom field value](https://developers.vtex.com/vtex-rest-api/reference/setsinglecustomfieldvalue)
- [DELETE - Remove single custom field value](https://developers.vtex.com/vtex-rest-api/reference/removesinglecustomfieldvalue)


## Configuration

Allows merchants to configure orderForm in the account and seller exchange on a given order.

- [GET - Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/getorderformconfiguration)
- [POST - Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration)
- [GET - Get window to change seller](https://developers.vtex.com/vtex-rest-api/reference/getwindowtochangeseller)
- [POST - Update window to change seller](https://developers.vtex.com/vtex-rest-api/reference/updatewindowtochangeseller)
- [POST - Clear orderForm messages](https://developers.vtex.com/vtex-rest-api/reference/clearorderformmessages)


## Fulfillment

Allows merchants to obtain pickup points and address information.

- [GET - List pickup points by location](https://developers.vtex.com/vtex-rest-api/reference/listpickupppointsbylocation)
- [GET - Get address by postal code](https://developers.vtex.com/vtex-rest-api/reference/getaddressbypostalcode)


## Order placement

Allows merchants to place and process orders by creating a new cart or using an existing cart.

- [POST - Place order from an existing cart](https://developers.vtex.com/vtex-rest-api/reference/placeorderfromexistingorderform)
- [PUT - Place order](https://developers.vtex.com/vtex-rest-api/reference/placeorder)
- [POST - Process order](https://developers.vtex.com/vtex-rest-api/reference/processorder)


## Region

Allows merchants to obtain a list of sellers serving a specific delivery region.

- [GET - Get sellers by region or address](https://developers.vtex.com/vtex-rest-api/reference/getsellersbyregion)
This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install checkout_api --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your checkout_api from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var CheckoutApi = require('checkout_api');


var api = new CheckoutApi.CartAttachmentsApi()
var contentType = "'application/json'"; // {String} Type of the content being sent.
var accept = "'application/json'"; // {String} HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
var orderFormId = "orderFormId_example"; // {String} ID of the orderForm that will receive client profile information.
var addClientPreferencesRequest = new CheckoutApi.AddClientPreferencesRequest(); // {AddClientPreferencesRequest} 
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.addClientPreferences(contentType, accept, orderFormId, addClientPreferencesRequest, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://vtex.local*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CheckoutApi.CartAttachmentsApi* | [**addClientPreferences**](docs/CartAttachmentsApi.md#addClientPreferences) | **POST** /api/checkout/pub/orderForm/{orderFormId}/attachments/clientPreferencesData | Add client preferences
*CheckoutApi.CartAttachmentsApi* | [**addClientProfile**](docs/CartAttachmentsApi.md#addClientProfile) | **POST** /api/checkout/pub/orderForm/{orderFormId}/attachments/clientProfileData | Add client profile
*CheckoutApi.CartAttachmentsApi* | [**addMarketingData**](docs/CartAttachmentsApi.md#addMarketingData) | **POST** /api/checkout/pub/orderForm/{orderFormId}/attachments/marketingData | Add marketing data
*CheckoutApi.CartAttachmentsApi* | [**addMerchantContextData**](docs/CartAttachmentsApi.md#addMerchantContextData) | **POST** /api/checkout/pub/orderForm/{orderFormId}/attachments/merchantContextData | Add merchant context data
*CheckoutApi.CartAttachmentsApi* | [**addPaymentData**](docs/CartAttachmentsApi.md#addPaymentData) | **POST** /api/checkout/pub/orderForm/{orderFormId}/attachments/paymentData | Add payment data
*CheckoutApi.CartAttachmentsApi* | [**addShippingAddress**](docs/CartAttachmentsApi.md#addShippingAddress) | **POST** /api/checkout/pub/orderForm/{orderFormId}/attachments/shippingData | Add shipping address and select delivery option
*CheckoutApi.CartAttachmentsApi* | [**getClientProfileByEmail**](docs/CartAttachmentsApi.md#getClientProfileByEmail) | **GET** /api/checkout/pub/profiles | Get client profile by email
*CheckoutApi.ConfigurationApi* | [**clearorderFormMessages**](docs/ConfigurationApi.md#clearorderFormMessages) | **POST** /api/checkout/pub/orderForm/{orderFormId}/messages/clear | Clear orderForm messages
*CheckoutApi.ConfigurationApi* | [**getWindowToChangeSeller**](docs/ConfigurationApi.md#getWindowToChangeSeller) | **GET** /api/checkout/pvt/configuration/window-to-change-seller | Get window to change seller
*CheckoutApi.ConfigurationApi* | [**getorderFormconfiguration**](docs/ConfigurationApi.md#getorderFormconfiguration) | **GET** /api/checkout/pvt/configuration/orderForm | Get orderForm configuration
*CheckoutApi.ConfigurationApi* | [**updateWindowToChangeSeller**](docs/ConfigurationApi.md#updateWindowToChangeSeller) | **POST** /api/checkout/pvt/configuration/window-to-change-seller | Update window to change seller
*CheckoutApi.ConfigurationApi* | [**updateorderFormconfiguration**](docs/ConfigurationApi.md#updateorderFormconfiguration) | **POST** /api/checkout/pvt/configuration/orderForm | Update orderForm configuration
*CheckoutApi.CustomDataApi* | [**removesinglecustomfieldvalue**](docs/CustomDataApi.md#removesinglecustomfieldvalue) | **DELETE** /api/checkout/pub/orderForm/{orderFormId}/customData/{appId}/{appFieldName} | Remove single custom field value
*CheckoutApi.CustomDataApi* | [**setMultipleCustomFieldValues**](docs/CustomDataApi.md#setMultipleCustomFieldValues) | **PUT** /api/checkout/pub/orderForm/{orderFormId}/customData/{appId} | Set multiple custom field values
*CheckoutApi.CustomDataApi* | [**setSingleCustomFieldValue**](docs/CustomDataApi.md#setSingleCustomFieldValue) | **PUT** /api/checkout/pub/orderForm/{orderFormId}/customData/{appId}/{appFieldName} | Set single custom field value
*CheckoutApi.FulfillmentApi* | [**getAddressByPostalCode**](docs/FulfillmentApi.md#getAddressByPostalCode) | **GET** /api/checkout/pub/postal-code/{countryCode}/{postalCode} | Get address by postal code
*CheckoutApi.FulfillmentApi* | [**listPickupPpointsByLocation**](docs/FulfillmentApi.md#listPickupPpointsByLocation) | **GET** /api/checkout/pub/pickup-points | List pickup points by location
*CheckoutApi.OrderPlacementApi* | [**placeOrder**](docs/OrderPlacementApi.md#placeOrder) | **PUT** /api/checkout/pub/orders | Place order
*CheckoutApi.OrderPlacementApi* | [**placeOrderFromExistingOrderForm**](docs/OrderPlacementApi.md#placeOrderFromExistingOrderForm) | **POST** /api/checkout/pub/orderForm/{orderFormId}/transaction | Place order from an existing cart
*CheckoutApi.OrderPlacementApi* | [**processOrder**](docs/OrderPlacementApi.md#processOrder) | **POST** /api/checkout/pub/gatewayCallback/{orderGroup} | Process order
*CheckoutApi.RegionApi* | [**getSellersByRegion**](docs/RegionApi.md#getSellersByRegion) | **GET** /api/checkout/pub/regions/{regionId} | Get sellers by region or address
*CheckoutApi.ShoppingCartApi* | [**addCoupons**](docs/ShoppingCartApi.md#addCoupons) | **POST** /api/checkout/pub/orderForm/{orderFormId}/coupons | Add coupons to the cart
*CheckoutApi.ShoppingCartApi* | [**cartSimulation**](docs/ShoppingCartApi.md#cartSimulation) | **POST** /api/checkout/pub/orderForms/simulation | Cart simulation
*CheckoutApi.ShoppingCartApi* | [**createANewCart**](docs/ShoppingCartApi.md#createANewCart) | **GET** /api/checkout/pub/orderForm | Get current or create a new cart
*CheckoutApi.ShoppingCartApi* | [**getCartInformationById**](docs/ShoppingCartApi.md#getCartInformationById) | **GET** /api/checkout/pub/orderForm/{orderFormId} | Get cart information by ID
*CheckoutApi.ShoppingCartApi* | [**getCartInstallments**](docs/ShoppingCartApi.md#getCartInstallments) | **GET** /api/checkout/pub/orderForm/{orderFormId}/installments | Cart installments
*CheckoutApi.ShoppingCartApi* | [**ignoreProfileData**](docs/ShoppingCartApi.md#ignoreProfileData) | **PATCH** /api/checkout/pub/orderForm/{orderFormId}/profile | Ignore profile data
*CheckoutApi.ShoppingCartApi* | [**items**](docs/ShoppingCartApi.md#items) | **POST** /api/checkout/pub/orderForm/{orderFormId}/items | Add cart items
*CheckoutApi.ShoppingCartApi* | [**itemsUpdate**](docs/ShoppingCartApi.md#itemsUpdate) | **POST** /api/checkout/pub/orderForm/{orderFormId}/items/update | Update cart items
*CheckoutApi.ShoppingCartApi* | [**priceChange**](docs/ShoppingCartApi.md#priceChange) | **PUT** /api/checkout/pub/orderForm/{orderFormId}/items/{itemIndex}/price | Change price
*CheckoutApi.ShoppingCartApi* | [**removeAllItems**](docs/ShoppingCartApi.md#removeAllItems) | **POST** /api/checkout/pub/orderForm/{orderFormId}/items/removeAll | Remove all items
*CheckoutApi.ShoppingCartApi* | [**removeallpersonaldata**](docs/ShoppingCartApi.md#removeallpersonaldata) | **GET** /checkout/changeToAnonymousUser/{orderFormId} | Remove all personal data


## Documentation for Models

 - [CheckoutApi.AddClientPreferencesRequest](docs/AddClientPreferencesRequest.md)
 - [CheckoutApi.AddClientProfileRequest](docs/AddClientProfileRequest.md)
 - [CheckoutApi.AddCoupons200Response](docs/AddCoupons200Response.md)
 - [CheckoutApi.AddCoupons200ResponseAvailableAddressesInner](docs/AddCoupons200ResponseAvailableAddressesInner.md)
 - [CheckoutApi.AddCoupons200ResponseClientPreferencesData](docs/AddCoupons200ResponseClientPreferencesData.md)
 - [CheckoutApi.AddCoupons200ResponseClientProfileData](docs/AddCoupons200ResponseClientProfileData.md)
 - [CheckoutApi.AddCoupons200ResponseItemMetadata](docs/AddCoupons200ResponseItemMetadata.md)
 - [CheckoutApi.AddCoupons200ResponseItemMetadataItemsInner](docs/AddCoupons200ResponseItemMetadataItemsInner.md)
 - [CheckoutApi.AddCoupons200ResponseItemsInner](docs/AddCoupons200ResponseItemsInner.md)
 - [CheckoutApi.AddCoupons200ResponseItemsInnerAdditionalInfo](docs/AddCoupons200ResponseItemsInnerAdditionalInfo.md)
 - [CheckoutApi.AddCoupons200ResponseItemsInnerBundleItemsInner](docs/AddCoupons200ResponseItemsInnerBundleItemsInner.md)
 - [CheckoutApi.AddCoupons200ResponseItemsInnerPriceDefinition](docs/AddCoupons200ResponseItemsInnerPriceDefinition.md)
 - [CheckoutApi.AddCoupons200ResponseItemsInnerPriceDefinitionSellingPricesInner](docs/AddCoupons200ResponseItemsInnerPriceDefinitionSellingPricesInner.md)
 - [CheckoutApi.AddCoupons200ResponseItemsInnerPriceTagsInner](docs/AddCoupons200ResponseItemsInnerPriceTagsInner.md)
 - [CheckoutApi.AddCoupons200ResponseItemsInnerProductCategories](docs/AddCoupons200ResponseItemsInnerProductCategories.md)
 - [CheckoutApi.AddCoupons200ResponseItemsOrdination](docs/AddCoupons200ResponseItemsOrdination.md)
 - [CheckoutApi.AddCoupons200ResponseMarketingData](docs/AddCoupons200ResponseMarketingData.md)
 - [CheckoutApi.AddCoupons200ResponsePaymentData](docs/AddCoupons200ResponsePaymentData.md)
 - [CheckoutApi.AddCoupons200ResponsePaymentDataGiftCardsInner](docs/AddCoupons200ResponsePaymentDataGiftCardsInner.md)
 - [CheckoutApi.AddCoupons200ResponsePaymentDataTransactionsInner](docs/AddCoupons200ResponsePaymentDataTransactionsInner.md)
 - [CheckoutApi.AddCoupons200ResponsePaymentDataTransactionsInnerPaymentsInner](docs/AddCoupons200ResponsePaymentDataTransactionsInnerPaymentsInner.md)
 - [CheckoutApi.AddCoupons200ResponseRatesAndBenefitsData](docs/AddCoupons200ResponseRatesAndBenefitsData.md)
 - [CheckoutApi.AddCoupons200ResponseSellersInner](docs/AddCoupons200ResponseSellersInner.md)
 - [CheckoutApi.AddCoupons200ResponseShippingData](docs/AddCoupons200ResponseShippingData.md)
 - [CheckoutApi.AddCoupons200ResponseShippingDataAddress](docs/AddCoupons200ResponseShippingDataAddress.md)
 - [CheckoutApi.AddCoupons200ResponseShippingDataAvailableAddressesInner](docs/AddCoupons200ResponseShippingDataAvailableAddressesInner.md)
 - [CheckoutApi.AddCoupons200ResponseShippingDataLogisticsInfoInner](docs/AddCoupons200ResponseShippingDataLogisticsInfoInner.md)
 - [CheckoutApi.AddCoupons200ResponseShippingDataLogisticsInfoInnerDeliveryChannelsInner](docs/AddCoupons200ResponseShippingDataLogisticsInfoInnerDeliveryChannelsInner.md)
 - [CheckoutApi.AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInner](docs/AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInner.md)
 - [CheckoutApi.AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerDeliveryIdsInner](docs/AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerDeliveryIdsInner.md)
 - [CheckoutApi.AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfo](docs/AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfo.md)
 - [CheckoutApi.AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfoAddress](docs/AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfoAddress.md)
 - [CheckoutApi.AddCouponsRequest](docs/AddCouponsRequest.md)
 - [CheckoutApi.AddMarketingDataRequest](docs/AddMarketingDataRequest.md)
 - [CheckoutApi.AddMerchantContextData200Response](docs/AddMerchantContextData200Response.md)
 - [CheckoutApi.AddMerchantContextDataRequest](docs/AddMerchantContextDataRequest.md)
 - [CheckoutApi.AddMerchantContextDataRequestSalesAssociateData](docs/AddMerchantContextDataRequestSalesAssociateData.md)
 - [CheckoutApi.AddPaymentDataRequest](docs/AddPaymentDataRequest.md)
 - [CheckoutApi.AddPaymentDataRequestPaymentsInner](docs/AddPaymentDataRequestPaymentsInner.md)
 - [CheckoutApi.AddShippingAddressRequest](docs/AddShippingAddressRequest.md)
 - [CheckoutApi.AddShippingAddressRequestLogisticsInfoInner](docs/AddShippingAddressRequestLogisticsInfoInner.md)
 - [CheckoutApi.AddShippingAddressRequestSelectedAddressesInner](docs/AddShippingAddressRequestSelectedAddressesInner.md)
 - [CheckoutApi.CartSimulation200Response](docs/CartSimulation200Response.md)
 - [CheckoutApi.CartSimulation200ResponseItemsInner](docs/CartSimulation200ResponseItemsInner.md)
 - [CheckoutApi.CartSimulation200ResponseItemsInnerPriceTagsInner](docs/CartSimulation200ResponseItemsInnerPriceTagsInner.md)
 - [CheckoutApi.CartSimulation200ResponseLogisticsInfoInner](docs/CartSimulation200ResponseLogisticsInfoInner.md)
 - [CheckoutApi.CartSimulation200ResponseLogisticsInfoInnerItemMetadata](docs/CartSimulation200ResponseLogisticsInfoInnerItemMetadata.md)
 - [CheckoutApi.CartSimulation200ResponseLogisticsInfoInnerItemMetadataItemsInner](docs/CartSimulation200ResponseLogisticsInfoInnerItemMetadataItemsInner.md)
 - [CheckoutApi.CartSimulation200ResponseLogisticsInfoInnerPurchaseConditions](docs/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditions.md)
 - [CheckoutApi.CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner](docs/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner.md)
 - [CheckoutApi.CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner](docs/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.md)
 - [CheckoutApi.CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows](docs/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows.md)
 - [CheckoutApi.CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerDeliveryWindow](docs/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerDeliveryWindow.md)
 - [CheckoutApi.CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerPickupStoreInfo](docs/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerPickupStoreInfo.md)
 - [CheckoutApi.CartSimulation200ResponseLogisticsInfoInnerTotalsInner](docs/CartSimulation200ResponseLogisticsInfoInnerTotalsInner.md)
 - [CheckoutApi.CartSimulation200ResponsePaymentData](docs/CartSimulation200ResponsePaymentData.md)
 - [CheckoutApi.CartSimulation200ResponsePaymentDataPaymentSystemsInner](docs/CartSimulation200ResponsePaymentDataPaymentSystemsInner.md)
 - [CheckoutApi.CartSimulation200ResponseRatesAndBenefitsData](docs/CartSimulation200ResponseRatesAndBenefitsData.md)
 - [CheckoutApi.CartSimulationRequest](docs/CartSimulationRequest.md)
 - [CheckoutApi.CartSimulationRequestItemsInner](docs/CartSimulationRequestItemsInner.md)
 - [CheckoutApi.ClearorderFormMessages200Response](docs/ClearorderFormMessages200Response.md)
 - [CheckoutApi.ClearorderFormMessages200ResponseMarketingData](docs/ClearorderFormMessages200ResponseMarketingData.md)
 - [CheckoutApi.GetClientProfileByEmail200Response](docs/GetClientProfileByEmail200Response.md)
 - [CheckoutApi.GetClientProfileByEmail200ResponseUserProfile](docs/GetClientProfileByEmail200ResponseUserProfile.md)
 - [CheckoutApi.GetSellersByRegion200Response](docs/GetSellersByRegion200Response.md)
 - [CheckoutApi.IgnoreProfileDataRequest](docs/IgnoreProfileDataRequest.md)
 - [CheckoutApi.Item](docs/Item.md)
 - [CheckoutApi.Items200Response](docs/Items200Response.md)
 - [CheckoutApi.Items200ResponseClientPreferencesData](docs/Items200ResponseClientPreferencesData.md)
 - [CheckoutApi.Items200ResponseItemsInner](docs/Items200ResponseItemsInner.md)
 - [CheckoutApi.Items200ResponseMarketingData](docs/Items200ResponseMarketingData.md)
 - [CheckoutApi.ItemsRequest](docs/ItemsRequest.md)
 - [CheckoutApi.ItemsRequestOrderItemsInner](docs/ItemsRequestOrderItemsInner.md)
 - [CheckoutApi.ItemsUpdate200Response](docs/ItemsUpdate200Response.md)
 - [CheckoutApi.ItemsUpdate200ResponseAvailableAddressesInner](docs/ItemsUpdate200ResponseAvailableAddressesInner.md)
 - [CheckoutApi.ItemsUpdate200ResponseItemsOrdination](docs/ItemsUpdate200ResponseItemsOrdination.md)
 - [CheckoutApi.ItemsUpdate200ResponseShippingData](docs/ItemsUpdate200ResponseShippingData.md)
 - [CheckoutApi.ItemsUpdate200ResponseShippingDataAddress](docs/ItemsUpdate200ResponseShippingDataAddress.md)
 - [CheckoutApi.ItemsUpdate200ResponseShippingDataAvailableAddressesInner](docs/ItemsUpdate200ResponseShippingDataAvailableAddressesInner.md)
 - [CheckoutApi.ItemsUpdate200ResponseShippingDataLogisticsInfoInner](docs/ItemsUpdate200ResponseShippingDataLogisticsInfoInner.md)
 - [CheckoutApi.ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInner](docs/ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInner.md)
 - [CheckoutApi.ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfo](docs/ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfo.md)
 - [CheckoutApi.ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfoAddress](docs/ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfoAddress.md)
 - [CheckoutApi.ItemsUpdateRequest](docs/ItemsUpdateRequest.md)
 - [CheckoutApi.ItemsUpdateRequestOrderItemsInner](docs/ItemsUpdateRequestOrderItemsInner.md)
 - [CheckoutApi.OrderFormSimulationRequest](docs/OrderFormSimulationRequest.md)
 - [CheckoutApi.PaymentConfiguration](docs/PaymentConfiguration.md)
 - [CheckoutApi.PlaceOrder200Response](docs/PlaceOrder200Response.md)
 - [CheckoutApi.PlaceOrder200ResponseOrdersInner](docs/PlaceOrder200ResponseOrdersInner.md)
 - [CheckoutApi.PlaceOrder200ResponseOrdersInnerItemsInner](docs/PlaceOrder200ResponseOrdersInnerItemsInner.md)
 - [CheckoutApi.PlaceOrder200ResponseTransactionData](docs/PlaceOrder200ResponseTransactionData.md)
 - [CheckoutApi.PlaceOrder200ResponseTransactionDataMerchantTransactionsInner](docs/PlaceOrder200ResponseTransactionDataMerchantTransactionsInner.md)
 - [CheckoutApi.PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner](docs/PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner.md)
 - [CheckoutApi.PlaceOrderFromExistingOrderFormRequest](docs/PlaceOrderFromExistingOrderFormRequest.md)
 - [CheckoutApi.PlaceOrderRequest](docs/PlaceOrderRequest.md)
 - [CheckoutApi.PlaceOrderRequestClientProfileData](docs/PlaceOrderRequestClientProfileData.md)
 - [CheckoutApi.PlaceOrderRequestItemsInner](docs/PlaceOrderRequestItemsInner.md)
 - [CheckoutApi.PlaceOrderRequestItemsInnerBundleItemsInner](docs/PlaceOrderRequestItemsInnerBundleItemsInner.md)
 - [CheckoutApi.PlaceOrderRequestItemsInnerItemAttachment](docs/PlaceOrderRequestItemsInnerItemAttachment.md)
 - [CheckoutApi.PlaceOrderRequestItemsInnerPriceTagsInner](docs/PlaceOrderRequestItemsInnerPriceTagsInner.md)
 - [CheckoutApi.PlaceOrderRequestMarketingData](docs/PlaceOrderRequestMarketingData.md)
 - [CheckoutApi.PlaceOrderRequestPaymentData](docs/PlaceOrderRequestPaymentData.md)
 - [CheckoutApi.PlaceOrderRequestPaymentDataGiftCardsInner](docs/PlaceOrderRequestPaymentDataGiftCardsInner.md)
 - [CheckoutApi.PlaceOrderRequestPaymentDataPaymentSystemsInner](docs/PlaceOrderRequestPaymentDataPaymentSystemsInner.md)
 - [CheckoutApi.PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator](docs/PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator.md)
 - [CheckoutApi.PlaceOrderRequestPaymentDataPaymentsInner](docs/PlaceOrderRequestPaymentDataPaymentsInner.md)
 - [CheckoutApi.PlaceOrderRequestShippingData](docs/PlaceOrderRequestShippingData.md)
 - [CheckoutApi.PlaceOrderRequestShippingDataAddress](docs/PlaceOrderRequestShippingDataAddress.md)
 - [CheckoutApi.PlaceOrderRequestShippingDataLogisticsInfoInner](docs/PlaceOrderRequestShippingDataLogisticsInfoInner.md)
 - [CheckoutApi.PlaceOrderRequestShippingDataLogisticsInfoInnerDeliveryWindow](docs/PlaceOrderRequestShippingDataLogisticsInfoInnerDeliveryWindow.md)
 - [CheckoutApi.PriceChangeRequest](docs/PriceChangeRequest.md)
 - [CheckoutApi.ProcessOrder500Response](docs/ProcessOrder500Response.md)
 - [CheckoutApi.ProcessOrder500ResponseError](docs/ProcessOrder500ResponseError.md)
 - [CheckoutApi.SetsinglecustomfieldvalueRequest](docs/SetsinglecustomfieldvalueRequest.md)
 - [CheckoutApi.UpdateorderFormconfigurationRequest](docs/UpdateorderFormconfigurationRequest.md)
 - [CheckoutApi.UpdateorderFormconfigurationRequestAppsInner](docs/UpdateorderFormconfigurationRequestAppsInner.md)
 - [CheckoutApi.UpdateorderFormconfigurationRequestTaxConfiguration](docs/UpdateorderFormconfigurationRequestTaxConfiguration.md)
 - [CheckoutApi.WaitingTime](docs/WaitingTime.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### appKey


- **Type**: API key
- **API key parameter name**: X-VTEX-API-AppKey
- **Location**: HTTP header

### appToken


- **Type**: API key
- **API key parameter name**: X-VTEX-API-AppToken
- **Location**: HTTP header

