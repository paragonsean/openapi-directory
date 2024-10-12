# LogicManagementClient.IntegrationAccountAgreementsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integrationAccountAgreementsCreateOrUpdate**](IntegrationAccountAgreementsApi.md#integrationAccountAgreementsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/agreements/{agreementName} | 
[**integrationAccountAgreementsDelete**](IntegrationAccountAgreementsApi.md#integrationAccountAgreementsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/agreements/{agreementName} | 
[**integrationAccountAgreementsGet**](IntegrationAccountAgreementsApi.md#integrationAccountAgreementsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/agreements/{agreementName} | 
[**integrationAccountAgreementsList**](IntegrationAccountAgreementsApi.md#integrationAccountAgreementsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/agreements | 
[**integrationAccountAgreementsListContentCallbackUrl**](IntegrationAccountAgreementsApi.md#integrationAccountAgreementsListContentCallbackUrl) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/agreements/{agreementName}/listContentCallbackUrl | 



## integrationAccountAgreementsCreateOrUpdate

> IntegrationAccountAgreement integrationAccountAgreementsCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, agreementName, apiVersion, agreement)



Creates or updates an integration account agreement.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountAgreementsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let agreementName = "agreementName_example"; // String | The integration account agreement name.
let apiVersion = "apiVersion_example"; // String | The API version.
let agreement = new LogicManagementClient.IntegrationAccountAgreement(); // IntegrationAccountAgreement | The integration account agreement.
apiInstance.integrationAccountAgreementsCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, agreementName, apiVersion, agreement, (error, data, response) => {
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
 **agreementName** | **String**| The integration account agreement name. | 
 **apiVersion** | **String**| The API version. | 
 **agreement** | [**IntegrationAccountAgreement**](IntegrationAccountAgreement.md)| The integration account agreement. | 

### Return type

[**IntegrationAccountAgreement**](IntegrationAccountAgreement.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## integrationAccountAgreementsDelete

> integrationAccountAgreementsDelete(subscriptionId, resourceGroupName, integrationAccountName, agreementName, apiVersion)



Deletes an integration account agreement.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountAgreementsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let agreementName = "agreementName_example"; // String | The integration account agreement name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationAccountAgreementsDelete(subscriptionId, resourceGroupName, integrationAccountName, agreementName, apiVersion, (error, data, response) => {
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
 **agreementName** | **String**| The integration account agreement name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationAccountAgreementsGet

> IntegrationAccountAgreement integrationAccountAgreementsGet(subscriptionId, resourceGroupName, integrationAccountName, agreementName, apiVersion)



Gets an integration account agreement.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountAgreementsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let agreementName = "agreementName_example"; // String | The integration account agreement name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationAccountAgreementsGet(subscriptionId, resourceGroupName, integrationAccountName, agreementName, apiVersion, (error, data, response) => {
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
 **agreementName** | **String**| The integration account agreement name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**IntegrationAccountAgreement**](IntegrationAccountAgreement.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationAccountAgreementsList

> IntegrationAccountAgreementListResult integrationAccountAgreementsList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, opts)



Gets a list of integration account agreements.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountAgreementsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'top': 56, // Number | The number of items to be included in the result.
  'filter': "filter_example" // String | The filter to apply on the operation. Options for filters include: AgreementType.
};
apiInstance.integrationAccountAgreementsList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, opts, (error, data, response) => {
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
 **filter** | **String**| The filter to apply on the operation. Options for filters include: AgreementType. | [optional] 

### Return type

[**IntegrationAccountAgreementListResult**](IntegrationAccountAgreementListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationAccountAgreementsListContentCallbackUrl

> WorkflowTriggerCallbackUrl integrationAccountAgreementsListContentCallbackUrl(subscriptionId, resourceGroupName, integrationAccountName, agreementName, apiVersion, listContentCallbackUrl)



Get the content callback url.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountAgreementsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let agreementName = "agreementName_example"; // String | The integration account agreement name.
let apiVersion = "apiVersion_example"; // String | The API version.
let listContentCallbackUrl = new LogicManagementClient.GetCallbackUrlParameters(); // GetCallbackUrlParameters | 
apiInstance.integrationAccountAgreementsListContentCallbackUrl(subscriptionId, resourceGroupName, integrationAccountName, agreementName, apiVersion, listContentCallbackUrl, (error, data, response) => {
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
 **agreementName** | **String**| The integration account agreement name. | 
 **apiVersion** | **String**| The API version. | 
 **listContentCallbackUrl** | [**GetCallbackUrlParameters**](GetCallbackUrlParameters.md)|  | 

### Return type

[**WorkflowTriggerCallbackUrl**](WorkflowTriggerCallbackUrl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

