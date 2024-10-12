# DevTestLabsClient.ServiceFabricSchedulesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serviceFabricSchedulesCreateOrUpdate**](ServiceFabricSchedulesApi.md#serviceFabricSchedulesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics/{serviceFabricName}/schedules/{name} | 
[**serviceFabricSchedulesDelete**](ServiceFabricSchedulesApi.md#serviceFabricSchedulesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics/{serviceFabricName}/schedules/{name} | 
[**serviceFabricSchedulesExecute**](ServiceFabricSchedulesApi.md#serviceFabricSchedulesExecute) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics/{serviceFabricName}/schedules/{name}/execute | 
[**serviceFabricSchedulesGet**](ServiceFabricSchedulesApi.md#serviceFabricSchedulesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics/{serviceFabricName}/schedules/{name} | 
[**serviceFabricSchedulesList**](ServiceFabricSchedulesApi.md#serviceFabricSchedulesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics/{serviceFabricName}/schedules | 
[**serviceFabricSchedulesUpdate**](ServiceFabricSchedulesApi.md#serviceFabricSchedulesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics/{serviceFabricName}/schedules/{name} | 



## serviceFabricSchedulesCreateOrUpdate

> Schedule serviceFabricSchedulesCreateOrUpdate(subscriptionId, resourceGroupName, labName, userName, serviceFabricName, name, apiVersion, schedule)



Create or replace an existing schedule.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ServiceFabricSchedulesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user profile.
let serviceFabricName = "serviceFabricName_example"; // String | The name of the service fabric.
let name = "name_example"; // String | The name of the schedule.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let schedule = new DevTestLabsClient.Schedule(); // Schedule | A schedule.
apiInstance.serviceFabricSchedulesCreateOrUpdate(subscriptionId, resourceGroupName, labName, userName, serviceFabricName, name, apiVersion, schedule, (error, data, response) => {
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
 **labName** | **String**| The name of the lab. | 
 **userName** | **String**| The name of the user profile. | 
 **serviceFabricName** | **String**| The name of the service fabric. | 
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


## serviceFabricSchedulesDelete

> serviceFabricSchedulesDelete(subscriptionId, resourceGroupName, labName, userName, serviceFabricName, name, apiVersion)



Delete schedule.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ServiceFabricSchedulesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user profile.
let serviceFabricName = "serviceFabricName_example"; // String | The name of the service fabric.
let name = "name_example"; // String | The name of the schedule.
let apiVersion = "'2018-09-15'"; // String | Client API version.
apiInstance.serviceFabricSchedulesDelete(subscriptionId, resourceGroupName, labName, userName, serviceFabricName, name, apiVersion, (error, data, response) => {
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
 **labName** | **String**| The name of the lab. | 
 **userName** | **String**| The name of the user profile. | 
 **serviceFabricName** | **String**| The name of the service fabric. | 
 **name** | **String**| The name of the schedule. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceFabricSchedulesExecute

> serviceFabricSchedulesExecute(subscriptionId, resourceGroupName, labName, userName, serviceFabricName, name, apiVersion)



Execute a schedule. This operation can take a while to complete.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ServiceFabricSchedulesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user profile.
let serviceFabricName = "serviceFabricName_example"; // String | The name of the service fabric.
let name = "name_example"; // String | The name of the schedule.
let apiVersion = "'2018-09-15'"; // String | Client API version.
apiInstance.serviceFabricSchedulesExecute(subscriptionId, resourceGroupName, labName, userName, serviceFabricName, name, apiVersion, (error, data, response) => {
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
 **labName** | **String**| The name of the lab. | 
 **userName** | **String**| The name of the user profile. | 
 **serviceFabricName** | **String**| The name of the service fabric. | 
 **name** | **String**| The name of the schedule. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceFabricSchedulesGet

> Schedule serviceFabricSchedulesGet(subscriptionId, resourceGroupName, labName, userName, serviceFabricName, name, apiVersion, opts)



Get schedule.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ServiceFabricSchedulesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user profile.
let serviceFabricName = "serviceFabricName_example"; // String | The name of the service fabric.
let name = "name_example"; // String | The name of the schedule.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example" // String | Specify the $expand query. Example: 'properties($select=status)'
};
apiInstance.serviceFabricSchedulesGet(subscriptionId, resourceGroupName, labName, userName, serviceFabricName, name, apiVersion, opts, (error, data, response) => {
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
 **labName** | **String**| The name of the lab. | 
 **userName** | **String**| The name of the user profile. | 
 **serviceFabricName** | **String**| The name of the service fabric. | 
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


## serviceFabricSchedulesList

> ScheduleList serviceFabricSchedulesList(subscriptionId, resourceGroupName, labName, userName, serviceFabricName, apiVersion, opts)



List schedules in a given service fabric.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ServiceFabricSchedulesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user profile.
let serviceFabricName = "serviceFabricName_example"; // String | The name of the service fabric.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example", // String | Specify the $expand query. Example: 'properties($select=status)'
  'filter': "filter_example", // String | The filter to apply to the operation. Example: '$filter=contains(name,'myName')
  'top': 56, // Number | The maximum number of resources to return from the operation. Example: '$top=10'
  'orderby': "orderby_example" // String | The ordering expression for the results, using OData notation. Example: '$orderby=name desc'
};
apiInstance.serviceFabricSchedulesList(subscriptionId, resourceGroupName, labName, userName, serviceFabricName, apiVersion, opts, (error, data, response) => {
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
 **labName** | **String**| The name of the lab. | 
 **userName** | **String**| The name of the user profile. | 
 **serviceFabricName** | **String**| The name of the service fabric. | 
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


## serviceFabricSchedulesUpdate

> Schedule serviceFabricSchedulesUpdate(subscriptionId, resourceGroupName, labName, userName, serviceFabricName, name, apiVersion, schedule)



Allows modifying tags of schedules. All other properties will be ignored.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ServiceFabricSchedulesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user profile.
let serviceFabricName = "serviceFabricName_example"; // String | The name of the service fabric.
let name = "name_example"; // String | The name of the schedule.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let schedule = new DevTestLabsClient.ScheduleFragment(); // ScheduleFragment | A schedule.
apiInstance.serviceFabricSchedulesUpdate(subscriptionId, resourceGroupName, labName, userName, serviceFabricName, name, apiVersion, schedule, (error, data, response) => {
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
 **labName** | **String**| The name of the lab. | 
 **userName** | **String**| The name of the user profile. | 
 **serviceFabricName** | **String**| The name of the service fabric. | 
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

