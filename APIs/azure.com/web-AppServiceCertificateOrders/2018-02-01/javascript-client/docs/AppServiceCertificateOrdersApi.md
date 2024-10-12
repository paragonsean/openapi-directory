# AppServiceCertificateOrdersApiClient.AppServiceCertificateOrdersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appServiceCertificateOrdersCreateOrUpdate**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName} | Create or update a certificate purchase order.
[**appServiceCertificateOrdersCreateOrUpdateCertificate**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersCreateOrUpdateCertificate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/certificates/{name} | Creates or updates a certificate and associates with key vault secret.
[**appServiceCertificateOrdersDelete**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName} | Delete an existing certificate order.
[**appServiceCertificateOrdersDeleteCertificate**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersDeleteCertificate) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/certificates/{name} | Delete the certificate associated with a certificate order.
[**appServiceCertificateOrdersGet**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName} | Get a certificate order.
[**appServiceCertificateOrdersGetCertificate**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersGetCertificate) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/certificates/{name} | Get the certificate associated with a certificate order.
[**appServiceCertificateOrdersList**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.CertificateRegistration/certificateOrders | List all certificate orders in a subscription.
[**appServiceCertificateOrdersListByResourceGroup**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders | Get certificate orders in a resource group.
[**appServiceCertificateOrdersListCertificates**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersListCertificates) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/certificates | List all certificates associated with a certificate order.
[**appServiceCertificateOrdersReissue**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersReissue) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/reissue | Reissue an existing certificate order.
[**appServiceCertificateOrdersRenew**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersRenew) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/renew | Renew an existing certificate order.
[**appServiceCertificateOrdersResendEmail**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersResendEmail) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/resendEmail | Resend certificate email.
[**appServiceCertificateOrdersResendRequestEmails**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersResendRequestEmails) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/resendRequestEmails | Verify domain ownership for this certificate order.
[**appServiceCertificateOrdersRetrieveCertificateActions**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersRetrieveCertificateActions) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{name}/retrieveCertificateActions | Retrieve the list of certificate actions.
[**appServiceCertificateOrdersRetrieveCertificateEmailHistory**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersRetrieveCertificateEmailHistory) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{name}/retrieveEmailHistory | Retrieve email history.
[**appServiceCertificateOrdersRetrieveSiteSeal**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersRetrieveSiteSeal) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/retrieveSiteSeal | Verify domain ownership for this certificate order.
[**appServiceCertificateOrdersUpdate**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName} | Create or update a certificate purchase order.
[**appServiceCertificateOrdersUpdateCertificate**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersUpdateCertificate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/certificates/{name} | Creates or updates a certificate and associates with key vault secret.
[**appServiceCertificateOrdersValidatePurchaseInformation**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersValidatePurchaseInformation) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.CertificateRegistration/validateCertificateRegistrationInformation | Validate information for a certificate order.
[**appServiceCertificateOrdersVerifyDomainOwnership**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersVerifyDomainOwnership) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/verifyDomainOwnership | Verify domain ownership for this certificate order.



## appServiceCertificateOrdersCreateOrUpdate

> AppServiceCertificateOrder appServiceCertificateOrdersCreateOrUpdate(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, certificateDistinguishedName)

Create or update a certificate purchase order.

Create or update a certificate purchase order.

### Example

```javascript
import AppServiceCertificateOrdersApiClient from 'app_service_certificate_orders_api_client';
let defaultClient = AppServiceCertificateOrdersApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceCertificateOrdersApiClient.AppServiceCertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let certificateDistinguishedName = new AppServiceCertificateOrdersApiClient.AppServiceCertificateOrder(); // AppServiceCertificateOrder | Distinguished name to use for the certificate order.
apiInstance.appServiceCertificateOrdersCreateOrUpdate(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, certificateDistinguishedName, (error, data, response) => {
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
 **certificateOrderName** | **String**| Name of the certificate order. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **certificateDistinguishedName** | [**AppServiceCertificateOrder**](AppServiceCertificateOrder.md)| Distinguished name to use for the certificate order. | 

### Return type

[**AppServiceCertificateOrder**](AppServiceCertificateOrder.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appServiceCertificateOrdersCreateOrUpdateCertificate

> AppServiceCertificateResource appServiceCertificateOrdersCreateOrUpdateCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion, keyVaultCertificate)

Creates or updates a certificate and associates with key vault secret.

Creates or updates a certificate and associates with key vault secret.

### Example

```javascript
import AppServiceCertificateOrdersApiClient from 'app_service_certificate_orders_api_client';
let defaultClient = AppServiceCertificateOrdersApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceCertificateOrdersApiClient.AppServiceCertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
let name = "name_example"; // String | Name of the certificate.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let keyVaultCertificate = new AppServiceCertificateOrdersApiClient.AppServiceCertificateResource(); // AppServiceCertificateResource | Key vault certificate resource Id.
apiInstance.appServiceCertificateOrdersCreateOrUpdateCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion, keyVaultCertificate, (error, data, response) => {
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
 **certificateOrderName** | **String**| Name of the certificate order. | 
 **name** | **String**| Name of the certificate. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **keyVaultCertificate** | [**AppServiceCertificateResource**](AppServiceCertificateResource.md)| Key vault certificate resource Id. | 

### Return type

[**AppServiceCertificateResource**](AppServiceCertificateResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appServiceCertificateOrdersDelete

> appServiceCertificateOrdersDelete(resourceGroupName, certificateOrderName, subscriptionId, apiVersion)

Delete an existing certificate order.

Delete an existing certificate order.

### Example

```javascript
import AppServiceCertificateOrdersApiClient from 'app_service_certificate_orders_api_client';
let defaultClient = AppServiceCertificateOrdersApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceCertificateOrdersApiClient.AppServiceCertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceCertificateOrdersDelete(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, (error, data, response) => {
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
 **certificateOrderName** | **String**| Name of the certificate order. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## appServiceCertificateOrdersDeleteCertificate

> appServiceCertificateOrdersDeleteCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion)

Delete the certificate associated with a certificate order.

Delete the certificate associated with a certificate order.

### Example

```javascript
import AppServiceCertificateOrdersApiClient from 'app_service_certificate_orders_api_client';
let defaultClient = AppServiceCertificateOrdersApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceCertificateOrdersApiClient.AppServiceCertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
let name = "name_example"; // String | Name of the certificate.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceCertificateOrdersDeleteCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **certificateOrderName** | **String**| Name of the certificate order. | 
 **name** | **String**| Name of the certificate. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## appServiceCertificateOrdersGet

> AppServiceCertificateOrder appServiceCertificateOrdersGet(resourceGroupName, certificateOrderName, subscriptionId, apiVersion)

Get a certificate order.

Get a certificate order.

### Example

```javascript
import AppServiceCertificateOrdersApiClient from 'app_service_certificate_orders_api_client';
let defaultClient = AppServiceCertificateOrdersApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceCertificateOrdersApiClient.AppServiceCertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order..
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceCertificateOrdersGet(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, (error, data, response) => {
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
 **certificateOrderName** | **String**| Name of the certificate order.. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**AppServiceCertificateOrder**](AppServiceCertificateOrder.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceCertificateOrdersGetCertificate

> AppServiceCertificateResource appServiceCertificateOrdersGetCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion)

Get the certificate associated with a certificate order.

Get the certificate associated with a certificate order.

### Example

```javascript
import AppServiceCertificateOrdersApiClient from 'app_service_certificate_orders_api_client';
let defaultClient = AppServiceCertificateOrdersApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceCertificateOrdersApiClient.AppServiceCertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
let name = "name_example"; // String | Name of the certificate.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceCertificateOrdersGetCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **certificateOrderName** | **String**| Name of the certificate order. | 
 **name** | **String**| Name of the certificate. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**AppServiceCertificateResource**](AppServiceCertificateResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceCertificateOrdersList

> AppServiceCertificateOrderCollection appServiceCertificateOrdersList(subscriptionId, apiVersion)

List all certificate orders in a subscription.

List all certificate orders in a subscription.

### Example

```javascript
import AppServiceCertificateOrdersApiClient from 'app_service_certificate_orders_api_client';
let defaultClient = AppServiceCertificateOrdersApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceCertificateOrdersApiClient.AppServiceCertificateOrdersApi();
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceCertificateOrdersList(subscriptionId, apiVersion, (error, data, response) => {
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

[**AppServiceCertificateOrderCollection**](AppServiceCertificateOrderCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceCertificateOrdersListByResourceGroup

> AppServiceCertificateOrderCollection appServiceCertificateOrdersListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)

Get certificate orders in a resource group.

Get certificate orders in a resource group.

### Example

```javascript
import AppServiceCertificateOrdersApiClient from 'app_service_certificate_orders_api_client';
let defaultClient = AppServiceCertificateOrdersApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceCertificateOrdersApiClient.AppServiceCertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceCertificateOrdersListByResourceGroup(resourceGroupName, subscriptionId, apiVersion, (error, data, response) => {
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

[**AppServiceCertificateOrderCollection**](AppServiceCertificateOrderCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceCertificateOrdersListCertificates

> AppServiceCertificateCollection appServiceCertificateOrdersListCertificates(resourceGroupName, certificateOrderName, subscriptionId, apiVersion)

List all certificates associated with a certificate order.

List all certificates associated with a certificate order.

### Example

```javascript
import AppServiceCertificateOrdersApiClient from 'app_service_certificate_orders_api_client';
let defaultClient = AppServiceCertificateOrdersApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceCertificateOrdersApiClient.AppServiceCertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceCertificateOrdersListCertificates(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, (error, data, response) => {
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
 **certificateOrderName** | **String**| Name of the certificate order. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**AppServiceCertificateCollection**](AppServiceCertificateCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceCertificateOrdersReissue

> appServiceCertificateOrdersReissue(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, reissueCertificateOrderRequest)

Reissue an existing certificate order.

Reissue an existing certificate order.

### Example

```javascript
import AppServiceCertificateOrdersApiClient from 'app_service_certificate_orders_api_client';
let defaultClient = AppServiceCertificateOrdersApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceCertificateOrdersApiClient.AppServiceCertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let reissueCertificateOrderRequest = new AppServiceCertificateOrdersApiClient.ReissueCertificateOrderRequest(); // ReissueCertificateOrderRequest | Parameters for the reissue.
apiInstance.appServiceCertificateOrdersReissue(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, reissueCertificateOrderRequest, (error, data, response) => {
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
 **certificateOrderName** | **String**| Name of the certificate order. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **reissueCertificateOrderRequest** | [**ReissueCertificateOrderRequest**](ReissueCertificateOrderRequest.md)| Parameters for the reissue. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## appServiceCertificateOrdersRenew

> appServiceCertificateOrdersRenew(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, renewCertificateOrderRequest)

Renew an existing certificate order.

Renew an existing certificate order.

### Example

```javascript
import AppServiceCertificateOrdersApiClient from 'app_service_certificate_orders_api_client';
let defaultClient = AppServiceCertificateOrdersApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceCertificateOrdersApiClient.AppServiceCertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let renewCertificateOrderRequest = new AppServiceCertificateOrdersApiClient.RenewCertificateOrderRequest(); // RenewCertificateOrderRequest | Renew parameters
apiInstance.appServiceCertificateOrdersRenew(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, renewCertificateOrderRequest, (error, data, response) => {
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
 **certificateOrderName** | **String**| Name of the certificate order. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **renewCertificateOrderRequest** | [**RenewCertificateOrderRequest**](RenewCertificateOrderRequest.md)| Renew parameters | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## appServiceCertificateOrdersResendEmail

> appServiceCertificateOrdersResendEmail(resourceGroupName, certificateOrderName, subscriptionId, apiVersion)

Resend certificate email.

Resend certificate email.

### Example

```javascript
import AppServiceCertificateOrdersApiClient from 'app_service_certificate_orders_api_client';
let defaultClient = AppServiceCertificateOrdersApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceCertificateOrdersApiClient.AppServiceCertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceCertificateOrdersResendEmail(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, (error, data, response) => {
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
 **certificateOrderName** | **String**| Name of the certificate order. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## appServiceCertificateOrdersResendRequestEmails

> appServiceCertificateOrdersResendRequestEmails(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, nameIdentifier)

Verify domain ownership for this certificate order.

Verify domain ownership for this certificate order.

### Example

```javascript
import AppServiceCertificateOrdersApiClient from 'app_service_certificate_orders_api_client';
let defaultClient = AppServiceCertificateOrdersApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceCertificateOrdersApiClient.AppServiceCertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let nameIdentifier = new AppServiceCertificateOrdersApiClient.AppServiceCertificateOrdersResendRequestEmailsRequest(); // AppServiceCertificateOrdersResendRequestEmailsRequest | Email address
apiInstance.appServiceCertificateOrdersResendRequestEmails(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, nameIdentifier, (error, data, response) => {
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
 **certificateOrderName** | **String**| Name of the certificate order. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **nameIdentifier** | [**AppServiceCertificateOrdersResendRequestEmailsRequest**](AppServiceCertificateOrdersResendRequestEmailsRequest.md)| Email address | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## appServiceCertificateOrdersRetrieveCertificateActions

> [CertificateOrderAction] appServiceCertificateOrdersRetrieveCertificateActions(resourceGroupName, name, subscriptionId, apiVersion)

Retrieve the list of certificate actions.

Retrieve the list of certificate actions.

### Example

```javascript
import AppServiceCertificateOrdersApiClient from 'app_service_certificate_orders_api_client';
let defaultClient = AppServiceCertificateOrdersApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceCertificateOrdersApiClient.AppServiceCertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the certificate order.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceCertificateOrdersRetrieveCertificateActions(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of the certificate order. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**[CertificateOrderAction]**](CertificateOrderAction.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceCertificateOrdersRetrieveCertificateEmailHistory

> [CertificateEmail] appServiceCertificateOrdersRetrieveCertificateEmailHistory(resourceGroupName, name, subscriptionId, apiVersion)

Retrieve email history.

Retrieve email history.

### Example

```javascript
import AppServiceCertificateOrdersApiClient from 'app_service_certificate_orders_api_client';
let defaultClient = AppServiceCertificateOrdersApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceCertificateOrdersApiClient.AppServiceCertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the certificate order.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceCertificateOrdersRetrieveCertificateEmailHistory(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of the certificate order. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**[CertificateEmail]**](CertificateEmail.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceCertificateOrdersRetrieveSiteSeal

> SiteSeal appServiceCertificateOrdersRetrieveSiteSeal(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, siteSealRequest)

Verify domain ownership for this certificate order.

Verify domain ownership for this certificate order.

### Example

```javascript
import AppServiceCertificateOrdersApiClient from 'app_service_certificate_orders_api_client';
let defaultClient = AppServiceCertificateOrdersApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceCertificateOrdersApiClient.AppServiceCertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let siteSealRequest = new AppServiceCertificateOrdersApiClient.SiteSealRequest(); // SiteSealRequest | Site seal request.
apiInstance.appServiceCertificateOrdersRetrieveSiteSeal(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, siteSealRequest, (error, data, response) => {
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
 **certificateOrderName** | **String**| Name of the certificate order. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **siteSealRequest** | [**SiteSealRequest**](SiteSealRequest.md)| Site seal request. | 

### Return type

[**SiteSeal**](SiteSeal.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appServiceCertificateOrdersUpdate

> AppServiceCertificateOrder appServiceCertificateOrdersUpdate(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, certificateDistinguishedName)

Create or update a certificate purchase order.

Create or update a certificate purchase order.

### Example

```javascript
import AppServiceCertificateOrdersApiClient from 'app_service_certificate_orders_api_client';
let defaultClient = AppServiceCertificateOrdersApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceCertificateOrdersApiClient.AppServiceCertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let certificateDistinguishedName = new AppServiceCertificateOrdersApiClient.AppServiceCertificateOrderPatchResource(); // AppServiceCertificateOrderPatchResource | Distinguished name to use for the certificate order.
apiInstance.appServiceCertificateOrdersUpdate(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, certificateDistinguishedName, (error, data, response) => {
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
 **certificateOrderName** | **String**| Name of the certificate order. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **certificateDistinguishedName** | [**AppServiceCertificateOrderPatchResource**](AppServiceCertificateOrderPatchResource.md)| Distinguished name to use for the certificate order. | 

### Return type

[**AppServiceCertificateOrder**](AppServiceCertificateOrder.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appServiceCertificateOrdersUpdateCertificate

> AppServiceCertificateResource appServiceCertificateOrdersUpdateCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion, keyVaultCertificate)

Creates or updates a certificate and associates with key vault secret.

Creates or updates a certificate and associates with key vault secret.

### Example

```javascript
import AppServiceCertificateOrdersApiClient from 'app_service_certificate_orders_api_client';
let defaultClient = AppServiceCertificateOrdersApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceCertificateOrdersApiClient.AppServiceCertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
let name = "name_example"; // String | Name of the certificate.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let keyVaultCertificate = new AppServiceCertificateOrdersApiClient.AppServiceCertificatePatchResource(); // AppServiceCertificatePatchResource | Key vault certificate resource Id.
apiInstance.appServiceCertificateOrdersUpdateCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion, keyVaultCertificate, (error, data, response) => {
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
 **certificateOrderName** | **String**| Name of the certificate order. | 
 **name** | **String**| Name of the certificate. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **keyVaultCertificate** | [**AppServiceCertificatePatchResource**](AppServiceCertificatePatchResource.md)| Key vault certificate resource Id. | 

### Return type

[**AppServiceCertificateResource**](AppServiceCertificateResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appServiceCertificateOrdersValidatePurchaseInformation

> appServiceCertificateOrdersValidatePurchaseInformation(subscriptionId, apiVersion, appServiceCertificateOrder)

Validate information for a certificate order.

Validate information for a certificate order.

### Example

```javascript
import AppServiceCertificateOrdersApiClient from 'app_service_certificate_orders_api_client';
let defaultClient = AppServiceCertificateOrdersApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceCertificateOrdersApiClient.AppServiceCertificateOrdersApi();
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let appServiceCertificateOrder = new AppServiceCertificateOrdersApiClient.AppServiceCertificateOrder(); // AppServiceCertificateOrder | Information for a certificate order.
apiInstance.appServiceCertificateOrdersValidatePurchaseInformation(subscriptionId, apiVersion, appServiceCertificateOrder, (error, data, response) => {
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
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **appServiceCertificateOrder** | [**AppServiceCertificateOrder**](AppServiceCertificateOrder.md)| Information for a certificate order. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## appServiceCertificateOrdersVerifyDomainOwnership

> appServiceCertificateOrdersVerifyDomainOwnership(resourceGroupName, certificateOrderName, subscriptionId, apiVersion)

Verify domain ownership for this certificate order.

Verify domain ownership for this certificate order.

### Example

```javascript
import AppServiceCertificateOrdersApiClient from 'app_service_certificate_orders_api_client';
let defaultClient = AppServiceCertificateOrdersApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceCertificateOrdersApiClient.AppServiceCertificateOrdersApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceCertificateOrdersVerifyDomainOwnership(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, (error, data, response) => {
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
 **certificateOrderName** | **String**| Name of the certificate order. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

