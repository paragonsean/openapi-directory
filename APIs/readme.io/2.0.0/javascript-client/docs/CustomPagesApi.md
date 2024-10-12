# ApiEndpoints.CustomPagesApi

All URIs are relative to *https://dash.readme.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCustomPage**](CustomPagesApi.md#createCustomPage) | **POST** /custompages | Create custom page
[**deleteCustomPage**](CustomPagesApi.md#deleteCustomPage) | **DELETE** /custompages/{slug} | Delete custom page
[**getCustomPage**](CustomPagesApi.md#getCustomPage) | **GET** /custompages/{slug} | Get custom page
[**getCustomPages**](CustomPagesApi.md#getCustomPages) | **GET** /custompages | Get custom pages
[**updateCustomPage**](CustomPagesApi.md#updateCustomPage) | **PUT** /custompages/{slug} | Update custom page



## createCustomPage

> createCustomPage(customPage)

Create custom page

Create a new custom page inside of this project

### Example

```javascript
import ApiEndpoints from 'api_endpoints';
let defaultClient = ApiEndpoints.ApiClient.instance;
// Configure HTTP basic authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.username = 'YOUR USERNAME';
apiKey.password = 'YOUR PASSWORD';

let apiInstance = new ApiEndpoints.CustomPagesApi();
let customPage = new ApiEndpoints.CustomPage(); // CustomPage | CustomPage object
apiInstance.createCustomPage(customPage, (error, data, response) => {
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
 **customPage** | [**CustomPage**](CustomPage.md)| CustomPage object | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## deleteCustomPage

> deleteCustomPage(slug)

Delete custom page

Delete the custom page with this slug

### Example

```javascript
import ApiEndpoints from 'api_endpoints';
let defaultClient = ApiEndpoints.ApiClient.instance;
// Configure HTTP basic authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.username = 'YOUR USERNAME';
apiKey.password = 'YOUR PASSWORD';

let apiInstance = new ApiEndpoints.CustomPagesApi();
let slug = "slug_example"; // String | Slug of custom page
apiInstance.deleteCustomPage(slug, (error, data, response) => {
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
 **slug** | **String**| Slug of custom page | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getCustomPage

> getCustomPage(slug)

Get custom page

Returns the custom page with this slug

### Example

```javascript
import ApiEndpoints from 'api_endpoints';
let defaultClient = ApiEndpoints.ApiClient.instance;
// Configure HTTP basic authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.username = 'YOUR USERNAME';
apiKey.password = 'YOUR PASSWORD';

let apiInstance = new ApiEndpoints.CustomPagesApi();
let slug = "slug_example"; // String | Slug of custom page
apiInstance.getCustomPage(slug, (error, data, response) => {
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
 **slug** | **String**| Slug of custom page | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getCustomPages

> getCustomPages(opts)

Get custom pages

Returns a list of custom pages associated with the project API key

### Example

```javascript
import ApiEndpoints from 'api_endpoints';
let defaultClient = ApiEndpoints.ApiClient.instance;
// Configure HTTP basic authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.username = 'YOUR USERNAME';
apiKey.password = 'YOUR PASSWORD';

let apiInstance = new ApiEndpoints.CustomPagesApi();
let opts = {
  'perPage': 10, // Number | Number of items to include in pagination (up to 100, defaults to 10)
  'page': 1 // Number | Used to specify further pages (starts at 1)
};
apiInstance.getCustomPages(opts, (error, data, response) => {
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
 **perPage** | **Number**| Number of items to include in pagination (up to 100, defaults to 10) | [optional] [default to 10]
 **page** | **Number**| Used to specify further pages (starts at 1) | [optional] [default to 1]

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateCustomPage

> updateCustomPage(slug, customPage)

Update custom page

Update a custom page with this slug

### Example

```javascript
import ApiEndpoints from 'api_endpoints';
let defaultClient = ApiEndpoints.ApiClient.instance;
// Configure HTTP basic authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.username = 'YOUR USERNAME';
apiKey.password = 'YOUR PASSWORD';

let apiInstance = new ApiEndpoints.CustomPagesApi();
let slug = "slug_example"; // String | Slug of custom page
let customPage = new ApiEndpoints.CustomPage(); // CustomPage | CustomPage object
apiInstance.updateCustomPage(slug, customPage, (error, data, response) => {
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
 **slug** | **String**| Slug of custom page | 
 **customPage** | [**CustomPage**](CustomPage.md)| CustomPage object | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

