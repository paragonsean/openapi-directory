# MonitorManagementClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logProfilesUpdate**](DefaultApi.md#logProfilesUpdate) | **PATCH** /subscriptions/{subscriptionId}/providers/microsoft.insights/logprofiles/{logProfileName} | 



## logProfilesUpdate

> LogProfileResource logProfilesUpdate(subscriptionId, logProfileName, apiVersion, logProfilesResource)



Updates an existing LogProfilesResource. To update other fields use the CreateOrUpdate method.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let logProfileName = "logProfileName_example"; // String | The name of the log profile.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let logProfilesResource = new MonitorManagementClient.LogProfileResourcePatch(); // LogProfileResourcePatch | Parameters supplied to the operation.
apiInstance.logProfilesUpdate(subscriptionId, logProfileName, apiVersion, logProfilesResource, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription Id. | 
 **logProfileName** | **String**| The name of the log profile. | 
 **apiVersion** | **String**| Client Api Version. | 
 **logProfilesResource** | [**LogProfileResourcePatch**](LogProfileResourcePatch.md)| Parameters supplied to the operation. | 

### Return type

[**LogProfileResource**](LogProfileResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

