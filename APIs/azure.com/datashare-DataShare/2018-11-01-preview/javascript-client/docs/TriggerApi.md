# DataShareManagementClient.TriggerApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**triggersCreate**](TriggerApi.md#triggersCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/triggers/{triggerName} | This method creates a trigger for a share subscription
[**triggersDelete**](TriggerApi.md#triggersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/triggers/{triggerName} | Delete Trigger in a shareSubscription.
[**triggersGet**](TriggerApi.md#triggersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/triggers/{triggerName} | Get Trigger in a shareSubscription.
[**triggersListByShareSubscription**](TriggerApi.md#triggersListByShareSubscription) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/triggers | List Triggers in a share subscription.



## triggersCreate

> Trigger triggersCreate(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, triggerName, apiVersion, trigger)

This method creates a trigger for a share subscription

Create a Trigger 

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.TriggerApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the share subscription which will hold the data set sink.
let triggerName = "triggerName_example"; // String | The name of the trigger.
let apiVersion = "apiVersion_example"; // String | The api version to use.
let trigger = new DataShareManagementClient.Trigger(); // Trigger | Trigger details.
apiInstance.triggersCreate(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, triggerName, apiVersion, trigger, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier | 
 **resourceGroupName** | **String**| The resource group name. | 
 **accountName** | **String**| The name of the share account. | 
 **shareSubscriptionName** | **String**| The name of the share subscription which will hold the data set sink. | 
 **triggerName** | **String**| The name of the trigger. | 
 **apiVersion** | **String**| The api version to use. | 
 **trigger** | [**Trigger**](Trigger.md)| Trigger details. | 

### Return type

[**Trigger**](Trigger.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## triggersDelete

> OperationResponse triggersDelete(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, triggerName, apiVersion)

Delete Trigger in a shareSubscription.

Delete a Trigger in a shareSubscription

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.TriggerApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the shareSubscription.
let triggerName = "triggerName_example"; // String | The name of the trigger.
let apiVersion = "apiVersion_example"; // String | The api version to use.
apiInstance.triggersDelete(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, triggerName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier | 
 **resourceGroupName** | **String**| The resource group name. | 
 **accountName** | **String**| The name of the share account. | 
 **shareSubscriptionName** | **String**| The name of the shareSubscription. | 
 **triggerName** | **String**| The name of the trigger. | 
 **apiVersion** | **String**| The api version to use. | 

### Return type

[**OperationResponse**](OperationResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## triggersGet

> Trigger triggersGet(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, triggerName, apiVersion)

Get Trigger in a shareSubscription.

Get a Trigger in a shareSubscription

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.TriggerApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the shareSubscription.
let triggerName = "triggerName_example"; // String | The name of the trigger.
let apiVersion = "apiVersion_example"; // String | The api version to use.
apiInstance.triggersGet(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, triggerName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier | 
 **resourceGroupName** | **String**| The resource group name. | 
 **accountName** | **String**| The name of the share account. | 
 **shareSubscriptionName** | **String**| The name of the shareSubscription. | 
 **triggerName** | **String**| The name of the trigger. | 
 **apiVersion** | **String**| The api version to use. | 

### Return type

[**Trigger**](Trigger.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## triggersListByShareSubscription

> TriggerList triggersListByShareSubscription(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, opts)

List Triggers in a share subscription.

List Triggers in a share subscription

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.TriggerApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the share subscription.
let apiVersion = "apiVersion_example"; // String | The api version to use.
let opts = {
  'skipToken': "skipToken_example" // String | Continuation token
};
apiInstance.triggersListByShareSubscription(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier | 
 **resourceGroupName** | **String**| The resource group name. | 
 **accountName** | **String**| The name of the share account. | 
 **shareSubscriptionName** | **String**| The name of the share subscription. | 
 **apiVersion** | **String**| The api version to use. | 
 **skipToken** | **String**| Continuation token | [optional] 

### Return type

[**TriggerList**](TriggerList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

