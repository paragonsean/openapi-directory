# BatchManagement.CertificateApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**certificateCancelDeletion**](CertificateApi.md#certificateCancelDeletion) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/certificates/{certificateName}/cancelDelete | Cancels a failed deletion of a certificate from the specified account.
[**certificateCreate**](CertificateApi.md#certificateCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/certificates/{certificateName} | 
[**certificateDelete**](CertificateApi.md#certificateDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/certificates/{certificateName} | 
[**certificateGet**](CertificateApi.md#certificateGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/certificates/{certificateName} | 
[**certificateListByBatchAccount**](CertificateApi.md#certificateListByBatchAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/certificates | 
[**certificateUpdate**](CertificateApi.md#certificateUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/certificates/{certificateName} | 



## certificateCancelDeletion

> Certificate certificateCancelDeletion(resourceGroupName, accountName, certificateName, apiVersion, subscriptionId)

Cancels a failed deletion of a certificate from the specified account.

If you try to delete a certificate that is being used by a pool or compute node, the status of the certificate changes to deleteFailed. If you decide that you want to continue using the certificate, you can use this operation to set the status of the certificate back to active. If you intend to delete the certificate, you do not need to run this operation after the deletion failed. You must make sure that the certificate is not being used by any resources, and then you can try again to delete the certificate.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.CertificateApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let certificateName = "certificateName_example"; // String | The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
apiInstance.certificateCancelDeletion(resourceGroupName, accountName, certificateName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | 
 **accountName** | **String**| The name of the Batch account. | 
 **certificateName** | **String**| The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 

### Return type

[**Certificate**](Certificate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificateCreate

> Certificate certificateCreate(resourceGroupName, accountName, certificateName, apiVersion, subscriptionId, parameters, opts)



Creates a new certificate inside the specified account.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.CertificateApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let certificateName = "certificateName_example"; // String | The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let parameters = new BatchManagement.CertificateCreateOrUpdateParameters(); // CertificateCreateOrUpdateParameters | Additional parameters for certificate creation.
let opts = {
  'ifMatch': "ifMatch_example", // String | The entity state (ETag) version of the certificate to update. A value of \"*\" can be used to apply the operation only if the certificate already exists. If omitted, this operation will always be applied.
  'ifNoneMatch': "ifNoneMatch_example" // String | Set to '*' to allow a new certificate to be created, but to prevent updating an existing certificate. Other values will be ignored.
};
apiInstance.certificateCreate(resourceGroupName, accountName, certificateName, apiVersion, subscriptionId, parameters, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | 
 **accountName** | **String**| The name of the Batch account. | 
 **certificateName** | **String**| The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **parameters** | [**CertificateCreateOrUpdateParameters**](CertificateCreateOrUpdateParameters.md)| Additional parameters for certificate creation. | 
 **ifMatch** | **String**| The entity state (ETag) version of the certificate to update. A value of \&quot;*\&quot; can be used to apply the operation only if the certificate already exists. If omitted, this operation will always be applied. | [optional] 
 **ifNoneMatch** | **String**| Set to &#39;*&#39; to allow a new certificate to be created, but to prevent updating an existing certificate. Other values will be ignored. | [optional] 

### Return type

[**Certificate**](Certificate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## certificateDelete

> certificateDelete(resourceGroupName, accountName, certificateName, apiVersion, subscriptionId)



Deletes the specified certificate.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.CertificateApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let certificateName = "certificateName_example"; // String | The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
apiInstance.certificateDelete(resourceGroupName, accountName, certificateName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | 
 **accountName** | **String**| The name of the Batch account. | 
 **certificateName** | **String**| The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificateGet

> Certificate certificateGet(resourceGroupName, accountName, certificateName, apiVersion, subscriptionId)



Gets information about the specified certificate.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.CertificateApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let certificateName = "certificateName_example"; // String | The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
apiInstance.certificateGet(resourceGroupName, accountName, certificateName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | 
 **accountName** | **String**| The name of the Batch account. | 
 **certificateName** | **String**| The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 

### Return type

[**Certificate**](Certificate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificateListByBatchAccount

> ListCertificatesResult certificateListByBatchAccount(resourceGroupName, accountName, apiVersion, subscriptionId, opts)



Lists all of the certificates in the specified account.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.CertificateApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let opts = {
  'maxresults': 56, // Number | The maximum number of items to return in the response.
  'select': "select_example", // String | Comma separated list of properties that should be returned. e.g. \"properties/provisioningState\". Only top level properties under properties/ are valid for selection.
  'filter': "filter_example" // String | OData filter expression. Valid properties for filtering are \"properties/provisioningState\", \"properties/provisioningStateTransitionTime\", \"name\".
};
apiInstance.certificateListByBatchAccount(resourceGroupName, accountName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | 
 **accountName** | **String**| The name of the Batch account. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **maxresults** | **Number**| The maximum number of items to return in the response. | [optional] 
 **select** | **String**| Comma separated list of properties that should be returned. e.g. \&quot;properties/provisioningState\&quot;. Only top level properties under properties/ are valid for selection. | [optional] 
 **filter** | **String**| OData filter expression. Valid properties for filtering are \&quot;properties/provisioningState\&quot;, \&quot;properties/provisioningStateTransitionTime\&quot;, \&quot;name\&quot;. | [optional] 

### Return type

[**ListCertificatesResult**](ListCertificatesResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificateUpdate

> Certificate certificateUpdate(resourceGroupName, accountName, certificateName, apiVersion, subscriptionId, parameters, opts)



Updates the properties of an existing certificate.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.CertificateApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let certificateName = "certificateName_example"; // String | The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let parameters = new BatchManagement.CertificateCreateOrUpdateParameters(); // CertificateCreateOrUpdateParameters | Certificate entity to update.
let opts = {
  'ifMatch': "ifMatch_example" // String | The entity state (ETag) version of the certificate to update. This value can be omitted or set to \"*\" to apply the operation unconditionally.
};
apiInstance.certificateUpdate(resourceGroupName, accountName, certificateName, apiVersion, subscriptionId, parameters, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | 
 **accountName** | **String**| The name of the Batch account. | 
 **certificateName** | **String**| The identifier for the certificate. This must be made up of algorithm and thumbprint separated by a dash, and must match the certificate data in the request. For example SHA1-a3d1c5. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **parameters** | [**CertificateCreateOrUpdateParameters**](CertificateCreateOrUpdateParameters.md)| Certificate entity to update. | 
 **ifMatch** | **String**| The entity state (ETag) version of the certificate to update. This value can be omitted or set to \&quot;*\&quot; to apply the operation unconditionally. | [optional] 

### Return type

[**Certificate**](Certificate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

