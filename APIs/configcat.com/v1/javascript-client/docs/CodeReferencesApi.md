# ConfigCatPublicManagementApi.CodeReferencesApi

All URIs are relative to *https://api.configcat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CodeReferencesDeleteReportsPost**](CodeReferencesApi.md#v1CodeReferencesDeleteReportsPost) | **POST** /v1/code-references/delete-reports | 
[**v1CodeReferencesPost**](CodeReferencesApi.md#v1CodeReferencesPost) | **POST** /v1/code-references | 



## v1CodeReferencesDeleteReportsPost

> v1CodeReferencesDeleteReportsPost(deleteRepositoryReportsRequest)



### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.CodeReferencesApi();
let deleteRepositoryReportsRequest = new ConfigCatPublicManagementApi.DeleteRepositoryReportsRequest(); // DeleteRepositoryReportsRequest | 
apiInstance.v1CodeReferencesDeleteReportsPost(deleteRepositoryReportsRequest, (error, data, response) => {
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
 **deleteRepositoryReportsRequest** | [**DeleteRepositoryReportsRequest**](DeleteRepositoryReportsRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: Not defined


## v1CodeReferencesPost

> v1CodeReferencesPost(codeReferenceRequest)



### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.CodeReferencesApi();
let codeReferenceRequest = new ConfigCatPublicManagementApi.CodeReferenceRequest(); // CodeReferenceRequest | 
apiInstance.v1CodeReferencesPost(codeReferenceRequest, (error, data, response) => {
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
 **codeReferenceRequest** | [**CodeReferenceRequest**](CodeReferenceRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: Not defined

