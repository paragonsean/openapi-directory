# SecurityCenter.ApplicationWhitelistingsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adaptiveApplicationControlsGet**](ApplicationWhitelistingsApi.md#adaptiveApplicationControlsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/applicationWhitelistings/{groupName} | 
[**adaptiveApplicationControlsList**](ApplicationWhitelistingsApi.md#adaptiveApplicationControlsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/applicationWhitelistings | 
[**adaptiveApplicationControlsPut**](ApplicationWhitelistingsApi.md#adaptiveApplicationControlsPut) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/applicationWhitelistings/{groupName} | 



## adaptiveApplicationControlsGet

> AppWhitelistingGroup adaptiveApplicationControlsGet(subscriptionId, ascLocation, groupName, apiVersion)



Gets an application control VM/server group.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.ApplicationWhitelistingsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let groupName = "groupName_example"; // String | Name of an application control VM/server group
let apiVersion = "apiVersion_example"; // String | API version for the operation
apiInstance.adaptiveApplicationControlsGet(subscriptionId, ascLocation, groupName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID | 
 **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | 
 **groupName** | **String**| Name of an application control VM/server group | 
 **apiVersion** | **String**| API version for the operation | 

### Return type

[**AppWhitelistingGroup**](AppWhitelistingGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adaptiveApplicationControlsList

> AppWhitelistingGroups adaptiveApplicationControlsList(subscriptionId, apiVersion, opts)



Gets a list of application control VM/server groups for the subscription.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.ApplicationWhitelistingsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let apiVersion = "apiVersion_example"; // String | API version for the operation
let opts = {
  'includePathRecommendations': true, // Boolean | Include the policy rules
  'summary': true // Boolean | Return output in a summarized form
};
apiInstance.adaptiveApplicationControlsList(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID | 
 **apiVersion** | **String**| API version for the operation | 
 **includePathRecommendations** | **Boolean**| Include the policy rules | [optional] 
 **summary** | **Boolean**| Return output in a summarized form | [optional] 

### Return type

[**AppWhitelistingGroups**](AppWhitelistingGroups.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adaptiveApplicationControlsPut

> AppWhitelistingGroup adaptiveApplicationControlsPut(subscriptionId, ascLocation, groupName, apiVersion, body)



Update an application control VM/server group

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.ApplicationWhitelistingsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let groupName = "groupName_example"; // String | Name of an application control VM/server group
let apiVersion = "apiVersion_example"; // String | API version for the operation
let body = new SecurityCenter.AppWhitelistingPutGroupData(); // AppWhitelistingPutGroupData | The updated VM/server group data
apiInstance.adaptiveApplicationControlsPut(subscriptionId, ascLocation, groupName, apiVersion, body, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID | 
 **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | 
 **groupName** | **String**| Name of an application control VM/server group | 
 **apiVersion** | **String**| API version for the operation | 
 **body** | [**AppWhitelistingPutGroupData**](AppWhitelistingPutGroupData.md)| The updated VM/server group data | 

### Return type

[**AppWhitelistingGroup**](AppWhitelistingGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

