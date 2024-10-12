# MicrosoftNetApp.NetAppAccountsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountsCreateOrUpdate**](NetAppAccountsApi.md#accountsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName} | 
[**accountsDelete**](NetAppAccountsApi.md#accountsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName} | 
[**accountsGet**](NetAppAccountsApi.md#accountsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName} | 
[**accountsList**](NetAppAccountsApi.md#accountsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts | 
[**accountsUpdate**](NetAppAccountsApi.md#accountsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName} | 



## accountsCreateOrUpdate

> NetAppAccount accountsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, body)



Create or update a NetApp account

### Example

```javascript
import MicrosoftNetApp from 'microsoft_net_app';
let defaultClient = MicrosoftNetApp.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftNetApp.NetAppAccountsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let accountName = "accountName_example"; // String | The name of the NetApp account
let apiVersion = "'2017-08-15'"; // String | Version of the API to be used with the client request.
let body = new MicrosoftNetApp.NetAppAccount(); // NetAppAccount | NetApp Account object supplied in the body of the operation.
apiInstance.accountsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, body, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **accountName** | **String**| The name of the NetApp account | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | [default to &#39;2017-08-15&#39;]
 **body** | [**NetAppAccount**](NetAppAccount.md)| NetApp Account object supplied in the body of the operation. | 

### Return type

[**NetAppAccount**](NetAppAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## accountsDelete

> accountsDelete(subscriptionId, resourceGroupName, accountName, apiVersion)



Delete a NetApp account

### Example

```javascript
import MicrosoftNetApp from 'microsoft_net_app';
let defaultClient = MicrosoftNetApp.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftNetApp.NetAppAccountsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let accountName = "accountName_example"; // String | The name of the NetApp account
let apiVersion = "'2017-08-15'"; // String | Version of the API to be used with the client request.
apiInstance.accountsDelete(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **accountName** | **String**| The name of the NetApp account | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | [default to &#39;2017-08-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsGet

> NetAppAccount accountsGet(subscriptionId, resourceGroupName, accountName, apiVersion)



Get the NetApp account

### Example

```javascript
import MicrosoftNetApp from 'microsoft_net_app';
let defaultClient = MicrosoftNetApp.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftNetApp.NetAppAccountsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let accountName = "accountName_example"; // String | The name of the NetApp account
let apiVersion = "'2017-08-15'"; // String | Version of the API to be used with the client request.
apiInstance.accountsGet(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **accountName** | **String**| The name of the NetApp account | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | [default to &#39;2017-08-15&#39;]

### Return type

[**NetAppAccount**](NetAppAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsList

> NetAppAccountList accountsList(subscriptionId, resourceGroupName, apiVersion)



Lists all NetApp accounts in the resource group

### Example

```javascript
import MicrosoftNetApp from 'microsoft_net_app';
let defaultClient = MicrosoftNetApp.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftNetApp.NetAppAccountsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "'2017-08-15'"; // String | Version of the API to be used with the client request.
apiInstance.accountsList(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | [default to &#39;2017-08-15&#39;]

### Return type

[**NetAppAccountList**](NetAppAccountList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsUpdate

> NetAppAccount accountsUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, body)



Patch a NetApp account

### Example

```javascript
import MicrosoftNetApp from 'microsoft_net_app';
let defaultClient = MicrosoftNetApp.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftNetApp.NetAppAccountsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let accountName = "accountName_example"; // String | The name of the NetApp account
let apiVersion = "'2017-08-15'"; // String | Version of the API to be used with the client request.
let body = new MicrosoftNetApp.NetAppAccountPatch(); // NetAppAccountPatch | NetApp Account object supplied in the body of the operation.
apiInstance.accountsUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, body, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **accountName** | **String**| The name of the NetApp account | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | [default to &#39;2017-08-15&#39;]
 **body** | [**NetAppAccountPatch**](NetAppAccountPatch.md)| NetApp Account object supplied in the body of the operation. | 

### Return type

[**NetAppAccount**](NetAppAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

