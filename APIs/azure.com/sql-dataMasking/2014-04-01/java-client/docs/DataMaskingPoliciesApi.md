# DataMaskingPoliciesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dataMaskingPoliciesCreateOrUpdate**](DataMaskingPoliciesApi.md#dataMaskingPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/dataMaskingPolicies/{dataMaskingPolicyName} |  |
| [**dataMaskingPoliciesGet**](DataMaskingPoliciesApi.md#dataMaskingPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/dataMaskingPolicies/{dataMaskingPolicyName} |  |


<a id="dataMaskingPoliciesCreateOrUpdate"></a>
# **dataMaskingPoliciesCreateOrUpdate**
> DataMaskingPolicy dataMaskingPoliciesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, dataMaskingPolicyName, parameters)



Creates or updates a database data masking policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataMaskingPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DataMaskingPoliciesApi apiInstance = new DataMaskingPoliciesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String dataMaskingPolicyName = "Default"; // String | The name of the database for which the data masking rule applies.
    DataMaskingPolicy parameters = new DataMaskingPolicy(); // DataMaskingPolicy | Parameters for creating or updating a data masking policy.
    try {
      DataMaskingPolicy result = apiInstance.dataMaskingPoliciesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, dataMaskingPolicyName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataMaskingPoliciesApi#dataMaskingPoliciesCreateOrUpdate");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **databaseName** | **String**| The name of the database. | |
| **dataMaskingPolicyName** | **String**| The name of the database for which the data masking rule applies. | [enum: Default] |
| **parameters** | [**DataMaskingPolicy**](DataMaskingPolicy.md)| Parameters for creating or updating a data masking policy. | |

### Return type

[**DataMaskingPolicy**](DataMaskingPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="dataMaskingPoliciesGet"></a>
# **dataMaskingPoliciesGet**
> DataMaskingPolicy dataMaskingPoliciesGet(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, dataMaskingPolicyName)



Gets a database data masking policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataMaskingPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DataMaskingPoliciesApi apiInstance = new DataMaskingPoliciesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String dataMaskingPolicyName = "Default"; // String | The name of the database for which the data masking rule applies.
    try {
      DataMaskingPolicy result = apiInstance.dataMaskingPoliciesGet(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, dataMaskingPolicyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataMaskingPoliciesApi#dataMaskingPoliciesGet");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **databaseName** | **String**| The name of the database. | |
| **dataMaskingPolicyName** | **String**| The name of the database for which the data masking rule applies. | [enum: Default] |

### Return type

[**DataMaskingPolicy**](DataMaskingPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

