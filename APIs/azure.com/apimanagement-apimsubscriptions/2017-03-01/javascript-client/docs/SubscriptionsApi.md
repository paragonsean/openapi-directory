# ApiManagementClient.SubscriptionsApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptionCreateOrUpdate**](SubscriptionsApi.md#subscriptionCreateOrUpdate) | **PUT** /subscriptions/{sid} | 
[**subscriptionDelete**](SubscriptionsApi.md#subscriptionDelete) | **DELETE** /subscriptions/{sid} | 
[**subscriptionGet**](SubscriptionsApi.md#subscriptionGet) | **GET** /subscriptions/{sid} | 
[**subscriptionList**](SubscriptionsApi.md#subscriptionList) | **GET** /subscriptions | 
[**subscriptionRegeneratePrimaryKey**](SubscriptionsApi.md#subscriptionRegeneratePrimaryKey) | **POST** /subscriptions/{sid}/regeneratePrimaryKey | 
[**subscriptionRegenerateSecondaryKey**](SubscriptionsApi.md#subscriptionRegenerateSecondaryKey) | **POST** /subscriptions/{sid}/regenerateSecondaryKey | 
[**subscriptionUpdate**](SubscriptionsApi.md#subscriptionUpdate) | **PATCH** /subscriptions/{sid} | 



## subscriptionCreateOrUpdate

> SubscriptionContract subscriptionCreateOrUpdate(sid, apiVersion, parameters, opts)



Creates or updates the subscription of specified user to the specified product.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.SubscriptionsApi();
let sid = "sid_example"; // String | Subscription entity Identifier. The entity represents the association between a user and a product in API Management.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let parameters = new ApiManagementClient.SubscriptionCreateParameters(); // SubscriptionCreateParameters | Create parameters.
let opts = {
  'notify': "'False'" // String | Notify the subscriber of the subscription state change to Submitted or Active state.
};
apiInstance.subscriptionCreateOrUpdate(sid, apiVersion, parameters, opts, (error, data, response) => {
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
 **sid** | **String**| Subscription entity Identifier. The entity represents the association between a user and a product in API Management. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **parameters** | [**SubscriptionCreateParameters**](SubscriptionCreateParameters.md)| Create parameters. | 
 **notify** | **String**| Notify the subscriber of the subscription state change to Submitted or Active state. | [optional] [default to &#39;False&#39;]

### Return type

[**SubscriptionContract**](SubscriptionContract.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## subscriptionDelete

> subscriptionDelete(sid, ifMatch, apiVersion)



Deletes the specified subscription.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.SubscriptionsApi();
let sid = "sid_example"; // String | Subscription entity Identifier. The entity represents the association between a user and a product in API Management.
let ifMatch = "ifMatch_example"; // String | ETag of the Subscription Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.subscriptionDelete(sid, ifMatch, apiVersion, (error, data, response) => {
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
 **sid** | **String**| Subscription entity Identifier. The entity represents the association between a user and a product in API Management. | 
 **ifMatch** | **String**| ETag of the Subscription Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subscriptionGet

> SubscriptionContract subscriptionGet(sid, apiVersion)



Gets the specified Subscription entity.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.SubscriptionsApi();
let sid = "sid_example"; // String | Subscription entity Identifier. The entity represents the association between a user and a product in API Management.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.subscriptionGet(sid, apiVersion, (error, data, response) => {
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
 **sid** | **String**| Subscription entity Identifier. The entity represents the association between a user and a product in API Management. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**SubscriptionContract**](SubscriptionContract.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subscriptionList

> SubscriptionCollection subscriptionList(apiVersion, opts)



Lists all subscriptions of the API Management service instance.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.SubscriptionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | | Field        | Supported operators    | Supported functions                         | |--------------|------------------------|---------------------------------------------| | id           | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name         | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | stateComment | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | userId       | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | productId    | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | state        | eq                     |                                             |
  'top': 56, // Number | Number of records to return.
  'skip': 56 // Number | Number of records to skip.
};
apiInstance.subscriptionList(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **filter** | **String**| | Field        | Supported operators    | Supported functions                         | |--------------|------------------------|---------------------------------------------| | id           | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name         | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | stateComment | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | userId       | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | productId    | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | state        | eq                     |                                             | | [optional] 
 **top** | **Number**| Number of records to return. | [optional] 
 **skip** | **Number**| Number of records to skip. | [optional] 

### Return type

[**SubscriptionCollection**](SubscriptionCollection.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subscriptionRegeneratePrimaryKey

> subscriptionRegeneratePrimaryKey(sid, apiVersion)



Regenerates primary key of existing subscription of the API Management service instance.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.SubscriptionsApi();
let sid = "sid_example"; // String | Subscription entity Identifier. The entity represents the association between a user and a product in API Management.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.subscriptionRegeneratePrimaryKey(sid, apiVersion, (error, data, response) => {
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
 **sid** | **String**| Subscription entity Identifier. The entity represents the association between a user and a product in API Management. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subscriptionRegenerateSecondaryKey

> subscriptionRegenerateSecondaryKey(sid, apiVersion)



Regenerates secondary key of existing subscription of the API Management service instance.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.SubscriptionsApi();
let sid = "sid_example"; // String | Subscription entity Identifier. The entity represents the association between a user and a product in API Management.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.subscriptionRegenerateSecondaryKey(sid, apiVersion, (error, data, response) => {
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
 **sid** | **String**| Subscription entity Identifier. The entity represents the association between a user and a product in API Management. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subscriptionUpdate

> subscriptionUpdate(sid, ifMatch, apiVersion, parameters, opts)



Updates the details of a subscription specified by its identifier.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.SubscriptionsApi();
let sid = "sid_example"; // String | Subscription entity Identifier. The entity represents the association between a user and a product in API Management.
let ifMatch = "ifMatch_example"; // String | ETag of the Subscription Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let parameters = new ApiManagementClient.SubscriptionUpdateParameters(); // SubscriptionUpdateParameters | Update parameters.
let opts = {
  'notify': "'False'" // String | Notify the subscriber of the subscription state change to Submitted or Active state.
};
apiInstance.subscriptionUpdate(sid, ifMatch, apiVersion, parameters, opts, (error, data, response) => {
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
 **sid** | **String**| Subscription entity Identifier. The entity represents the association between a user and a product in API Management. | 
 **ifMatch** | **String**| ETag of the Subscription Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **parameters** | [**SubscriptionUpdateParameters**](SubscriptionUpdateParameters.md)| Update parameters. | 
 **notify** | **String**| Notify the subscriber of the subscription state change to Submitted or Active state. | [optional] [default to &#39;False&#39;]

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

