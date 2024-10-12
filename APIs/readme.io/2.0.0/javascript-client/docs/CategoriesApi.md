# ApiEndpoints.CategoriesApi

All URIs are relative to *https://dash.readme.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCategory**](CategoriesApi.md#getCategory) | **GET** /categories/{slug} | Get category
[**getCategoryDocs**](CategoriesApi.md#getCategoryDocs) | **GET** /categories/{slug}/docs | Get docs for category



## getCategory

> getCategory(slug, xReadmeVersion)

Get category

Returns the category with this slug

### Example

```javascript
import ApiEndpoints from 'api_endpoints';
let defaultClient = ApiEndpoints.ApiClient.instance;
// Configure HTTP basic authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.username = 'YOUR USERNAME';
apiKey.password = 'YOUR PASSWORD';

let apiInstance = new ApiEndpoints.CategoriesApi();
let slug = "getting-started"; // String | Slug of category. Slugs must be all lowercase, and replace spaces with hyphens. For example, for the the category \"Getting Started\", enter the slug \"getting-started\"
let xReadmeVersion = "v3.0"; // String | Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions.
apiInstance.getCategory(slug, xReadmeVersion, (error, data, response) => {
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
 **slug** | **String**| Slug of category. Slugs must be all lowercase, and replace spaces with hyphens. For example, for the the category \&quot;Getting Started\&quot;, enter the slug \&quot;getting-started\&quot; | 
 **xReadmeVersion** | **String**| Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions. | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getCategoryDocs

> getCategoryDocs(slug, xReadmeVersion)

Get docs for category

Returns the docs and children docs within this category

### Example

```javascript
import ApiEndpoints from 'api_endpoints';
let defaultClient = ApiEndpoints.ApiClient.instance;
// Configure HTTP basic authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.username = 'YOUR USERNAME';
apiKey.password = 'YOUR PASSWORD';

let apiInstance = new ApiEndpoints.CategoriesApi();
let slug = "getting-started"; // String | Slug of category. Slugs must be all lowercase, and replace spaces with hyphens. For example, for the the category \"Getting Started\", enter the slug \"getting-started\"
let xReadmeVersion = "v3.0"; // String | Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions.
apiInstance.getCategoryDocs(slug, xReadmeVersion, (error, data, response) => {
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
 **slug** | **String**| Slug of category. Slugs must be all lowercase, and replace spaces with hyphens. For example, for the the category \&quot;Getting Started\&quot;, enter the slug \&quot;getting-started\&quot; | 
 **xReadmeVersion** | **String**| Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions. | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

