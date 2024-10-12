# KeyVaultManagementClient.KeyVaultApi

All URIs are relative to *https://management.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quotasList**](KeyVaultApi.md#quotasList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.KeyVault.Admin/locations/{location}/quotas | 



## quotasList

> QuotaList quotasList(subscriptionId, location, apiVersion)



Get a list of all quota objects for KeyVault at a location.

### Example

```javascript
import KeyVaultManagementClient from 'key_vault_management_client';
let defaultClient = KeyVaultManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new KeyVaultManagementClient.KeyVaultApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | The location of the quota.
let apiVersion = "'2017-02-01-preview'"; // String | Client Api Version.
apiInstance.quotasList(subscriptionId, location, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **location** | **String**| The location of the quota. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2017-02-01-preview&#39;]

### Return type

[**QuotaList**](QuotaList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

