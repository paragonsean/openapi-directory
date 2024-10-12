# SecurityCenter.AutomationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**automationsCreateOrUpdate**](AutomationsApi.md#automationsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/automations/{automationName} | 
[**automationsDelete**](AutomationsApi.md#automationsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/automations/{automationName} | 
[**automationsGet**](AutomationsApi.md#automationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/automations/{automationName} | 
[**automationsList**](AutomationsApi.md#automationsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/automations | 
[**automationsListByResourceGroup**](AutomationsApi.md#automationsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/automations | 
[**automationsValidate**](AutomationsApi.md#automationsValidate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/automations/{automationName}/validate | 



## automationsCreateOrUpdate

> Automation automationsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, automationName, automation)



Creates or updates a security automation. If a security automation is already created and a subsequent request is issued for the same automation id, then it will be updated.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AutomationsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let automationName = "automationName_example"; // String | The security automation name.
let automation = new SecurityCenter.Automation(); // Automation | The security automation resource
apiInstance.automationsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, automationName, automation, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **automationName** | **String**| The security automation name. | 
 **automation** | [**Automation**](Automation.md)| The security automation resource | 

### Return type

[**Automation**](Automation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## automationsDelete

> automationsDelete(apiVersion, subscriptionId, resourceGroupName, automationName)



Deletes a security automation.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AutomationsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let automationName = "automationName_example"; // String | The security automation name.
apiInstance.automationsDelete(apiVersion, subscriptionId, resourceGroupName, automationName, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **automationName** | **String**| The security automation name. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## automationsGet

> Automation automationsGet(apiVersion, subscriptionId, resourceGroupName, automationName)



Retrieves information about the model of a security automation.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AutomationsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let automationName = "automationName_example"; // String | The security automation name.
apiInstance.automationsGet(apiVersion, subscriptionId, resourceGroupName, automationName, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **automationName** | **String**| The security automation name. | 

### Return type

[**Automation**](Automation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## automationsList

> AutomationList automationsList(apiVersion, subscriptionId)



Lists all the security automations in the specified subscription. Use the &#39;nextLink&#39; property in the response to get the next page of security automations for the specified subscription.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AutomationsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
apiInstance.automationsList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 

### Return type

[**AutomationList**](AutomationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## automationsListByResourceGroup

> AutomationList automationsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)



Lists all the security automations in the specified resource group. Use the &#39;nextLink&#39; property in the response to get the next page of security automations for the specified resource group.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AutomationsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
apiInstance.automationsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 

### Return type

[**AutomationList**](AutomationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## automationsValidate

> AutomationValidationStatus automationsValidate(apiVersion, subscriptionId, resourceGroupName, automationName, automation)



Validates the security automation model before create or update. Any validation errors are returned to the client.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AutomationsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let automationName = "automationName_example"; // String | The security automation name.
let automation = new SecurityCenter.Automation(); // Automation | The security automation resource
apiInstance.automationsValidate(apiVersion, subscriptionId, resourceGroupName, automationName, automation, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **automationName** | **String**| The security automation name. | 
 **automation** | [**Automation**](Automation.md)| The security automation resource | 

### Return type

[**AutomationValidationStatus**](AutomationValidationStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

