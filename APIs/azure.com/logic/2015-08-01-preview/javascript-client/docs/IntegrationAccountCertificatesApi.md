# LogicManagementClient.IntegrationAccountCertificatesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integrationAccountCertificatesCreateOrUpdate**](IntegrationAccountCertificatesApi.md#integrationAccountCertificatesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/certificates/{certificateName} | 
[**integrationAccountCertificatesDelete**](IntegrationAccountCertificatesApi.md#integrationAccountCertificatesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/certificates/{certificateName} | 
[**integrationAccountCertificatesGet**](IntegrationAccountCertificatesApi.md#integrationAccountCertificatesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/certificates/{certificateName} | 
[**integrationAccountCertificatesList**](IntegrationAccountCertificatesApi.md#integrationAccountCertificatesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/certificates | 



## integrationAccountCertificatesCreateOrUpdate

> IntegrationAccountCertificate integrationAccountCertificatesCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, certificateName, apiVersion, certificate)



Creates or updates an integration account certificate.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';

let apiInstance = new LogicManagementClient.IntegrationAccountCertificatesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let certificateName = "certificateName_example"; // String | The integration account certificate name.
let apiVersion = "apiVersion_example"; // String | The API version.
let certificate = new LogicManagementClient.IntegrationAccountCertificate(); // IntegrationAccountCertificate | The integration account certificate.
apiInstance.integrationAccountCertificatesCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, certificateName, apiVersion, certificate, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **integrationAccountName** | **String**| The integration account name. | 
 **certificateName** | **String**| The integration account certificate name. | 
 **apiVersion** | **String**| The API version. | 
 **certificate** | [**IntegrationAccountCertificate**](IntegrationAccountCertificate.md)| The integration account certificate. | 

### Return type

[**IntegrationAccountCertificate**](IntegrationAccountCertificate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## integrationAccountCertificatesDelete

> integrationAccountCertificatesDelete(subscriptionId, resourceGroupName, integrationAccountName, certificateName, apiVersion)



Deletes an integration account certificate.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';

let apiInstance = new LogicManagementClient.IntegrationAccountCertificatesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let certificateName = "certificateName_example"; // String | The integration account certificate name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationAccountCertificatesDelete(subscriptionId, resourceGroupName, integrationAccountName, certificateName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **integrationAccountName** | **String**| The integration account name. | 
 **certificateName** | **String**| The integration account certificate name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## integrationAccountCertificatesGet

> IntegrationAccountCertificate integrationAccountCertificatesGet(subscriptionId, resourceGroupName, integrationAccountName, certificateName, apiVersion)



Gets an integration account certificate.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';

let apiInstance = new LogicManagementClient.IntegrationAccountCertificatesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let certificateName = "certificateName_example"; // String | The integration account certificate name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationAccountCertificatesGet(subscriptionId, resourceGroupName, integrationAccountName, certificateName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **integrationAccountName** | **String**| The integration account name. | 
 **certificateName** | **String**| The integration account certificate name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**IntegrationAccountCertificate**](IntegrationAccountCertificate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## integrationAccountCertificatesList

> IntegrationAccountCertificateListResult integrationAccountCertificatesList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, opts)



Gets a list of integration account certificates.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';

let apiInstance = new LogicManagementClient.IntegrationAccountCertificatesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'top': 56 // Number | The number of items to be included in the result.
};
apiInstance.integrationAccountCertificatesList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **integrationAccountName** | **String**| The integration account name. | 
 **apiVersion** | **String**| The API version. | 
 **top** | **Number**| The number of items to be included in the result. | [optional] 

### Return type

[**IntegrationAccountCertificateListResult**](IntegrationAccountCertificateListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

