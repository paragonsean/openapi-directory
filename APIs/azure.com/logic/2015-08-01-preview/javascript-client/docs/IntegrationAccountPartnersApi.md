# LogicManagementClient.IntegrationAccountPartnersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integrationAccountPartnersCreateOrUpdate**](IntegrationAccountPartnersApi.md#integrationAccountPartnersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/partners/{partnerName} | 
[**integrationAccountPartnersDelete**](IntegrationAccountPartnersApi.md#integrationAccountPartnersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/partners/{partnerName} | 
[**integrationAccountPartnersGet**](IntegrationAccountPartnersApi.md#integrationAccountPartnersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/partners/{partnerName} | 
[**integrationAccountPartnersList**](IntegrationAccountPartnersApi.md#integrationAccountPartnersList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/partners | 



## integrationAccountPartnersCreateOrUpdate

> IntegrationAccountPartner integrationAccountPartnersCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, partnerName, apiVersion, partner)



Creates or updates an integration account partner.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';

let apiInstance = new LogicManagementClient.IntegrationAccountPartnersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let partnerName = "partnerName_example"; // String | The integration account partner name.
let apiVersion = "apiVersion_example"; // String | The API version.
let partner = new LogicManagementClient.IntegrationAccountPartner(); // IntegrationAccountPartner | The integration account partner.
apiInstance.integrationAccountPartnersCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, partnerName, apiVersion, partner, (error, data, response) => {
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
 **partnerName** | **String**| The integration account partner name. | 
 **apiVersion** | **String**| The API version. | 
 **partner** | [**IntegrationAccountPartner**](IntegrationAccountPartner.md)| The integration account partner. | 

### Return type

[**IntegrationAccountPartner**](IntegrationAccountPartner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## integrationAccountPartnersDelete

> integrationAccountPartnersDelete(subscriptionId, resourceGroupName, integrationAccountName, partnerName, apiVersion)



Deletes an integration account partner.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';

let apiInstance = new LogicManagementClient.IntegrationAccountPartnersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let partnerName = "partnerName_example"; // String | The integration account partner name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationAccountPartnersDelete(subscriptionId, resourceGroupName, integrationAccountName, partnerName, apiVersion, (error, data, response) => {
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
 **partnerName** | **String**| The integration account partner name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## integrationAccountPartnersGet

> IntegrationAccountPartner integrationAccountPartnersGet(subscriptionId, resourceGroupName, integrationAccountName, partnerName, apiVersion)



Gets an integration account partner.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';

let apiInstance = new LogicManagementClient.IntegrationAccountPartnersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let partnerName = "partnerName_example"; // String | The integration account partner name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationAccountPartnersGet(subscriptionId, resourceGroupName, integrationAccountName, partnerName, apiVersion, (error, data, response) => {
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
 **partnerName** | **String**| The integration account partner name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**IntegrationAccountPartner**](IntegrationAccountPartner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## integrationAccountPartnersList

> IntegrationAccountPartnerListResult integrationAccountPartnersList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, opts)



Gets a list of integration account partners.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';

let apiInstance = new LogicManagementClient.IntegrationAccountPartnersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'top': 56, // Number | The number of items to be included in the result.
  'filter': "filter_example" // String | The filter to apply on the operation.
};
apiInstance.integrationAccountPartnersList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, opts, (error, data, response) => {
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
 **filter** | **String**| The filter to apply on the operation. | [optional] 

### Return type

[**IntegrationAccountPartnerListResult**](IntegrationAccountPartnerListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

