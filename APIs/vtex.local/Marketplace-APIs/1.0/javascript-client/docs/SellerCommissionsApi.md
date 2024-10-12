# MarketplaceApi.SellerCommissionsApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkUpsertSellerCommissions**](SellerCommissionsApi.md#bulkUpsertSellerCommissions) | **PUT** /seller-register/pvt/sellers/{sellerId}/commissions/categories | Upsert Seller Commissions in Bulk
[**listSellerCommissions**](SellerCommissionsApi.md#listSellerCommissions) | **GET** /seller-register/pvt/sellers/{sellerId}/commissions | List Seller Commissions by seller ID
[**removeSellerCommissions**](SellerCommissionsApi.md#removeSellerCommissions) | **DELETE** /seller-register/pvt/sellers/{sellerId}/commissions/{categoryId} | Remove Seller Commissions by Category ID
[**retrieveSellerCommissions**](SellerCommissionsApi.md#retrieveSellerCommissions) | **GET** /seller-register/pvt/sellers/{sellerId}/commissions/{categoryId} | Get Seller Commissions by Category ID
[**upsertSellerCommissions**](SellerCommissionsApi.md#upsertSellerCommissions) | **PUT** /seller-register/pvt/sellers/{sellerId}/commissions/{categoryId} | Upsert Seller Commissions by Category ID



## bulkUpsertSellerCommissions

> bulkUpsertSellerCommissions(accountName, environment, accept, contentType, sellerId, bulkUpsertSellerCommissionsRequest)

Upsert Seller Commissions in Bulk

This endpoint is used by marketplace operators to define comissions for multiple categories.

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

let apiInstance = new MarketplaceApi.SellerCommissionsApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
let environment = "'vtexcommercestable'"; // String | Environment to use. Used as part of the URL.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let sellerId = "'seller123'"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
let bulkUpsertSellerCommissionsRequest = [{"categoryFullPath":null,"categoryId":"6","freightCommissionPercentage":2.43,"productCommissionPercentage":9.85}]; // [BulkUpsertSellerCommissionsRequest] | 
apiInstance.bulkUpsertSellerCommissions(accountName, environment, accept, contentType, sellerId, bulkUpsertSellerCommissionsRequest, (error, data, response) => {
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
 **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account. | [default to &#39;apiexamples&#39;]
 **environment** | **String**| Environment to use. Used as part of the URL. | [default to &#39;vtexcommercestable&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace. | [default to &#39;seller123&#39;]
 **bulkUpsertSellerCommissionsRequest** | [**[BulkUpsertSellerCommissionsRequest]**](BulkUpsertSellerCommissionsRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## listSellerCommissions

> listSellerCommissions(accountName, environment, sellerId, accept, contentType)

List Seller Commissions by seller ID

This endpoint retrieves all comissions configured for a specific seller.

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

let apiInstance = new MarketplaceApi.SellerCommissionsApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
let environment = "'vtexcommercestable'"; // String | Environment to use. Used as part of the URL.
let sellerId = "'seller123'"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
apiInstance.listSellerCommissions(accountName, environment, sellerId, accept, contentType, (error, data, response) => {
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
 **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account. | [default to &#39;apiexamples&#39;]
 **environment** | **String**| Environment to use. Used as part of the URL. | [default to &#39;vtexcommercestable&#39;]
 **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace. | [default to &#39;seller123&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## removeSellerCommissions

> removeSellerCommissions(accountName, environment, accept, contentType, sellerId, categoryId)

Remove Seller Commissions by Category ID

This endpoint removes a seller comission on the selected category.

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

let apiInstance = new MarketplaceApi.SellerCommissionsApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
let environment = "'vtexcommercestable'"; // String | Environment to use. Used as part of the URL.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let sellerId = "'seller123'"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
let categoryId = "'6'"; // String | ID of the category in which the comission was applied
apiInstance.removeSellerCommissions(accountName, environment, accept, contentType, sellerId, categoryId, (error, data, response) => {
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
 **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account. | [default to &#39;apiexamples&#39;]
 **environment** | **String**| Environment to use. Used as part of the URL. | [default to &#39;vtexcommercestable&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace. | [default to &#39;seller123&#39;]
 **categoryId** | **String**| ID of the category in which the comission was applied | [default to &#39;6&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## retrieveSellerCommissions

> retrieveSellerCommissions(accountName, environment, accept, contentType, sellerId, categoryId)

Get Seller Commissions by Category ID

This endpoint retrieves seller comissions applied to the selected category.

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

let apiInstance = new MarketplaceApi.SellerCommissionsApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
let environment = "'vtexcommercestable'"; // String | Environment to use. Used as part of the URL.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let sellerId = "'seller123'"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
let categoryId = "'6'"; // String | ID of the category in which the comission was applied
apiInstance.retrieveSellerCommissions(accountName, environment, accept, contentType, sellerId, categoryId, (error, data, response) => {
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
 **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account. | [default to &#39;apiexamples&#39;]
 **environment** | **String**| Environment to use. Used as part of the URL. | [default to &#39;vtexcommercestable&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace. | [default to &#39;seller123&#39;]
 **categoryId** | **String**| ID of the category in which the comission was applied | [default to &#39;6&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## upsertSellerCommissions

> upsertSellerCommissions(accountName, environment, sellerId, categoryId, accept, contentType, upsertSellerCommissionsRequest)

Upsert Seller Commissions by Category ID

This endpoint is used by marketplace operators to define comissions for a single category, by ID.

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

let apiInstance = new MarketplaceApi.SellerCommissionsApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
let environment = "'vtexcommercestable'"; // String | Environment to use. Used as part of the URL.
let sellerId = "'seller123'"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
let categoryId = "'6'"; // String | ID of the category in which the comission will be applied.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let upsertSellerCommissionsRequest = {"categoryFullPath":null,"categoryId":"6","freightCommissionPercentage":2.43,"productCommissionPercentage":9.85}; // UpsertSellerCommissionsRequest | 
apiInstance.upsertSellerCommissions(accountName, environment, sellerId, categoryId, accept, contentType, upsertSellerCommissionsRequest, (error, data, response) => {
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
 **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account. | [default to &#39;apiexamples&#39;]
 **environment** | **String**| Environment to use. Used as part of the URL. | [default to &#39;vtexcommercestable&#39;]
 **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace. | [default to &#39;seller123&#39;]
 **categoryId** | **String**| ID of the category in which the comission will be applied. | [default to &#39;6&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **upsertSellerCommissionsRequest** | [**UpsertSellerCommissionsRequest**](UpsertSellerCommissionsRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

