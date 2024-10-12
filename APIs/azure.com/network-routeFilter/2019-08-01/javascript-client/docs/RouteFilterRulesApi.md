# NetworkManagementClient.RouteFilterRulesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**routeFilterRulesCreateOrUpdate**](RouteFilterRulesApi.md#routeFilterRulesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules/{ruleName} | 
[**routeFilterRulesDelete**](RouteFilterRulesApi.md#routeFilterRulesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules/{ruleName} | 
[**routeFilterRulesGet**](RouteFilterRulesApi.md#routeFilterRulesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules/{ruleName} | 
[**routeFilterRulesListByRouteFilter**](RouteFilterRulesApi.md#routeFilterRulesListByRouteFilter) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules | 
[**routeFilterRulesUpdate**](RouteFilterRulesApi.md#routeFilterRulesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules/{ruleName} | 



## routeFilterRulesCreateOrUpdate

> RouteFilterRule routeFilterRulesCreateOrUpdate(resourceGroupName, routeFilterName, ruleName, apiVersion, subscriptionId, routeFilterRuleParameters)



Creates or updates a route in the specified route filter.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.RouteFilterRulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let routeFilterName = "routeFilterName_example"; // String | The name of the route filter.
let ruleName = "ruleName_example"; // String | The name of the route filter rule.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let routeFilterRuleParameters = new NetworkManagementClient.RouteFilterRule(); // RouteFilterRule | Parameters supplied to the create or update route filter rule operation.
apiInstance.routeFilterRulesCreateOrUpdate(resourceGroupName, routeFilterName, ruleName, apiVersion, subscriptionId, routeFilterRuleParameters, (error, data, response) => {
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
 **routeFilterName** | **String**| The name of the route filter. | 
 **ruleName** | **String**| The name of the route filter rule. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **routeFilterRuleParameters** | [**RouteFilterRule**](RouteFilterRule.md)| Parameters supplied to the create or update route filter rule operation. | 

### Return type

[**RouteFilterRule**](RouteFilterRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## routeFilterRulesDelete

> routeFilterRulesDelete(resourceGroupName, routeFilterName, ruleName, apiVersion, subscriptionId)



Deletes the specified rule from a route filter.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.RouteFilterRulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let routeFilterName = "routeFilterName_example"; // String | The name of the route filter.
let ruleName = "ruleName_example"; // String | The name of the rule.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.routeFilterRulesDelete(resourceGroupName, routeFilterName, ruleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **routeFilterName** | **String**| The name of the route filter. | 
 **ruleName** | **String**| The name of the rule. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## routeFilterRulesGet

> RouteFilterRule routeFilterRulesGet(resourceGroupName, routeFilterName, ruleName, apiVersion, subscriptionId)



Gets the specified rule from a route filter.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.RouteFilterRulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let routeFilterName = "routeFilterName_example"; // String | The name of the route filter.
let ruleName = "ruleName_example"; // String | The name of the rule.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.routeFilterRulesGet(resourceGroupName, routeFilterName, ruleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **routeFilterName** | **String**| The name of the route filter. | 
 **ruleName** | **String**| The name of the rule. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**RouteFilterRule**](RouteFilterRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## routeFilterRulesListByRouteFilter

> RouteFilterRuleListResult routeFilterRulesListByRouteFilter(resourceGroupName, routeFilterName, apiVersion, subscriptionId)



Gets all RouteFilterRules in a route filter.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.RouteFilterRulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let routeFilterName = "routeFilterName_example"; // String | The name of the route filter.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.routeFilterRulesListByRouteFilter(resourceGroupName, routeFilterName, apiVersion, subscriptionId, (error, data, response) => {
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
 **routeFilterName** | **String**| The name of the route filter. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**RouteFilterRuleListResult**](RouteFilterRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## routeFilterRulesUpdate

> RouteFilterRule routeFilterRulesUpdate(resourceGroupName, routeFilterName, ruleName, apiVersion, subscriptionId, routeFilterRuleParameters)



Updates a route in the specified route filter.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.RouteFilterRulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let routeFilterName = "routeFilterName_example"; // String | The name of the route filter.
let ruleName = "ruleName_example"; // String | The name of the route filter rule.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let routeFilterRuleParameters = new NetworkManagementClient.PatchRouteFilterRule(); // PatchRouteFilterRule | Parameters supplied to the update route filter rule operation.
apiInstance.routeFilterRulesUpdate(resourceGroupName, routeFilterName, ruleName, apiVersion, subscriptionId, routeFilterRuleParameters, (error, data, response) => {
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
 **routeFilterName** | **String**| The name of the route filter. | 
 **ruleName** | **String**| The name of the route filter rule. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **routeFilterRuleParameters** | [**PatchRouteFilterRule**](PatchRouteFilterRule.md)| Parameters supplied to the update route filter rule operation. | 

### Return type

[**RouteFilterRule**](RouteFilterRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

