# ServiceTierAdvisorsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serviceTierAdvisorsGet**](ServiceTierAdvisorsApi.md#serviceTierAdvisorsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/serviceTierAdvisors/{serviceTierAdvisorName} |  |
| [**serviceTierAdvisorsListByDatabase**](ServiceTierAdvisorsApi.md#serviceTierAdvisorsListByDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/serviceTierAdvisors |  |


<a id="serviceTierAdvisorsGet"></a>
# **serviceTierAdvisorsGet**
> ServiceTierAdvisor serviceTierAdvisorsGet(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, serviceTierAdvisorName)



Gets a service tier advisor.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceTierAdvisorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ServiceTierAdvisorsApi apiInstance = new ServiceTierAdvisorsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of database.
    String serviceTierAdvisorName = "serviceTierAdvisorName_example"; // String | The name of service tier advisor.
    try {
      ServiceTierAdvisor result = apiInstance.serviceTierAdvisorsGet(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, serviceTierAdvisorName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceTierAdvisorsApi#serviceTierAdvisorsGet");
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
| **databaseName** | **String**| The name of database. | |
| **serviceTierAdvisorName** | **String**| The name of service tier advisor. | |

### Return type

[**ServiceTierAdvisor**](ServiceTierAdvisor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="serviceTierAdvisorsListByDatabase"></a>
# **serviceTierAdvisorsListByDatabase**
> ServiceTierAdvisorListResult serviceTierAdvisorsListByDatabase(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName)



Returns service tier advisors for specified database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceTierAdvisorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ServiceTierAdvisorsApi apiInstance = new ServiceTierAdvisorsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of database.
    try {
      ServiceTierAdvisorListResult result = apiInstance.serviceTierAdvisorsListByDatabase(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceTierAdvisorsApi#serviceTierAdvisorsListByDatabase");
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
| **databaseName** | **String**| The name of database. | |

### Return type

[**ServiceTierAdvisorListResult**](ServiceTierAdvisorListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

