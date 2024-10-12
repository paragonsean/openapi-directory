# CertificatesApiClient.CertificatesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**certificatesCreateOrUpdate**](CertificatesApi.md#certificatesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/certificates/{name} | Create or update a certificate.
[**certificatesDelete**](CertificatesApi.md#certificatesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/certificates/{name} | Delete a certificate.
[**certificatesGet**](CertificatesApi.md#certificatesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/certificates/{name} | Get a certificate.
[**certificatesList**](CertificatesApi.md#certificatesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/certificates | Get all certificates for a subscription.
[**certificatesListByResourceGroup**](CertificatesApi.md#certificatesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/certificates | Get all certificates in a resource group.
[**certificatesUpdate**](CertificatesApi.md#certificatesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/certificates/{name} | Create or update a certificate.



## certificatesCreateOrUpdate

> Certificate certificatesCreateOrUpdate(resourceGroupName, name, subscriptionId, apiVersion, certificateEnvelope)

Create or update a certificate.

Description for Create or update a certificate.

### Example

```javascript
import CertificatesApiClient from 'certificates_api_client';
let defaultClient = CertificatesApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CertificatesApiClient.CertificatesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the certificate.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let certificateEnvelope = new CertificatesApiClient.Certificate(); // Certificate | Details of certificate, if it exists already.
apiInstance.certificatesCreateOrUpdate(resourceGroupName, name, subscriptionId, apiVersion, certificateEnvelope, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the certificate. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **certificateEnvelope** | [**Certificate**](Certificate.md)| Details of certificate, if it exists already. | 

### Return type

[**Certificate**](Certificate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## certificatesDelete

> certificatesDelete(resourceGroupName, name, subscriptionId, apiVersion)

Delete a certificate.

Description for Delete a certificate.

### Example

```javascript
import CertificatesApiClient from 'certificates_api_client';
let defaultClient = CertificatesApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CertificatesApiClient.CertificatesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the certificate.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.certificatesDelete(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the certificate. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificatesGet

> Certificate certificatesGet(resourceGroupName, name, subscriptionId, apiVersion)

Get a certificate.

Description for Get a certificate.

### Example

```javascript
import CertificatesApiClient from 'certificates_api_client';
let defaultClient = CertificatesApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CertificatesApiClient.CertificatesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the certificate.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.certificatesGet(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the certificate. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**Certificate**](Certificate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificatesList

> CertificateCollection certificatesList(subscriptionId, apiVersion)

Get all certificates for a subscription.

Description for Get all certificates for a subscription.

### Example

```javascript
import CertificatesApiClient from 'certificates_api_client';
let defaultClient = CertificatesApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CertificatesApiClient.CertificatesApi();
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.certificatesList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**CertificateCollection**](CertificateCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificatesListByResourceGroup

> CertificateCollection certificatesListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)

Get all certificates in a resource group.

Description for Get all certificates in a resource group.

### Example

```javascript
import CertificatesApiClient from 'certificates_api_client';
let defaultClient = CertificatesApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CertificatesApiClient.CertificatesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.certificatesListByResourceGroup(resourceGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**CertificateCollection**](CertificateCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificatesUpdate

> Certificate certificatesUpdate(resourceGroupName, name, subscriptionId, apiVersion, certificateEnvelope)

Create or update a certificate.

Description for Create or update a certificate.

### Example

```javascript
import CertificatesApiClient from 'certificates_api_client';
let defaultClient = CertificatesApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CertificatesApiClient.CertificatesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the certificate.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let certificateEnvelope = new CertificatesApiClient.CertificatePatchResource(); // CertificatePatchResource | Details of certificate, if it exists already.
apiInstance.certificatesUpdate(resourceGroupName, name, subscriptionId, apiVersion, certificateEnvelope, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the certificate. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **certificateEnvelope** | [**CertificatePatchResource**](CertificatePatchResource.md)| Details of certificate, if it exists already. | 

### Return type

[**Certificate**](Certificate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

