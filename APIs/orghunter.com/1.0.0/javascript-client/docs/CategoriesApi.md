# OrgHunter.CategoriesApi

All URIs are relative to *http://data.orghunter.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCategories**](CategoriesApi.md#getCategories) | **POST** /v1/categories | Get categories!



## getCategories

> getCategories()

Get categories!

&lt;p&gt;This operation provides a list of categories.&lt;/p&gt;

### Example

```javascript
import OrgHunter from 'org_hunter';
let defaultClient = OrgHunter.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new OrgHunter.CategoriesApi();
apiInstance.getCategories((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

