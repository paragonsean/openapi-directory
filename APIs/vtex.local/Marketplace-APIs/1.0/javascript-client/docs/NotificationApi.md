# MarketplaceApi.NotificationApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inventoryNotification**](NotificationApi.md#inventoryNotification) | **POST** /notificator/{sellerId}/changenotification/{skuId}/inventory | Notify marketplace of inventory update
[**priceNotification**](NotificationApi.md#priceNotification) | **POST** /notificator/{sellerId}/changenotification/{skuId}/price | Notify marketplace of price update



## inventoryNotification

> inventoryNotification(accountName, environment, accept, contentType, sellerId, skuId)

Notify marketplace of inventory update

This endpoint is used by *sellers* to notify marketplaces that the inventory level has changed for one of their SKUs.   There is no request body in this call, indicating the new inventory level, for instance. It only notifies a specific marketplace (&#x60;accountName&#x60;) that a seller (&#x60;sellerId&#x60;) has changed the inventory level of an SKU (&#x60;skuId&#x60;).   *Marketplaces* will then call the [fulfillment endpoint](https://developers.vtex.com/vtex-rest-api/reference/fulfillment-simulation) provided in the seller registration form to get the updated inventory  information.

### Example

```javascript
import MarketplaceApi from 'marketplace_api';
let defaultClient = MarketplaceApi.ApiClient.instance;
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

let apiInstance = new MarketplaceApi.NotificationApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account that belongs to the marketplace. The notification will be posted into this account.
let environment = "'vtexcommercestable'"; // String | Environment to use. Used as part of the URL.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let sellerId = "'seller123'"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built.
let skuId = "'1234'"; // String | A string that identifies the SKU in the seller, that suffered the change. This is the ID that the marketplace will use for all  references to this SKU, such as price and inventory notifications.
apiInstance.inventoryNotification(accountName, environment, accept, contentType, sellerId, skuId, (error, data, response) => {
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
 **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. The notification will be posted into this account. | [default to &#39;apiexamples&#39;]
 **environment** | **String**| Environment to use. Used as part of the URL. | [default to &#39;vtexcommercestable&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built. | [default to &#39;seller123&#39;]
 **skuId** | **String**| A string that identifies the SKU in the seller, that suffered the change. This is the ID that the marketplace will use for all  references to this SKU, such as price and inventory notifications. | [default to &#39;1234&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## priceNotification

> priceNotification(accountName, contentType, environment, accept, sellerId, skuId)

Notify marketplace of price update

This endpoint is used by *sellers* to notify marketplaces that the price has changed for one of their SKUs.   There is no request body in this call, indicating the new price value, for instance. It only notifies a specific marketplace (&#x60;accountName&#x60;) that a seller (&#x60;sellerId&#x60;) has changed the price of an SKU (&#x60;skuId&#x60;).   *Marketplaces* will then call the [fulfillment endpoint](https://developers.vtex.com/vtex-rest-api/reference/fulfillment-simulation) provided in the seller registration form to get the updated price information.

### Example

```javascript
import MarketplaceApi from 'marketplace_api';
let defaultClient = MarketplaceApi.ApiClient.instance;
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

let apiInstance = new MarketplaceApi.NotificationApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account that belongs to the marketplace. The notification will be posted into this account.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let environment = "'vtexcommercestable'"; // String | Environment to use. Used as part of the URL.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let sellerId = "'seller123'"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built.
let skuId = "'1234'"; // String | A string that identifies the seller's SKU that suffered the change. This is the ID that the marketplace will use for all  references to this SKU, such as price and inventory notifications.
apiInstance.priceNotification(accountName, contentType, environment, accept, sellerId, skuId, (error, data, response) => {
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
 **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. The notification will be posted into this account. | [default to &#39;apiexamples&#39;]
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **environment** | **String**| Environment to use. Used as part of the URL. | [default to &#39;vtexcommercestable&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built. | [default to &#39;seller123&#39;]
 **skuId** | **String**| A string that identifies the seller&#39;s SKU that suffered the change. This is the ID that the marketplace will use for all  references to this SKU, such as price and inventory notifications. | [default to &#39;1234&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

