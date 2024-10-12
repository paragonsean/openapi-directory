# IotDpsClient.PUTApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dpsCertificateCreateOrUpdate**](PUTApi.md#dpsCertificateCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName}/certificates/{certificateName} | Upload the certificate to the provisioning service.
[**iotDpsResourceCreateOrUpdate**](PUTApi.md#iotDpsResourceCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName} | Create or update the metadata of the provisioning service.



## dpsCertificateCreateOrUpdate

> CertificateResponse dpsCertificateCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, provisioningServiceName, certificateName, certificateDescription, opts)

Upload the certificate to the provisioning service.

Add new certificate or update an existing certificate.

### Example

```javascript
import IotDpsClient from 'iot_dps_client';
let defaultClient = IotDpsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotDpsClient.PUTApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group identifier.
let provisioningServiceName = "provisioningServiceName_example"; // String | The name of the provisioning service.
let certificateName = "certificateName_example"; // String | The name of the certificate create or update.
let certificateDescription = new IotDpsClient.CertificateBodyDescription(); // CertificateBodyDescription | The certificate body.
let opts = {
  'ifMatch': "ifMatch_example" // String | ETag of the certificate. This is required to update an existing certificate, and ignored while creating a brand new certificate.
};
apiInstance.dpsCertificateCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, provisioningServiceName, certificateName, certificateDescription, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| Resource group identifier. | 
 **provisioningServiceName** | **String**| The name of the provisioning service. | 
 **certificateName** | **String**| The name of the certificate create or update. | 
 **certificateDescription** | [**CertificateBodyDescription**](CertificateBodyDescription.md)| The certificate body. | 
 **ifMatch** | **String**| ETag of the certificate. This is required to update an existing certificate, and ignored while creating a brand new certificate. | [optional] 

### Return type

[**CertificateResponse**](CertificateResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## iotDpsResourceCreateOrUpdate

> ProvisioningServiceDescription iotDpsResourceCreateOrUpdate(subscriptionId, resourceGroupName, provisioningServiceName, apiVersion, iotDpsDescription)

Create or update the metadata of the provisioning service.

Create or update the metadata of the provisioning service. The usual pattern to modify a property is to retrieve the provisioning service metadata and security metadata, and then combine them with the modified values in a new body to update the provisioning service.

### Example

```javascript
import IotDpsClient from 'iot_dps_client';
let defaultClient = IotDpsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotDpsClient.PUTApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group identifier.
let provisioningServiceName = "provisioningServiceName_example"; // String | Name of provisioning service to create or update.
let apiVersion = "apiVersion_example"; // String | The version of the API.
let iotDpsDescription = new IotDpsClient.ProvisioningServiceDescription(); // ProvisioningServiceDescription | Description of the provisioning service to create or update.
apiInstance.iotDpsResourceCreateOrUpdate(subscriptionId, resourceGroupName, provisioningServiceName, apiVersion, iotDpsDescription, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| Resource group identifier. | 
 **provisioningServiceName** | **String**| Name of provisioning service to create or update. | 
 **apiVersion** | **String**| The version of the API. | 
 **iotDpsDescription** | [**ProvisioningServiceDescription**](ProvisioningServiceDescription.md)| Description of the provisioning service to create or update. | 

### Return type

[**ProvisioningServiceDescription**](ProvisioningServiceDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

