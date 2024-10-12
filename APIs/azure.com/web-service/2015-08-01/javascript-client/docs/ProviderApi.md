# WebSiteManagementClient.ProviderApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**providerGetPublishingUser**](ProviderApi.md#providerGetPublishingUser) | **GET** /providers/Microsoft.Web/publishingUsers/web | Gets publishing user
[**providerGetSourceControl**](ProviderApi.md#providerGetSourceControl) | **GET** /providers/Microsoft.Web/sourcecontrols/{sourceControlType} | Gets source control token
[**providerGetSourceControls**](ProviderApi.md#providerGetSourceControls) | **GET** /providers/Microsoft.Web/sourcecontrols | Gets the source controls available for Azure websites
[**providerUpdatePublishingUser**](ProviderApi.md#providerUpdatePublishingUser) | **PUT** /providers/Microsoft.Web/publishingUsers/web | Updates publishing user
[**providerUpdateSourceControl**](ProviderApi.md#providerUpdateSourceControl) | **PUT** /providers/Microsoft.Web/sourcecontrols/{sourceControlType} | Updates source control token



## providerGetPublishingUser

> User providerGetPublishingUser(apiVersion)

Gets publishing user

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ProviderApi();
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.providerGetPublishingUser(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| API Version | 

### Return type

[**User**](User.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## providerGetSourceControl

> SourceControl providerGetSourceControl(sourceControlType, apiVersion)

Gets source control token

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ProviderApi();
let sourceControlType = "sourceControlType_example"; // String | Type of source control
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.providerGetSourceControl(sourceControlType, apiVersion, (error, data, response) => {
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
 **sourceControlType** | **String**| Type of source control | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SourceControl**](SourceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## providerGetSourceControls

> SourceControlCollection providerGetSourceControls(apiVersion)

Gets the source controls available for Azure websites

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ProviderApi();
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.providerGetSourceControls(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| API Version | 

### Return type

[**SourceControlCollection**](SourceControlCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## providerUpdatePublishingUser

> User providerUpdatePublishingUser(apiVersion, requestMessage)

Updates publishing user

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ProviderApi();
let apiVersion = "apiVersion_example"; // String | API Version
let requestMessage = new WebSiteManagementClient.User(); // User | Details of publishing user
apiInstance.providerUpdatePublishingUser(apiVersion, requestMessage, (error, data, response) => {
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
 **apiVersion** | **String**| API Version | 
 **requestMessage** | [**User**](User.md)| Details of publishing user | 

### Return type

[**User**](User.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## providerUpdateSourceControl

> SourceControl providerUpdateSourceControl(sourceControlType, apiVersion, requestMessage)

Updates source control token

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ProviderApi();
let sourceControlType = "sourceControlType_example"; // String | Type of source control
let apiVersion = "apiVersion_example"; // String | API Version
let requestMessage = new WebSiteManagementClient.SourceControl(); // SourceControl | Source control token information
apiInstance.providerUpdateSourceControl(sourceControlType, apiVersion, requestMessage, (error, data, response) => {
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
 **sourceControlType** | **String**| Type of source control | 
 **apiVersion** | **String**| API Version | 
 **requestMessage** | [**SourceControl**](SourceControl.md)| Source control token information | 

### Return type

[**SourceControl**](SourceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml

