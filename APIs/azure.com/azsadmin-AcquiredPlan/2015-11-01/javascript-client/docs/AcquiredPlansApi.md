# SubscriptionsManagementClient.AcquiredPlansApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acquiredPlansCreate**](AcquiredPlansApi.md#acquiredPlansCreate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Subscriptions.Admin/subscriptions/{targetSubscriptionId}/acquiredPlans/{planAcquisitionId} | 
[**acquiredPlansDelete**](AcquiredPlansApi.md#acquiredPlansDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Subscriptions.Admin/subscriptions/{targetSubscriptionId}/acquiredPlans/{planAcquisitionId} | 
[**acquiredPlansGet**](AcquiredPlansApi.md#acquiredPlansGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Subscriptions.Admin/subscriptions/{targetSubscriptionId}/acquiredPlans/{planAcquisitionId} | 
[**acquiredPlansList**](AcquiredPlansApi.md#acquiredPlansList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Subscriptions.Admin/subscriptions/{targetSubscriptionId}/acquiredPlans | 



## acquiredPlansCreate

> PlanAcquisition acquiredPlansCreate(subscriptionId, targetSubscriptionId, planAcquisitionId, apiVersion, newAcquiredPlan)



Creates an acquired plan.

### Example

```javascript
import SubscriptionsManagementClient from 'subscriptions_management_client';
let defaultClient = SubscriptionsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionsManagementClient.AcquiredPlansApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let targetSubscriptionId = "targetSubscriptionId_example"; // String | The target subscription ID.
let planAcquisitionId = "planAcquisitionId_example"; // String | The plan acquisition Identifier
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
let newAcquiredPlan = new SubscriptionsManagementClient.PlanAcquisition(); // PlanAcquisition | The new acquired plan.
apiInstance.acquiredPlansCreate(subscriptionId, targetSubscriptionId, planAcquisitionId, apiVersion, newAcquiredPlan, (error, data, response) => {
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
 **targetSubscriptionId** | **String**| The target subscription ID. | 
 **planAcquisitionId** | **String**| The plan acquisition Identifier | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]
 **newAcquiredPlan** | [**PlanAcquisition**](PlanAcquisition.md)| The new acquired plan. | 

### Return type

[**PlanAcquisition**](PlanAcquisition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## acquiredPlansDelete

> acquiredPlansDelete(subscriptionId, targetSubscriptionId, planAcquisitionId, apiVersion)



Deletes an acquired plan.

### Example

```javascript
import SubscriptionsManagementClient from 'subscriptions_management_client';
let defaultClient = SubscriptionsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionsManagementClient.AcquiredPlansApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let targetSubscriptionId = "targetSubscriptionId_example"; // String | The target subscription ID.
let planAcquisitionId = "planAcquisitionId_example"; // String | The plan acquisition Identifier
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.acquiredPlansDelete(subscriptionId, targetSubscriptionId, planAcquisitionId, apiVersion, (error, data, response) => {
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
 **targetSubscriptionId** | **String**| The target subscription ID. | 
 **planAcquisitionId** | **String**| The plan acquisition Identifier | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## acquiredPlansGet

> PlanAcquisition acquiredPlansGet(subscriptionId, targetSubscriptionId, planAcquisitionId, apiVersion)



Gets the specified plan acquired by a subscription consuming the offer.

### Example

```javascript
import SubscriptionsManagementClient from 'subscriptions_management_client';
let defaultClient = SubscriptionsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionsManagementClient.AcquiredPlansApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let targetSubscriptionId = "targetSubscriptionId_example"; // String | The target subscription ID.
let planAcquisitionId = "planAcquisitionId_example"; // String | The plan acquisition Identifier
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.acquiredPlansGet(subscriptionId, targetSubscriptionId, planAcquisitionId, apiVersion, (error, data, response) => {
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
 **targetSubscriptionId** | **String**| The target subscription ID. | 
 **planAcquisitionId** | **String**| The plan acquisition Identifier | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]

### Return type

[**PlanAcquisition**](PlanAcquisition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## acquiredPlansList

> PlanAcquisitionList acquiredPlansList(subscriptionId, targetSubscriptionId, apiVersion)



Get a collection of all acquired plans that subscription has access to.

### Example

```javascript
import SubscriptionsManagementClient from 'subscriptions_management_client';
let defaultClient = SubscriptionsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SubscriptionsManagementClient.AcquiredPlansApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let targetSubscriptionId = "targetSubscriptionId_example"; // String | The target subscription ID.
let apiVersion = "'2015-11-01'"; // String | Client Api Version.
apiInstance.acquiredPlansList(subscriptionId, targetSubscriptionId, apiVersion, (error, data, response) => {
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
 **targetSubscriptionId** | **String**| The target subscription ID. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2015-11-01&#39;]

### Return type

[**PlanAcquisitionList**](PlanAcquisitionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

