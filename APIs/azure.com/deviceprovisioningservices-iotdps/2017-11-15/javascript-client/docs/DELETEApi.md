# IotDpsClient.DELETEApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dpsCertificateDelete**](DELETEApi.md#dpsCertificateDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName}/certificates/{certificateName} | Delete the Provisioning Service Certificate.
[**iotDpsResourceDelete**](DELETEApi.md#iotDpsResourceDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName} | Delete the Provisioning Service



## dpsCertificateDelete

> dpsCertificateDelete(subscriptionId, resourceGroupName, ifMatch, provisioningServiceName, certificateName, apiVersion, opts)

Delete the Provisioning Service Certificate.

Deletes the specified certificate associated with the Provisioning Service

### Example

```javascript
import IotDpsClient from 'iot_dps_client';
let defaultClient = IotDpsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotDpsClient.DELETEApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group identifier.
let ifMatch = "ifMatch_example"; // String | ETag of the certificate
let provisioningServiceName = "provisioningServiceName_example"; // String | The name of the provisioning service.
let certificateName = "certificateName_example"; // String | This is a mandatory field, and is the logical name of the certificate that the provisioning service will access by.
let apiVersion = "apiVersion_example"; // String | The version of the API.
let opts = {
  'certificateName2': "certificateName_example", // String | This is optional, and it is the Common Name of the certificate.
  'certificateRawBytes': null, // Blob | Raw data within the certificate.
  'certificateIsVerified': true, // Boolean | Indicates if certificate has been verified by owner of the private key.
  'certificatePurpose': "certificatePurpose_example", // String | A description that mentions the purpose of the certificate.
  'certificateCreated': new Date("2013-10-20T19:20:30+01:00"), // Date | Time the certificate is created.
  'certificateLastUpdated': new Date("2013-10-20T19:20:30+01:00"), // Date | Time the certificate is last updated.
  'certificateHasPrivateKey': true, // Boolean | Indicates if the certificate contains a private key.
  'certificateNonce': "certificateNonce_example" // String | Random number generated to indicate Proof of Possession.
};
apiInstance.dpsCertificateDelete(subscriptionId, resourceGroupName, ifMatch, provisioningServiceName, certificateName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| Resource group identifier. | 
 **ifMatch** | **String**| ETag of the certificate | 
 **provisioningServiceName** | **String**| The name of the provisioning service. | 
 **certificateName** | **String**| This is a mandatory field, and is the logical name of the certificate that the provisioning service will access by. | 
 **apiVersion** | **String**| The version of the API. | 
 **certificateName2** | **String**| This is optional, and it is the Common Name of the certificate. | [optional] 
 **certificateRawBytes** | **Blob**| Raw data within the certificate. | [optional] 
 **certificateIsVerified** | **Boolean**| Indicates if certificate has been verified by owner of the private key. | [optional] 
 **certificatePurpose** | **String**| A description that mentions the purpose of the certificate. | [optional] 
 **certificateCreated** | **Date**| Time the certificate is created. | [optional] 
 **certificateLastUpdated** | **Date**| Time the certificate is last updated. | [optional] 
 **certificateHasPrivateKey** | **Boolean**| Indicates if the certificate contains a private key. | [optional] 
 **certificateNonce** | **String**| Random number generated to indicate Proof of Possession. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iotDpsResourceDelete

> iotDpsResourceDelete(provisioningServiceName, subscriptionId, resourceGroupName, apiVersion)

Delete the Provisioning Service

Deletes the Provisioning Service.

### Example

```javascript
import IotDpsClient from 'iot_dps_client';
let defaultClient = IotDpsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotDpsClient.DELETEApi();
let provisioningServiceName = "provisioningServiceName_example"; // String | Name of provisioning service to delete.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group identifier.
let apiVersion = "apiVersion_example"; // String | The version of the API.
apiInstance.iotDpsResourceDelete(provisioningServiceName, subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **provisioningServiceName** | **String**| Name of provisioning service to delete. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| Resource group identifier. | 
 **apiVersion** | **String**| The version of the API. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

