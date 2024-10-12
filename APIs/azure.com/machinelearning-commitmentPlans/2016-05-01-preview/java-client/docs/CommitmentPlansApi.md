# CommitmentPlansApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**commitmentPlansCreateOrUpdate**](CommitmentPlansApi.md#commitmentPlansCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/commitmentPlans/{commitmentPlanName} |  |
| [**commitmentPlansGet**](CommitmentPlansApi.md#commitmentPlansGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/commitmentPlans/{commitmentPlanName} |  |
| [**commitmentPlansList**](CommitmentPlansApi.md#commitmentPlansList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MachineLearning/commitmentPlans |  |
| [**commitmentPlansListInResourceGroup**](CommitmentPlansApi.md#commitmentPlansListInResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/commitmentPlans |  |
| [**commitmentPlansPatch**](CommitmentPlansApi.md#commitmentPlansPatch) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/commitmentPlans/{commitmentPlanName} |  |
| [**commitmentPlansRemove**](CommitmentPlansApi.md#commitmentPlansRemove) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/commitmentPlans/{commitmentPlanName} |  |
| [**usageHistoryList**](CommitmentPlansApi.md#usageHistoryList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/commitmentPlans/{commitmentPlanName}/usageHistory |  |


<a id="commitmentPlansCreateOrUpdate"></a>
# **commitmentPlansCreateOrUpdate**
> CommitmentPlan commitmentPlansCreateOrUpdate(subscriptionId, resourceGroupName, commitmentPlanName, apiVersion, createOrUpdatePayload)



Create a new Azure ML commitment plan resource or updates an existing one.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommitmentPlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    CommitmentPlansApi apiInstance = new CommitmentPlansApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String commitmentPlanName = "commitmentPlanName_example"; // String | The Azure ML commitment plan name.
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
    CommitmentPlan createOrUpdatePayload = new CommitmentPlan(); // CommitmentPlan | The payload to create or update the Azure ML commitment plan.
    try {
      CommitmentPlan result = apiInstance.commitmentPlansCreateOrUpdate(subscriptionId, resourceGroupName, commitmentPlanName, apiVersion, createOrUpdatePayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommitmentPlansApi#commitmentPlansCreateOrUpdate");
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
| **createOrUpdatePayload** | [**CommitmentPlan**](CommitmentPlan.md)| The payload to create or update the Azure ML commitment plan. | |

### Return type

[**CommitmentPlan**](CommitmentPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |

<a id="commitmentPlansGet"></a>
# **commitmentPlansGet**
> CommitmentPlan commitmentPlansGet(subscriptionId, resourceGroupName, commitmentPlanName, apiVersion)



Retrieve an Azure ML commitment plan by its subscription, resource group and name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommitmentPlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    CommitmentPlansApi apiInstance = new CommitmentPlansApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String commitmentPlanName = "commitmentPlanName_example"; // String | The Azure ML commitment plan name.
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
    try {
      CommitmentPlan result = apiInstance.commitmentPlansGet(subscriptionId, resourceGroupName, commitmentPlanName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommitmentPlansApi#commitmentPlansGet");
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

### Return type

[**CommitmentPlan**](CommitmentPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="commitmentPlansList"></a>
# **commitmentPlansList**
> CommitmentPlanListResult commitmentPlansList(subscriptionId, apiVersion, $skipToken)



Retrieve all Azure ML commitment plans in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommitmentPlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    CommitmentPlansApi apiInstance = new CommitmentPlansApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
    String $skipToken = "$skipToken_example"; // String | Continuation token for pagination.
    try {
      CommitmentPlanListResult result = apiInstance.commitmentPlansList(subscriptionId, apiVersion, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommitmentPlansApi#commitmentPlansList");
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
| **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | |
| **$skipToken** | **String**| Continuation token for pagination. | [optional] |

### Return type

[**CommitmentPlanListResult**](CommitmentPlanListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="commitmentPlansListInResourceGroup"></a>
# **commitmentPlansListInResourceGroup**
> CommitmentPlanListResult commitmentPlansListInResourceGroup(subscriptionId, resourceGroupName, apiVersion, $skipToken)



Retrieve all Azure ML commitment plans in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommitmentPlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    CommitmentPlansApi apiInstance = new CommitmentPlansApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
    String $skipToken = "$skipToken_example"; // String | Continuation token for pagination.
    try {
      CommitmentPlanListResult result = apiInstance.commitmentPlansListInResourceGroup(subscriptionId, resourceGroupName, apiVersion, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommitmentPlansApi#commitmentPlansListInResourceGroup");
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
| **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | |
| **$skipToken** | **String**| Continuation token for pagination. | [optional] |

### Return type

[**CommitmentPlanListResult**](CommitmentPlanListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="commitmentPlansPatch"></a>
# **commitmentPlansPatch**
> CommitmentPlan commitmentPlansPatch(subscriptionId, resourceGroupName, commitmentPlanName, apiVersion, patchPayload)



Patch an existing Azure ML commitment plan resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommitmentPlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    CommitmentPlansApi apiInstance = new CommitmentPlansApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String commitmentPlanName = "commitmentPlanName_example"; // String | The Azure ML commitment plan name.
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
    CommitmentPlanPatchPayload patchPayload = new CommitmentPlanPatchPayload(); // CommitmentPlanPatchPayload | The payload to use to patch the Azure ML commitment plan. Only tags and SKU may be modified on an existing commitment plan.
    try {
      CommitmentPlan result = apiInstance.commitmentPlansPatch(subscriptionId, resourceGroupName, commitmentPlanName, apiVersion, patchPayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommitmentPlansApi#commitmentPlansPatch");
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
| **patchPayload** | [**CommitmentPlanPatchPayload**](CommitmentPlanPatchPayload.md)| The payload to use to patch the Azure ML commitment plan. Only tags and SKU may be modified on an existing commitment plan. | |

### Return type

[**CommitmentPlan**](CommitmentPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="commitmentPlansRemove"></a>
# **commitmentPlansRemove**
> commitmentPlansRemove(subscriptionId, resourceGroupName, commitmentPlanName, apiVersion)



Remove an existing Azure ML commitment plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommitmentPlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    CommitmentPlansApi apiInstance = new CommitmentPlansApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String commitmentPlanName = "commitmentPlanName_example"; // String | The Azure ML commitment plan name.
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
    try {
      apiInstance.commitmentPlansRemove(subscriptionId, resourceGroupName, commitmentPlanName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommitmentPlansApi#commitmentPlansRemove");
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="usageHistoryList"></a>
# **usageHistoryList**
> PlanUsageHistoryListResult usageHistoryList(subscriptionId, resourceGroupName, commitmentPlanName, apiVersion, $skipToken)



Retrieve the usage history for an Azure ML commitment plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommitmentPlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    CommitmentPlansApi apiInstance = new CommitmentPlansApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String commitmentPlanName = "commitmentPlanName_example"; // String | The Azure ML commitment plan name.
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
    String $skipToken = "$skipToken_example"; // String | Continuation token for pagination.
    try {
      PlanUsageHistoryListResult result = apiInstance.usageHistoryList(subscriptionId, resourceGroupName, commitmentPlanName, apiVersion, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommitmentPlansApi#usageHistoryList");
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

[**PlanUsageHistoryListResult**](PlanUsageHistoryListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

