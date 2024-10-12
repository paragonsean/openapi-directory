# CustomerInsightsManagementClient.LinksApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**linksCreateOrUpdate**](LinksApi.md#linksCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomerInsights/hubs/{hubName}/links/{linkName} | 
[**linksDelete**](LinksApi.md#linksDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomerInsights/hubs/{hubName}/links/{linkName} | 
[**linksGet**](LinksApi.md#linksGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomerInsights/hubs/{hubName}/links/{linkName} | 
[**linksListByHub**](LinksApi.md#linksListByHub) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomerInsights/hubs/{hubName}/links | 



## linksCreateOrUpdate

> LinkResourceFormat linksCreateOrUpdate(resourceGroupName, hubName, linkName, apiVersion, subscriptionId, parameters)



Creates a link or updates an existing link in the hub.

### Example

```javascript
import CustomerInsightsManagementClient from 'customer_insights_management_client';
let defaultClient = CustomerInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CustomerInsightsManagementClient.LinksApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let hubName = "hubName_example"; // String | The name of the hub.
let linkName = "linkName_example"; // String | The name of the link.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new CustomerInsightsManagementClient.LinkResourceFormat(); // LinkResourceFormat | Parameters supplied to the CreateOrUpdate Link operation.
apiInstance.linksCreateOrUpdate(resourceGroupName, hubName, linkName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **hubName** | **String**| The name of the hub. | 
 **linkName** | **String**| The name of the link. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**LinkResourceFormat**](LinkResourceFormat.md)| Parameters supplied to the CreateOrUpdate Link operation. | 

### Return type

[**LinkResourceFormat**](LinkResourceFormat.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## linksDelete

> linksDelete(resourceGroupName, hubName, linkName, apiVersion, subscriptionId)



Deletes a link in the hub.

### Example

```javascript
import CustomerInsightsManagementClient from 'customer_insights_management_client';
let defaultClient = CustomerInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CustomerInsightsManagementClient.LinksApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let hubName = "hubName_example"; // String | The name of the hub.
let linkName = "linkName_example"; // String | The name of the link.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.linksDelete(resourceGroupName, hubName, linkName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **hubName** | **String**| The name of the hub. | 
 **linkName** | **String**| The name of the link. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## linksGet

> LinkResourceFormat linksGet(resourceGroupName, hubName, linkName, apiVersion, subscriptionId)



Gets a link in the hub.

### Example

```javascript
import CustomerInsightsManagementClient from 'customer_insights_management_client';
let defaultClient = CustomerInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CustomerInsightsManagementClient.LinksApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let hubName = "hubName_example"; // String | The name of the hub.
let linkName = "linkName_example"; // String | The name of the link.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.linksGet(resourceGroupName, hubName, linkName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **hubName** | **String**| The name of the hub. | 
 **linkName** | **String**| The name of the link. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**LinkResourceFormat**](LinkResourceFormat.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## linksListByHub

> LinkListResult linksListByHub(resourceGroupName, hubName, apiVersion, subscriptionId)



Gets all the links in the specified hub.

### Example

```javascript
import CustomerInsightsManagementClient from 'customer_insights_management_client';
let defaultClient = CustomerInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CustomerInsightsManagementClient.LinksApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let hubName = "hubName_example"; // String | The name of the hub.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.linksListByHub(resourceGroupName, hubName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **hubName** | **String**| The name of the hub. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**LinkListResult**](LinkListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

