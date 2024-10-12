# SubscriptionsManagementClient.PlansApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**plansCreateOrUpdate**](PlansApi.md#plansCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Subscriptions.Admin/plans/{plan} | 
[**plansDelete**](PlansApi.md#plansDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Subscriptions.Admin/plans/{plan} | 
[**plansGet**](PlansApi.md#plansGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Subscriptions.Admin/plans/{plan} | 
[**plansList**](PlansApi.md#plansList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Subscriptions.Admin/plans | 
[**plansListAll**](PlansApi.md#plansListAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Subscriptions.Admin/plans | 
[**plansListMetricDefinitions**](PlansApi.md#plansListMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Subscriptions.Admin/plans/{plan}/metricDefinitions | 
[**plansListMetrics**](PlansApi.md#plansListMetrics) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Subscriptions.Admin/plans/{plan}/metrics | 



## plansCreateOrUpdate

> Plan plansCreateOrUpdate(subscriptionId, resourceGroupName, plan, apiVersion, newPlan)



Create or update the plan.

### Example

```javascript
import SubscriptionsManagementClient from 'subscriptions_management_client';
let defaultClient = SubscriptionsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionsManagementClient.PlansApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group the resource is located under.
let plan = "plan_example"; // String | Name of the plan.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
let newPlan = new SubscriptionsManagementClient.Plan(); // Plan | New plan.
apiInstance.plansCreateOrUpdate(subscriptionId, resourceGroupName, plan, apiVersion, newPlan, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The resource group the resource is located under. | 
 **plan** | **String**| Name of the plan. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]
 **newPlan** | [**Plan**](Plan.md)| New plan. | 

### Return type

[**Plan**](Plan.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## plansDelete

> plansDelete(subscriptionId, resourceGroupName, plan, apiVersion)



Delete the specified plan.

### Example

```javascript
import SubscriptionsManagementClient from 'subscriptions_management_client';
let defaultClient = SubscriptionsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionsManagementClient.PlansApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group the resource is located under.
let plan = "plan_example"; // String | Name of the plan.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.plansDelete(subscriptionId, resourceGroupName, plan, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The resource group the resource is located under. | 
 **plan** | **String**| Name of the plan. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## plansGet

> Plan plansGet(subscriptionId, resourceGroupName, plan, apiVersion)



Get the specified plan.

### Example

```javascript
import SubscriptionsManagementClient from 'subscriptions_management_client';
let defaultClient = SubscriptionsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionsManagementClient.PlansApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group the resource is located under.
let plan = "plan_example"; // String | Name of the plan.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.plansGet(subscriptionId, resourceGroupName, plan, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The resource group the resource is located under. | 
 **plan** | **String**| Name of the plan. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]

### Return type

[**Plan**](Plan.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## plansList

> PlanList plansList(subscriptionId, resourceGroupName, apiVersion)



Get the list of plans under a resource group.

### Example

```javascript
import SubscriptionsManagementClient from 'subscriptions_management_client';
let defaultClient = SubscriptionsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionsManagementClient.PlansApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group the resource is located under.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.plansList(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The resource group the resource is located under. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]

### Return type

[**PlanList**](PlanList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## plansListAll

> PlanList plansListAll(subscriptionId, apiVersion)



List all plans across all subscriptions.

### Example

```javascript
import SubscriptionsManagementClient from 'subscriptions_management_client';
let defaultClient = SubscriptionsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionsManagementClient.PlansApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.plansListAll(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]

### Return type

[**PlanList**](PlanList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## plansListMetricDefinitions

> PlansListMetricDefinitions200Response plansListMetricDefinitions(subscriptionId, resourceGroupName, plan, apiVersion)



Get the metric definitions of the specified plan.

### Example

```javascript
import SubscriptionsManagementClient from 'subscriptions_management_client';
let defaultClient = SubscriptionsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionsManagementClient.PlansApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group the resource is located under.
let plan = "plan_example"; // String | Name of the plan.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.plansListMetricDefinitions(subscriptionId, resourceGroupName, plan, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The resource group the resource is located under. | 
 **plan** | **String**| Name of the plan. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]

### Return type

[**PlansListMetricDefinitions200Response**](PlansListMetricDefinitions200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## plansListMetrics

> PlansListMetrics200Response plansListMetrics(subscriptionId, resourceGroupName, plan, apiVersion)



Get the metrics of the specified plan.

### Example

```javascript
import SubscriptionsManagementClient from 'subscriptions_management_client';
let defaultClient = SubscriptionsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionsManagementClient.PlansApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group the resource is located under.
let plan = "plan_example"; // String | Name of the plan.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.plansListMetrics(subscriptionId, resourceGroupName, plan, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The resource group the resource is located under. | 
 **plan** | **String**| Name of the plan. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]

### Return type

[**PlansListMetrics200Response**](PlansListMetrics200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

