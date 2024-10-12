# TopLevelDomainsApiClient.TopLevelDomainsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**topLevelDomainsGet**](TopLevelDomainsApi.md#topLevelDomainsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/topLevelDomains/{name} | Get details of a top-level domain.
[**topLevelDomainsList**](TopLevelDomainsApi.md#topLevelDomainsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/topLevelDomains | Get all top-level domains supported for registration.
[**topLevelDomainsListAgreements**](TopLevelDomainsApi.md#topLevelDomainsListAgreements) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DomainRegistration/topLevelDomains/{name}/listAgreements | Gets all legal agreements that user needs to accept before purchasing a domain.



## topLevelDomainsGet

> TopLevelDomain topLevelDomainsGet(name, subscriptionId, apiVersion)

Get details of a top-level domain.

Description for Get details of a top-level domain.

### Example

```javascript
import TopLevelDomainsApiClient from 'top_level_domains_api_client';
let defaultClient = TopLevelDomainsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TopLevelDomainsApiClient.TopLevelDomainsApi();
let name = "name_example"; // String | Name of the top-level domain.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.topLevelDomainsGet(name, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of the top-level domain. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**TopLevelDomain**](TopLevelDomain.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## topLevelDomainsList

> TopLevelDomainCollection topLevelDomainsList(subscriptionId, apiVersion)

Get all top-level domains supported for registration.

Description for Get all top-level domains supported for registration.

### Example

```javascript
import TopLevelDomainsApiClient from 'top_level_domains_api_client';
let defaultClient = TopLevelDomainsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TopLevelDomainsApiClient.TopLevelDomainsApi();
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.topLevelDomainsList(subscriptionId, apiVersion, (error, data, response) => {
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

[**TopLevelDomainCollection**](TopLevelDomainCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## topLevelDomainsListAgreements

> TldLegalAgreementCollection topLevelDomainsListAgreements(name, subscriptionId, apiVersion, agreementOption)

Gets all legal agreements that user needs to accept before purchasing a domain.

Description for Gets all legal agreements that user needs to accept before purchasing a domain.

### Example

```javascript
import TopLevelDomainsApiClient from 'top_level_domains_api_client';
let defaultClient = TopLevelDomainsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TopLevelDomainsApiClient.TopLevelDomainsApi();
let name = "name_example"; // String | Name of the top-level domain.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let agreementOption = new TopLevelDomainsApiClient.TopLevelDomainAgreementOption(); // TopLevelDomainAgreementOption | Domain agreement options.
apiInstance.topLevelDomainsListAgreements(name, subscriptionId, apiVersion, agreementOption, (error, data, response) => {
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
 **name** | **String**| Name of the top-level domain. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **agreementOption** | [**TopLevelDomainAgreementOption**](TopLevelDomainAgreementOption.md)| Domain agreement options. | 

### Return type

[**TldLegalAgreementCollection**](TldLegalAgreementCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

