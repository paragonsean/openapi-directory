# ApiEndpoints.ChangelogApi

All URIs are relative to *https://dash.readme.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createChangelog**](ChangelogApi.md#createChangelog) | **POST** /changelogs | Create changelog
[**deleteChangelog**](ChangelogApi.md#deleteChangelog) | **DELETE** /changelogs/{slug} | Delete changelog
[**getChangelog**](ChangelogApi.md#getChangelog) | **GET** /changelogs/{slug} | Get changelog
[**getChangelogs**](ChangelogApi.md#getChangelogs) | **GET** /changelogs | Get changelogs
[**updateChangelog**](ChangelogApi.md#updateChangelog) | **PUT** /changelogs/{slug} | Update changelog



## createChangelog

> createChangelog(changelog)

Create changelog

Create a new changelog inside of this project

### Example

```javascript
import ApiEndpoints from 'api_endpoints';
let defaultClient = ApiEndpoints.ApiClient.instance;
// Configure HTTP basic authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.username = 'YOUR USERNAME';
apiKey.password = 'YOUR PASSWORD';

let apiInstance = new ApiEndpoints.ChangelogApi();
let changelog = new ApiEndpoints.Changelog(); // Changelog | Changelog object
apiInstance.createChangelog(changelog, (error, data, response) => {
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
 **changelog** | [**Changelog**](Changelog.md)| Changelog object | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## deleteChangelog

> deleteChangelog(slug)

Delete changelog

Delete the changelog with this slug

### Example

```javascript
import ApiEndpoints from 'api_endpoints';
let defaultClient = ApiEndpoints.ApiClient.instance;
// Configure HTTP basic authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.username = 'YOUR USERNAME';
apiKey.password = 'YOUR PASSWORD';

let apiInstance = new ApiEndpoints.ChangelogApi();
let slug = "slug_example"; // String | Slug of changelog
apiInstance.deleteChangelog(slug, (error, data, response) => {
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
 **slug** | **String**| Slug of changelog | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getChangelog

> getChangelog(slug)

Get changelog

Returns the changelog with this slug

### Example

```javascript
import ApiEndpoints from 'api_endpoints';
let defaultClient = ApiEndpoints.ApiClient.instance;
// Configure HTTP basic authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.username = 'YOUR USERNAME';
apiKey.password = 'YOUR PASSWORD';

let apiInstance = new ApiEndpoints.ChangelogApi();
let slug = "slug_example"; // String | Slug of changelog
apiInstance.getChangelog(slug, (error, data, response) => {
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
 **slug** | **String**| Slug of changelog | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getChangelogs

> getChangelogs(opts)

Get changelogs

Returns a list of changelogs associated with the project API key

### Example

```javascript
import ApiEndpoints from 'api_endpoints';
let defaultClient = ApiEndpoints.ApiClient.instance;
// Configure HTTP basic authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.username = 'YOUR USERNAME';
apiKey.password = 'YOUR PASSWORD';

let apiInstance = new ApiEndpoints.ChangelogApi();
let opts = {
  'perPage': 10, // Number | Number of items to include in pagination (up to 100, defaults to 10)
  'page': 1 // Number | Used to specify further pages (starts at 1)
};
apiInstance.getChangelogs(opts, (error, data, response) => {
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


## updateChangelog

> updateChangelog(slug, changelog)

Update changelog

Update a changelog with this slug

### Example

```javascript
import ApiEndpoints from 'api_endpoints';
let defaultClient = ApiEndpoints.ApiClient.instance;
// Configure HTTP basic authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.username = 'YOUR USERNAME';
apiKey.password = 'YOUR PASSWORD';

let apiInstance = new ApiEndpoints.ChangelogApi();
let slug = "slug_example"; // String | Slug of changelog
let changelog = new ApiEndpoints.Changelog(); // Changelog | Changelog object
apiInstance.updateChangelog(slug, changelog, (error, data, response) => {
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
 **slug** | **String**| Slug of changelog | 
 **changelog** | [**Changelog**](Changelog.md)| Changelog object | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

