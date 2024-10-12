# MicrocksApiV17.MockApi

All URIs are relative to *http://microcks.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteService**](MockApi.md#deleteService) | **DELETE** /services/{id} | Delete Service
[**exportSnapshot**](MockApi.md#exportSnapshot) | **GET** /export | Export a snapshot
[**getService**](MockApi.md#getService) | **GET** /services/{id} | Get Service
[**getServices**](MockApi.md#getServices) | **GET** /services | Get Services and APIs
[**getServicesCounter**](MockApi.md#getServicesCounter) | **GET** /services/count | Get the Services counter
[**getServicesLabels**](MockApi.md#getServicesLabels) | **GET** /services/labels | Get the already used labels for Services
[**importSnapshot**](MockApi.md#importSnapshot) | **POST** /import | Import a snapshot
[**overrideServiceOperation**](MockApi.md#overrideServiceOperation) | **PUT** /services/{id}/operation | Override Service Operation
[**searchServices**](MockApi.md#searchServices) | **GET** /services/search | Search for Services and APIs
[**updateServiceMetadata**](MockApi.md#updateServiceMetadata) | **PUT** /services/{id}/metadata | Update Service Metadata



## deleteService

> deleteService(id)

Delete Service

Delete a Service

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.MockApi();
let id = "id_example"; // String | Unique identifier of Service to managed
apiInstance.deleteService(id, (error, data, response) => {
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
 **id** | **String**| Unique identifier of Service to managed | 

### Return type

null (empty response body)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## exportSnapshot

> File exportSnapshot(serviceIds)

Export a snapshot

Export a repostiory snapshot with requested services

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.MockApi();
let serviceIds = ["null"]; // [String] | List of service identifiers to export
apiInstance.exportSnapshot(serviceIds, (error, data, response) => {
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
 **serviceIds** | [**[String]**](String.md)| List of service identifiers to export | 

### Return type

**File**

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getService

> GetService200Response getService(id, opts)

Get Service

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.MockApi();
let id = "id_example"; // String | Unique identifier of Service to managed
let opts = {
  'messages': true // Boolean | Whether to include details on services messages into result. Default is false
};
apiInstance.getService(id, opts, (error, data, response) => {
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
 **id** | **String**| Unique identifier of Service to managed | 
 **messages** | **Boolean**| Whether to include details on services messages into result. Default is false | [optional] 

### Return type

[**GetService200Response**](GetService200Response.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServices

> Service getServices(opts)

Get Services and APIs

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.MockApi();
let opts = {
  'page': 56, // Number | Page of Services to retrieve (starts at and defaults to 0)
  'size': 56 // Number | Size of a page. Maximum number of Services to include in a response (defaults to 20)
};
apiInstance.getServices(opts, (error, data, response) => {
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
 **page** | **Number**| Page of Services to retrieve (starts at and defaults to 0) | [optional] 
 **size** | **Number**| Size of a page. Maximum number of Services to include in a response (defaults to 20) | [optional] 

### Return type

[**Service**](Service.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServicesCounter

> Counter getServicesCounter()

Get the Services counter

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.MockApi();
apiInstance.getServicesCounter((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Counter**](Counter.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServicesLabels

> {String: Array} getServicesLabels()

Get the already used labels for Services

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.MockApi();
apiInstance.getServicesLabels((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**{String: Array}**

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importSnapshot

> importSnapshot(file)

Import a snapshot

Import a repository snapshot previsouly exported into Microcks

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.MockApi();
let file = "/path/to/file"; // File | The repository snapshot file
apiInstance.importSnapshot(file, (error, data, response) => {
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
 **file** | **File**| The repository snapshot file | 

### Return type

null (empty response body)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


## overrideServiceOperation

> overrideServiceOperation(id, operationName, operationOverrideDTO)

Override Service Operation

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.MockApi();
let id = "id_example"; // String | Unique identifier of Service to managed
let operationName = "operationName_example"; // String | Name of operation to update
let operationOverrideDTO = new MicrocksApiV17.OperationOverrideDTO(); // OperationOverrideDTO | 
apiInstance.overrideServiceOperation(id, operationName, operationOverrideDTO, (error, data, response) => {
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
 **id** | **String**| Unique identifier of Service to managed | 
 **operationName** | **String**| Name of operation to update | 
 **operationOverrideDTO** | [**OperationOverrideDTO**](OperationOverrideDTO.md)|  | 

### Return type

null (empty response body)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## searchServices

> [Service] searchServices(queryMap)

Search for Services and APIs

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.MockApi();
let queryMap = {key: "null"}; // {String: String} | Map of criterion. Key can be simply 'name' with value as the searched string. You can also search by label using keys like 'labels.x' where 'x' is the label and value the label value
apiInstance.searchServices(queryMap, (error, data, response) => {
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
 **queryMap** | [**{String: String}**](String.md)| Map of criterion. Key can be simply &#39;name&#39; with value as the searched string. You can also search by label using keys like &#39;labels.x&#39; where &#39;x&#39; is the label and value the label value | 

### Return type

[**[Service]**](Service.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateServiceMetadata

> updateServiceMetadata(id, metadata)

Update Service Metadata

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.MockApi();
let id = "id_example"; // String | Unique identifier of Service to managed
let metadata = new MicrocksApiV17.Metadata(); // Metadata | 
apiInstance.updateServiceMetadata(id, metadata, (error, data, response) => {
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
 **id** | **String**| Unique identifier of Service to managed | 
 **metadata** | [**Metadata**](Metadata.md)|  | 

### Return type

null (empty response body)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

