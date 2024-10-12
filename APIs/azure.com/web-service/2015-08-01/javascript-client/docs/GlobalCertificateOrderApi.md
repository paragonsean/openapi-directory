# WebSiteManagementClient.GlobalCertificateOrderApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**globalCertificateOrderGetAllCertificateOrders**](GlobalCertificateOrderApi.md#globalCertificateOrderGetAllCertificateOrders) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.CertificateRegistration/certificateOrders | Lists all domains in a subscription
[**globalCertificateOrderValidateCertificatePurchaseInformation**](GlobalCertificateOrderApi.md#globalCertificateOrderValidateCertificatePurchaseInformation) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.CertificateRegistration/validateCertificateRegistrationInformation | Validate certificate purchase information



## globalCertificateOrderGetAllCertificateOrders

> CertificateOrderCollection globalCertificateOrderGetAllCertificateOrders(subscriptionId, apiVersion)

Lists all domains in a subscription

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.GlobalCertificateOrderApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.globalCertificateOrderGetAllCertificateOrders(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**CertificateOrderCollection**](CertificateOrderCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## globalCertificateOrderValidateCertificatePurchaseInformation

> Object globalCertificateOrderValidateCertificatePurchaseInformation(subscriptionId, apiVersion, certificateOrder)

Validate certificate purchase information

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.GlobalCertificateOrderApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let certificateOrder = new WebSiteManagementClient.CertificateOrder(); // CertificateOrder | Certificate order
apiInstance.globalCertificateOrderValidateCertificatePurchaseInformation(subscriptionId, apiVersion, certificateOrder, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **certificateOrder** | [**CertificateOrder**](CertificateOrder.md)| Certificate order | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml

