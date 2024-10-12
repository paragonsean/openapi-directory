# DataShareManagementClient.ShareSubscriptionApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consumerSourceDataSetsListByShareSubscription**](ShareSubscriptionApi.md#consumerSourceDataSetsListByShareSubscription) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/ConsumerSourceDataSets | Get source dataSets of a shareSubscription.
[**shareSubscriptionsCancelSynchronization**](ShareSubscriptionApi.md#shareSubscriptionsCancelSynchronization) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/cancelSynchronization | Request cancellation of a data share snapshot
[**shareSubscriptionsCreate**](ShareSubscriptionApi.md#shareSubscriptionsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName} | Create shareSubscription in an account.
[**shareSubscriptionsDelete**](ShareSubscriptionApi.md#shareSubscriptionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName} | Delete shareSubscription in an account.
[**shareSubscriptionsGet**](ShareSubscriptionApi.md#shareSubscriptionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName} | Get shareSubscription in an account.
[**shareSubscriptionsListByAccount**](ShareSubscriptionApi.md#shareSubscriptionsListByAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions | List of available share subscriptions under an account.
[**shareSubscriptionsListSourceShareSynchronizationSettings**](ShareSubscriptionApi.md#shareSubscriptionsListSourceShareSynchronizationSettings) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/listSourceShareSynchronizationSettings | Get source share synchronization settings for a shareSubscription.
[**shareSubscriptionsListSynchronizationDetails**](ShareSubscriptionApi.md#shareSubscriptionsListSynchronizationDetails) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/listSynchronizationDetails | List data set level details for a share subscription synchronization
[**shareSubscriptionsListSynchronizations**](ShareSubscriptionApi.md#shareSubscriptionsListSynchronizations) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/listSynchronizations | List Synchronizations in a share subscription.
[**shareSubscriptionsSynchronize**](ShareSubscriptionApi.md#shareSubscriptionsSynchronize) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/Synchronize | Initiate an asynchronous data share job



## consumerSourceDataSetsListByShareSubscription

> ConsumerSourceDataSetList consumerSourceDataSetsListByShareSubscription(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, opts)

Get source dataSets of a shareSubscription.

Get source dataSets of a shareSubscription

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.ShareSubscriptionApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the shareSubscription.
let apiVersion = "apiVersion_example"; // String | The api version to use.
let opts = {
  'skipToken': "skipToken_example" // String | Continuation token
};
apiInstance.consumerSourceDataSetsListByShareSubscription(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The api version to use. | 
 **skipToken** | **String**| Continuation token | [optional] 

### Return type

[**ConsumerSourceDataSetList**](ConsumerSourceDataSetList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## shareSubscriptionsCancelSynchronization

> ShareSubscriptionSynchronization shareSubscriptionsCancelSynchronization(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, shareSubscriptionSynchronization)

Request cancellation of a data share snapshot

Request to cancel a synchronization.

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.ShareSubscriptionApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the shareSubscription.
let apiVersion = "apiVersion_example"; // String | The api version to use.
let shareSubscriptionSynchronization = new DataShareManagementClient.ShareSubscriptionSynchronization(); // ShareSubscriptionSynchronization | Share Subscription Synchronization payload.
apiInstance.shareSubscriptionsCancelSynchronization(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, shareSubscriptionSynchronization, (error, data, response) => {
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
 **apiVersion** | **String**| The api version to use. | 
 **shareSubscriptionSynchronization** | [**ShareSubscriptionSynchronization**](ShareSubscriptionSynchronization.md)| Share Subscription Synchronization payload. | 

### Return type

[**ShareSubscriptionSynchronization**](ShareSubscriptionSynchronization.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## shareSubscriptionsCreate

> ShareSubscription shareSubscriptionsCreate(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, shareSubscription)

Create shareSubscription in an account.

Create a shareSubscription in an account

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.ShareSubscriptionApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the shareSubscription.
let apiVersion = "apiVersion_example"; // String | The api version to use.
let shareSubscription = new DataShareManagementClient.ShareSubscription(); // ShareSubscription | create parameters for shareSubscription
apiInstance.shareSubscriptionsCreate(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, shareSubscription, (error, data, response) => {
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
 **apiVersion** | **String**| The api version to use. | 
 **shareSubscription** | [**ShareSubscription**](ShareSubscription.md)| create parameters for shareSubscription | 

### Return type

[**ShareSubscription**](ShareSubscription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## shareSubscriptionsDelete

> OperationResponse shareSubscriptionsDelete(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion)

Delete shareSubscription in an account.

Delete a shareSubscription in an account

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.ShareSubscriptionApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the shareSubscription.
let apiVersion = "apiVersion_example"; // String | The api version to use.
apiInstance.shareSubscriptionsDelete(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The api version to use. | 

### Return type

[**OperationResponse**](OperationResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## shareSubscriptionsGet

> ShareSubscription shareSubscriptionsGet(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion)

Get shareSubscription in an account.

Get a shareSubscription in an account

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.ShareSubscriptionApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the shareSubscription.
let apiVersion = "apiVersion_example"; // String | The api version to use.
apiInstance.shareSubscriptionsGet(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The api version to use. | 

### Return type

[**ShareSubscription**](ShareSubscription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## shareSubscriptionsListByAccount

> ShareSubscriptionList shareSubscriptionsListByAccount(subscriptionId, resourceGroupName, accountName, apiVersion, opts)

List of available share subscriptions under an account.

List share subscriptions in an account

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.ShareSubscriptionApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let apiVersion = "apiVersion_example"; // String | The api version to use.
let opts = {
  'skipToken': "skipToken_example" // String | Continuation Token
};
apiInstance.shareSubscriptionsListByAccount(subscriptionId, resourceGroupName, accountName, apiVersion, opts, (error, data, response) => {
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

[**ShareSubscriptionList**](ShareSubscriptionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## shareSubscriptionsListSourceShareSynchronizationSettings

> SourceShareSynchronizationSettingList shareSubscriptionsListSourceShareSynchronizationSettings(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, opts)

Get source share synchronization settings for a shareSubscription.

Get synchronization settings set on a share

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.ShareSubscriptionApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the shareSubscription.
let apiVersion = "apiVersion_example"; // String | The api version to use.
let opts = {
  'skipToken': "skipToken_example" // String | Continuation token
};
apiInstance.shareSubscriptionsListSourceShareSynchronizationSettings(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The api version to use. | 
 **skipToken** | **String**| Continuation token | [optional] 

### Return type

[**SourceShareSynchronizationSettingList**](SourceShareSynchronizationSettingList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## shareSubscriptionsListSynchronizationDetails

> SynchronizationDetailsList shareSubscriptionsListSynchronizationDetails(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, shareSubscriptionSynchronization, opts)

List data set level details for a share subscription synchronization

List synchronization details

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.ShareSubscriptionApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the share subscription.
let apiVersion = "apiVersion_example"; // String | The api version to use.
let shareSubscriptionSynchronization = new DataShareManagementClient.ShareSubscriptionSynchronization(); // ShareSubscriptionSynchronization | Share Subscription Synchronization payload.
let opts = {
  'skipToken': "skipToken_example" // String | Continuation token
};
apiInstance.shareSubscriptionsListSynchronizationDetails(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, shareSubscriptionSynchronization, opts, (error, data, response) => {
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
 **shareSubscriptionSynchronization** | [**ShareSubscriptionSynchronization**](ShareSubscriptionSynchronization.md)| Share Subscription Synchronization payload. | 
 **skipToken** | **String**| Continuation token | [optional] 

### Return type

[**SynchronizationDetailsList**](SynchronizationDetailsList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## shareSubscriptionsListSynchronizations

> ShareSubscriptionSynchronizationList shareSubscriptionsListSynchronizations(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, opts)

List Synchronizations in a share subscription.

List synchronizations of a share subscription

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.ShareSubscriptionApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the share subscription.
let apiVersion = "apiVersion_example"; // String | The api version to use.
let opts = {
  'skipToken': "skipToken_example" // String | Continuation token
};
apiInstance.shareSubscriptionsListSynchronizations(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, opts, (error, data, response) => {
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

[**ShareSubscriptionSynchronizationList**](ShareSubscriptionSynchronizationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## shareSubscriptionsSynchronize

> ShareSubscriptionSynchronization shareSubscriptionsSynchronize(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, synchronize)

Initiate an asynchronous data share job

Initiate a copy

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.ShareSubscriptionApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of share subscription
let apiVersion = "apiVersion_example"; // String | The api version to use.
let synchronize = new DataShareManagementClient.Synchronize(); // Synchronize | Synchronize payload
apiInstance.shareSubscriptionsSynchronize(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, synchronize, (error, data, response) => {
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
 **shareSubscriptionName** | **String**| The name of share subscription | 
 **apiVersion** | **String**| The api version to use. | 
 **synchronize** | [**Synchronize**](Synchronize.md)| Synchronize payload | 

### Return type

[**ShareSubscriptionSynchronization**](ShareSubscriptionSynchronization.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

