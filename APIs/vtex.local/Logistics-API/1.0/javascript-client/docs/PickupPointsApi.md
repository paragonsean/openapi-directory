# LogisticsApi.PickupPointsApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**callDelete**](PickupPointsApi.md#callDelete) | **DELETE** /api/logistics/pvt/configuration/pickuppoints/{pickupPointId} | Delete Pickup Point
[**createUpdatePickupPoint**](PickupPointsApi.md#createUpdatePickupPoint) | **PUT** /api/logistics/pvt/configuration/pickuppoints/{pickupPointId} | Create/Update Pickup Point
[**getById**](PickupPointsApi.md#getById) | **GET** /api/logistics/pvt/configuration/pickuppoints/{pickupPointId} | List Pickup Point By ID
[**getpaged**](PickupPointsApi.md#getpaged) | **GET** /api/logistics/pvt/configuration/pickuppoints/_search | List paged Pickup Points
[**listAllPickupPpoints**](PickupPointsApi.md#listAllPickupPpoints) | **GET** /api/logistics/pvt/configuration/pickuppoints | List all pickup points



## callDelete

> callDelete(contentType, accept, pickupPointId)

Delete Pickup Point

Deletes a given pickup point for your store, by pickup point ID.

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
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

let apiInstance = new LogisticsApi.PickupPointsApi();
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let pickupPointId = "pickupPointId_example"; // String | 
apiInstance.callDelete(contentType, accept, pickupPointId, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json; charset&#x3D;utf-8&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **pickupPointId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createUpdatePickupPoint

> CreateUpdate createUpdatePickupPoint(contentType, accept, pickupPointId, createUpdatePickupPointRequest)

Create/Update Pickup Point

Creates or updates [pickup points](https://help.vtex.com/en/subcategory/pickup-points--1c5Btie9ou2Gg2iUo0ggqM#) in your store by Pickup Point ID.

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
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

let apiInstance = new LogisticsApi.PickupPointsApi();
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let pickupPointId = "123456789"; // String | Pickup Point ID. Cannot contain spaces.
let createUpdatePickupPointRequest = {"address":{"city":"Rio de Janeiro","complement":"","country":{"acronym":"BRA","name":"Brazil"},"location":{"latitude":-22.974477767944336,"longitude":-43.18672561645508},"neighborhood":"Copacabana","number":"","postalCode":"22070002","reference":"Grey building","state":"RJ","street":"Avenida Atl├óntica"},"businessHours":[{"closingTime":72000,"dayOfWeek":1,"openingTime":"08:00:00"},{"closingTime":72000,"dayOfWeek":2,"openingTime":"08:00:00"},{"closingTime":72000,"dayOfWeek":3,"openingTime":"08:00:00"},{"closingTime":72000,"dayOfWeek":4,"openingTime":"08:00:00"},{"closingTime":72000,"dayOfWeek":5,"openingTime":"08:00:00"}],"description":"","formatted_address":"undefined","id":"1a227d3","instructions":"Obrigat├│rio apresentar documento de identifica├º├úo","isActive":true,"name":"Loja Copacabana","tagsLabel":["zonasul","rio de janeiro"]}; // CreateUpdatePickupPointRequest | 
apiInstance.createUpdatePickupPoint(contentType, accept, pickupPointId, createUpdatePickupPointRequest, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json; charset&#x3D;utf-8&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **pickupPointId** | **String**| Pickup Point ID. Cannot contain spaces. | 
 **createUpdatePickupPointRequest** | [**CreateUpdatePickupPointRequest**](CreateUpdatePickupPointRequest.md)|  | 

### Return type

[**CreateUpdate**](CreateUpdate.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json; charset=utf-8
- **Accept**: application/json; charset=utf-8


## getById

> GetById1 getById(contentType, accept, pickupPointId)

List Pickup Point By ID

Lists your store&#39;s pickup points while searching by ID.

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
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

let apiInstance = new LogisticsApi.PickupPointsApi();
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let pickupPointId = "pickupPointId_example"; // String | 
apiInstance.getById(contentType, accept, pickupPointId, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json; charset&#x3D;utf-8&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **pickupPointId** | **String**|  | 

### Return type

[**GetById1**](GetById1.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## getpaged

> getpaged(page, pageSize, keyword, contentType, accept)

List paged Pickup Points

Lists paged pickup points in your store.

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
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

let apiInstance = new LogisticsApi.PickupPointsApi();
let page = "{{pageNumber}}"; // String | 
let pageSize = "{{pageSize}}"; // String | 
let keyword = ""; // String | 
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
apiInstance.getpaged(page, pageSize, keyword, contentType, accept, (error, data, response) => {
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
 **page** | **String**|  | 
 **pageSize** | **String**|  | 
 **keyword** | **String**|  | 
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json; charset&#x3D;utf-8&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listAllPickupPpoints

> [ListAllPickupPpoints200ResponseInner] listAllPickupPpoints(contentType, accept)

List all pickup points

Lists all of your store&#39;s pickup points.

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
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

let apiInstance = new LogisticsApi.PickupPointsApi();
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
apiInstance.listAllPickupPpoints(contentType, accept, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json; charset&#x3D;utf-8&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]

### Return type

[**[ListAllPickupPpoints200ResponseInner]**](ListAllPickupPpoints200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8

