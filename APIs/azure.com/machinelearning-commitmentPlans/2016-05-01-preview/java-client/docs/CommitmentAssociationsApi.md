# CommitmentAssociationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**commitmentAssociationsGet**](CommitmentAssociationsApi.md#commitmentAssociationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/commitmentPlans/{commitmentPlanName}/commitmentAssociations/{commitmentAssociationName} |  |
| [**commitmentAssociationsList**](CommitmentAssociationsApi.md#commitmentAssociationsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/commitmentPlans/{commitmentPlanName}/commitmentAssociations |  |
| [**commitmentAssociationsMove**](CommitmentAssociationsApi.md#commitmentAssociationsMove) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/commitmentPlans/{commitmentPlanName}/commitmentAssociations/{commitmentAssociationName}/move |  |


<a id="commitmentAssociationsGet"></a>
# **commitmentAssociationsGet**
> CommitmentAssociation commitmentAssociationsGet(subscriptionId, resourceGroupName, commitmentPlanName, commitmentAssociationName, apiVersion)



Get a commitment association.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommitmentAssociationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    CommitmentAssociationsApi apiInstance = new CommitmentAssociationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String commitmentPlanName = "commitmentPlanName_example"; // String | The Azure ML commitment plan name.
    String commitmentAssociationName = "commitmentAssociationName_example"; // String | The commitment association name.
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
    try {
      CommitmentAssociation result = apiInstance.commitmentAssociationsGet(subscriptionId, resourceGroupName, commitmentPlanName, commitmentAssociationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommitmentAssociationsApi#commitmentAssociationsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **commitmentPlanName** | **String**| The Azure ML commitment plan name. | |
| **commitmentAssociationName** | **String**| The commitment association name. | |
| **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | |

### Return type

[**CommitmentAssociation**](CommitmentAssociation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="commitmentAssociationsList"></a>
# **commitmentAssociationsList**
> CommitmentAssociationListResult commitmentAssociationsList(subscriptionId, resourceGroupName, commitmentPlanName, apiVersion, $skipToken)



Get all commitment associations for a parent commitment plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommitmentAssociationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    CommitmentAssociationsApi apiInstance = new CommitmentAssociationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String commitmentPlanName = "commitmentPlanName_example"; // String | The Azure ML commitment plan name.
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
    String $skipToken = "$skipToken_example"; // String | Continuation token for pagination.
    try {
      CommitmentAssociationListResult result = apiInstance.commitmentAssociationsList(subscriptionId, resourceGroupName, commitmentPlanName, apiVersion, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommitmentAssociationsApi#commitmentAssociationsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **commitmentPlanName** | **String**| The Azure ML commitment plan name. | |
| **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | |
| **$skipToken** | **String**| Continuation token for pagination. | [optional] |

### Return type

[**CommitmentAssociationListResult**](CommitmentAssociationListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="commitmentAssociationsMove"></a>
# **commitmentAssociationsMove**
> CommitmentAssociation commitmentAssociationsMove(subscriptionId, resourceGroupName, commitmentPlanName, commitmentAssociationName, apiVersion, movePayload)



Re-parent a commitment association from one commitment plan to another.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommitmentAssociationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    CommitmentAssociationsApi apiInstance = new CommitmentAssociationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String commitmentPlanName = "commitmentPlanName_example"; // String | The Azure ML commitment plan name.
    String commitmentAssociationName = "commitmentAssociationName_example"; // String | The commitment association name.
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
    MoveCommitmentAssociationRequest movePayload = new MoveCommitmentAssociationRequest(); // MoveCommitmentAssociationRequest | The move request payload.
    try {
      CommitmentAssociation result = apiInstance.commitmentAssociationsMove(subscriptionId, resourceGroupName, commitmentPlanName, commitmentAssociationName, apiVersion, movePayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommitmentAssociationsApi#commitmentAssociationsMove");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **commitmentPlanName** | **String**| The Azure ML commitment plan name. | |
| **commitmentAssociationName** | **String**| The commitment association name. | |
| **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | |
| **movePayload** | [**MoveCommitmentAssociationRequest**](MoveCommitmentAssociationRequest.md)| The move request payload. | |

### Return type

[**CommitmentAssociation**](CommitmentAssociation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

