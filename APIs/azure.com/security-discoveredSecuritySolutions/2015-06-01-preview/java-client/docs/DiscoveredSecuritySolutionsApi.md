# DiscoveredSecuritySolutionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**discoveredSecuritySolutionsGet**](DiscoveredSecuritySolutionsApi.md#discoveredSecuritySolutionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/discoveredSecuritySolutions/{discoveredSecuritySolutionName} |  |
| [**discoveredSecuritySolutionsList**](DiscoveredSecuritySolutionsApi.md#discoveredSecuritySolutionsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/discoveredSecuritySolutions |  |
| [**discoveredSecuritySolutionsListByHomeRegion**](DiscoveredSecuritySolutionsApi.md#discoveredSecuritySolutionsListByHomeRegion) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/discoveredSecuritySolutions |  |


<a id="discoveredSecuritySolutionsGet"></a>
# **discoveredSecuritySolutionsGet**
> DiscoveredSecuritySolution discoveredSecuritySolutionsGet(subscriptionId, resourceGroupName, ascLocation, discoveredSecuritySolutionName, apiVersion)



Gets a specific discovered Security Solution.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveredSecuritySolutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiscoveredSecuritySolutionsApi apiInstance = new DiscoveredSecuritySolutionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String discoveredSecuritySolutionName = "discoveredSecuritySolutionName_example"; // String | Name of a discovered security solution.
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    try {
      DiscoveredSecuritySolution result = apiInstance.discoveredSecuritySolutionsGet(subscriptionId, resourceGroupName, ascLocation, discoveredSecuritySolutionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveredSecuritySolutionsApi#discoveredSecuritySolutionsGet");
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
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | |
| **discoveredSecuritySolutionName** | **String**| Name of a discovered security solution. | |
| **apiVersion** | **String**| API version for the operation | |

### Return type

[**DiscoveredSecuritySolution**](DiscoveredSecuritySolution.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="discoveredSecuritySolutionsList"></a>
# **discoveredSecuritySolutionsList**
> DiscoveredSecuritySolutionList discoveredSecuritySolutionsList(subscriptionId, apiVersion)



Gets a list of discovered Security Solutions for the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveredSecuritySolutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiscoveredSecuritySolutionsApi apiInstance = new DiscoveredSecuritySolutionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    try {
      DiscoveredSecuritySolutionList result = apiInstance.discoveredSecuritySolutionsList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveredSecuritySolutionsApi#discoveredSecuritySolutionsList");
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
| **subscriptionId** | **String**| Azure subscription ID | |
| **apiVersion** | **String**| API version for the operation | |

### Return type

[**DiscoveredSecuritySolutionList**](DiscoveredSecuritySolutionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="discoveredSecuritySolutionsListByHomeRegion"></a>
# **discoveredSecuritySolutionsListByHomeRegion**
> DiscoveredSecuritySolutionList discoveredSecuritySolutionsListByHomeRegion(subscriptionId, ascLocation, apiVersion)



Gets a list of discovered Security Solutions for the subscription and location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveredSecuritySolutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiscoveredSecuritySolutionsApi apiInstance = new DiscoveredSecuritySolutionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    try {
      DiscoveredSecuritySolutionList result = apiInstance.discoveredSecuritySolutionsListByHomeRegion(subscriptionId, ascLocation, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveredSecuritySolutionsApi#discoveredSecuritySolutionsListByHomeRegion");
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
| **subscriptionId** | **String**| Azure subscription ID | |
| **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | |
| **apiVersion** | **String**| API version for the operation | |

### Return type

[**DiscoveredSecuritySolutionList**](DiscoveredSecuritySolutionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

