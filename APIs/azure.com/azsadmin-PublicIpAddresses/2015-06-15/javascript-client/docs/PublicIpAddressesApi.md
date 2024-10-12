# NetworkAdminManagementClient.PublicIpAddressesApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**publicIPAddressesList**](PublicIpAddressesApi.md#publicIPAddressesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network.Admin/adminPublicIpAddresses | 



## publicIPAddressesList

> PublicIpAddressList publicIPAddressesList(subscriptionId, apiVersion, opts)



List of public ip addresses.

### Example

```javascript
import NetworkAdminManagementClient from 'network_admin_management_client';
let defaultClient = NetworkAdminManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkAdminManagementClient.PublicIpAddressesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "'2015-06-15'"; // String | Client API Version.
let opts = {
  'filter': "filter_example", // String | OData filter parameter.
  'orderBy': "orderBy_example", // String | OData orderBy parameter.
  'top': "top_example", // String | OData top parameter.
  'skip': "skip_example", // String | OData skip parameter.
  'inlineCount': "inlineCount_example" // String | OData inline count parameter.
};
apiInstance.publicIPAddressesList(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2015-06-15&#39;]
 **filter** | **String**| OData filter parameter. | [optional] 
 **orderBy** | **String**| OData orderBy parameter. | [optional] 
 **top** | **String**| OData top parameter. | [optional] 
 **skip** | **String**| OData skip parameter. | [optional] 
 **inlineCount** | **String**| OData inline count parameter. | [optional] 

### Return type

[**PublicIpAddressList**](PublicIpAddressList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

