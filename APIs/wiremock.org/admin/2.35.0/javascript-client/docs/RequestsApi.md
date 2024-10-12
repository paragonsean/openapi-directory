# WireMock.RequestsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminRequestsCountPost**](RequestsApi.md#adminRequestsCountPost) | **POST** /__admin/requests/count | Count requests by criteria
[**adminRequestsDelete**](RequestsApi.md#adminRequestsDelete) | **DELETE** /__admin/requests | Delete all requests in journal
[**adminRequestsFindPost**](RequestsApi.md#adminRequestsFindPost) | **POST** /__admin/requests/find | Find requests by criteria
[**adminRequestsGet**](RequestsApi.md#adminRequestsGet) | **GET** /__admin/requests | Get all requests in journal
[**adminRequestsRemoveByMetadataPost**](RequestsApi.md#adminRequestsRemoveByMetadataPost) | **POST** /__admin/requests/remove-by-metadata | Delete requests mappings matching metadata
[**adminRequestsRemovePost**](RequestsApi.md#adminRequestsRemovePost) | **POST** /__admin/requests/remove | Remove requests by criteria
[**adminRequestsRequestIdDelete**](RequestsApi.md#adminRequestsRequestIdDelete) | **DELETE** /__admin/requests/{requestId} | Delete request by ID
[**adminRequestsRequestIdGet**](RequestsApi.md#adminRequestsRequestIdGet) | **GET** /__admin/requests/{requestId} | Get request by ID
[**adminRequestsResetPost**](RequestsApi.md#adminRequestsResetPost) | **POST** /__admin/requests/reset | Empty the request journal
[**adminRequestsUnmatchedGet**](RequestsApi.md#adminRequestsUnmatchedGet) | **GET** /__admin/requests/unmatched | Find unmatched requests



## adminRequestsCountPost

> AdminRequestsCountPost200Response adminRequestsCountPost(adminMappingsGet200ResponseMappingsInnerRequest)

Count requests by criteria

Count requests logged in the journal matching the specified criteria

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.RequestsApi();
let adminMappingsGet200ResponseMappingsInnerRequest = {"headers":{"Content-Type":{"matches":".*/xml"}},"method":"POST","url":"/resource"}; // AdminMappingsGet200ResponseMappingsInnerRequest | 
apiInstance.adminRequestsCountPost(adminMappingsGet200ResponseMappingsInnerRequest, (error, data, response) => {
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
 **adminMappingsGet200ResponseMappingsInnerRequest** | [**AdminMappingsGet200ResponseMappingsInnerRequest**](AdminMappingsGet200ResponseMappingsInnerRequest.md)|  | 

### Return type

[**AdminRequestsCountPost200Response**](AdminRequestsCountPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## adminRequestsDelete

> adminRequestsDelete()

Delete all requests in journal

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.RequestsApi();
apiInstance.adminRequestsDelete((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## adminRequestsFindPost

> adminRequestsFindPost(adminMappingsGet200ResponseMappingsInnerRequest)

Find requests by criteria

Retrieve details of requests logged in the journal matching the specified criteria

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.RequestsApi();
let adminMappingsGet200ResponseMappingsInnerRequest = {"headers":{"Content-Type":{"matches":".*/xml"}},"method":"POST","url":"/resource"}; // AdminMappingsGet200ResponseMappingsInnerRequest | 
apiInstance.adminRequestsFindPost(adminMappingsGet200ResponseMappingsInnerRequest, (error, data, response) => {
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
 **adminMappingsGet200ResponseMappingsInnerRequest** | [**AdminMappingsGet200ResponseMappingsInnerRequest**](AdminMappingsGet200ResponseMappingsInnerRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## adminRequestsGet

> adminRequestsGet(opts)

Get all requests in journal

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.RequestsApi();
let opts = {
  'limit': "10", // String | The maximum number of results to return
  'since': "2016-10-05T12:33:01.000Z" // String | Only return logged requests after this date
};
apiInstance.adminRequestsGet(opts, (error, data, response) => {
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
 **limit** | **String**| The maximum number of results to return | [optional] 
 **since** | **String**| Only return logged requests after this date | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adminRequestsRemoveByMetadataPost

> adminRequestsRemoveByMetadataPost(opts)

Delete requests mappings matching metadata

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.RequestsApi();
let opts = {
  'adminMappingsFindByMetadataPostRequest': {"matchesJsonPath":{"equalToJson":"{ \"inner\": 42 }","expression":"$.outer"}} // AdminMappingsFindByMetadataPostRequest | 
};
apiInstance.adminRequestsRemoveByMetadataPost(opts, (error, data, response) => {
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
 **adminMappingsFindByMetadataPostRequest** | [**AdminMappingsFindByMetadataPostRequest**](AdminMappingsFindByMetadataPostRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## adminRequestsRemovePost

> adminRequestsRemovePost(adminMappingsGet200ResponseMappingsInnerRequest)

Remove requests by criteria

Removed requests logged in the journal matching the specified criteria

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.RequestsApi();
let adminMappingsGet200ResponseMappingsInnerRequest = {"headers":{"Content-Type":{"matches":".*/xml"}},"method":"POST","url":"/resource"}; // AdminMappingsGet200ResponseMappingsInnerRequest | 
apiInstance.adminRequestsRemovePost(adminMappingsGet200ResponseMappingsInnerRequest, (error, data, response) => {
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
 **adminMappingsGet200ResponseMappingsInnerRequest** | [**AdminMappingsGet200ResponseMappingsInnerRequest**](AdminMappingsGet200ResponseMappingsInnerRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## adminRequestsRequestIdDelete

> adminRequestsRequestIdDelete(requestId)

Delete request by ID

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.RequestsApi();
let requestId = "12fb14bb-600e-4bfa-bd8d-be7f12562c99"; // String | The UUID of the logged request
apiInstance.adminRequestsRequestIdDelete(requestId, (error, data, response) => {
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
 **requestId** | **String**| The UUID of the logged request | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## adminRequestsRequestIdGet

> adminRequestsRequestIdGet(requestId)

Get request by ID

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.RequestsApi();
let requestId = "12fb14bb-600e-4bfa-bd8d-be7f12562c99"; // String | The UUID of the logged request
apiInstance.adminRequestsRequestIdGet(requestId, (error, data, response) => {
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
 **requestId** | **String**| The UUID of the logged request | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adminRequestsResetPost

> adminRequestsResetPost()

Empty the request journal

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.RequestsApi();
apiInstance.adminRequestsResetPost((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## adminRequestsUnmatchedGet

> adminRequestsUnmatchedGet()

Find unmatched requests

Get details of logged requests that weren&#39;t matched by any stub mapping

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.RequestsApi();
apiInstance.adminRequestsUnmatchedGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

