# AzureMlCommitmentPlansManagementClient.CommitmentPlansApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commitmentPlansCreateOrUpdate**](CommitmentPlansApi.md#commitmentPlansCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/commitmentPlans/{commitmentPlanName} | 
[**commitmentPlansGet**](CommitmentPlansApi.md#commitmentPlansGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/commitmentPlans/{commitmentPlanName} | 
[**commitmentPlansList**](CommitmentPlansApi.md#commitmentPlansList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MachineLearning/commitmentPlans | 
[**commitmentPlansListInResourceGroup**](CommitmentPlansApi.md#commitmentPlansListInResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/commitmentPlans | 
[**commitmentPlansPatch**](CommitmentPlansApi.md#commitmentPlansPatch) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/commitmentPlans/{commitmentPlanName} | 
[**commitmentPlansRemove**](CommitmentPlansApi.md#commitmentPlansRemove) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/commitmentPlans/{commitmentPlanName} | 
[**usageHistoryList**](CommitmentPlansApi.md#usageHistoryList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/commitmentPlans/{commitmentPlanName}/usageHistory | 



## commitmentPlansCreateOrUpdate

> CommitmentPlan commitmentPlansCreateOrUpdate(subscriptionId, resourceGroupName, commitmentPlanName, apiVersion, createOrUpdatePayload)



Create a new Azure ML commitment plan resource or updates an existing one.

### Example

```javascript
import AzureMlCommitmentPlansManagementClient from 'azure_ml_commitment_plans_management_client';

let apiInstance = new AzureMlCommitmentPlansManagementClient.CommitmentPlansApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let commitmentPlanName = "commitmentPlanName_example"; // String | The Azure ML commitment plan name.
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
let createOrUpdatePayload = new AzureMlCommitmentPlansManagementClient.CommitmentPlan(); // CommitmentPlan | The payload to create or update the Azure ML commitment plan.
apiInstance.commitmentPlansCreateOrUpdate(subscriptionId, resourceGroupName, commitmentPlanName, apiVersion, createOrUpdatePayload, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **commitmentPlanName** | **String**| The Azure ML commitment plan name. | 
 **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | 
 **createOrUpdatePayload** | [**CommitmentPlan**](CommitmentPlan.md)| The payload to create or update the Azure ML commitment plan. | 

### Return type

[**CommitmentPlan**](CommitmentPlan.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## commitmentPlansGet

> CommitmentPlan commitmentPlansGet(subscriptionId, resourceGroupName, commitmentPlanName, apiVersion)



Retrieve an Azure ML commitment plan by its subscription, resource group and name.

### Example

```javascript
import AzureMlCommitmentPlansManagementClient from 'azure_ml_commitment_plans_management_client';

let apiInstance = new AzureMlCommitmentPlansManagementClient.CommitmentPlansApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let commitmentPlanName = "commitmentPlanName_example"; // String | The Azure ML commitment plan name.
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
apiInstance.commitmentPlansGet(subscriptionId, resourceGroupName, commitmentPlanName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **commitmentPlanName** | **String**| The Azure ML commitment plan name. | 
 **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | 

### Return type

[**CommitmentPlan**](CommitmentPlan.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## commitmentPlansList

> CommitmentPlanListResult commitmentPlansList(subscriptionId, apiVersion, opts)



Retrieve all Azure ML commitment plans in a subscription.

### Example

```javascript
import AzureMlCommitmentPlansManagementClient from 'azure_ml_commitment_plans_management_client';

let apiInstance = new AzureMlCommitmentPlansManagementClient.CommitmentPlansApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
let opts = {
  'skipToken': "skipToken_example" // String | Continuation token for pagination.
};
apiInstance.commitmentPlansList(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | 
 **skipToken** | **String**| Continuation token for pagination. | [optional] 

### Return type

[**CommitmentPlanListResult**](CommitmentPlanListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## commitmentPlansListInResourceGroup

> CommitmentPlanListResult commitmentPlansListInResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts)



Retrieve all Azure ML commitment plans in a resource group.

### Example

```javascript
import AzureMlCommitmentPlansManagementClient from 'azure_ml_commitment_plans_management_client';

let apiInstance = new AzureMlCommitmentPlansManagementClient.CommitmentPlansApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
let opts = {
  'skipToken': "skipToken_example" // String | Continuation token for pagination.
};
apiInstance.commitmentPlansListInResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | 
 **skipToken** | **String**| Continuation token for pagination. | [optional] 

### Return type

[**CommitmentPlanListResult**](CommitmentPlanListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## commitmentPlansPatch

> CommitmentPlan commitmentPlansPatch(subscriptionId, resourceGroupName, commitmentPlanName, apiVersion, patchPayload)



Patch an existing Azure ML commitment plan resource.

### Example

```javascript
import AzureMlCommitmentPlansManagementClient from 'azure_ml_commitment_plans_management_client';

let apiInstance = new AzureMlCommitmentPlansManagementClient.CommitmentPlansApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let commitmentPlanName = "commitmentPlanName_example"; // String | The Azure ML commitment plan name.
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
let patchPayload = new AzureMlCommitmentPlansManagementClient.CommitmentPlanPatchPayload(); // CommitmentPlanPatchPayload | The payload to use to patch the Azure ML commitment plan. Only tags and SKU may be modified on an existing commitment plan.
apiInstance.commitmentPlansPatch(subscriptionId, resourceGroupName, commitmentPlanName, apiVersion, patchPayload, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **commitmentPlanName** | **String**| The Azure ML commitment plan name. | 
 **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | 
 **patchPayload** | [**CommitmentPlanPatchPayload**](CommitmentPlanPatchPayload.md)| The payload to use to patch the Azure ML commitment plan. Only tags and SKU may be modified on an existing commitment plan. | 

### Return type

[**CommitmentPlan**](CommitmentPlan.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## commitmentPlansRemove

> commitmentPlansRemove(subscriptionId, resourceGroupName, commitmentPlanName, apiVersion)



Remove an existing Azure ML commitment plan.

### Example

```javascript
import AzureMlCommitmentPlansManagementClient from 'azure_ml_commitment_plans_management_client';

let apiInstance = new AzureMlCommitmentPlansManagementClient.CommitmentPlansApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let commitmentPlanName = "commitmentPlanName_example"; // String | The Azure ML commitment plan name.
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
apiInstance.commitmentPlansRemove(subscriptionId, resourceGroupName, commitmentPlanName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **commitmentPlanName** | **String**| The Azure ML commitment plan name. | 
 **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usageHistoryList

> PlanUsageHistoryListResult usageHistoryList(subscriptionId, resourceGroupName, commitmentPlanName, apiVersion, opts)



Retrieve the usage history for an Azure ML commitment plan.

### Example

```javascript
import AzureMlCommitmentPlansManagementClient from 'azure_ml_commitment_plans_management_client';

let apiInstance = new AzureMlCommitmentPlansManagementClient.CommitmentPlansApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let commitmentPlanName = "commitmentPlanName_example"; // String | The Azure ML commitment plan name.
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
let opts = {
  'skipToken': "skipToken_example" // String | Continuation token for pagination.
};
apiInstance.usageHistoryList(subscriptionId, resourceGroupName, commitmentPlanName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **commitmentPlanName** | **String**| The Azure ML commitment plan name. | 
 **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | 
 **skipToken** | **String**| Continuation token for pagination. | [optional] 

### Return type

[**PlanUsageHistoryListResult**](PlanUsageHistoryListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

