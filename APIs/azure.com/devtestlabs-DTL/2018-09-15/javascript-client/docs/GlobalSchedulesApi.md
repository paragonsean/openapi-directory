# DevTestLabsClient.GlobalSchedulesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**globalSchedulesCreateOrUpdate**](GlobalSchedulesApi.md#globalSchedulesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/schedules/{name} | 
[**globalSchedulesDelete**](GlobalSchedulesApi.md#globalSchedulesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/schedules/{name} | 
[**globalSchedulesExecute**](GlobalSchedulesApi.md#globalSchedulesExecute) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/schedules/{name}/execute | 
[**globalSchedulesGet**](GlobalSchedulesApi.md#globalSchedulesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/schedules/{name} | 
[**globalSchedulesListByResourceGroup**](GlobalSchedulesApi.md#globalSchedulesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/schedules | 
[**globalSchedulesListBySubscription**](GlobalSchedulesApi.md#globalSchedulesListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DevTestLab/schedules | 
[**globalSchedulesRetarget**](GlobalSchedulesApi.md#globalSchedulesRetarget) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/schedules/{name}/retarget | 
[**globalSchedulesUpdate**](GlobalSchedulesApi.md#globalSchedulesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/schedules/{name} | 



## globalSchedulesCreateOrUpdate

> Schedule globalSchedulesCreateOrUpdate(subscriptionId, resourceGroupName, name, apiVersion, schedule)



Create or replace an existing schedule.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.GlobalSchedulesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let name = "name_example"; // String | The name of the schedule.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let schedule = new DevTestLabsClient.Schedule(); // Schedule | A schedule.
apiInstance.globalSchedulesCreateOrUpdate(subscriptionId, resourceGroupName, name, apiVersion, schedule, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **name** | **String**| The name of the schedule. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]
 **schedule** | [**Schedule**](Schedule.md)| A schedule. | 

### Return type

[**Schedule**](Schedule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## globalSchedulesDelete

> globalSchedulesDelete(subscriptionId, resourceGroupName, name, apiVersion)



Delete schedule.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.GlobalSchedulesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let name = "name_example"; // String | The name of the schedule.
let apiVersion = "'2018-09-15'"; // String | Client API version.
apiInstance.globalSchedulesDelete(subscriptionId, resourceGroupName, name, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **name** | **String**| The name of the schedule. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## globalSchedulesExecute

> globalSchedulesExecute(subscriptionId, resourceGroupName, name, apiVersion)



Execute a schedule. This operation can take a while to complete.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.GlobalSchedulesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let name = "name_example"; // String | The name of the schedule.
let apiVersion = "'2018-09-15'"; // String | Client API version.
apiInstance.globalSchedulesExecute(subscriptionId, resourceGroupName, name, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **name** | **String**| The name of the schedule. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## globalSchedulesGet

> Schedule globalSchedulesGet(subscriptionId, resourceGroupName, name, apiVersion, opts)



Get schedule.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.GlobalSchedulesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let name = "name_example"; // String | The name of the schedule.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example" // String | Specify the $expand query. Example: 'properties($select=status)'
};
apiInstance.globalSchedulesGet(subscriptionId, resourceGroupName, name, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **name** | **String**| The name of the schedule. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;status)&#39; | [optional] 

### Return type

[**Schedule**](Schedule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## globalSchedulesListByResourceGroup

> ScheduleList globalSchedulesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts)



List schedules in a resource group.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.GlobalSchedulesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example", // String | Specify the $expand query. Example: 'properties($select=status)'
  'filter': "filter_example", // String | The filter to apply to the operation. Example: '$filter=contains(name,'myName')
  'top': 56, // Number | The maximum number of resources to return from the operation. Example: '$top=10'
  'orderby': "orderby_example" // String | The ordering expression for the results, using OData notation. Example: '$orderby=name desc'
};
apiInstance.globalSchedulesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;status)&#39; | [optional] 
 **filter** | **String**| The filter to apply to the operation. Example: &#39;$filter&#x3D;contains(name,&#39;myName&#39;) | [optional] 
 **top** | **Number**| The maximum number of resources to return from the operation. Example: &#39;$top&#x3D;10&#39; | [optional] 
 **orderby** | **String**| The ordering expression for the results, using OData notation. Example: &#39;$orderby&#x3D;name desc&#39; | [optional] 

### Return type

[**ScheduleList**](ScheduleList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## globalSchedulesListBySubscription

> ScheduleList globalSchedulesListBySubscription(subscriptionId, apiVersion, opts)



List schedules in a subscription.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.GlobalSchedulesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example", // String | Specify the $expand query. Example: 'properties($select=status)'
  'filter': "filter_example", // String | The filter to apply to the operation. Example: '$filter=contains(name,'myName')
  'top': 56, // Number | The maximum number of resources to return from the operation. Example: '$top=10'
  'orderby': "orderby_example" // String | The ordering expression for the results, using OData notation. Example: '$orderby=name desc'
};
apiInstance.globalSchedulesListBySubscription(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;status)&#39; | [optional] 
 **filter** | **String**| The filter to apply to the operation. Example: &#39;$filter&#x3D;contains(name,&#39;myName&#39;) | [optional] 
 **top** | **Number**| The maximum number of resources to return from the operation. Example: &#39;$top&#x3D;10&#39; | [optional] 
 **orderby** | **String**| The ordering expression for the results, using OData notation. Example: &#39;$orderby&#x3D;name desc&#39; | [optional] 

### Return type

[**ScheduleList**](ScheduleList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## globalSchedulesRetarget

> globalSchedulesRetarget(subscriptionId, resourceGroupName, name, apiVersion, retargetScheduleProperties)



Updates a schedule&#39;s target resource Id. This operation can take a while to complete.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.GlobalSchedulesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let name = "name_example"; // String | The name of the schedule.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let retargetScheduleProperties = new DevTestLabsClient.RetargetScheduleProperties(); // RetargetScheduleProperties | Properties for retargeting a virtual machine schedule.
apiInstance.globalSchedulesRetarget(subscriptionId, resourceGroupName, name, apiVersion, retargetScheduleProperties, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **name** | **String**| The name of the schedule. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]
 **retargetScheduleProperties** | [**RetargetScheduleProperties**](RetargetScheduleProperties.md)| Properties for retargeting a virtual machine schedule. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## globalSchedulesUpdate

> Schedule globalSchedulesUpdate(subscriptionId, resourceGroupName, name, apiVersion, schedule)



Allows modifying tags of schedules. All other properties will be ignored.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.GlobalSchedulesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let name = "name_example"; // String | The name of the schedule.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let schedule = new DevTestLabsClient.ScheduleFragment(); // ScheduleFragment | A schedule.
apiInstance.globalSchedulesUpdate(subscriptionId, resourceGroupName, name, apiVersion, schedule, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **name** | **String**| The name of the schedule. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]
 **schedule** | [**ScheduleFragment**](ScheduleFragment.md)| A schedule. | 

### Return type

[**Schedule**](Schedule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

