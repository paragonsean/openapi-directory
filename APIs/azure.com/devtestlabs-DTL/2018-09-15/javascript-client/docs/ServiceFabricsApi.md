# DevTestLabsClient.ServiceFabricsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serviceFabricsCreateOrUpdate**](ServiceFabricsApi.md#serviceFabricsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics/{name} | 
[**serviceFabricsDelete**](ServiceFabricsApi.md#serviceFabricsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics/{name} | 
[**serviceFabricsGet**](ServiceFabricsApi.md#serviceFabricsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics/{name} | 
[**serviceFabricsList**](ServiceFabricsApi.md#serviceFabricsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics | 
[**serviceFabricsListApplicableSchedules**](ServiceFabricsApi.md#serviceFabricsListApplicableSchedules) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics/{name}/listApplicableSchedules | 
[**serviceFabricsStart**](ServiceFabricsApi.md#serviceFabricsStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics/{name}/start | 
[**serviceFabricsStop**](ServiceFabricsApi.md#serviceFabricsStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics/{name}/stop | 
[**serviceFabricsUpdate**](ServiceFabricsApi.md#serviceFabricsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/servicefabrics/{name} | 



## serviceFabricsCreateOrUpdate

> ServiceFabric serviceFabricsCreateOrUpdate(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, serviceFabric)



Create or replace an existing service fabric. This operation can take a while to complete.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ServiceFabricsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user profile.
let name = "name_example"; // String | The name of the service fabric.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let serviceFabric = new DevTestLabsClient.ServiceFabric(); // ServiceFabric | A Service Fabric.
apiInstance.serviceFabricsCreateOrUpdate(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, serviceFabric, (error, data, response) => {
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
 **name** | **String**| The name of the service fabric. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]
 **serviceFabric** | [**ServiceFabric**](ServiceFabric.md)| A Service Fabric. | 

### Return type

[**ServiceFabric**](ServiceFabric.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serviceFabricsDelete

> serviceFabricsDelete(subscriptionId, resourceGroupName, labName, userName, name, apiVersion)



Delete service fabric. This operation can take a while to complete.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ServiceFabricsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user profile.
let name = "name_example"; // String | The name of the service fabric.
let apiVersion = "'2018-09-15'"; // String | Client API version.
apiInstance.serviceFabricsDelete(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, (error, data, response) => {
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
 **name** | **String**| The name of the service fabric. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceFabricsGet

> ServiceFabric serviceFabricsGet(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, opts)



Get service fabric.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ServiceFabricsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user profile.
let name = "name_example"; // String | The name of the service fabric.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example" // String | Specify the $expand query. Example: 'properties($expand=applicableSchedule)'
};
apiInstance.serviceFabricsGet(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, opts, (error, data, response) => {
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
 **name** | **String**| The name of the service fabric. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($expand&#x3D;applicableSchedule)&#39; | [optional] 

### Return type

[**ServiceFabric**](ServiceFabric.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceFabricsList

> ServiceFabricList serviceFabricsList(subscriptionId, resourceGroupName, labName, userName, apiVersion, opts)



List service fabrics in a given user profile.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ServiceFabricsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user profile.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example", // String | Specify the $expand query. Example: 'properties($expand=applicableSchedule)'
  'filter': "filter_example", // String | The filter to apply to the operation. Example: '$filter=contains(name,'myName')
  'top': 56, // Number | The maximum number of resources to return from the operation. Example: '$top=10'
  'orderby': "orderby_example" // String | The ordering expression for the results, using OData notation. Example: '$orderby=name desc'
};
apiInstance.serviceFabricsList(subscriptionId, resourceGroupName, labName, userName, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($expand&#x3D;applicableSchedule)&#39; | [optional] 
 **filter** | **String**| The filter to apply to the operation. Example: &#39;$filter&#x3D;contains(name,&#39;myName&#39;) | [optional] 
 **top** | **Number**| The maximum number of resources to return from the operation. Example: &#39;$top&#x3D;10&#39; | [optional] 
 **orderby** | **String**| The ordering expression for the results, using OData notation. Example: &#39;$orderby&#x3D;name desc&#39; | [optional] 

### Return type

[**ServiceFabricList**](ServiceFabricList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceFabricsListApplicableSchedules

> ApplicableSchedule serviceFabricsListApplicableSchedules(subscriptionId, resourceGroupName, labName, userName, name, apiVersion)



Lists the applicable start/stop schedules, if any.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ServiceFabricsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user profile.
let name = "name_example"; // String | The name of the service fabric.
let apiVersion = "'2018-09-15'"; // String | Client API version.
apiInstance.serviceFabricsListApplicableSchedules(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, (error, data, response) => {
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
 **name** | **String**| The name of the service fabric. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]

### Return type

[**ApplicableSchedule**](ApplicableSchedule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceFabricsStart

> serviceFabricsStart(subscriptionId, resourceGroupName, labName, userName, name, apiVersion)



Start a service fabric. This operation can take a while to complete.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ServiceFabricsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user profile.
let name = "name_example"; // String | The name of the service fabric.
let apiVersion = "'2018-09-15'"; // String | Client API version.
apiInstance.serviceFabricsStart(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, (error, data, response) => {
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
 **name** | **String**| The name of the service fabric. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceFabricsStop

> serviceFabricsStop(subscriptionId, resourceGroupName, labName, userName, name, apiVersion)



Stop a service fabric This operation can take a while to complete.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ServiceFabricsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user profile.
let name = "name_example"; // String | The name of the service fabric.
let apiVersion = "'2018-09-15'"; // String | Client API version.
apiInstance.serviceFabricsStop(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, (error, data, response) => {
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
 **name** | **String**| The name of the service fabric. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceFabricsUpdate

> ServiceFabric serviceFabricsUpdate(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, serviceFabric)



Allows modifying tags of service fabrics. All other properties will be ignored.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.ServiceFabricsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user profile.
let name = "name_example"; // String | The name of the service fabric.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let serviceFabric = new DevTestLabsClient.ServiceFabricFragment(); // ServiceFabricFragment | A Service Fabric.
apiInstance.serviceFabricsUpdate(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, serviceFabric, (error, data, response) => {
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
 **name** | **String**| The name of the service fabric. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]
 **serviceFabric** | [**ServiceFabricFragment**](ServiceFabricFragment.md)| A Service Fabric. | 

### Return type

[**ServiceFabric**](ServiceFabric.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

