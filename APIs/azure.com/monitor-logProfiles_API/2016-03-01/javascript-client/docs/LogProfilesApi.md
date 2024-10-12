# MonitorManagementClient.LogProfilesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logProfilesCreateOrUpdate**](LogProfilesApi.md#logProfilesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/microsoft.insights/logprofiles/{logProfileName} | 
[**logProfilesDelete**](LogProfilesApi.md#logProfilesDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/microsoft.insights/logprofiles/{logProfileName} | 
[**logProfilesGet**](LogProfilesApi.md#logProfilesGet) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.insights/logprofiles/{logProfileName} | 
[**logProfilesList**](LogProfilesApi.md#logProfilesList) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.insights/logprofiles | 



## logProfilesCreateOrUpdate

> LogProfileResource logProfilesCreateOrUpdate(logProfileName, apiVersion, subscriptionId, parameters)



Create or update a log profile in Azure Monitoring REST API.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.LogProfilesApi();
let logProfileName = "logProfileName_example"; // String | The name of the log profile.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let parameters = new MonitorManagementClient.LogProfileResource(); // LogProfileResource | Parameters supplied to the operation.
apiInstance.logProfilesCreateOrUpdate(logProfileName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **logProfileName** | **String**| The name of the log profile. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| The Azure subscription Id. | 
 **parameters** | [**LogProfileResource**](LogProfileResource.md)| Parameters supplied to the operation. | 

### Return type

[**LogProfileResource**](LogProfileResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## logProfilesDelete

> logProfilesDelete(logProfileName, apiVersion, subscriptionId)



Deletes the log profile.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.LogProfilesApi();
let logProfileName = "logProfileName_example"; // String | The name of the log profile.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
apiInstance.logProfilesDelete(logProfileName, apiVersion, subscriptionId, (error, data, response) => {
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
 **logProfileName** | **String**| The name of the log profile. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| The Azure subscription Id. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## logProfilesGet

> LogProfileResource logProfilesGet(logProfileName, apiVersion, subscriptionId)



Gets the log profile.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.LogProfilesApi();
let logProfileName = "logProfileName_example"; // String | The name of the log profile.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
apiInstance.logProfilesGet(logProfileName, apiVersion, subscriptionId, (error, data, response) => {
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
 **logProfileName** | **String**| The name of the log profile. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| The Azure subscription Id. | 

### Return type

[**LogProfileResource**](LogProfileResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## logProfilesList

> LogProfileCollection logProfilesList(apiVersion, subscriptionId)



List the log profiles.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.LogProfilesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
apiInstance.logProfilesList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| The Azure subscription Id. | 

### Return type

[**LogProfileCollection**](LogProfileCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

