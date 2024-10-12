# WireMock.StubMappingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminMappingsDelete**](StubMappingsApi.md#adminMappingsDelete) | **DELETE** /__admin/mappings | Delete all stub mappings
[**adminMappingsFindByMetadataPost**](StubMappingsApi.md#adminMappingsFindByMetadataPost) | **POST** /__admin/mappings/find-by-metadata | 
[**adminMappingsGet**](StubMappingsApi.md#adminMappingsGet) | **GET** /__admin/mappings | Get all stub mappings
[**adminMappingsImportPost**](StubMappingsApi.md#adminMappingsImportPost) | **POST** /__admin/mappings/import | Import stub mappings
[**adminMappingsPost**](StubMappingsApi.md#adminMappingsPost) | **POST** /__admin/mappings | Create a new stub mapping
[**adminMappingsRemoveByMetadataPost**](StubMappingsApi.md#adminMappingsRemoveByMetadataPost) | **POST** /__admin/mappings/remove-by-metadata | Delete stub mappings matching metadata
[**adminMappingsResetPost**](StubMappingsApi.md#adminMappingsResetPost) | **POST** /__admin/mappings/reset | Reset stub mappings
[**adminMappingsSavePost**](StubMappingsApi.md#adminMappingsSavePost) | **POST** /__admin/mappings/save | Persist stub mappings
[**adminMappingsStubMappingIdDelete**](StubMappingsApi.md#adminMappingsStubMappingIdDelete) | **DELETE** /__admin/mappings/{stubMappingId} | Delete a stub mapping
[**adminMappingsStubMappingIdGet**](StubMappingsApi.md#adminMappingsStubMappingIdGet) | **GET** /__admin/mappings/{stubMappingId} | Get stub mapping by ID
[**adminMappingsStubMappingIdPut**](StubMappingsApi.md#adminMappingsStubMappingIdPut) | **PUT** /__admin/mappings/{stubMappingId} | Update a stub mapping



## adminMappingsDelete

> adminMappingsDelete()

Delete all stub mappings

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.StubMappingsApi();
apiInstance.adminMappingsDelete((error, data, response) => {
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


## adminMappingsFindByMetadataPost

> AdminMappingsGet200Response adminMappingsFindByMetadataPost(adminMappingsFindByMetadataPostRequest)



Find stubs by matching on their metadata

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.StubMappingsApi();
let adminMappingsFindByMetadataPostRequest = {"matchesJsonPath":{"equalToJson":"{ \"inner\": 42 }","expression":"$.outer"}}; // AdminMappingsFindByMetadataPostRequest | 
apiInstance.adminMappingsFindByMetadataPost(adminMappingsFindByMetadataPostRequest, (error, data, response) => {
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
 **adminMappingsFindByMetadataPostRequest** | [**AdminMappingsFindByMetadataPostRequest**](AdminMappingsFindByMetadataPostRequest.md)|  | 

### Return type

[**AdminMappingsGet200Response**](AdminMappingsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## adminMappingsGet

> AdminMappingsGet200Response adminMappingsGet(opts)

Get all stub mappings

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.StubMappingsApi();
let opts = {
  'limit': 10, // Number | The maximum number of results to return
  'offset': 0 // Number | The start index of the results to return
};
apiInstance.adminMappingsGet(opts, (error, data, response) => {
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
 **limit** | **Number**| The maximum number of results to return | [optional] 
 **offset** | **Number**| The start index of the results to return | [optional] 

### Return type

[**AdminMappingsGet200Response**](AdminMappingsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adminMappingsImportPost

> adminMappingsImportPost()

Import stub mappings

Import given stub mappings to the backing store

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.StubMappingsApi();
apiInstance.adminMappingsImportPost((error, data, response) => {
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


## adminMappingsPost

> AdminMappingsGet200ResponseMappingsInner adminMappingsPost(opts)

Create a new stub mapping

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.StubMappingsApi();
let opts = {
  'adminMappingsGet200ResponseMappingsInner': {"request":{"method":"GET","url":"/some/thing"},"response":{"body":"Hello world!","headers":{"Content-Type":"text/plain"},"status":200}} // AdminMappingsGet200ResponseMappingsInner | 
};
apiInstance.adminMappingsPost(opts, (error, data, response) => {
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
 **adminMappingsGet200ResponseMappingsInner** | [**AdminMappingsGet200ResponseMappingsInner**](AdminMappingsGet200ResponseMappingsInner.md)|  | [optional] 

### Return type

[**AdminMappingsGet200ResponseMappingsInner**](AdminMappingsGet200ResponseMappingsInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## adminMappingsRemoveByMetadataPost

> adminMappingsRemoveByMetadataPost(opts)

Delete stub mappings matching metadata

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.StubMappingsApi();
let opts = {
  'adminMappingsFindByMetadataPostRequest': {"matchesJsonPath":{"equalToJson":"{ \"inner\": 42 }","expression":"$.outer"}} // AdminMappingsFindByMetadataPostRequest | 
};
apiInstance.adminMappingsRemoveByMetadataPost(opts, (error, data, response) => {
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
- **Accept**: Not defined


## adminMappingsResetPost

> adminMappingsResetPost()

Reset stub mappings

Restores stub mappings to the defaults defined back in the backing store

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.StubMappingsApi();
apiInstance.adminMappingsResetPost((error, data, response) => {
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


## adminMappingsSavePost

> adminMappingsSavePost()

Persist stub mappings

Save all persistent stub mappings to the backing store

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.StubMappingsApi();
apiInstance.adminMappingsSavePost((error, data, response) => {
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


## adminMappingsStubMappingIdDelete

> adminMappingsStubMappingIdDelete(stubMappingId)

Delete a stub mapping

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.StubMappingsApi();
let stubMappingId = "730d3e32-d098-4169-a20c-554c3bedce58"; // String | The UUID of stub mapping
apiInstance.adminMappingsStubMappingIdDelete(stubMappingId, (error, data, response) => {
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
 **stubMappingId** | **String**| The UUID of stub mapping | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## adminMappingsStubMappingIdGet

> AdminMappingsGet200ResponseMappingsInner adminMappingsStubMappingIdGet(stubMappingId)

Get stub mapping by ID

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.StubMappingsApi();
let stubMappingId = "730d3e32-d098-4169-a20c-554c3bedce58"; // String | The UUID of stub mapping
apiInstance.adminMappingsStubMappingIdGet(stubMappingId, (error, data, response) => {
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
 **stubMappingId** | **String**| The UUID of stub mapping | 

### Return type

[**AdminMappingsGet200ResponseMappingsInner**](AdminMappingsGet200ResponseMappingsInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adminMappingsStubMappingIdPut

> AdminMappingsGet200ResponseMappingsInner adminMappingsStubMappingIdPut(stubMappingId, opts)

Update a stub mapping

### Example

```javascript
import WireMock from 'wire_mock';

let apiInstance = new WireMock.StubMappingsApi();
let stubMappingId = "730d3e32-d098-4169-a20c-554c3bedce58"; // String | The UUID of stub mapping
let opts = {
  'adminMappingsGet200ResponseMappingsInner': {"request":{"method":"GET","url":"/some/thing"},"response":{"body":"Hello world!","headers":{"Content-Type":"text/plain"},"status":200}} // AdminMappingsGet200ResponseMappingsInner | 
};
apiInstance.adminMappingsStubMappingIdPut(stubMappingId, opts, (error, data, response) => {
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
 **stubMappingId** | **String**| The UUID of stub mapping | 
 **adminMappingsGet200ResponseMappingsInner** | [**AdminMappingsGet200ResponseMappingsInner**](AdminMappingsGet200ResponseMappingsInner.md)|  | [optional] 

### Return type

[**AdminMappingsGet200ResponseMappingsInner**](AdminMappingsGet200ResponseMappingsInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

