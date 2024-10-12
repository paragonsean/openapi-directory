# DeploymentAdminClient.ActionPlanOperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**actionPlanOperationsGet**](ActionPlanOperationsApi.md#actionPlanOperationsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/actionPlans/{planId}/operations/{operationId} | 
[**actionPlanOperationsList**](ActionPlanOperationsApi.md#actionPlanOperationsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/actionPlans/{planId}/operations | 



## actionPlanOperationsGet

> ActionPlanOperationResourceEntity actionPlanOperationsGet(subscriptionId, planId, operationId, apiVersion)



Gets the specified action plan operation

### Example

```javascript
import DeploymentAdminClient from 'deployment_admin_client';
let defaultClient = DeploymentAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentAdminClient.ActionPlanOperationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let planId = "planId_example"; // String | Identifier of the action plan.
let operationId = "operationId_example"; // String | Identifier of the action plan operation.
let apiVersion = "'2019-01-01'"; // String | Client API Version.
apiInstance.actionPlanOperationsGet(subscriptionId, planId, operationId, apiVersion, (error, data, response) => {
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
 **operationId** | **String**| Identifier of the action plan operation. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2019-01-01&#39;]

### Return type

[**ActionPlanOperationResourceEntity**](ActionPlanOperationResourceEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## actionPlanOperationsList

> ActionPlanOperationsList actionPlanOperationsList(subscriptionId, planId, apiVersion)



Lists the action plan operations

### Example

```javascript
import DeploymentAdminClient from 'deployment_admin_client';
let defaultClient = DeploymentAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentAdminClient.ActionPlanOperationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let planId = "planId_example"; // String | Identifier of the action plan.
let apiVersion = "'2019-01-01'"; // String | Client API Version.
apiInstance.actionPlanOperationsList(subscriptionId, planId, apiVersion, (error, data, response) => {
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

[**ActionPlanOperationsList**](ActionPlanOperationsList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

