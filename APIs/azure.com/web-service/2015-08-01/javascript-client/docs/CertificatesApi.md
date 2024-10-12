# WebSiteManagementClient.CertificatesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**certificatesCreateOrUpdateCertificate**](CertificatesApi.md#certificatesCreateOrUpdateCertificate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/certificates/{name} | Creates or modifies an existing certificate.
[**certificatesCreateOrUpdateCsr**](CertificatesApi.md#certificatesCreateOrUpdateCsr) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/csrs/{name} | Creates or modifies an existing certificate signing request.
[**certificatesDeleteCertificate**](CertificatesApi.md#certificatesDeleteCertificate) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/certificates/{name} | Delete a certificate by name in a specified subscription and resourcegroup.
[**certificatesDeleteCsr**](CertificatesApi.md#certificatesDeleteCsr) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/csrs/{name} | Delete the certificate signing request.
[**certificatesGetCertificate**](CertificatesApi.md#certificatesGetCertificate) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/certificates/{name} | Get a certificate by certificate name for a subscription in the specified resource group.
[**certificatesGetCertificates**](CertificatesApi.md#certificatesGetCertificates) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/certificates | Get certificates for a subscription in the specified resource group.
[**certificatesGetCsr**](CertificatesApi.md#certificatesGetCsr) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/csrs/{name} | Gets a certificate signing request by certificate name for a subscription in the specified resource group
[**certificatesGetCsrs**](CertificatesApi.md#certificatesGetCsrs) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/csrs | Gets the certificate signing requests for a subscription in the specified resource group
[**certificatesUpdateCertificate**](CertificatesApi.md#certificatesUpdateCertificate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/certificates/{name} | Creates or modifies an existing certificate.
[**certificatesUpdateCsr**](CertificatesApi.md#certificatesUpdateCsr) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/csrs/{name} | Creates or modifies an existing certificate signing request.



## certificatesCreateOrUpdateCertificate

> Certificate certificatesCreateOrUpdateCertificate(resourceGroupName, name, subscriptionId, apiVersion, certificateEnvelope)

Creates or modifies an existing certificate.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.CertificatesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
let name = "name_example"; // String | Name of the certificate.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let certificateEnvelope = new WebSiteManagementClient.Certificate(); // Certificate | Details of certificate if it exists already.
apiInstance.certificatesCreateOrUpdateCertificate(resourceGroupName, name, subscriptionId, apiVersion, certificateEnvelope, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group | 
 **name** | **String**| Name of the certificate. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **certificateEnvelope** | [**Certificate**](Certificate.md)| Details of certificate if it exists already. | 

### Return type

[**Certificate**](Certificate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## certificatesCreateOrUpdateCsr

> Csr certificatesCreateOrUpdateCsr(resourceGroupName, name, subscriptionId, apiVersion, csrEnvelope)

Creates or modifies an existing certificate signing request.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.CertificatesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
let name = "name_example"; // String | Name of the certificate.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let csrEnvelope = new WebSiteManagementClient.Csr(); // Csr | Details of certificate signing request if it exists already.
apiInstance.certificatesCreateOrUpdateCsr(resourceGroupName, name, subscriptionId, apiVersion, csrEnvelope, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group | 
 **name** | **String**| Name of the certificate. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **csrEnvelope** | [**Csr**](Csr.md)| Details of certificate signing request if it exists already. | 

### Return type

[**Csr**](Csr.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## certificatesDeleteCertificate

> Object certificatesDeleteCertificate(resourceGroupName, name, subscriptionId, apiVersion)

Delete a certificate by name in a specified subscription and resourcegroup.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.CertificatesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
let name = "name_example"; // String | Name of the certificate to be deleted.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.certificatesDeleteCertificate(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group | 
 **name** | **String**| Name of the certificate to be deleted. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## certificatesDeleteCsr

> Object certificatesDeleteCsr(resourceGroupName, name, subscriptionId, apiVersion)

Delete the certificate signing request.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.CertificatesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
let name = "name_example"; // String | Name of the certificate signing request.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.certificatesDeleteCsr(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group | 
 **name** | **String**| Name of the certificate signing request. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## certificatesGetCertificate

> Certificate certificatesGetCertificate(resourceGroupName, name, subscriptionId, apiVersion)

Get a certificate by certificate name for a subscription in the specified resource group.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.CertificatesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
let name = "name_example"; // String | Name of the certificate.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.certificatesGetCertificate(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group | 
 **name** | **String**| Name of the certificate. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**Certificate**](Certificate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## certificatesGetCertificates

> CertificateCollection certificatesGetCertificates(resourceGroupName, subscriptionId, apiVersion)

Get certificates for a subscription in the specified resource group.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.CertificatesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.certificatesGetCertificates(resourceGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**CertificateCollection**](CertificateCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## certificatesGetCsr

> Csr certificatesGetCsr(resourceGroupName, name, subscriptionId, apiVersion)

Gets a certificate signing request by certificate name for a subscription in the specified resource group

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.CertificatesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
let name = "name_example"; // String | Name of the certificate.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.certificatesGetCsr(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group | 
 **name** | **String**| Name of the certificate. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**Csr**](Csr.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## certificatesGetCsrs

> [Csr] certificatesGetCsrs(resourceGroupName, subscriptionId, apiVersion)

Gets the certificate signing requests for a subscription in the specified resource group

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.CertificatesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.certificatesGetCsrs(resourceGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**[Csr]**](Csr.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## certificatesUpdateCertificate

> Certificate certificatesUpdateCertificate(resourceGroupName, name, subscriptionId, apiVersion, certificateEnvelope)

Creates or modifies an existing certificate.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.CertificatesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
let name = "name_example"; // String | Name of the certificate.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let certificateEnvelope = new WebSiteManagementClient.Certificate(); // Certificate | Details of certificate if it exists already.
apiInstance.certificatesUpdateCertificate(resourceGroupName, name, subscriptionId, apiVersion, certificateEnvelope, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group | 
 **name** | **String**| Name of the certificate. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **certificateEnvelope** | [**Certificate**](Certificate.md)| Details of certificate if it exists already. | 

### Return type

[**Certificate**](Certificate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## certificatesUpdateCsr

> Csr certificatesUpdateCsr(resourceGroupName, name, subscriptionId, apiVersion, csrEnvelope)

Creates or modifies an existing certificate signing request.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.CertificatesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
let name = "name_example"; // String | Name of the certificate.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let csrEnvelope = new WebSiteManagementClient.Csr(); // Csr | Details of certificate signing request if it exists already.
apiInstance.certificatesUpdateCsr(resourceGroupName, name, subscriptionId, apiVersion, csrEnvelope, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group | 
 **name** | **String**| Name of the certificate. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **csrEnvelope** | [**Csr**](Csr.md)| Details of certificate signing request if it exists already. | 

### Return type

[**Csr**](Csr.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml

