# WebSiteManagementClient.TopLevelDomainsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**topLevelDomainsGetGetTopLevelDomains**](TopLevelDomainsApi.md#topLevelDomainsGetGetTopLevelDomains) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/topLevelDomains | Lists all top level domains supported for registration
[**topLevelDomainsGetTopLevelDomain**](TopLevelDomainsApi.md#topLevelDomainsGetTopLevelDomain) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/topLevelDomains/{name} | Gets details of a top level domain
[**topLevelDomainsListTopLevelDomainAgreements**](TopLevelDomainsApi.md#topLevelDomainsListTopLevelDomainAgreements) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/topLevelDomains/{name}/listAgreements | Lists legal agreements that user needs to accept before purchasing domain



## topLevelDomainsGetGetTopLevelDomains

> TopLevelDomainCollection topLevelDomainsGetGetTopLevelDomains(subscriptionId, apiVersion)

Lists all top level domains supported for registration

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.TopLevelDomainsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.topLevelDomainsGetGetTopLevelDomains(subscriptionId, apiVersion, (error, data, response) => {
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

[**TopLevelDomainCollection**](TopLevelDomainCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## topLevelDomainsGetTopLevelDomain

> TopLevelDomain topLevelDomainsGetTopLevelDomain(name, subscriptionId, apiVersion)

Gets details of a top level domain

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.TopLevelDomainsApi();
let name = "name_example"; // String | Name of the top level domain
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.topLevelDomainsGetTopLevelDomain(name, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of the top level domain | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**TopLevelDomain**](TopLevelDomain.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## topLevelDomainsListTopLevelDomainAgreements

> TldLegalAgreementCollection topLevelDomainsListTopLevelDomainAgreements(name, subscriptionId, apiVersion, agreementOption)

Lists legal agreements that user needs to accept before purchasing domain

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.TopLevelDomainsApi();
let name = "name_example"; // String | Name of the top level domain
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let agreementOption = new WebSiteManagementClient.TopLevelDomainAgreementOption(); // TopLevelDomainAgreementOption | Domain agreement options
apiInstance.topLevelDomainsListTopLevelDomainAgreements(name, subscriptionId, apiVersion, agreementOption, (error, data, response) => {
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
 **name** | **String**| Name of the top level domain | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **agreementOption** | [**TopLevelDomainAgreementOption**](TopLevelDomainAgreementOption.md)| Domain agreement options | 

### Return type

[**TldLegalAgreementCollection**](TldLegalAgreementCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json

