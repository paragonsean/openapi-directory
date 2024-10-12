# VMwareCloudSimple.CustomizationPoliciesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customizationPoliciesGet**](CustomizationPoliciesApi.md#customizationPoliciesGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/locations/{regionId}/privateClouds/{pcName}/customizationPolicies/{customizationPolicyName} | Implements get of customization policy
[**customizationPoliciesList**](CustomizationPoliciesApi.md#customizationPoliciesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/locations/{regionId}/privateClouds/{pcName}/customizationPolicies | Implements get of customization policies list



## customizationPoliciesGet

> CustomizationPolicy customizationPoliciesGet(apiVersion, subscriptionId, regionId, pcName, customizationPolicyName)

Implements get of customization policy

Returns customization policy by its name

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.CustomizationPoliciesApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let regionId = "regionId_example"; // String | The region Id (westus, eastus)
let pcName = "pcName_example"; // String | The private cloud name
let customizationPolicyName = "customizationPolicyName_example"; // String | customization policy name
apiInstance.customizationPoliciesGet(apiVersion, subscriptionId, regionId, pcName, customizationPolicyName, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **regionId** | **String**| The region Id (westus, eastus) | 
 **pcName** | **String**| The private cloud name | 
 **customizationPolicyName** | **String**| customization policy name | 

### Return type

[**CustomizationPolicy**](CustomizationPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customizationPoliciesList

> CustomizationPoliciesListResponse customizationPoliciesList(subscriptionId, regionId, pcName, apiVersion, opts)

Implements get of customization policies list

Returns list of customization policies in region for private cloud

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.CustomizationPoliciesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let regionId = "regionId_example"; // String | The region Id (westus, eastus)
let pcName = "pcName_example"; // String | The private cloud name
let apiVersion = "apiVersion_example"; // String | Client API version.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the list operation. only type is allowed here as a filter e.g. $filter=type eq 'xxxx'
};
apiInstance.customizationPoliciesList(subscriptionId, regionId, pcName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **regionId** | **String**| The region Id (westus, eastus) | 
 **pcName** | **String**| The private cloud name | 
 **apiVersion** | **String**| Client API version. | 
 **filter** | **String**| The filter to apply on the list operation. only type is allowed here as a filter e.g. $filter&#x3D;type eq &#39;xxxx&#39; | [optional] 

### Return type

[**CustomizationPoliciesListResponse**](CustomizationPoliciesListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

