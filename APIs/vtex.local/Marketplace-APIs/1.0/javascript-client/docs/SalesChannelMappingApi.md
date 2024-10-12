# MarketplaceApi.SalesChannelMappingApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieveMapping**](SalesChannelMappingApi.md#retrieveMapping) | **GET** /seller-register/pvt/sellers/{sellerId}/sales-channel/mapping | Get Sales Channel Mapping Data
[**upsertMapping**](SalesChannelMappingApi.md#upsertMapping) | **PUT** /seller-register/pvt/sellers/{sellerId}/sales-channel/mapping | Upsert Sales Channel Mapping



## retrieveMapping

> [Object] retrieveMapping(contentType, accept, accountName, environment, an, sellerId)

Get Sales Channel Mapping Data

Retrieves information about the mapping between marketplace&#39;s sales channels and a specific seller.

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

let apiInstance = new MarketplaceApi.SalesChannelMappingApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let accountName = "'apiexamples'"; // String | Name of the VTEX account that belongs to the marketplace. Used as part of the URL
let environment = "'vtexcommercestable'"; // String | Environment to use. Used as part of the URL.
let an = "'apiexamples'"; // String | Marketplace's account name, the same one inputted on the endpoint's path.
let sellerId = "'seller123'"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
apiInstance.retrieveMapping(contentType, accept, accountName, environment, an, sellerId, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. Used as part of the URL | [default to &#39;apiexamples&#39;]
 **environment** | **String**| Environment to use. Used as part of the URL. | [default to &#39;vtexcommercestable&#39;]
 **an** | **String**| Marketplace&#39;s account name, the same one inputted on the endpoint&#39;s path. | [default to &#39;apiexamples&#39;]
 **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace. | [default to &#39;seller123&#39;]

### Return type

**[Object]**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## upsertMapping

> [Object] upsertMapping(contentType, accept, accountName, environment, an, sellerId, upsertMappingRequest)

Upsert Sales Channel Mapping

This endpoint allows the marketplace to map its sales channels with a seller&#39;s [affiliate](https://help.vtex.com/en/tutorial/configuring-affiliates--tutorials_187). The seller can have multiple sales channels associated with the same marketplace, by creating different affiliates. The mapping enables the seller to segment catalog, prices, inventory, logistics, and payments in the marketplace.

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

let apiInstance = new MarketplaceApi.SalesChannelMappingApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let accountName = "'apiexamples'"; // String | Name of the VTEX account that belongs to the marketplace. Used as part of the URL.
let environment = "'vtexcommercestable'"; // String | Environment to use. Used as part of the URL.
let an = "'apiexamples'"; // String | Marketplace's account name, the same one inputted on the endpoint's path.
let sellerId = "'seller123'"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
let upsertMappingRequest = [{"marketplaceSalesChannel":1,"sellerChannel":"GCB"},{"marketplaceSalesChannel":2,"sellerChannel":"GCB"}]; // [UpsertMappingRequest] | 
apiInstance.upsertMapping(contentType, accept, accountName, environment, an, sellerId, upsertMappingRequest, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. Used as part of the URL. | [default to &#39;apiexamples&#39;]
 **environment** | **String**| Environment to use. Used as part of the URL. | [default to &#39;vtexcommercestable&#39;]
 **an** | **String**| Marketplace&#39;s account name, the same one inputted on the endpoint&#39;s path. | [default to &#39;apiexamples&#39;]
 **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace. | [default to &#39;seller123&#39;]
 **upsertMappingRequest** | [**[UpsertMappingRequest]**](UpsertMappingRequest.md)|  | 

### Return type

**[Object]**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

