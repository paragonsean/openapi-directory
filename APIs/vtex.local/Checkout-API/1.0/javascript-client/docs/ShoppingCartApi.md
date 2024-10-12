# CheckoutApi.ShoppingCartApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addCoupons**](ShoppingCartApi.md#addCoupons) | **POST** /api/checkout/pub/orderForm/{orderFormId}/coupons | Add coupons to the cart
[**cartSimulation**](ShoppingCartApi.md#cartSimulation) | **POST** /api/checkout/pub/orderForms/simulation | Cart simulation
[**createANewCart**](ShoppingCartApi.md#createANewCart) | **GET** /api/checkout/pub/orderForm | Get current or create a new cart
[**getCartInformationById**](ShoppingCartApi.md#getCartInformationById) | **GET** /api/checkout/pub/orderForm/{orderFormId} | Get cart information by ID
[**getCartInstallments**](ShoppingCartApi.md#getCartInstallments) | **GET** /api/checkout/pub/orderForm/{orderFormId}/installments | Cart installments
[**ignoreProfileData**](ShoppingCartApi.md#ignoreProfileData) | **PATCH** /api/checkout/pub/orderForm/{orderFormId}/profile | Ignore profile data
[**items**](ShoppingCartApi.md#items) | **POST** /api/checkout/pub/orderForm/{orderFormId}/items | Add cart items
[**itemsUpdate**](ShoppingCartApi.md#itemsUpdate) | **POST** /api/checkout/pub/orderForm/{orderFormId}/items/update | Update cart items
[**priceChange**](ShoppingCartApi.md#priceChange) | **PUT** /api/checkout/pub/orderForm/{orderFormId}/items/{itemIndex}/price | Change price
[**removeAllItems**](ShoppingCartApi.md#removeAllItems) | **POST** /api/checkout/pub/orderForm/{orderFormId}/items/removeAll | Remove all items
[**removeallpersonaldata**](ShoppingCartApi.md#removeallpersonaldata) | **GET** /checkout/changeToAnonymousUser/{orderFormId} | Remove all personal data



## addCoupons

> AddCoupons200Response addCoupons(orderFormId, contentType, accept, addCouponsRequest)

Add coupons to the cart

Use this request to add coupons to a given shopping cart.

### Example

```javascript
import CheckoutApi from 'checkout_api';

let apiInstance = new CheckoutApi.ShoppingCartApi();
let orderFormId = "'ede846222cd44046ba6c638442c3505a'"; // String | ID of the orderForm that will receive coupon information.
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let addCouponsRequest = new CheckoutApi.AddCouponsRequest(); // AddCouponsRequest | 
apiInstance.addCoupons(orderFormId, contentType, accept, addCouponsRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orderFormId** | **String**| ID of the orderForm that will receive coupon information. | [default to &#39;ede846222cd44046ba6c638442c3505a&#39;]
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **addCouponsRequest** | [**AddCouponsRequest**](AddCouponsRequest.md)|  | 

### Return type

[**AddCoupons200Response**](AddCoupons200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cartSimulation

> CartSimulation200Response cartSimulation(contentType, accept, opts)

Cart simulation

This endpoint is used to simulate a cart in VTEX Checkout.    It receives an **SKU ID**, the **quantity** of items in the cart and the ID of the **Seller**.    It sends back all information about the cart, such as the selling price of each item, rates and benefits data, payment and logistics info.    This is useful whenever you need to know the availability of fulfilling an order for a specific cart setting, since the API response will let you know the updated price, inventory and shipping data.    **Important**: The fields (&#x60;sku id&#x60;, &#x60;quantity&#x60;, &#x60;seller&#x60;, &#x60;country&#x60;, &#x60;postalCode&#x60; and &#x60;geoCoordinates&#x60;) are just examples of content that you can simulate in your cart. You can add more fields to the request as per your need. Access the [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) guide to check the available fields.

### Example

```javascript
import CheckoutApi from 'checkout_api';

let apiInstance = new CheckoutApi.ShoppingCartApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'rnbBehavior': 0, // Number | This parameter defines which promotions apply to the simulation. Use `0` for simulations at cart stage, which means all promotions apply. In case of window simulation use `1`, which indicates promotions that apply nominal discounts over the total purchase value shouldn't be considered on the simulation.    Note that if this not sent, the parameter is `1`.
  'sc': 1, // Number | Trade Policy (Sales Channel) identification.
  'cartSimulationRequest': new CheckoutApi.CartSimulationRequest() // CartSimulationRequest | 
};
apiInstance.cartSimulation(contentType, accept, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **rnbBehavior** | **Number**| This parameter defines which promotions apply to the simulation. Use &#x60;0&#x60; for simulations at cart stage, which means all promotions apply. In case of window simulation use &#x60;1&#x60;, which indicates promotions that apply nominal discounts over the total purchase value shouldn&#39;t be considered on the simulation.    Note that if this not sent, the parameter is &#x60;1&#x60;. | [optional] [default to 0]
 **sc** | **Number**| Trade Policy (Sales Channel) identification. | [optional] 
 **cartSimulationRequest** | [**CartSimulationRequest**](CartSimulationRequest.md)|  | [optional] 

### Return type

[**CartSimulation200Response**](CartSimulation200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createANewCart

> createANewCart(contentType, accept, opts)

Get current or create a new cart

You can use this request to get your current shopping cart information (&#x60;orderFormId&#x60;) or to create a new cart.    **Important**: To create a new empty shopping cart you need to send this request with the query param &#x60;forceNewCart&#x3D;true&#x60;.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; obtained in response is the identification code of the newly created cart.    &gt; This request has a time out of 45 seconds.

### Example

```javascript
import CheckoutApi from 'checkout_api';

let apiInstance = new CheckoutApi.ShoppingCartApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'forceNewCart': true // Boolean | Use this query parameter to create a new empty shopping cart.
};
apiInstance.createANewCart(contentType, accept, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **forceNewCart** | **Boolean**| Use this query parameter to create a new empty shopping cart. | [optional] [default to true]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCartInformationById

> getCartInformationById(orderFormId, contentType, accept, opts)

Get cart information by ID

Use this request to get all information associated to a given shopping  cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 45 seconds.

### Example

```javascript
import CheckoutApi from 'checkout_api';

let apiInstance = new CheckoutApi.ShoppingCartApi();
let orderFormId = "'ede846222cd44046ba6c638442c3505a'"; // String | ID of the orderForm corresponding to the cart whose information you want to retrieve.
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'refreshOutdatedData': true // Boolean | It is possible to use the [Update cart items request](https://developers.vtex.com/vtex-rest-api/reference/cart-update#itemsupdate) so as to allow outdated information in the `orderForm`, which may improve performance in some cases. To guarantee that all cart information is updated, send this request with this parameter as `true`. We recommend doing this in the final stages of the shopping experience, starting from the checkout page.
};
apiInstance.getCartInformationById(orderFormId, contentType, accept, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orderFormId** | **String**| ID of the orderForm corresponding to the cart whose information you want to retrieve. | [default to &#39;ede846222cd44046ba6c638442c3505a&#39;]
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **refreshOutdatedData** | **Boolean**| It is possible to use the [Update cart items request](https://developers.vtex.com/vtex-rest-api/reference/cart-update#itemsupdate) so as to allow outdated information in the &#x60;orderForm&#x60;, which may improve performance in some cases. To guarantee that all cart information is updated, send this request with this parameter as &#x60;true&#x60;. We recommend doing this in the final stages of the shopping experience, starting from the checkout page. | [optional] [default to true]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCartInstallments

> getCartInstallments(orderFormId, paymentSystem, contentType, accept)

Cart installments

Retrieves possible amount of installments and respective values for a given cart with a given payment method.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    This endpoint can be used to get the installment options for only one payment method at a time.    This endpoint should be called only after the selected &#x60;orderForm&#x60; already has a &#x60;paymentData&#x60;.

### Example

```javascript
import CheckoutApi from 'checkout_api';

let apiInstance = new CheckoutApi.ShoppingCartApi();
let orderFormId = "orderFormId_example"; // String | ID of the `orderForm` to be consulted for installments.
let paymentSystem = 56; // Number | ID of the payment method to be consulted for installments.
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
apiInstance.getCartInstallments(orderFormId, paymentSystem, contentType, accept, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orderFormId** | **String**| ID of the &#x60;orderForm&#x60; to be consulted for installments. | 
 **paymentSystem** | **Number**| ID of the payment method to be consulted for installments. | 
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ignoreProfileData

> ignoreProfileData(orderFormId, contentType, accept, ignoreProfileDataRequest)

Ignore profile data

When a shopper provides an email address at Checkout, the platform tries to retrieve existing profile information for that email and add it to the shopping cart information. Use this request if you want to change this behavior for a given cart, meaning profile information will not be included in the order automattically.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    Note that this request will only work if you have not sent the &#x60;clientProfileData&#x60; to the cart yet. Sending it to a cart that already has a &#x60;clientProfileData&#x60; should return a status &#x60;403 Forbidden&#x60; error, with an &#x60;Access denied&#x60; message.

### Example

```javascript
import CheckoutApi from 'checkout_api';

let apiInstance = new CheckoutApi.ShoppingCartApi();
let orderFormId = "'ede846222cd44046ba6c638442c3505a'"; // String | ID of the orderForm corresponding to the cart whose items will have the price changed.
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let ignoreProfileDataRequest = {"price":10000}; // IgnoreProfileDataRequest | 
apiInstance.ignoreProfileData(orderFormId, contentType, accept, ignoreProfileDataRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orderFormId** | **String**| ID of the orderForm corresponding to the cart whose items will have the price changed. | [default to &#39;ede846222cd44046ba6c638442c3505a&#39;]
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **ignoreProfileDataRequest** | [**IgnoreProfileDataRequest**](IgnoreProfileDataRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## items

> Items200Response items(contentType, accept, orderFormId, itemsRequest, opts)

Add cart items

Use this request to add a new item to the shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 45 seconds.

### Example

```javascript
import CheckoutApi from 'checkout_api';

let apiInstance = new CheckoutApi.ShoppingCartApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let orderFormId = "'ede846222cd44046ba6c638442c3505a'"; // String | ID of the orderForm corresponding to the cart in which the new item will be added.
let itemsRequest = new CheckoutApi.ItemsRequest(); // ItemsRequest | 
let opts = {
  'allowedOutdatedData': [null] // [Object] | In order to optimize performance, this parameter allows some information to not be updated when there are changes in the minicart. For instance, if a shopper adds another unit of a given SKU to the cart, it may not be necessary to recalculate payment information, which could impact performance.    This array accepts strings and currently the only possible value is `”paymentData”`.
};
apiInstance.items(contentType, accept, orderFormId, itemsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **orderFormId** | **String**| ID of the orderForm corresponding to the cart in which the new item will be added. | [default to &#39;ede846222cd44046ba6c638442c3505a&#39;]
 **itemsRequest** | [**ItemsRequest**](ItemsRequest.md)|  | 
 **allowedOutdatedData** | [**[Object]**](Object.md)| In order to optimize performance, this parameter allows some information to not be updated when there are changes in the minicart. For instance, if a shopper adds another unit of a given SKU to the cart, it may not be necessary to recalculate payment information, which could impact performance.    This array accepts strings and currently the only possible value is &#x60;”paymentData”&#x60;. | [optional] 

### Return type

[**Items200Response**](Items200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## itemsUpdate

> ItemsUpdate200Response itemsUpdate(contentType, accept, orderFormId, itemsUpdateRequest, opts)

Update cart items

You can use this request to:    1. Change the quantity of one or more items in a specific cart.  2. Remove an item from the cart (by sending the &#x60;quantity&#x60; value &#x3D; &#x60;0&#x60; in the request body).    **Important**: To remove all items from the cart at the same time, use the [Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems) endpoint.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure that represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 45 seconds.

### Example

```javascript
import CheckoutApi from 'checkout_api';

let apiInstance = new CheckoutApi.ShoppingCartApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let orderFormId = "'ede846222cd44046ba6c638442c3505a'"; // String | ID of the `orderForm` corresponding to the cart whose items you want to update.
let itemsUpdateRequest = new CheckoutApi.ItemsUpdateRequest(); // ItemsUpdateRequest | 
let opts = {
  'allowedOutdatedData': [null] // [Object] | In order to optimize performance, this parameter allows some information to not be updated when there are changes in the minicart. For instance, if a shopper adds another unit of a given SKU to the cart, it may not be necessary to recalculate payment information, which could impact performance.    This array accepts strings and currently the only possible value is `”paymentData”`.
};
apiInstance.itemsUpdate(contentType, accept, orderFormId, itemsUpdateRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **orderFormId** | **String**| ID of the &#x60;orderForm&#x60; corresponding to the cart whose items you want to update. | [default to &#39;ede846222cd44046ba6c638442c3505a&#39;]
 **itemsUpdateRequest** | [**ItemsUpdateRequest**](ItemsUpdateRequest.md)|  | 
 **allowedOutdatedData** | [**[Object]**](Object.md)| In order to optimize performance, this parameter allows some information to not be updated when there are changes in the minicart. For instance, if a shopper adds another unit of a given SKU to the cart, it may not be necessary to recalculate payment information, which could impact performance.    This array accepts strings and currently the only possible value is &#x60;”paymentData”&#x60;. | [optional] 

### Return type

[**ItemsUpdate200Response**](ItemsUpdate200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## priceChange

> priceChange(orderFormId, itemIndex, contentType, accept, priceChangeRequest)

Change price

This request changes the price of an SKU in a cart. You can also perform type of bulk price change with the [Update cart items request](https://developers.vtex.com/vtex-rest-api/reference/shopping-cart#itemsupdate)    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    You need to inform which cart you are referring to, by sending its &#x60;orderFormId&#x60;; and what is the item whose price you want to change, by sending its &#x60;itemIndex&#x60;.    You also need to pass the new price value in the body.    Remember that, to use this endpoint, the feature of *manual price* must be active. To check if it&#39;s active, use the [Get orderForm configuration](https://developers.vtex.com/reference#getorderformconfiguration) endpoint. To make it active, use the [Update orderForm configuration](https://developers.vtex.com/reference#updateorderformconfiguration) endpoint, making the &#x60;allowManualPrice&#x60; field &#x60;true&#x60;.    &gt; Whenever you use this request to change the price of an item, all items in that cart with the same SKU are affected by this change. This applies even to items that share the SKU but have been separated into different objects in the &#x60;items&#x60; array due to customizations or attachments, for example.

### Example

```javascript
import CheckoutApi from 'checkout_api';
let defaultClient = CheckoutApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CheckoutApi.ShoppingCartApi();
let orderFormId = "'ede846222cd44046ba6c638442c3505a'"; // String | ID of the orderForm corresponding to the cart whose items will have the price changed.
let itemIndex = "itemIndex_example"; // String | The index of the item in the cart. Each cart item is identified by an index, starting in 0.
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let priceChangeRequest = {"price":10000}; // PriceChangeRequest | 
apiInstance.priceChange(orderFormId, itemIndex, contentType, accept, priceChangeRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orderFormId** | **String**| ID of the orderForm corresponding to the cart whose items will have the price changed. | [default to &#39;ede846222cd44046ba6c638442c3505a&#39;]
 **itemIndex** | **String**| The index of the item in the cart. Each cart item is identified by an index, starting in 0. | 
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **priceChangeRequest** | [**PriceChangeRequest**](PriceChangeRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeAllItems

> Object removeAllItems(orderFormId, contentType, accept, opts)

Remove all items

This request removes all items from a given cart, leaving it empty.    You must send an empty JSON in the body of the request.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    **Important**: **Request Body** must always be sent with empty value \&quot;{ }\&quot; in this endpoint.

### Example

```javascript
import CheckoutApi from 'checkout_api';

let apiInstance = new CheckoutApi.ShoppingCartApi();
let orderFormId = "'ede846222cd44046ba6c638442c3505a'"; // String | ID of the orderForm corresponding to the cart whose items you want to remove.
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'body': {key: null} // Object | 
};
apiInstance.removeAllItems(orderFormId, contentType, accept, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orderFormId** | **String**| ID of the orderForm corresponding to the cart whose items you want to remove. | [default to &#39;ede846222cd44046ba6c638442c3505a&#39;]
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **body** | **Object**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeallpersonaldata

> Object removeallpersonaldata(contentType, accept, orderFormId)

Remove all personal data

This call removes all user information, making a cart anonymous while leaving the items.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure that represents a shopping cart and contains all information about it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    This call works by creating a new orderForm, setting a new cookie, and returning a redirect 302 to the cart URL (&#x60;/checkout/#/orderform&#x60;).

### Example

```javascript
import CheckoutApi from 'checkout_api';

let apiInstance = new CheckoutApi.ShoppingCartApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let orderFormId = "'ede846222cd44046ba6c638442c3505a'"; // String | ID of the orderForm corresponding to the cart whose user's personal data you want to remove.
apiInstance.removeallpersonaldata(contentType, accept, orderFormId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **orderFormId** | **String**| ID of the orderForm corresponding to the cart whose user&#39;s personal data you want to remove. | [default to &#39;ede846222cd44046ba6c638442c3505a&#39;]

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

