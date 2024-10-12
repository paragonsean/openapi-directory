# VRealizeNetworkInsightApiReference.ApplicationsApi

All URIs are relative to *http://vmware.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addApplication**](ApplicationsApi.md#addApplication) | **POST** /groups/applications | Create an application
[**addTier**](ApplicationsApi.md#addTier) | **POST** /groups/applications/{id}/tiers | Create tier in application
[**deleteApplication**](ApplicationsApi.md#deleteApplication) | **DELETE** /groups/applications/{id} | Delete an application
[**deleteTier**](ApplicationsApi.md#deleteTier) | **DELETE** /groups/applications/{id}/tiers/{tier-id} | Delete tier
[**getApplication**](ApplicationsApi.md#getApplication) | **GET** /groups/applications/{id} | Show application details
[**getApplicationTier**](ApplicationsApi.md#getApplicationTier) | **GET** /groups/applications/{id}/tiers/{tier-id} | Show tier details
[**getTier**](ApplicationsApi.md#getTier) | **GET** /groups/tiers/{tier-id} | Show tier details
[**listApplicationTiers**](ApplicationsApi.md#listApplicationTiers) | **GET** /groups/applications/{id}/tiers | List tiers of an application
[**listApplications**](ApplicationsApi.md#listApplications) | **GET** /groups/applications | List applications



## addApplication

> Application addApplication(applicationRequest)

Create an application

Application is a group of tiers. A tier is a group of virtual machines based on membership criteria. Tiers are bound to single application. An application name is unique and should not conflict with another application name.

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.ApplicationsApi();
let applicationRequest = new VRealizeNetworkInsightApiReference.ApplicationRequest(); // ApplicationRequest | 
apiInstance.addApplication(applicationRequest, (error, data, response) => {
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
 **applicationRequest** | [**ApplicationRequest**](ApplicationRequest.md)|  | 

### Return type

[**Application**](Application.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, create_time, created_by, entity_id, entity_type, last_modified_by, last_modified_time, name


## addTier

> addTier(id, tierRequest)

Create tier in application

Create a tier of an application by with specified membership criteria. The membership criteria id defined in terms of virtual machines or ip addresses/subnet. Please refer to API Guide on how to construct membership criteria.

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.ApplicationsApi();
let id = "id_example"; // String | entity id
let tierRequest = new VRealizeNetworkInsightApiReference.TierRequest(); // TierRequest | 
apiInstance.addTier(id, tierRequest, (error, data, response) => {
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
 **id** | **String**| entity id | 
 **tierRequest** | [**TierRequest**](TierRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application, application/json, entity_id, entity_type, group_membership_criteria, name


## deleteApplication

> deleteApplication(id)

Delete an application

Deleting an application deletes all the tiers of the application along with the application

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.ApplicationsApi();
let id = "id_example"; // String | entity id
apiInstance.deleteApplication(id, (error, data, response) => {
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
 **id** | **String**| entity id | 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteTier

> deleteTier(id, tierId)

Delete tier

Delete tier of an application

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.ApplicationsApi();
let id = "id_example"; // String | entity id
let tierId = "tierId_example"; // String | 
apiInstance.deleteTier(id, tierId, (error, data, response) => {
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
 **id** | **String**| entity id | 
 **tierId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getApplication

> Application getApplication(id)

Show application details

Show application details

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.ApplicationsApi();
let id = "id_example"; // String | entity id
apiInstance.getApplication(id, (error, data, response) => {
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
 **id** | **String**| entity id | 

### Return type

[**Application**](Application.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, create_time, created_by, entity_id, entity_type, last_modified_by, last_modified_time, name


## getApplicationTier

> getApplicationTier(id, tierId)

Show tier details

Show tier details

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.ApplicationsApi();
let id = "id_example"; // String | entity id
let tierId = "tierId_example"; // String | 
apiInstance.getApplicationTier(id, tierId, (error, data, response) => {
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
 **id** | **String**| entity id | 
 **tierId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application, application/json, entity_id, entity_type, group_membership_criteria, name


## getTier

> getTier(tierId, authorization)

Show tier details

Show tier details

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.ApplicationsApi();
let tierId = "tierId_example"; // String | 
let authorization = "authorization_example"; // String | Authorization Header
apiInstance.getTier(tierId, authorization, (error, data, response) => {
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
 **tierId** | **String**|  | 
 **authorization** | **String**| Authorization Header | 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application, application/json, entity_id, entity_type, group_membership_criteria, name


## listApplicationTiers

> TierListResponse listApplicationTiers(id)

List tiers of an application

List tiers of an application

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.ApplicationsApi();
let id = "id_example"; // String | entity id
apiInstance.listApplicationTiers(id, (error, data, response) => {
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
 **id** | **String**| entity id | 

### Return type

[**TierListResponse**](TierListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, results


## listApplications

> PagedListResponse listApplications(opts)

List applications

List applications

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.ApplicationsApi();
let opts = {
  'size': 10, // Number | page size of results
  'cursor': "cursor_example", // String | cursor from previous response
  'startTime': 3.4, // Number | start time for query in epoch seconds
  'endTime': 3.4 // Number | end time for query in epoch seconds
};
apiInstance.listApplications(opts, (error, data, response) => {
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
 **size** | **Number**| page size of results | [optional] [default to 10]
 **cursor** | **String**| cursor from previous response | [optional] 
 **startTime** | **Number**| start time for query in epoch seconds | [optional] 
 **endTime** | **Number**| end time for query in epoch seconds | [optional] 

### Return type

[**PagedListResponse**](PagedListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, results, total_count

