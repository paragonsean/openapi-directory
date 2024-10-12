# DevTestLabsClient.VirtualNetworksApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualNetworksCreateOrUpdate**](VirtualNetworksApi.md#virtualNetworksCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/virtualnetworks/{name} | 
[**virtualNetworksDelete**](VirtualNetworksApi.md#virtualNetworksDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/virtualnetworks/{name} | 
[**virtualNetworksGet**](VirtualNetworksApi.md#virtualNetworksGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/virtualnetworks/{name} | 
[**virtualNetworksList**](VirtualNetworksApi.md#virtualNetworksList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/virtualnetworks | 
[**virtualNetworksUpdate**](VirtualNetworksApi.md#virtualNetworksUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/virtualnetworks/{name} | 



## virtualNetworksCreateOrUpdate

> VirtualNetwork virtualNetworksCreateOrUpdate(subscriptionId, resourceGroupName, labName, name, apiVersion, virtualNetwork)



Create or replace an existing virtual network. This operation can take a while to complete.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.VirtualNetworksApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let name = "name_example"; // String | The name of the virtual network.
let apiVersion = "'2016-05-15'"; // String | Client API version.
let virtualNetwork = new DevTestLabsClient.VirtualNetwork(); // VirtualNetwork | A virtual network.
apiInstance.virtualNetworksCreateOrUpdate(subscriptionId, resourceGroupName, labName, name, apiVersion, virtualNetwork, (error, data, response) => {
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
 **name** | **String**| The name of the virtual network. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2016-05-15&#39;]
 **virtualNetwork** | [**VirtualNetwork**](VirtualNetwork.md)| A virtual network. | 

### Return type

[**VirtualNetwork**](VirtualNetwork.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualNetworksDelete

> virtualNetworksDelete(subscriptionId, resourceGroupName, labName, name, apiVersion)



Delete virtual network. This operation can take a while to complete.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.VirtualNetworksApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let name = "name_example"; // String | The name of the virtual network.
let apiVersion = "'2016-05-15'"; // String | Client API version.
apiInstance.virtualNetworksDelete(subscriptionId, resourceGroupName, labName, name, apiVersion, (error, data, response) => {
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
 **name** | **String**| The name of the virtual network. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2016-05-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualNetworksGet

> VirtualNetwork virtualNetworksGet(subscriptionId, resourceGroupName, labName, name, apiVersion, opts)



Get virtual network.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.VirtualNetworksApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let name = "name_example"; // String | The name of the virtual network.
let apiVersion = "'2016-05-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example" // String | Specify the $expand query. Example: 'properties($expand=externalSubnets)'
};
apiInstance.virtualNetworksGet(subscriptionId, resourceGroupName, labName, name, apiVersion, opts, (error, data, response) => {
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
 **name** | **String**| The name of the virtual network. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2016-05-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($expand&#x3D;externalSubnets)&#39; | [optional] 

### Return type

[**VirtualNetwork**](VirtualNetwork.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualNetworksList

> ResponseWithContinuationVirtualNetwork virtualNetworksList(subscriptionId, resourceGroupName, labName, apiVersion, opts)



List virtual networks in a given lab.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.VirtualNetworksApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let apiVersion = "'2016-05-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example", // String | Specify the $expand query. Example: 'properties($expand=externalSubnets)'
  'filter': "filter_example", // String | The filter to apply to the operation.
  'top': 56, // Number | The maximum number of resources to return from the operation.
  'orderby': "orderby_example" // String | The ordering expression for the results, using OData notation.
};
apiInstance.virtualNetworksList(subscriptionId, resourceGroupName, labName, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | [default to &#39;2016-05-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($expand&#x3D;externalSubnets)&#39; | [optional] 
 **filter** | **String**| The filter to apply to the operation. | [optional] 
 **top** | **Number**| The maximum number of resources to return from the operation. | [optional] 
 **orderby** | **String**| The ordering expression for the results, using OData notation. | [optional] 

### Return type

[**ResponseWithContinuationVirtualNetwork**](ResponseWithContinuationVirtualNetwork.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualNetworksUpdate

> VirtualNetwork virtualNetworksUpdate(subscriptionId, resourceGroupName, labName, name, apiVersion, virtualNetwork)



Modify properties of virtual networks.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.VirtualNetworksApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let name = "name_example"; // String | The name of the virtual network.
let apiVersion = "'2016-05-15'"; // String | Client API version.
let virtualNetwork = new DevTestLabsClient.VirtualNetworkFragment(); // VirtualNetworkFragment | A virtual network.
apiInstance.virtualNetworksUpdate(subscriptionId, resourceGroupName, labName, name, apiVersion, virtualNetwork, (error, data, response) => {
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
 **name** | **String**| The name of the virtual network. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2016-05-15&#39;]
 **virtualNetwork** | [**VirtualNetworkFragment**](VirtualNetworkFragment.md)| A virtual network. | 

### Return type

[**VirtualNetwork**](VirtualNetwork.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

