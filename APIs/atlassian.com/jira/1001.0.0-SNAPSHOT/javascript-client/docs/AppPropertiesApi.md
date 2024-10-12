# TheJiraCloudPlatformRestApi.AppPropertiesApi

All URIs are relative to *https://your-domain.atlassian.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addonPropertiesResourceDeleteAddonPropertyDelete**](AppPropertiesApi.md#addonPropertiesResourceDeleteAddonPropertyDelete) | **DELETE** /rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey} | Delete app property
[**addonPropertiesResourceGetAddonPropertiesGet**](AppPropertiesApi.md#addonPropertiesResourceGetAddonPropertiesGet) | **GET** /rest/atlassian-connect/1/addons/{addonKey}/properties | Get app properties
[**addonPropertiesResourceGetAddonPropertyGet**](AppPropertiesApi.md#addonPropertiesResourceGetAddonPropertyGet) | **GET** /rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey} | Get app property
[**addonPropertiesResourcePutAddonPropertyPut**](AppPropertiesApi.md#addonPropertiesResourcePutAddonPropertyPut) | **PUT** /rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey} | Set app property



## addonPropertiesResourceDeleteAddonPropertyDelete

> addonPropertiesResourceDeleteAddonPropertyDelete(addonKey, propertyKey)

Delete app property

Deletes an app&#39;s property.  **[Permissions](#permissions) required:** Only a Connect app whose key matches &#x60;addonKey&#x60; can make this request.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';

let apiInstance = new TheJiraCloudPlatformRestApi.AppPropertiesApi();
let addonKey = "addonKey_example"; // String | The key of the app, as defined in its descriptor.
let propertyKey = "propertyKey_example"; // String | The key of the property.
apiInstance.addonPropertiesResourceDeleteAddonPropertyDelete(addonKey, propertyKey, (error, data, response) => {
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
 **addonKey** | **String**| The key of the app, as defined in its descriptor. | 
 **propertyKey** | **String**| The key of the property. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addonPropertiesResourceGetAddonPropertiesGet

> PropertyKeys addonPropertiesResourceGetAddonPropertiesGet(addonKey)

Get app properties

Gets all the properties of an app.  **[Permissions](#permissions) required:** Only a Connect app whose key matches &#x60;addonKey&#x60; can make this request. Additionally, Forge apps published on the Marketplace can access properties of Connect apps they were [migrated from](https://developer.atlassian.com/platform/forge/build-a-connect-on-forge-app/).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.AppPropertiesApi();
let addonKey = "addonKey_example"; // String | The key of the app, as defined in its descriptor.
apiInstance.addonPropertiesResourceGetAddonPropertiesGet(addonKey, (error, data, response) => {
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
 **addonKey** | **String**| The key of the app, as defined in its descriptor. | 

### Return type

[**PropertyKeys**](PropertyKeys.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addonPropertiesResourceGetAddonPropertyGet

> EntityProperty addonPropertiesResourceGetAddonPropertyGet(addonKey, propertyKey)

Get app property

Returns the key and value of an app&#39;s property.  **[Permissions](#permissions) required:** Only a Connect app whose key matches &#x60;addonKey&#x60; can make this request. Additionally, Forge apps published on the Marketplace can access properties of Connect apps they were [migrated from](https://developer.atlassian.com/platform/forge/build-a-connect-on-forge-app/).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.AppPropertiesApi();
let addonKey = "addonKey_example"; // String | The key of the app, as defined in its descriptor.
let propertyKey = "propertyKey_example"; // String | The key of the property.
apiInstance.addonPropertiesResourceGetAddonPropertyGet(addonKey, propertyKey, (error, data, response) => {
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
 **addonKey** | **String**| The key of the app, as defined in its descriptor. | 
 **propertyKey** | **String**| The key of the property. | 

### Return type

[**EntityProperty**](EntityProperty.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addonPropertiesResourcePutAddonPropertyPut

> OperationMessage addonPropertiesResourcePutAddonPropertyPut(addonKey, propertyKey, body)

Set app property

Sets the value of an app&#39;s property. Use this resource to store custom data for your app.  The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.  **[Permissions](#permissions) required:** Only a Connect app whose key matches &#x60;addonKey&#x60; can make this request.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';

let apiInstance = new TheJiraCloudPlatformRestApi.AppPropertiesApi();
let addonKey = "addonKey_example"; // String | The key of the app, as defined in its descriptor.
let propertyKey = "propertyKey_example"; // String | The key of the property.
let body = null; // Object | 
apiInstance.addonPropertiesResourcePutAddonPropertyPut(addonKey, propertyKey, body, (error, data, response) => {
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
 **addonKey** | **String**| The key of the app, as defined in its descriptor. | 
 **propertyKey** | **String**| The key of the property. | 
 **body** | **Object**|  | 

### Return type

[**OperationMessage**](OperationMessage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

