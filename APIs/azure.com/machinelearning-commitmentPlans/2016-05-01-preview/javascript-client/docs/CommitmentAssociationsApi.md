# AzureMlCommitmentPlansManagementClient.CommitmentAssociationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commitmentAssociationsGet**](CommitmentAssociationsApi.md#commitmentAssociationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/commitmentPlans/{commitmentPlanName}/commitmentAssociations/{commitmentAssociationName} | 
[**commitmentAssociationsList**](CommitmentAssociationsApi.md#commitmentAssociationsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/commitmentPlans/{commitmentPlanName}/commitmentAssociations | 
[**commitmentAssociationsMove**](CommitmentAssociationsApi.md#commitmentAssociationsMove) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/commitmentPlans/{commitmentPlanName}/commitmentAssociations/{commitmentAssociationName}/move | 



## commitmentAssociationsGet

> CommitmentAssociation commitmentAssociationsGet(subscriptionId, resourceGroupName, commitmentPlanName, commitmentAssociationName, apiVersion)



Get a commitment association.

### Example

```javascript
import AzureMlCommitmentPlansManagementClient from 'azure_ml_commitment_plans_management_client';

let apiInstance = new AzureMlCommitmentPlansManagementClient.CommitmentAssociationsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let commitmentPlanName = "commitmentPlanName_example"; // String | The Azure ML commitment plan name.
let commitmentAssociationName = "commitmentAssociationName_example"; // String | The commitment association name.
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
apiInstance.commitmentAssociationsGet(subscriptionId, resourceGroupName, commitmentPlanName, commitmentAssociationName, apiVersion, (error, data, response) => {
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
 **commitmentAssociationName** | **String**| The commitment association name. | 
 **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | 

### Return type

[**CommitmentAssociation**](CommitmentAssociation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## commitmentAssociationsList

> CommitmentAssociationListResult commitmentAssociationsList(subscriptionId, resourceGroupName, commitmentPlanName, apiVersion, opts)



Get all commitment associations for a parent commitment plan.

### Example

```javascript
import AzureMlCommitmentPlansManagementClient from 'azure_ml_commitment_plans_management_client';

let apiInstance = new AzureMlCommitmentPlansManagementClient.CommitmentAssociationsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let commitmentPlanName = "commitmentPlanName_example"; // String | The Azure ML commitment plan name.
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
let opts = {
  'skipToken': "skipToken_example" // String | Continuation token for pagination.
};
apiInstance.commitmentAssociationsList(subscriptionId, resourceGroupName, commitmentPlanName, apiVersion, opts, (error, data, response) => {
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

[**CommitmentAssociationListResult**](CommitmentAssociationListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## commitmentAssociationsMove

> CommitmentAssociation commitmentAssociationsMove(subscriptionId, resourceGroupName, commitmentPlanName, commitmentAssociationName, apiVersion, movePayload)



Re-parent a commitment association from one commitment plan to another.

### Example

```javascript
import AzureMlCommitmentPlansManagementClient from 'azure_ml_commitment_plans_management_client';

let apiInstance = new AzureMlCommitmentPlansManagementClient.CommitmentAssociationsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let commitmentPlanName = "commitmentPlanName_example"; // String | The Azure ML commitment plan name.
let commitmentAssociationName = "commitmentAssociationName_example"; // String | The commitment association name.
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
let movePayload = new AzureMlCommitmentPlansManagementClient.MoveCommitmentAssociationRequest(); // MoveCommitmentAssociationRequest | The move request payload.
apiInstance.commitmentAssociationsMove(subscriptionId, resourceGroupName, commitmentPlanName, commitmentAssociationName, apiVersion, movePayload, (error, data, response) => {
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
 **commitmentAssociationName** | **String**| The commitment association name. | 
 **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | 
 **movePayload** | [**MoveCommitmentAssociationRequest**](MoveCommitmentAssociationRequest.md)| The move request payload. | 

### Return type

[**CommitmentAssociation**](CommitmentAssociation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

