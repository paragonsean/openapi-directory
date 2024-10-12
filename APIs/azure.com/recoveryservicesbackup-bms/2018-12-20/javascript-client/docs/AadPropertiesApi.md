# RecoveryServicesBackupClient.AadPropertiesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aadPropertiesGet**](AadPropertiesApi.md#aadPropertiesGet) | **GET** /Subscriptions/{subscriptionId}/providers/Microsoft.RecoveryServices/locations/{azureRegion}/backupAadProperties/default | Fetches the AAD properties from target region BCM stamp.



## aadPropertiesGet

> AADPropertiesResource aadPropertiesGet(apiVersion, azureRegion, subscriptionId)

Fetches the AAD properties from target region BCM stamp.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.AadPropertiesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let azureRegion = "azureRegion_example"; // String | Azure region to hit Api
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
apiInstance.aadPropertiesGet(apiVersion, azureRegion, subscriptionId, (error, data, response) => {
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
 **azureRegion** | **String**| Azure region to hit Api | 
 **subscriptionId** | **String**| The subscription Id. | 

### Return type

[**AADPropertiesResource**](AADPropertiesResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

