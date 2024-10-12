# IotHubClient.CertificatesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**certificatesCreateOrUpdate**](CertificatesApi.md#certificatesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName} | Upload the certificate to the IoT hub.
[**certificatesDelete**](CertificatesApi.md#certificatesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName} | Delete an X509 certificate.
[**certificatesGenerateVerificationCode**](CertificatesApi.md#certificatesGenerateVerificationCode) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}/generateVerificationCode | Generate verification code for proof of possession flow.
[**certificatesGet**](CertificatesApi.md#certificatesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName} | Get the certificate.
[**certificatesListByIotHub**](CertificatesApi.md#certificatesListByIotHub) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates | Get the certificate list.
[**certificatesVerify**](CertificatesApi.md#certificatesVerify) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}/verify | Verify certificate&#39;s private key possession.



## certificatesCreateOrUpdate

> CertificateDescription certificatesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, certificateName, certificateDescription, opts)

Upload the certificate to the IoT hub.

Adds new or replaces existing certificate.

### Example

```javascript
import IotHubClient from 'iot_hub_client';
let defaultClient = IotHubClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotHubClient.CertificatesApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
let resourceName = "resourceName_example"; // String | The name of the IoT hub.
let certificateName = "certificateName_example"; // String | The name of the certificate
let certificateDescription = new IotHubClient.CertificateBodyDescription(); // CertificateBodyDescription | The certificate body.
let opts = {
  'ifMatch': "ifMatch_example" // String | ETag of the Certificate. Do not specify for creating a brand new certificate. Required to update an existing certificate.
};
apiInstance.certificatesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, certificateName, certificateDescription, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the IoT hub. | 
 **resourceName** | **String**| The name of the IoT hub. | 
 **certificateName** | **String**| The name of the certificate | 
 **certificateDescription** | [**CertificateBodyDescription**](CertificateBodyDescription.md)| The certificate body. | 
 **ifMatch** | **String**| ETag of the Certificate. Do not specify for creating a brand new certificate. Required to update an existing certificate. | [optional] 

### Return type

[**CertificateDescription**](CertificateDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## certificatesDelete

> certificatesDelete(apiVersion, subscriptionId, resourceGroupName, resourceName, certificateName, ifMatch)

Delete an X509 certificate.

Deletes an existing X509 certificate or does nothing if it does not exist.

### Example

```javascript
import IotHubClient from 'iot_hub_client';
let defaultClient = IotHubClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotHubClient.CertificatesApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
let resourceName = "resourceName_example"; // String | The name of the IoT hub.
let certificateName = "certificateName_example"; // String | The name of the certificate
let ifMatch = "ifMatch_example"; // String | ETag of the Certificate.
apiInstance.certificatesDelete(apiVersion, subscriptionId, resourceGroupName, resourceName, certificateName, ifMatch, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the IoT hub. | 
 **resourceName** | **String**| The name of the IoT hub. | 
 **certificateName** | **String**| The name of the certificate | 
 **ifMatch** | **String**| ETag of the Certificate. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificatesGenerateVerificationCode

> CertificateWithNonceDescription certificatesGenerateVerificationCode(apiVersion, subscriptionId, resourceGroupName, resourceName, certificateName, ifMatch)

Generate verification code for proof of possession flow.

Generates verification code for proof of possession flow. The verification code will be used to generate a leaf certificate.

### Example

```javascript
import IotHubClient from 'iot_hub_client';
let defaultClient = IotHubClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotHubClient.CertificatesApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
let resourceName = "resourceName_example"; // String | The name of the IoT hub.
let certificateName = "certificateName_example"; // String | The name of the certificate
let ifMatch = "ifMatch_example"; // String | ETag of the Certificate.
apiInstance.certificatesGenerateVerificationCode(apiVersion, subscriptionId, resourceGroupName, resourceName, certificateName, ifMatch, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the IoT hub. | 
 **resourceName** | **String**| The name of the IoT hub. | 
 **certificateName** | **String**| The name of the certificate | 
 **ifMatch** | **String**| ETag of the Certificate. | 

### Return type

[**CertificateWithNonceDescription**](CertificateWithNonceDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificatesGet

> CertificateDescription certificatesGet(apiVersion, subscriptionId, resourceGroupName, resourceName, certificateName)

Get the certificate.

Returns the certificate.

### Example

```javascript
import IotHubClient from 'iot_hub_client';
let defaultClient = IotHubClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotHubClient.CertificatesApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
let resourceName = "resourceName_example"; // String | The name of the IoT hub.
let certificateName = "certificateName_example"; // String | The name of the certificate
apiInstance.certificatesGet(apiVersion, subscriptionId, resourceGroupName, resourceName, certificateName, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the IoT hub. | 
 **resourceName** | **String**| The name of the IoT hub. | 
 **certificateName** | **String**| The name of the certificate | 

### Return type

[**CertificateDescription**](CertificateDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificatesListByIotHub

> CertificateListDescription certificatesListByIotHub(apiVersion, subscriptionId, resourceGroupName, resourceName)

Get the certificate list.

Returns the list of certificates.

### Example

```javascript
import IotHubClient from 'iot_hub_client';
let defaultClient = IotHubClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotHubClient.CertificatesApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
let resourceName = "resourceName_example"; // String | The name of the IoT hub.
apiInstance.certificatesListByIotHub(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the IoT hub. | 
 **resourceName** | **String**| The name of the IoT hub. | 

### Return type

[**CertificateListDescription**](CertificateListDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificatesVerify

> CertificateDescription certificatesVerify(apiVersion, subscriptionId, resourceGroupName, resourceName, certificateName, ifMatch, certificateVerificationBody)

Verify certificate&#39;s private key possession.

Verifies the certificate&#39;s private key possession by providing the leaf cert issued by the verifying pre uploaded certificate.

### Example

```javascript
import IotHubClient from 'iot_hub_client';
let defaultClient = IotHubClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotHubClient.CertificatesApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
let resourceName = "resourceName_example"; // String | The name of the IoT hub.
let certificateName = "certificateName_example"; // String | The name of the certificate
let ifMatch = "ifMatch_example"; // String | ETag of the Certificate.
let certificateVerificationBody = new IotHubClient.CertificateVerificationDescription(); // CertificateVerificationDescription | The name of the certificate
apiInstance.certificatesVerify(apiVersion, subscriptionId, resourceGroupName, resourceName, certificateName, ifMatch, certificateVerificationBody, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the IoT hub. | 
 **resourceName** | **String**| The name of the IoT hub. | 
 **certificateName** | **String**| The name of the certificate | 
 **ifMatch** | **String**| ETag of the Certificate. | 
 **certificateVerificationBody** | [**CertificateVerificationDescription**](CertificateVerificationDescription.md)| The name of the certificate | 

### Return type

[**CertificateDescription**](CertificateDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

