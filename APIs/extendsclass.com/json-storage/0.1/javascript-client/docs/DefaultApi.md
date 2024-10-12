# JsonStorage.DefaultApi

All URIs are relative to *https://extendsclass.com/api/json-storage*

Method | HTTP request | Description
------------- | ------------- | -------------
[**binIdDelete**](DefaultApi.md#binIdDelete) | **DELETE** /bin/{id} | Delete a json bin
[**binIdGet**](DefaultApi.md#binIdGet) | **GET** /bin/{id} | Return a json bin
[**binIdPatch**](DefaultApi.md#binIdPatch) | **PATCH** /bin/{id} | Partially update a json bin with JSON Merge Patch
[**binIdPut**](DefaultApi.md#binIdPut) | **PUT** /bin/{id} | Update a json bin
[**binPost**](DefaultApi.md#binPost) | **POST** /bin | Create a json bin



## binIdDelete

> DeleteStatus binIdDelete(id)

Delete a json bin

### Example

```javascript
import JsonStorage from 'json_storage';

let apiInstance = new JsonStorage.DefaultApi();
let id = "id_example"; // String | 
apiInstance.binIdDelete(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**DeleteStatus**](DeleteStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## binIdGet

> Object binIdGet(id)

Return a json bin

### Example

```javascript
import JsonStorage from 'json_storage';

let apiInstance = new JsonStorage.DefaultApi();
let id = "id_example"; // String | 
apiInstance.binIdGet(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## binIdPatch

> UpdateStatus binIdPatch(id)

Partially update a json bin with JSON Merge Patch

### Example

```javascript
import JsonStorage from 'json_storage';

let apiInstance = new JsonStorage.DefaultApi();
let id = "id_example"; // String | 
apiInstance.binIdPatch(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**UpdateStatus**](UpdateStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## binIdPut

> UpdateStatus binIdPut(id)

Update a json bin

### Example

```javascript
import JsonStorage from 'json_storage';

let apiInstance = new JsonStorage.DefaultApi();
let id = "id_example"; // String | 
apiInstance.binIdPut(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**UpdateStatus**](UpdateStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## binPost

> CreateStatus binPost()

Create a json bin

### Example

```javascript
import JsonStorage from 'json_storage';

let apiInstance = new JsonStorage.DefaultApi();
apiInstance.binPost((error, data, response) => {
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

[**CreateStatus**](CreateStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

