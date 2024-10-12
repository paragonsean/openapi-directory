# DataShareManagementClient.ShareApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**providerShareSubscriptionsGetByShare**](ShareApi.md#providerShareSubscriptionsGetByShare) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/providerShareSubscriptions/{providerShareSubscriptionId} | Get share subscription in a provider share.
[**providerShareSubscriptionsListByShare**](ShareApi.md#providerShareSubscriptionsListByShare) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/providerShareSubscriptions | List of available share subscriptions to a provider share.
[**providerShareSubscriptionsReinstate**](ShareApi.md#providerShareSubscriptionsReinstate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/providerShareSubscriptions/{providerShareSubscriptionId}/reinstate | Reinstate share subscription in a provider share.
[**providerShareSubscriptionsRevoke**](ShareApi.md#providerShareSubscriptionsRevoke) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/providerShareSubscriptions/{providerShareSubscriptionId}/revoke | Revoke share subscription in a provider share.
[**sharesCreate**](ShareApi.md#sharesCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName} | Create a share in the given account.
[**sharesDelete**](ShareApi.md#sharesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName} | Deletes a share
[**sharesGet**](ShareApi.md#sharesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName} | Get a specified share
[**sharesListByAccount**](ShareApi.md#sharesListByAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares | List of available shares under an account.
[**sharesListSynchronizationDetails**](ShareApi.md#sharesListSynchronizationDetails) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/listSynchronizationDetails | List data set level details for a share synchronization
[**sharesListSynchronizations**](ShareApi.md#sharesListSynchronizations) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/listSynchronizations | List Synchronizations in a share



## providerShareSubscriptionsGetByShare

> ProviderShareSubscription providerShareSubscriptionsGetByShare(subscriptionId, resourceGroupName, accountName, shareName, providerShareSubscriptionId, apiVersion)

Get share subscription in a provider share.

Get share subscription in a provider share

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.ShareApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareName = "shareName_example"; // String | The name of the share.
let providerShareSubscriptionId = "providerShareSubscriptionId_example"; // String | To locate shareSubscription
let apiVersion = "apiVersion_example"; // String | The api version to use.
apiInstance.providerShareSubscriptionsGetByShare(subscriptionId, resourceGroupName, accountName, shareName, providerShareSubscriptionId, apiVersion, (error, data, response) => {
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
 **shareName** | **String**| The name of the share. | 
 **providerShareSubscriptionId** | **String**| To locate shareSubscription | 
 **apiVersion** | **String**| The api version to use. | 

### Return type

[**ProviderShareSubscription**](ProviderShareSubscription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## providerShareSubscriptionsListByShare

> ProviderShareSubscriptionList providerShareSubscriptionsListByShare(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, opts)

List of available share subscriptions to a provider share.

List share subscriptions in a provider share

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.ShareApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareName = "shareName_example"; // String | The name of the share.
let apiVersion = "apiVersion_example"; // String | The api version to use.
let opts = {
  'skipToken': "skipToken_example" // String | Continuation Token
};
apiInstance.providerShareSubscriptionsListByShare(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, opts, (error, data, response) => {
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
 **shareName** | **String**| The name of the share. | 
 **apiVersion** | **String**| The api version to use. | 
 **skipToken** | **String**| Continuation Token | [optional] 

### Return type

[**ProviderShareSubscriptionList**](ProviderShareSubscriptionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## providerShareSubscriptionsReinstate

> ProviderShareSubscription providerShareSubscriptionsReinstate(subscriptionId, resourceGroupName, accountName, shareName, providerShareSubscriptionId, apiVersion)

Reinstate share subscription in a provider share.

Reinstate share subscription in a provider share

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.ShareApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareName = "shareName_example"; // String | The name of the share.
let providerShareSubscriptionId = "providerShareSubscriptionId_example"; // String | To locate shareSubscription
let apiVersion = "apiVersion_example"; // String | The api version to use.
apiInstance.providerShareSubscriptionsReinstate(subscriptionId, resourceGroupName, accountName, shareName, providerShareSubscriptionId, apiVersion, (error, data, response) => {
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
 **shareName** | **String**| The name of the share. | 
 **providerShareSubscriptionId** | **String**| To locate shareSubscription | 
 **apiVersion** | **String**| The api version to use. | 

### Return type

[**ProviderShareSubscription**](ProviderShareSubscription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## providerShareSubscriptionsRevoke

> ProviderShareSubscription providerShareSubscriptionsRevoke(subscriptionId, resourceGroupName, accountName, shareName, providerShareSubscriptionId, apiVersion)

Revoke share subscription in a provider share.

Revoke share subscription in a provider share

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.ShareApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareName = "shareName_example"; // String | The name of the share.
let providerShareSubscriptionId = "providerShareSubscriptionId_example"; // String | To locate shareSubscription
let apiVersion = "apiVersion_example"; // String | The api version to use.
apiInstance.providerShareSubscriptionsRevoke(subscriptionId, resourceGroupName, accountName, shareName, providerShareSubscriptionId, apiVersion, (error, data, response) => {
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
 **shareName** | **String**| The name of the share. | 
 **providerShareSubscriptionId** | **String**| To locate shareSubscription | 
 **apiVersion** | **String**| The api version to use. | 

### Return type

[**ProviderShareSubscription**](ProviderShareSubscription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sharesCreate

> Share sharesCreate(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, share)

Create a share in the given account.

Create a share 

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.ShareApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareName = "shareName_example"; // String | The name of the share.
let apiVersion = "apiVersion_example"; // String | The api version to use.
let share = new DataShareManagementClient.Share(); // Share | The share payload
apiInstance.sharesCreate(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, share, (error, data, response) => {
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
 **shareName** | **String**| The name of the share. | 
 **apiVersion** | **String**| The api version to use. | 
 **share** | [**Share**](Share.md)| The share payload | 

### Return type

[**Share**](Share.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sharesDelete

> OperationResponse sharesDelete(subscriptionId, resourceGroupName, accountName, shareName, apiVersion)

Deletes a share

Delete a share 

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.ShareApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareName = "shareName_example"; // String | The name of the share.
let apiVersion = "apiVersion_example"; // String | The api version to use.
apiInstance.sharesDelete(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, (error, data, response) => {
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
 **shareName** | **String**| The name of the share. | 
 **apiVersion** | **String**| The api version to use. | 

### Return type

[**OperationResponse**](OperationResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sharesGet

> Share sharesGet(subscriptionId, resourceGroupName, accountName, shareName, apiVersion)

Get a specified share

Get a share 

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.ShareApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareName = "shareName_example"; // String | The name of the share to retrieve.
let apiVersion = "apiVersion_example"; // String | The api version to use.
apiInstance.sharesGet(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, (error, data, response) => {
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
 **shareName** | **String**| The name of the share to retrieve. | 
 **apiVersion** | **String**| The api version to use. | 

### Return type

[**Share**](Share.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sharesListByAccount

> ShareList sharesListByAccount(subscriptionId, resourceGroupName, accountName, apiVersion, opts)

List of available shares under an account.

List shares in an account

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.ShareApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let apiVersion = "apiVersion_example"; // String | The api version to use.
let opts = {
  'skipToken': "skipToken_example" // String | Continuation Token
};
apiInstance.sharesListByAccount(subscriptionId, resourceGroupName, accountName, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The api version to use. | 
 **skipToken** | **String**| Continuation Token | [optional] 

### Return type

[**ShareList**](ShareList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sharesListSynchronizationDetails

> SynchronizationDetailsList sharesListSynchronizationDetails(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, shareSynchronization, opts)

List data set level details for a share synchronization

List synchronization details

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.ShareApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareName = "shareName_example"; // String | The name of the share.
let apiVersion = "apiVersion_example"; // String | The api version to use.
let shareSynchronization = new DataShareManagementClient.ShareSynchronization(); // ShareSynchronization | Share Synchronization payload.
let opts = {
  'skipToken': "skipToken_example" // String | Continuation token
};
apiInstance.sharesListSynchronizationDetails(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, shareSynchronization, opts, (error, data, response) => {
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
 **shareName** | **String**| The name of the share. | 
 **apiVersion** | **String**| The api version to use. | 
 **shareSynchronization** | [**ShareSynchronization**](ShareSynchronization.md)| Share Synchronization payload. | 
 **skipToken** | **String**| Continuation token | [optional] 

### Return type

[**SynchronizationDetailsList**](SynchronizationDetailsList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sharesListSynchronizations

> ShareSynchronizationList sharesListSynchronizations(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, opts)

List Synchronizations in a share

List synchronizations of a share

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.ShareApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareName = "shareName_example"; // String | The name of the share.
let apiVersion = "apiVersion_example"; // String | The api version to use.
let opts = {
  'skipToken': "skipToken_example" // String | Continuation token
};
apiInstance.sharesListSynchronizations(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, opts, (error, data, response) => {
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
 **shareName** | **String**| The name of the share. | 
 **apiVersion** | **String**| The api version to use. | 
 **skipToken** | **String**| Continuation token | [optional] 

### Return type

[**ShareSynchronizationList**](ShareSynchronizationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

