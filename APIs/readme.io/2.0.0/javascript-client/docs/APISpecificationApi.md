# ApiEndpoints.APISpecificationApi

All URIs are relative to *https://dash.readme.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteAPISpecification**](APISpecificationApi.md#deleteAPISpecification) | **DELETE** /api-specification/{id} | 
[**getAPISpecification**](APISpecificationApi.md#getAPISpecification) | **GET** /api-specification | 
[**updateAPISpecification**](APISpecificationApi.md#updateAPISpecification) | **PUT** /api-specification/{id} | 
[**uploadAPISpecification**](APISpecificationApi.md#uploadAPISpecification) | **POST** /api-specification | 



## deleteAPISpecification

> deleteAPISpecification(id)



Delete an API specification in ReadMe

### Example

```javascript
import ApiEndpoints from 'api_endpoints';
let defaultClient = ApiEndpoints.ApiClient.instance;
// Configure HTTP basic authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.username = 'YOUR USERNAME';
apiKey.password = 'YOUR PASSWORD';

let apiInstance = new ApiEndpoints.APISpecificationApi();
let id = "id_example"; // String | ID of the API specification. The unique ID for each API can be found by navigating to your **API Definitions** page.
apiInstance.deleteAPISpecification(id, (error, data, response) => {
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
 **id** | **String**| ID of the API specification. The unique ID for each API can be found by navigating to your **API Definitions** page. | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAPISpecification

> getAPISpecification(xReadmeVersion, opts)



Get API specification metadata

### Example

```javascript
import ApiEndpoints from 'api_endpoints';
let defaultClient = ApiEndpoints.ApiClient.instance;
// Configure HTTP basic authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.username = 'YOUR USERNAME';
apiKey.password = 'YOUR PASSWORD';

let apiInstance = new ApiEndpoints.APISpecificationApi();
let xReadmeVersion = "v3.0"; // String | Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions.
let opts = {
  'perPage': 10, // Number | Number of items to include in pagination (up to 100, defaults to 10)
  'page': 1 // Number | Used to specify further pages (starts at 1)
};
apiInstance.getAPISpecification(xReadmeVersion, opts, (error, data, response) => {
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
 **xReadmeVersion** | **String**| Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions. | 
 **perPage** | **Number**| Number of items to include in pagination (up to 100, defaults to 10) | [optional] [default to 10]
 **page** | **Number**| Used to specify further pages (starts at 1) | [optional] [default to 1]

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateAPISpecification

> updateAPISpecification(id, opts)



Update an API specification in ReadMe

### Example

```javascript
import ApiEndpoints from 'api_endpoints';
let defaultClient = ApiEndpoints.ApiClient.instance;
// Configure HTTP basic authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.username = 'YOUR USERNAME';
apiKey.password = 'YOUR PASSWORD';

let apiInstance = new ApiEndpoints.APISpecificationApi();
let id = "id_example"; // String | ID of the API specification. The unique ID for each API can be found by navigating to your **API Definitions** page.
let opts = {
  'spec': "/path/to/file" // File | OpenAPI/Swagger file
};
apiInstance.updateAPISpecification(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the API specification. The unique ID for each API can be found by navigating to your **API Definitions** page. | 
 **spec** | **File**| OpenAPI/Swagger file | [optional] 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


## uploadAPISpecification

> uploadAPISpecification(xReadmeVersion, opts)



Upload an API specification to ReadMe. Or, to use a newer solution see https://docs.readme.com/guides/docs/automatically-sync-api-specification-with-github

### Example

```javascript
import ApiEndpoints from 'api_endpoints';
let defaultClient = ApiEndpoints.ApiClient.instance;
// Configure HTTP basic authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.username = 'YOUR USERNAME';
apiKey.password = 'YOUR PASSWORD';

let apiInstance = new ApiEndpoints.APISpecificationApi();
let xReadmeVersion = "v3.0"; // String | Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions.
let opts = {
  'spec': "/path/to/file" // File | OpenAPI/Swagger file
};
apiInstance.uploadAPISpecification(xReadmeVersion, opts, (error, data, response) => {
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
 **xReadmeVersion** | **String**| Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions. | 
 **spec** | **File**| OpenAPI/Swagger file | [optional] 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined

