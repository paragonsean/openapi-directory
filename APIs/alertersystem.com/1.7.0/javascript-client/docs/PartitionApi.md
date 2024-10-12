# AlerterSystemApi.PartitionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiPartitionGetCollection**](PartitionApi.md#apiPartitionGetCollection) | **GET** /api/partition | Retrieves the collection of Partition resources.
[**apiPartitionIdDelete**](PartitionApi.md#apiPartitionIdDelete) | **DELETE** /api/partition/{id} | Removes the Partition resource.
[**apiPartitionIdGet**](PartitionApi.md#apiPartitionIdGet) | **GET** /api/partition/{id} | Retrieves a Partition resource.
[**apiPartitionIdPatch**](PartitionApi.md#apiPartitionIdPatch) | **PATCH** /api/partition/{id} | Updates the Partition resource.
[**apiPartitionIdPut**](PartitionApi.md#apiPartitionIdPut) | **PUT** /api/partition/{id} | Replaces the Partition resource.
[**apiPartitionPost**](PartitionApi.md#apiPartitionPost) | **POST** /api/partition | Creates a Partition resource.



## apiPartitionGetCollection

> [PartitionGet] apiPartitionGetCollection(opts)

Retrieves the collection of Partition resources.

Retrieves the collection of Partition resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.PartitionApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiPartitionGetCollection(opts, (error, data, response) => {
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
 **page** | **Number**| The collection page number | [optional] [default to 1]
 **dataSegmentCode** | **String**|  | [optional] 
 **dataSegmentCode2** | [**[String]**](String.md)|  | [optional] 
 **properties** | [**[String]**](String.md)| Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty} | [optional] 

### Return type

[**[PartitionGet]**](PartitionGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiPartitionIdDelete

> apiPartitionIdDelete(id)

Removes the Partition resource.

Removes the Partition resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.PartitionApi();
let id = "id_example"; // String | Partition identifier
apiInstance.apiPartitionIdDelete(id, (error, data, response) => {
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
 **id** | **String**| Partition identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiPartitionIdGet

> PartitionGet apiPartitionIdGet(id)

Retrieves a Partition resource.

Retrieves a Partition resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.PartitionApi();
let id = "id_example"; // String | Partition identifier
apiInstance.apiPartitionIdGet(id, (error, data, response) => {
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
 **id** | **String**| Partition identifier | 

### Return type

[**PartitionGet**](PartitionGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiPartitionIdPatch

> PartitionGet apiPartitionIdPatch(id, partitionPatch)

Updates the Partition resource.

Updates the Partition resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.PartitionApi();
let id = "id_example"; // String | Partition identifier
let partitionPatch = new AlerterSystemApi.PartitionPatch(); // PartitionPatch | The updated Partition resource
apiInstance.apiPartitionIdPatch(id, partitionPatch, (error, data, response) => {
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
 **id** | **String**| Partition identifier | 
 **partitionPatch** | [**PartitionPatch**](PartitionPatch.md)| The updated Partition resource | 

### Return type

[**PartitionGet**](PartitionGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiPartitionIdPut

> PartitionGet apiPartitionIdPut(id, partitionPut)

Replaces the Partition resource.

Replaces the Partition resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.PartitionApi();
let id = "id_example"; // String | Partition identifier
let partitionPut = new AlerterSystemApi.PartitionPut(); // PartitionPut | The updated Partition resource
apiInstance.apiPartitionIdPut(id, partitionPut, (error, data, response) => {
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
 **id** | **String**| Partition identifier | 
 **partitionPut** | [**PartitionPut**](PartitionPut.md)| The updated Partition resource | 

### Return type

[**PartitionGet**](PartitionGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiPartitionPost

> PartitionGet apiPartitionPost(partitionPost)

Creates a Partition resource.

Creates a Partition resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.PartitionApi();
let partitionPost = new AlerterSystemApi.PartitionPost(); // PartitionPost | The new Partition resource
apiInstance.apiPartitionPost(partitionPost, (error, data, response) => {
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
 **partitionPost** | [**PartitionPost**](PartitionPost.md)| The new Partition resource | 

### Return type

[**PartitionGet**](PartitionGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

