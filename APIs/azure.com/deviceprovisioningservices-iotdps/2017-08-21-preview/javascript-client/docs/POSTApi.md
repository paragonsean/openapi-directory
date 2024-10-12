# IotDpsClient.POSTApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dpsCertificateGenerateVerificationCode**](POSTApi.md#dpsCertificateGenerateVerificationCode) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName}/certificates/{certificateName}/generateVerificationCode | 
[**dpsCertificateVerifyCertificate**](POSTApi.md#dpsCertificateVerifyCertificate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName}/certificates/{certificateName}/verify | 
[**iotDpsResourceCheckNameAvailability**](POSTApi.md#iotDpsResourceCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Devices/checkProvisioningServiceNameAvailability | Check if a provisioning service name is available.
[**iotDpsResourceGetKeysForKeyName**](POSTApi.md#iotDpsResourceGetKeysForKeyName) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName}/keys/{keyName}/listkeys | Get a shared access policy by name from a provisioning service.
[**iotDpsResourceListKeys**](POSTApi.md#iotDpsResourceListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName}/listkeys | Get the security metadata for a provisioning service.



## dpsCertificateGenerateVerificationCode

> VerificationCodeResponse dpsCertificateGenerateVerificationCode(certificateName, ifMatch, subscriptionId, resourceGroupName, provisioningServiceName, apiVersion, opts)



Generate verification code for Proof of Possession.

### Example

```javascript
import IotDpsClient from 'iot_dps_client';
let defaultClient = IotDpsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotDpsClient.POSTApi();
let certificateName = "certificateName_example"; // String | The mandatory logical name of the certificate, that the provisioning service uses to access.
let ifMatch = "ifMatch_example"; // String | ETag of the certificate. This is required to update an existing certificate, and ignored while creating a brand new certificate.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | name of resource group.
let provisioningServiceName = "provisioningServiceName_example"; // String | Name of provisioning service.
let apiVersion = "apiVersion_example"; // String | The version of the API.
let opts = {
  'certificateName2': "certificateName_example", // String | Common Name for the certificate.
  'certificateRawBytes': null, // Blob | Raw data of certificate.
  'certificateIsVerified': true, // Boolean | Indicates if the certificate has been verified by owner of the private key.
  'certificatePurpose': "certificatePurpose_example", // String | Description mentioning the purpose of the certificate.
  'certificateCreated': new Date("2013-10-20T19:20:30+01:00"), // Date | Certificate creation time.
  'certificateLastUpdated': new Date("2013-10-20T19:20:30+01:00"), // Date | Certificate last updated time.
  'certificateHasPrivateKey': true, // Boolean | Indicates if the certificate contains private key.
  'certificateNonce': "certificateNonce_example" // String | Random number generated to indicate Proof of Possession.
};
apiInstance.dpsCertificateGenerateVerificationCode(certificateName, ifMatch, subscriptionId, resourceGroupName, provisioningServiceName, apiVersion, opts, (error, data, response) => {
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
 **certificateName** | **String**| The mandatory logical name of the certificate, that the provisioning service uses to access. | 
 **ifMatch** | **String**| ETag of the certificate. This is required to update an existing certificate, and ignored while creating a brand new certificate. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| name of resource group. | 
 **provisioningServiceName** | **String**| Name of provisioning service. | 
 **apiVersion** | **String**| The version of the API. | 
 **certificateName2** | **String**| Common Name for the certificate. | [optional] 
 **certificateRawBytes** | **Blob**| Raw data of certificate. | [optional] 
 **certificateIsVerified** | **Boolean**| Indicates if the certificate has been verified by owner of the private key. | [optional] 
 **certificatePurpose** | **String**| Description mentioning the purpose of the certificate. | [optional] 
 **certificateCreated** | **Date**| Certificate creation time. | [optional] 
 **certificateLastUpdated** | **Date**| Certificate last updated time. | [optional] 
 **certificateHasPrivateKey** | **Boolean**| Indicates if the certificate contains private key. | [optional] 
 **certificateNonce** | **String**| Random number generated to indicate Proof of Possession. | [optional] 

### Return type

[**VerificationCodeResponse**](VerificationCodeResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dpsCertificateVerifyCertificate

> CertificateResponse dpsCertificateVerifyCertificate(certificateName, ifMatch, subscriptionId, resourceGroupName, provisioningServiceName, apiVersion, request, opts)



Verifies certificate for the provisioning service.

### Example

```javascript
import IotDpsClient from 'iot_dps_client';
let defaultClient = IotDpsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotDpsClient.POSTApi();
let certificateName = "certificateName_example"; // String | The mandatory logical name of the certificate, that the provisioning service uses to access.
let ifMatch = "ifMatch_example"; // String | ETag of the certificate.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let provisioningServiceName = "provisioningServiceName_example"; // String | Provisioning service name.
let apiVersion = "apiVersion_example"; // String | The version of the API.
let request = new IotDpsClient.VerificationCodeRequest(); // VerificationCodeRequest | 
let opts = {
  'certificateName2': "certificateName_example", // String | Common Name for the certificate.
  'certificateRawBytes': null, // Blob | Raw data of certificate.
  'certificateIsVerified': true, // Boolean | Indicates if the certificate has been verified by owner of the private key.
  'certificatePurpose': "certificatePurpose_example", // String | Describe the purpose of the certificate.
  'certificateCreated': new Date("2013-10-20T19:20:30+01:00"), // Date | Certificate creation time.
  'certificateLastUpdated': new Date("2013-10-20T19:20:30+01:00"), // Date | Certificate last updated time.
  'certificateHasPrivateKey': true, // Boolean | Indicates if the certificate contains private key.
  'certificateNonce': "certificateNonce_example" // String | Random number generated to indicate Proof of Possession.
};
apiInstance.dpsCertificateVerifyCertificate(certificateName, ifMatch, subscriptionId, resourceGroupName, provisioningServiceName, apiVersion, request, opts, (error, data, response) => {
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
 **certificateName** | **String**| The mandatory logical name of the certificate, that the provisioning service uses to access. | 
 **ifMatch** | **String**| ETag of the certificate. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| Resource group name. | 
 **provisioningServiceName** | **String**| Provisioning service name. | 
 **apiVersion** | **String**| The version of the API. | 
 **request** | [**VerificationCodeRequest**](VerificationCodeRequest.md)|  | 
 **certificateName2** | **String**| Common Name for the certificate. | [optional] 
 **certificateRawBytes** | **Blob**| Raw data of certificate. | [optional] 
 **certificateIsVerified** | **Boolean**| Indicates if the certificate has been verified by owner of the private key. | [optional] 
 **certificatePurpose** | **String**| Describe the purpose of the certificate. | [optional] 
 **certificateCreated** | **Date**| Certificate creation time. | [optional] 
 **certificateLastUpdated** | **Date**| Certificate last updated time. | [optional] 
 **certificateHasPrivateKey** | **Boolean**| Indicates if the certificate contains private key. | [optional] 
 **certificateNonce** | **String**| Random number generated to indicate Proof of Possession. | [optional] 

### Return type

[**CertificateResponse**](CertificateResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## iotDpsResourceCheckNameAvailability

> NameAvailabilityInfo iotDpsResourceCheckNameAvailability(subscriptionId, apiVersion, _arguments)

Check if a provisioning service name is available.

Check if a provisioning service name is available.

### Example

```javascript
import IotDpsClient from 'iot_dps_client';
let defaultClient = IotDpsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotDpsClient.POSTApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let apiVersion = "apiVersion_example"; // String | The version of the API.
let _arguments = new IotDpsClient.OperationInputs(); // OperationInputs | Set the name parameter in the OperationInputs structure to the name of the provisioning service to check.
apiInstance.iotDpsResourceCheckNameAvailability(subscriptionId, apiVersion, _arguments, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. | 
 **_arguments** | [**OperationInputs**](OperationInputs.md)| Set the name parameter in the OperationInputs structure to the name of the provisioning service to check. | 

### Return type

[**NameAvailabilityInfo**](NameAvailabilityInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## iotDpsResourceGetKeysForKeyName

> SharedAccessSignatureAuthorizationRuleAccessRightsDescription iotDpsResourceGetKeysForKeyName(provisioningServiceName, keyName, subscriptionId, resourceGroupName, apiVersion)

Get a shared access policy by name from a provisioning service.

Get a shared access policy by name from a provisioning service.

### Example

```javascript
import IotDpsClient from 'iot_dps_client';
let defaultClient = IotDpsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotDpsClient.POSTApi();
let provisioningServiceName = "provisioningServiceName_example"; // String | Name of the provisioning service.
let keyName = "keyName_example"; // String | Logical key name to get key-values for.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the provisioning service.
let apiVersion = "apiVersion_example"; // String | The version of the API.
apiInstance.iotDpsResourceGetKeysForKeyName(provisioningServiceName, keyName, subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **provisioningServiceName** | **String**| Name of the provisioning service. | 
 **keyName** | **String**| Logical key name to get key-values for. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the provisioning service. | 
 **apiVersion** | **String**| The version of the API. | 

### Return type

[**SharedAccessSignatureAuthorizationRuleAccessRightsDescription**](SharedAccessSignatureAuthorizationRuleAccessRightsDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iotDpsResourceListKeys

> SharedAccessSignatureAuthorizationRuleListResult iotDpsResourceListKeys(provisioningServiceName, subscriptionId, resourceGroupName, apiVersion)

Get the security metadata for a provisioning service.

Get the security metadata for a provisioning service.

### Example

```javascript
import IotDpsClient from 'iot_dps_client';
let defaultClient = IotDpsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotDpsClient.POSTApi();
let provisioningServiceName = "provisioningServiceName_example"; // String | The provisioning service name to get the shared access keys for.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | resource group name
let apiVersion = "apiVersion_example"; // String | The version of the API.
apiInstance.iotDpsResourceListKeys(provisioningServiceName, subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **provisioningServiceName** | **String**| The provisioning service name to get the shared access keys for. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| resource group name | 
 **apiVersion** | **String**| The version of the API. | 

### Return type

[**SharedAccessSignatureAuthorizationRuleListResult**](SharedAccessSignatureAuthorizationRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

