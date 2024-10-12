# Signl4Api.CategoriesApi

All URIs are relative to *https://connect.signl4.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categoriesImagesGet**](CategoriesApi.md#categoriesImagesGet) | **GET** /categories/images | Gets the names of all alert category images.  You can get the image by going to account.signl4.com/images/alerts/categoryImageName.svg
[**categoriesTeamIdCategoryIdDelete**](CategoriesApi.md#categoriesTeamIdCategoryIdDelete) | **DELETE** /categories/{teamId}/{categoryId} | Delete an existing category
[**categoriesTeamIdCategoryIdGet**](CategoriesApi.md#categoriesTeamIdCategoryIdGet) | **GET** /categories/{teamId}/{categoryId} | Get a specific category
[**categoriesTeamIdCategoryIdMetricsGet**](CategoriesApi.md#categoriesTeamIdCategoryIdMetricsGet) | **GET** /categories/{teamId}/{categoryId}/metrics | Get metrics for a specific category
[**categoriesTeamIdCategoryIdPut**](CategoriesApi.md#categoriesTeamIdCategoryIdPut) | **PUT** /categories/{teamId}/{categoryId} | Update an existing category
[**categoriesTeamIdCategoryIdSubscriptionsGet**](CategoriesApi.md#categoriesTeamIdCategoryIdSubscriptionsGet) | **GET** /categories/{teamId}/{categoryId}/subscriptions | Get category subscriptions
[**categoriesTeamIdCategoryIdSubscriptionsPost**](CategoriesApi.md#categoriesTeamIdCategoryIdSubscriptionsPost) | **POST** /categories/{teamId}/{categoryId}/subscriptions | Set category subscriptions
[**categoriesTeamIdGet**](CategoriesApi.md#categoriesTeamIdGet) | **GET** /categories/{teamId} | Get all categories
[**categoriesTeamIdMetricsGet**](CategoriesApi.md#categoriesTeamIdMetricsGet) | **GET** /categories/{teamId}/metrics | Get metrics for all categories
[**categoriesTeamIdPost**](CategoriesApi.md#categoriesTeamIdPost) | **POST** /categories/{teamId} | Create a new category



## categoriesImagesGet

> [String] categoriesImagesGet()

Gets the names of all alert category images.  You can get the image by going to account.signl4.com/images/alerts/categoryImageName.svg

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.CategoriesApi();
apiInstance.categoriesImagesGet((error, data, response) => {
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

**[String]**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## categoriesTeamIdCategoryIdDelete

> categoriesTeamIdCategoryIdDelete(teamId, categoryId)

Delete an existing category

Sample Request:                    DELETE /categories/cbb70402-1359-477f-ac92-0171cf2b5ff7/c0054336-cd89-4abf-882d-ba69b5adb25e

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.CategoriesApi();
let teamId = "teamId_example"; // String | ID of the team the category belongs to
let categoryId = "categoryId_example"; // String | ID of the category to delete
apiInstance.categoriesTeamIdCategoryIdDelete(teamId, categoryId, (error, data, response) => {
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
 **teamId** | **String**| ID of the team the category belongs to | 
 **categoryId** | **String**| ID of the category to delete | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## categoriesTeamIdCategoryIdGet

> CategoryInfo categoriesTeamIdCategoryIdGet(teamId, categoryId)

Get a specific category

Sample Request:                    GET /categories/cbb70402-1359-477f-ac92-0171cf2b5ff7/c0054336-cd89-4abf-882d-ba69b5adb25e

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.CategoriesApi();
let teamId = "teamId_example"; // String | ID of the team the category belongs to
let categoryId = "categoryId_example"; // String | ID of the category to get
apiInstance.categoriesTeamIdCategoryIdGet(teamId, categoryId, (error, data, response) => {
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
 **teamId** | **String**| ID of the team the category belongs to | 
 **categoryId** | **String**| ID of the category to get | 

### Return type

[**CategoryInfo**](CategoryInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## categoriesTeamIdCategoryIdMetricsGet

> CategoryMetrics categoriesTeamIdCategoryIdMetricsGet(teamId, categoryId)

Get metrics for a specific category

Sample Request:                    GET /categories/cbb70402-1359-477f-ac92-0171cf2b5ff7/c0054336-cd89-4abf-882d-ba69b5adb25e/metrics

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.CategoriesApi();
let teamId = "teamId_example"; // String | ID of the team the category belongs to
let categoryId = "categoryId_example"; // String | ID of the category to get
apiInstance.categoriesTeamIdCategoryIdMetricsGet(teamId, categoryId, (error, data, response) => {
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
 **teamId** | **String**| ID of the team the category belongs to | 
 **categoryId** | **String**| ID of the category to get | 

### Return type

[**CategoryMetrics**](CategoryMetrics.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## categoriesTeamIdCategoryIdPut

> CategoryInfo categoriesTeamIdCategoryIdPut(teamId, categoryId, opts)

Update an existing category

Sample Request:                    PUT /categories/cbb70402-1359-477f-ac92-0171cf2b5ff7/c0054336-cd89-4abf-882d-ba69b5adb25e      {          \&quot;name\&quot;: \&quot;Water-Updated\&quot;,          \&quot;imageName\&quot;: \&quot;water.svg\&quot;,          \&quot;color\&quot;: \&quot;#0000cc\&quot;,          \&quot;keywordMatching\&quot;: \&quot;All\&quot;,          \&quot;keywords\&quot;: [              {                  \&quot;value\&quot;: \&quot;H2O\&quot;              },              {                  \&quot;value\&quot;: \&quot;Water\&quot;              },              {                  \&quot;value\&quot;: \&quot;Wet\&quot;              }          ]      }

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.CategoriesApi();
let teamId = "teamId_example"; // String | ID of the team the category belongs to
let categoryId = "categoryId_example"; // String | 
let opts = {
  'categoryInfo': new Signl4Api.CategoryInfo() // CategoryInfo | Category to be updated
};
apiInstance.categoriesTeamIdCategoryIdPut(teamId, categoryId, opts, (error, data, response) => {
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
 **teamId** | **String**| ID of the team the category belongs to | 
 **categoryId** | **String**|  | 
 **categoryInfo** | [**CategoryInfo**](CategoryInfo.md)| Category to be updated | [optional] 

### Return type

[**CategoryInfo**](CategoryInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## categoriesTeamIdCategoryIdSubscriptionsGet

> [CategorySubscriptionInfo] categoriesTeamIdCategoryIdSubscriptionsGet(teamId, categoryId)

Get category subscriptions

Sample Request:                    GET /categories/cbb70402-1359-477f-ac92-0171cf2b5ff7/c0054336-cd89-4abf-882d-ba69b5adb25e/subscriptions      {      }

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.CategoriesApi();
let teamId = "teamId_example"; // String | ID of the team the category belongs to
let categoryId = "categoryId_example"; // String | Category to get subscriptions for
apiInstance.categoriesTeamIdCategoryIdSubscriptionsGet(teamId, categoryId, (error, data, response) => {
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
 **teamId** | **String**| ID of the team the category belongs to | 
 **categoryId** | **String**| Category to get subscriptions for | 

### Return type

[**[CategorySubscriptionInfo]**](CategorySubscriptionInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## categoriesTeamIdCategoryIdSubscriptionsPost

> [CategorySubscriptionInfo] categoriesTeamIdCategoryIdSubscriptionsPost(teamId, categoryId, opts)

Set category subscriptions

Sample Request:                    POST /categories/cbb70402-1359-477f-ac92-0171cf2b5ff7/c0054336-cd89-4abf-882d-ba69b5adb25e/subscriptions      {      }

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.CategoriesApi();
let teamId = "teamId_example"; // String | ID of the team the category belongs to
let categoryId = "categoryId_example"; // String | Category to be updated
let opts = {
  'categorySubscriptionInfo': [new Signl4Api.CategorySubscriptionInfo()] // [CategorySubscriptionInfo] | 
};
apiInstance.categoriesTeamIdCategoryIdSubscriptionsPost(teamId, categoryId, opts, (error, data, response) => {
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
 **teamId** | **String**| ID of the team the category belongs to | 
 **categoryId** | **String**| Category to be updated | 
 **categorySubscriptionInfo** | [**[CategorySubscriptionInfo]**](CategorySubscriptionInfo.md)|  | [optional] 

### Return type

[**[CategorySubscriptionInfo]**](CategorySubscriptionInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## categoriesTeamIdGet

> [CategoryInfo] categoriesTeamIdGet(teamId)

Get all categories

Sample Request:                    GET /categories/cbb70402-1359-477f-ac92-0171cf2b5ff7

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.CategoriesApi();
let teamId = "teamId_example"; // String | ID of the team the categories belong to
apiInstance.categoriesTeamIdGet(teamId, (error, data, response) => {
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
 **teamId** | **String**| ID of the team the categories belong to | 

### Return type

[**[CategoryInfo]**](CategoryInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## categoriesTeamIdMetricsGet

> [CategoryMetrics] categoriesTeamIdMetricsGet(teamId)

Get metrics for all categories

Sample Request:                    GET /categories/cbb70402-1359-477f-ac92-0171cf2b5ff7/metrics

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.CategoriesApi();
let teamId = "teamId_example"; // String | ID of the team the categories belongs to
apiInstance.categoriesTeamIdMetricsGet(teamId, (error, data, response) => {
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
 **teamId** | **String**| ID of the team the categories belongs to | 

### Return type

[**[CategoryMetrics]**](CategoryMetrics.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## categoriesTeamIdPost

> CategoryInfo categoriesTeamIdPost(teamId, opts)

Create a new category

Sample Request:                    POST /categories/cbb70402-1359-477f-ac92-0171cf2b5ff7      {          \&quot;name\&quot;: \&quot;Water\&quot;,          \&quot;imageName\&quot;: \&quot;water.svg\&quot;,          \&quot;color\&quot;: \&quot;#0000cc\&quot;,          \&quot;keywordMatching\&quot;: \&quot;Any\&quot;,          \&quot;keywords\&quot;: [              {                  \&quot;value\&quot;: \&quot;H2O\&quot;              },              {                  \&quot;value\&quot;: \&quot;Water\&quot;              }          ]      }

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.CategoriesApi();
let teamId = "teamId_example"; // String | ID of the team the category belongs to
let opts = {
  'categoryInfo': new Signl4Api.CategoryInfo() // CategoryInfo | Category to be created
};
apiInstance.categoriesTeamIdPost(teamId, opts, (error, data, response) => {
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
 **teamId** | **String**| ID of the team the category belongs to | 
 **categoryInfo** | [**CategoryInfo**](CategoryInfo.md)| Category to be created | [optional] 

### Return type

[**CategoryInfo**](CategoryInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain

