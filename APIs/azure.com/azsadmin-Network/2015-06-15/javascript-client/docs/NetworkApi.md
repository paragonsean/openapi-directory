# NetworkAdminManagementClient.NetworkApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locationsOperationResultsList**](NetworkApi.md#locationsOperationResultsList) | **GET** /providers/Microsoft.Network.Admin/locations/{location}/operationResults | 
[**locationsOperationsList**](NetworkApi.md#locationsOperationsList) | **GET** /providers/Microsoft.Network.Admin/locations/{location}/operations | 
[**onPremLocationsList**](NetworkApi.md#onPremLocationsList) | **GET** /providers/Microsoft.Network.Admin/locations | 
[**operationsList**](NetworkApi.md#operationsList) | **GET** /providers/Microsoft.Network.Admin/operations | 
[**resourceProviderStateGet**](NetworkApi.md#resourceProviderStateGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network.Admin/adminOverview | 



## locationsOperationResultsList

> OperationResultList locationsOperationResultsList(apiVersion, location)



Returns the list of operation results for a location

### Example

```javascript
import NetworkAdminManagementClient from 'network_admin_management_client';
let defaultClient = NetworkAdminManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkAdminManagementClient.NetworkApi();
let apiVersion = "'2015-06-15'"; // String | Client API Version.
let location = "location_example"; // String | Location of the resource.
apiInstance.locationsOperationResultsList(apiVersion, location, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | [default to &#39;2015-06-15&#39;]
 **location** | **String**| Location of the resource. | 

### Return type

[**OperationResultList**](OperationResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## locationsOperationsList

> OperationList locationsOperationsList(apiVersion, location)



Returns the list of support REST operations.

### Example

```javascript
import NetworkAdminManagementClient from 'network_admin_management_client';
let defaultClient = NetworkAdminManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkAdminManagementClient.NetworkApi();
let apiVersion = "'2015-06-15'"; // String | Client API Version.
let location = "location_example"; // String | Location of the resource.
apiInstance.locationsOperationsList(apiVersion, location, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | [default to &#39;2015-06-15&#39;]
 **location** | **String**| Location of the resource. | 

### Return type

[**OperationList**](OperationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## onPremLocationsList

> LocationsList onPremLocationsList(apiVersion)



Returns the list of supported locations

### Example

```javascript
import NetworkAdminManagementClient from 'network_admin_management_client';
let defaultClient = NetworkAdminManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkAdminManagementClient.NetworkApi();
let apiVersion = "'2015-06-15'"; // String | Client API Version.
apiInstance.onPremLocationsList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | [default to &#39;2015-06-15&#39;]

### Return type

[**LocationsList**](LocationsList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## operationsList

> OperationList operationsList(apiVersion)



Returns the list of support REST operations.

### Example

```javascript
import NetworkAdminManagementClient from 'network_admin_management_client';
let defaultClient = NetworkAdminManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkAdminManagementClient.NetworkApi();
let apiVersion = "'2015-06-15'"; // String | Client API Version.
apiInstance.operationsList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | [default to &#39;2015-06-15&#39;]

### Return type

[**OperationList**](OperationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourceProviderStateGet

> AdminOverview resourceProviderStateGet(subscriptionId, apiVersion)



Get an overview of the state of the network resource provider.

### Example

```javascript
import NetworkAdminManagementClient from 'network_admin_management_client';
let defaultClient = NetworkAdminManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkAdminManagementClient.NetworkApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "'2015-06-15'"; // String | Client API Version.
apiInstance.resourceProviderStateGet(subscriptionId, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | [default to &#39;2015-06-15&#39;]

### Return type

[**AdminOverview**](AdminOverview.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

