# DeploymentAdminClient.ActionPlansApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**actionPlansGet**](ActionPlansApi.md#actionPlansGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/actionPlans/{planId} | 
[**actionPlansList**](ActionPlansApi.md#actionPlansList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/actionPlans | 



## actionPlansGet

> ActionPlanResourceEntity actionPlansGet(subscriptionId, planId, apiVersion)



Gets the specified action plan

### Example

```javascript
import DeploymentAdminClient from 'deployment_admin_client';
let defaultClient = DeploymentAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentAdminClient.ActionPlansApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let planId = "planId_example"; // String | Identifier of the action plan.
let apiVersion = "'2019-01-01'"; // String | Client API Version.
apiInstance.actionPlansGet(subscriptionId, planId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **planId** | **String**| Identifier of the action plan. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2019-01-01&#39;]

### Return type

[**ActionPlanResourceEntity**](ActionPlanResourceEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## actionPlansList

> ActionPlanList actionPlansList(subscriptionId, apiVersion)



Gets the list of action plans

### Example

```javascript
import DeploymentAdminClient from 'deployment_admin_client';
let defaultClient = DeploymentAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentAdminClient.ActionPlansApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "'2019-01-01'"; // String | Client API Version.
apiInstance.actionPlansList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2019-01-01&#39;]

### Return type

[**ActionPlanList**](ActionPlanList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

