# ApiEndpoints.SwaggerApi

All URIs are relative to *https://dash.readme.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteSwagger**](SwaggerApi.md#deleteSwagger) | **DELETE** /swagger/{id} | 
[**updateSwagger**](SwaggerApi.md#updateSwagger) | **PUT** /swagger/{id} | 
[**uploadSwagger**](SwaggerApi.md#uploadSwagger) | **POST** /swagger | 



## deleteSwagger

> deleteSwagger(id)



DEPRECATED. Instead, use https://docs.readme.com/developers/reference/api-specification#deleteapispecification to delete a Swagger file in ReadMe

### Example

```javascript
import ApiEndpoints from 'api_endpoints';
let defaultClient = ApiEndpoints.ApiClient.instance;
// Configure HTTP basic authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.username = 'YOUR USERNAME';
apiKey.password = 'YOUR PASSWORD';

let apiInstance = new ApiEndpoints.SwaggerApi();
let id = "id_example"; // String | ID of swagger the file
apiInstance.deleteSwagger(id, (error, data, response) => {
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
 **id** | **String**| ID of swagger the file | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateSwagger

> updateSwagger(id, opts)



DEPRECATED. Instead, use https://docs.readme.com/developers/reference/api-specification#updateapispecification to update a Swagger file.

### Example

```javascript
import ApiEndpoints from 'api_endpoints';
let defaultClient = ApiEndpoints.ApiClient.instance;
// Configure HTTP basic authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.username = 'YOUR USERNAME';
apiKey.password = 'YOUR PASSWORD';

let apiInstance = new ApiEndpoints.SwaggerApi();
let id = "id_example"; // String | ID of the Swagger file
let opts = {
  'swagger': "/path/to/file" // File | Swagger file
};
apiInstance.updateSwagger(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the Swagger file | 
 **swagger** | **File**| Swagger file | [optional] 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


## uploadSwagger

> uploadSwagger(opts)



DEPRECATED. Instead use https://docs.readme.com/developers/reference/api-specification#uploadapispecification to upload a Swagger file to ReadMe

### Example

```javascript
import ApiEndpoints from 'api_endpoints';
let defaultClient = ApiEndpoints.ApiClient.instance;
// Configure HTTP basic authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.username = 'YOUR USERNAME';
apiKey.password = 'YOUR PASSWORD';

let apiInstance = new ApiEndpoints.SwaggerApi();
let opts = {
  'swagger': "/path/to/file" // File | Swagger file
};
apiInstance.uploadSwagger(opts, (error, data, response) => {
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
 **swagger** | **File**| Swagger file | [optional] 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined

