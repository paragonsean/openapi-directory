# Sakari.TemplatesApi

All URIs are relative to *https://api.sakari.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**templatesCreate**](TemplatesApi.md#templatesCreate) | **POST** /v1/accounts/{accountId}/templates | Create template
[**templatesFetch**](TemplatesApi.md#templatesFetch) | **GET** /v1/accounts/{accountId}/templates/{templateId} | Fetch template by ID
[**templatesFetchAll**](TemplatesApi.md#templatesFetchAll) | **GET** /v1/accounts/{accountId}/templates | Fetch templates
[**templatesRemove**](TemplatesApi.md#templatesRemove) | **DELETE** /v1/accounts/{accountId}/templates/{templateId} | Deletes a template
[**templatesUpdate**](TemplatesApi.md#templatesUpdate) | **PUT** /v1/accounts/{accountId}/templates/{templateId} | Updates a template



## templatesCreate

> TemplatesResponse templatesCreate(accountId, opts)

Create template

### Example

```javascript
import Sakari from 'sakari';
let defaultClient = Sakari.ApiClient.instance;
// Configure OAuth2 access token for authorization: sakari_auth
let sakari_auth = defaultClient.authentications['sakari_auth'];
sakari_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Sakari.TemplatesApi();
let accountId = "accountId_example"; // String | Account to apply operations to
let opts = {
  'templateRequest': new Sakari.TemplateRequest() // TemplateRequest | 
};
apiInstance.templatesCreate(accountId, opts, (error, data, response) => {
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
 **accountId** | **String**| Account to apply operations to | 
 **templateRequest** | [**TemplateRequest**](TemplateRequest.md)|  | [optional] 

### Return type

[**TemplatesResponse**](TemplatesResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## templatesFetch

> TemplateResponse templatesFetch(accountId, templateId)

Fetch template by ID

### Example

```javascript
import Sakari from 'sakari';
let defaultClient = Sakari.ApiClient.instance;
// Configure OAuth2 access token for authorization: sakari_auth
let sakari_auth = defaultClient.authentications['sakari_auth'];
sakari_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Sakari.TemplatesApi();
let accountId = "accountId_example"; // String | Account to apply operations to
let templateId = "templateId_example"; // String | ID of template to return
apiInstance.templatesFetch(accountId, templateId, (error, data, response) => {
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
 **accountId** | **String**| Account to apply operations to | 
 **templateId** | **String**| ID of template to return | 

### Return type

[**TemplateResponse**](TemplateResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## templatesFetchAll

> TemplatesResponse templatesFetchAll(accountId, opts)

Fetch templates

### Example

```javascript
import Sakari from 'sakari';
let defaultClient = Sakari.ApiClient.instance;
// Configure OAuth2 access token for authorization: sakari_auth
let sakari_auth = defaultClient.authentications['sakari_auth'];
sakari_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Sakari.TemplatesApi();
let accountId = "accountId_example"; // String | Account to apply operations to
let opts = {
  'offset': 789, // Number | Results to skip when paginating through a result set
  'limit': 789, // Number | Maximum number of results to return
  'name': "name_example" // String | Filter by name or part of
};
apiInstance.templatesFetchAll(accountId, opts, (error, data, response) => {
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
 **accountId** | **String**| Account to apply operations to | 
 **offset** | **Number**| Results to skip when paginating through a result set | [optional] 
 **limit** | **Number**| Maximum number of results to return | [optional] 
 **name** | **String**| Filter by name or part of | [optional] 

### Return type

[**TemplatesResponse**](TemplatesResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## templatesRemove

> CampaignsRemove200Response templatesRemove(accountId, templateId)

Deletes a template

### Example

```javascript
import Sakari from 'sakari';
let defaultClient = Sakari.ApiClient.instance;
// Configure OAuth2 access token for authorization: sakari_auth
let sakari_auth = defaultClient.authentications['sakari_auth'];
sakari_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Sakari.TemplatesApi();
let accountId = "accountId_example"; // String | Account to apply operations to
let templateId = "templateId_example"; // String | Template id to delete
apiInstance.templatesRemove(accountId, templateId, (error, data, response) => {
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
 **accountId** | **String**| Account to apply operations to | 
 **templateId** | **String**| Template id to delete | 

### Return type

[**CampaignsRemove200Response**](CampaignsRemove200Response.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## templatesUpdate

> TemplateResponse templatesUpdate(accountId, templateId)

Updates a template

### Example

```javascript
import Sakari from 'sakari';
let defaultClient = Sakari.ApiClient.instance;
// Configure OAuth2 access token for authorization: sakari_auth
let sakari_auth = defaultClient.authentications['sakari_auth'];
sakari_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Sakari.TemplatesApi();
let accountId = "accountId_example"; // String | Account to apply operations to
let templateId = "templateId_example"; // String | ID of template
apiInstance.templatesUpdate(accountId, templateId, (error, data, response) => {
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
 **accountId** | **String**| Account to apply operations to | 
 **templateId** | **String**| ID of template | 

### Return type

[**TemplateResponse**](TemplateResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

