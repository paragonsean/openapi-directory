# WebSiteManagementClient.CertificateOrdersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**certificateOrdersCreateOrUpdateCertificate**](CertificateOrdersApi.md#certificateOrdersCreateOrUpdateCertificate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/certificates/{name} | Associates a Key Vault secret to a certificate store that will be used for storing the certificate once it&#39;s ready
[**certificateOrdersCreateOrUpdateCertificateOrder**](CertificateOrdersApi.md#certificateOrdersCreateOrUpdateCertificateOrder) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{name} | Create or update a certificate purchase order
[**certificateOrdersDeleteCertificate**](CertificateOrdersApi.md#certificateOrdersDeleteCertificate) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/certificates/{name} | Deletes the certificate associated with the certificate order
[**certificateOrdersDeleteCertificateOrder**](CertificateOrdersApi.md#certificateOrdersDeleteCertificateOrder) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{name} | Delete an existing certificate order
[**certificateOrdersGetCertificate**](CertificateOrdersApi.md#certificateOrdersGetCertificate) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/certificates/{name} | Get certificate associated with the certificate order
[**certificateOrdersGetCertificateOrder**](CertificateOrdersApi.md#certificateOrdersGetCertificateOrder) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{name} | Get a certificate order
[**certificateOrdersGetCertificateOrders**](CertificateOrdersApi.md#certificateOrdersGetCertificateOrders) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders | Get certificate orders in a resource group
[**certificateOrdersGetCertificates**](CertificateOrdersApi.md#certificateOrdersGetCertificates) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/certificates | List all certificates associated with a certificate order (only one certificate can be associated with an order at a time)
[**certificateOrdersReissueCertificateOrder**](CertificateOrdersApi.md#certificateOrdersReissueCertificateOrder) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{name}/reissue | Reissue an existing certificate order
[**certificateOrdersRenewCertificateOrder**](CertificateOrdersApi.md#certificateOrdersRenewCertificateOrder) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{name}/renew | Renew an existing certificate order
[**certificateOrdersResendCertificateEmail**](CertificateOrdersApi.md#certificateOrdersResendCertificateEmail) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{name}/resendEmail | Resend certificate email
[**certificateOrdersRetrieveCertificateActions**](CertificateOrdersApi.md#certificateOrdersRetrieveCertificateActions) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{name}/retrieveCertificateActions | Retrieve the list of certificate actions
[**certificateOrdersRetrieveCertificateEmailHistory**](CertificateOrdersApi.md#certificateOrdersRetrieveCertificateEmailHistory) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{name}/retrieveEmailHistory | Retrieve email history
[**certificateOrdersUpdateCertificate**](CertificateOrdersApi.md#certificateOrdersUpdateCertificate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/certificates/{name} | Associates a Key Vault secret to a certificate store that will be used for storing the certificate once it&#39;s ready
[**certificateOrdersUpdateCertificateOrder**](CertificateOrdersApi.md#certificateOrdersUpdateCertificateOrder) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{name} | Create or update a certificate purchase order
[**certificateOrdersVerifyDomainOwnership**](CertificateOrdersApi.md#certificateOrdersVerifyDomainOwnership) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{name}/verifyDomainOwnership | Verify domain ownership for this certificate order



## certificateOrdersCreateOrUpdateCertificate

> CertificateOrderCertificate certificateOrdersCreateOrUpdateCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion, keyVaultCertificate)

Associates a Key Vault secret to a certificate store that will be used for storing the certificate once it&#39;s ready

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.CertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let certificateOrderName = "certificateOrderName_example"; // String | Certificate name
let name = "name_example"; // String | Certificate name
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let keyVaultCertificate = new WebSiteManagementClient.CertificateOrderCertificate(); // CertificateOrderCertificate | Key Vault secret csm Id
apiInstance.certificateOrdersCreateOrUpdateCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion, keyVaultCertificate, (error, data, response) => {
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
 **resourceGroupName** | **String**| Azure resource group name | 
 **certificateOrderName** | **String**| Certificate name | 
 **name** | **String**| Certificate name | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **keyVaultCertificate** | [**CertificateOrderCertificate**](CertificateOrderCertificate.md)| Key Vault secret csm Id | 

### Return type

[**CertificateOrderCertificate**](CertificateOrderCertificate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## certificateOrdersCreateOrUpdateCertificateOrder

> CertificateOrder certificateOrdersCreateOrUpdateCertificateOrder(resourceGroupName, name, subscriptionId, apiVersion, certificateDistinguishedName)

Create or update a certificate purchase order

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.CertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let name = "name_example"; // String | Certificate name
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let certificateDistinguishedName = new WebSiteManagementClient.CertificateOrder(); // CertificateOrder | Distinguished name to be used for purchasing certificate
apiInstance.certificateOrdersCreateOrUpdateCertificateOrder(resourceGroupName, name, subscriptionId, apiVersion, certificateDistinguishedName, (error, data, response) => {
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
 **resourceGroupName** | **String**| Azure resource group name | 
 **name** | **String**| Certificate name | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **certificateDistinguishedName** | [**CertificateOrder**](CertificateOrder.md)| Distinguished name to be used for purchasing certificate | 

### Return type

[**CertificateOrder**](CertificateOrder.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## certificateOrdersDeleteCertificate

> Object certificateOrdersDeleteCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion)

Deletes the certificate associated with the certificate order

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.CertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let certificateOrderName = "certificateOrderName_example"; // String | Certificate name
let name = "name_example"; // String | Certificate name
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.certificateOrdersDeleteCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Azure resource group name | 
 **certificateOrderName** | **String**| Certificate name | 
 **name** | **String**| Certificate name | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## certificateOrdersDeleteCertificateOrder

> Object certificateOrdersDeleteCertificateOrder(resourceGroupName, name, subscriptionId, apiVersion)

Delete an existing certificate order

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.CertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let name = "name_example"; // String | Certificate name
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.certificateOrdersDeleteCertificateOrder(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Azure resource group name | 
 **name** | **String**| Certificate name | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## certificateOrdersGetCertificate

> CertificateOrderCertificate certificateOrdersGetCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion)

Get certificate associated with the certificate order

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.CertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let certificateOrderName = "certificateOrderName_example"; // String | Certificate name
let name = "name_example"; // String | Certificate name
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.certificateOrdersGetCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Azure resource group name | 
 **certificateOrderName** | **String**| Certificate name | 
 **name** | **String**| Certificate name | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**CertificateOrderCertificate**](CertificateOrderCertificate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## certificateOrdersGetCertificateOrder

> CertificateOrder certificateOrdersGetCertificateOrder(resourceGroupName, name, subscriptionId, apiVersion)

Get a certificate order

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.CertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let name = "name_example"; // String | Certificate name
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.certificateOrdersGetCertificateOrder(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Azure resource group name | 
 **name** | **String**| Certificate name | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**CertificateOrder**](CertificateOrder.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## certificateOrdersGetCertificateOrders

> CertificateOrderCollection certificateOrdersGetCertificateOrders(resourceGroupName, subscriptionId, apiVersion)

Get certificate orders in a resource group

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.CertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.certificateOrdersGetCertificateOrders(resourceGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Azure resource group name | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**CertificateOrderCollection**](CertificateOrderCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## certificateOrdersGetCertificates

> CertificateOrderCertificateCollection certificateOrdersGetCertificates(resourceGroupName, certificateOrderName, subscriptionId, apiVersion)

List all certificates associated with a certificate order (only one certificate can be associated with an order at a time)

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.CertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let certificateOrderName = "certificateOrderName_example"; // String | Certificate name
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.certificateOrdersGetCertificates(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Azure resource group name | 
 **certificateOrderName** | **String**| Certificate name | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**CertificateOrderCertificateCollection**](CertificateOrderCertificateCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## certificateOrdersReissueCertificateOrder

> Object certificateOrdersReissueCertificateOrder(resourceGroupName, name, subscriptionId, apiVersion, reissueCertificateOrderRequest)

Reissue an existing certificate order

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.CertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let name = "name_example"; // String | Certificate name
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let reissueCertificateOrderRequest = new WebSiteManagementClient.ReissueCertificateOrderRequest(); // ReissueCertificateOrderRequest | Reissue parameters
apiInstance.certificateOrdersReissueCertificateOrder(resourceGroupName, name, subscriptionId, apiVersion, reissueCertificateOrderRequest, (error, data, response) => {
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
 **resourceGroupName** | **String**| Azure resource group name | 
 **name** | **String**| Certificate name | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **reissueCertificateOrderRequest** | [**ReissueCertificateOrderRequest**](ReissueCertificateOrderRequest.md)| Reissue parameters | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## certificateOrdersRenewCertificateOrder

> Object certificateOrdersRenewCertificateOrder(resourceGroupName, name, subscriptionId, apiVersion, renewCertificateOrderRequest)

Renew an existing certificate order

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.CertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let name = "name_example"; // String | Certificate name
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let renewCertificateOrderRequest = new WebSiteManagementClient.RenewCertificateOrderRequest(); // RenewCertificateOrderRequest | Renew parameters
apiInstance.certificateOrdersRenewCertificateOrder(resourceGroupName, name, subscriptionId, apiVersion, renewCertificateOrderRequest, (error, data, response) => {
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
 **resourceGroupName** | **String**| Azure resource group name | 
 **name** | **String**| Certificate name | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **renewCertificateOrderRequest** | [**RenewCertificateOrderRequest**](RenewCertificateOrderRequest.md)| Renew parameters | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## certificateOrdersResendCertificateEmail

> Object certificateOrdersResendCertificateEmail(resourceGroupName, name, subscriptionId, apiVersion)

Resend certificate email

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.CertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let name = "name_example"; // String | Certificate order name
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.certificateOrdersResendCertificateEmail(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Azure resource group name | 
 **name** | **String**| Certificate order name | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## certificateOrdersRetrieveCertificateActions

> [CertificateOrderAction] certificateOrdersRetrieveCertificateActions(resourceGroupName, name, subscriptionId, apiVersion)

Retrieve the list of certificate actions

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.CertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let name = "name_example"; // String | Certificate order name
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.certificateOrdersRetrieveCertificateActions(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Azure resource group name | 
 **name** | **String**| Certificate order name | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**[CertificateOrderAction]**](CertificateOrderAction.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## certificateOrdersRetrieveCertificateEmailHistory

> [CertificateEmail] certificateOrdersRetrieveCertificateEmailHistory(resourceGroupName, name, subscriptionId, apiVersion)

Retrieve email history

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.CertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let name = "name_example"; // String | Certificate order name
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.certificateOrdersRetrieveCertificateEmailHistory(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Azure resource group name | 
 **name** | **String**| Certificate order name | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**[CertificateEmail]**](CertificateEmail.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## certificateOrdersUpdateCertificate

> CertificateOrderCertificate certificateOrdersUpdateCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion, keyVaultCertificate)

Associates a Key Vault secret to a certificate store that will be used for storing the certificate once it&#39;s ready

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.CertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let certificateOrderName = "certificateOrderName_example"; // String | Certificate name
let name = "name_example"; // String | Certificate name
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let keyVaultCertificate = new WebSiteManagementClient.CertificateOrderCertificate(); // CertificateOrderCertificate | Key Vault secret csm Id
apiInstance.certificateOrdersUpdateCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion, keyVaultCertificate, (error, data, response) => {
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
 **resourceGroupName** | **String**| Azure resource group name | 
 **certificateOrderName** | **String**| Certificate name | 
 **name** | **String**| Certificate name | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **keyVaultCertificate** | [**CertificateOrderCertificate**](CertificateOrderCertificate.md)| Key Vault secret csm Id | 

### Return type

[**CertificateOrderCertificate**](CertificateOrderCertificate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## certificateOrdersUpdateCertificateOrder

> CertificateOrder certificateOrdersUpdateCertificateOrder(resourceGroupName, name, subscriptionId, apiVersion, certificateDistinguishedName)

Create or update a certificate purchase order

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.CertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let name = "name_example"; // String | Certificate name
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let certificateDistinguishedName = new WebSiteManagementClient.CertificateOrder(); // CertificateOrder | Distinguished name to be used for purchasing certificate
apiInstance.certificateOrdersUpdateCertificateOrder(resourceGroupName, name, subscriptionId, apiVersion, certificateDistinguishedName, (error, data, response) => {
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
 **resourceGroupName** | **String**| Azure resource group name | 
 **name** | **String**| Certificate name | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **certificateDistinguishedName** | [**CertificateOrder**](CertificateOrder.md)| Distinguished name to be used for purchasing certificate | 

### Return type

[**CertificateOrder**](CertificateOrder.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## certificateOrdersVerifyDomainOwnership

> Object certificateOrdersVerifyDomainOwnership(resourceGroupName, name, subscriptionId, apiVersion)

Verify domain ownership for this certificate order

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.CertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let name = "name_example"; // String | Certificate order name
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.certificateOrdersVerifyDomainOwnership(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Azure resource group name | 
 **name** | **String**| Certificate order name | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

