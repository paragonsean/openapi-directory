# ApiEndpoints.DocsApi

All URIs are relative to *https://dash.readme.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createDoc**](DocsApi.md#createDoc) | **POST** /docs | Create doc
[**deleteDoc**](DocsApi.md#deleteDoc) | **DELETE** /docs/{slug} | Delete doc
[**getDoc**](DocsApi.md#getDoc) | **GET** /docs/{slug} | Get doc
[**searchDocs**](DocsApi.md#searchDocs) | **POST** /docs/search | Search docs
[**updateDoc**](DocsApi.md#updateDoc) | **PUT** /docs/{slug} | Update doc



## createDoc

> createDoc(xReadmeVersion, doc)

Create doc

Create a new doc inside of this project

### Example

```javascript
import ApiEndpoints from 'api_endpoints';
let defaultClient = ApiEndpoints.ApiClient.instance;
// Configure HTTP basic authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.username = 'YOUR USERNAME';
apiKey.password = 'YOUR PASSWORD';

let apiInstance = new ApiEndpoints.DocsApi();
let xReadmeVersion = "v3.0"; // String | Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions.
let doc = new ApiEndpoints.Doc(); // Doc | Doc object
apiInstance.createDoc(xReadmeVersion, doc, (error, data, response) => {
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
 **doc** | [**Doc**](Doc.md)| Doc object | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## deleteDoc

> deleteDoc(slug, xReadmeVersion)

Delete doc

Delete the doc with this slug

### Example

```javascript
import ApiEndpoints from 'api_endpoints';
let defaultClient = ApiEndpoints.ApiClient.instance;
// Configure HTTP basic authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.username = 'YOUR USERNAME';
apiKey.password = 'YOUR PASSWORD';

let apiInstance = new ApiEndpoints.DocsApi();
let slug = "new-features"; // String | Slug of doc. must be lowercase, and replace spaces with hyphens. For example, for the page titled \"New Features\", enter the slug \"new-features\"
let xReadmeVersion = "v3.0"; // String | Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions.
apiInstance.deleteDoc(slug, xReadmeVersion, (error, data, response) => {
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
 **slug** | **String**| Slug of doc. must be lowercase, and replace spaces with hyphens. For example, for the page titled \&quot;New Features\&quot;, enter the slug \&quot;new-features\&quot; | 
 **xReadmeVersion** | **String**| Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions. | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDoc

> getDoc(slug, xReadmeVersion)

Get doc

Returns the doc with this slug

### Example

```javascript
import ApiEndpoints from 'api_endpoints';
let defaultClient = ApiEndpoints.ApiClient.instance;
// Configure HTTP basic authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.username = 'YOUR USERNAME';
apiKey.password = 'YOUR PASSWORD';

let apiInstance = new ApiEndpoints.DocsApi();
let slug = "new-features"; // String | Slug of doc. must be lowercase, and replace spaces with hyphens. For example, for the page titled \"New Features\", enter the slug \"new-features\"
let xReadmeVersion = "v3.0"; // String | Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions.
apiInstance.getDoc(slug, xReadmeVersion, (error, data, response) => {
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
 **slug** | **String**| Slug of doc. must be lowercase, and replace spaces with hyphens. For example, for the page titled \&quot;New Features\&quot;, enter the slug \&quot;new-features\&quot; | 
 **xReadmeVersion** | **String**| Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions. | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## searchDocs

> searchDocs(search, xReadmeVersion)

Search docs

Returns all docs that match the search

### Example

```javascript
import ApiEndpoints from 'api_endpoints';
let defaultClient = ApiEndpoints.ApiClient.instance;
// Configure HTTP basic authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.username = 'YOUR USERNAME';
apiKey.password = 'YOUR PASSWORD';

let apiInstance = new ApiEndpoints.DocsApi();
let search = "search_example"; // String | Search string to look for
let xReadmeVersion = "v3.0"; // String | Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions.
apiInstance.searchDocs(search, xReadmeVersion, (error, data, response) => {
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
 **search** | **String**| Search string to look for | 
 **xReadmeVersion** | **String**| Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions. | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateDoc

> updateDoc(slug, xReadmeVersion, doc)

Update doc

Update a doc with this slug

### Example

```javascript
import ApiEndpoints from 'api_endpoints';
let defaultClient = ApiEndpoints.ApiClient.instance;
// Configure HTTP basic authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.username = 'YOUR USERNAME';
apiKey.password = 'YOUR PASSWORD';

let apiInstance = new ApiEndpoints.DocsApi();
let slug = "new-features"; // String | Slug of doc. must be lowercase, and replace spaces with hyphens. For example, for the page titled \"New Features\", enter the slug \"new-features\"
let xReadmeVersion = "v3.0"; // String | Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions.
let doc = new ApiEndpoints.Doc(); // Doc | Doc object
apiInstance.updateDoc(slug, xReadmeVersion, doc, (error, data, response) => {
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
 **slug** | **String**| Slug of doc. must be lowercase, and replace spaces with hyphens. For example, for the page titled \&quot;New Features\&quot;, enter the slug \&quot;new-features\&quot; | 
 **xReadmeVersion** | **String**| Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions. | 
 **doc** | [**Doc**](Doc.md)| Doc object | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

