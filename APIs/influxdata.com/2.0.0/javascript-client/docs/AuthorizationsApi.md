# InfluxOssApiService.AuthorizationsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteAuthorizationsID**](AuthorizationsApi.md#deleteAuthorizationsID) | **DELETE** /authorizations/{authID} | Delete an authorization
[**getAuthorizations**](AuthorizationsApi.md#getAuthorizations) | **GET** /authorizations | List all authorizations
[**getAuthorizationsID**](AuthorizationsApi.md#getAuthorizationsID) | **GET** /authorizations/{authID} | Retrieve an authorization
[**patchAuthorizationsID**](AuthorizationsApi.md#patchAuthorizationsID) | **PATCH** /authorizations/{authID} | Update an authorization to be active or inactive
[**postAuthorizations**](AuthorizationsApi.md#postAuthorizations) | **POST** /authorizations | Create an authorization



## deleteAuthorizationsID

> deleteAuthorizationsID(authID, opts)

Delete an authorization

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.AuthorizationsApi();
let authID = "authID_example"; // String | The ID of the authorization to delete.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteAuthorizationsID(authID, opts, (error, data, response) => {
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
 **authID** | **String**| The ID of the authorization to delete. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAuthorizations

> Authorizations getAuthorizations(opts)

List all authorizations

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.AuthorizationsApi();
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'userID': "userID_example", // String | Only show authorizations that belong to a user ID.
  'user': "user_example", // String | Only show authorizations that belong to a user name.
  'orgID': "orgID_example", // String | Only show authorizations that belong to an organization ID.
  'org': "org_example" // String | Only show authorizations that belong to a organization name.
};
apiInstance.getAuthorizations(opts, (error, data, response) => {
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
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 
 **userID** | **String**| Only show authorizations that belong to a user ID. | [optional] 
 **user** | **String**| Only show authorizations that belong to a user name. | [optional] 
 **orgID** | **String**| Only show authorizations that belong to an organization ID. | [optional] 
 **org** | **String**| Only show authorizations that belong to a organization name. | [optional] 

### Return type

[**Authorizations**](Authorizations.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAuthorizationsID

> Authorization getAuthorizationsID(authID, opts)

Retrieve an authorization

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.AuthorizationsApi();
let authID = "authID_example"; // String | The ID of the authorization to get.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getAuthorizationsID(authID, opts, (error, data, response) => {
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
 **authID** | **String**| The ID of the authorization to get. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Authorization**](Authorization.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchAuthorizationsID

> Authorization patchAuthorizationsID(authID, authorizationUpdateRequest, opts)

Update an authorization to be active or inactive

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.AuthorizationsApi();
let authID = "authID_example"; // String | The ID of the authorization to update.
let authorizationUpdateRequest = new InfluxOssApiService.AuthorizationUpdateRequest(); // AuthorizationUpdateRequest | Authorization to update
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.patchAuthorizationsID(authID, authorizationUpdateRequest, opts, (error, data, response) => {
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
 **authID** | **String**| The ID of the authorization to update. | 
 **authorizationUpdateRequest** | [**AuthorizationUpdateRequest**](AuthorizationUpdateRequest.md)| Authorization to update | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Authorization**](Authorization.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postAuthorizations

> Authorization postAuthorizations(authorizationPostRequest, opts)

Create an authorization

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.AuthorizationsApi();
let authorizationPostRequest = new InfluxOssApiService.AuthorizationPostRequest(); // AuthorizationPostRequest | Authorization to create
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postAuthorizations(authorizationPostRequest, opts, (error, data, response) => {
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
 **authorizationPostRequest** | [**AuthorizationPostRequest**](AuthorizationPostRequest.md)| Authorization to create | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Authorization**](Authorization.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

