# ExternalSecuritySolutionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**externalSecuritySolutionsGet**](ExternalSecuritySolutionsApi.md#externalSecuritySolutionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/ExternalSecuritySolutions/{externalSecuritySolutionsName} |  |
| [**externalSecuritySolutionsList**](ExternalSecuritySolutionsApi.md#externalSecuritySolutionsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/externalSecuritySolutions |  |
| [**externalSecuritySolutionsListByHomeRegion**](ExternalSecuritySolutionsApi.md#externalSecuritySolutionsListByHomeRegion) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/ExternalSecuritySolutions |  |


<a id="externalSecuritySolutionsGet"></a>
# **externalSecuritySolutionsGet**
> ExternalSecuritySolution externalSecuritySolutionsGet(subscriptionId, resourceGroupName, ascLocation, externalSecuritySolutionsName, apiVersion)



Gets a specific external Security Solution.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExternalSecuritySolutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExternalSecuritySolutionsApi apiInstance = new ExternalSecuritySolutionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String externalSecuritySolutionsName = "externalSecuritySolutionsName_example"; // String | Name of an external security solution.
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    try {
      ExternalSecuritySolution result = apiInstance.externalSecuritySolutionsGet(subscriptionId, resourceGroupName, ascLocation, externalSecuritySolutionsName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExternalSecuritySolutionsApi#externalSecuritySolutionsGet");
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
| **externalSecuritySolutionsName** | **String**| Name of an external security solution. | |
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |

### Return type

[**ExternalSecuritySolution**](ExternalSecuritySolution.md)

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

<a id="externalSecuritySolutionsList"></a>
# **externalSecuritySolutionsList**
> ExternalSecuritySolutionList externalSecuritySolutionsList(apiVersion, subscriptionId)



Gets a list of external security solutions for the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExternalSecuritySolutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExternalSecuritySolutionsApi apiInstance = new ExternalSecuritySolutionsApi(defaultClient);
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    try {
      ExternalSecuritySolutionList result = apiInstance.externalSecuritySolutionsList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExternalSecuritySolutionsApi#externalSecuritySolutionsList");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |

### Return type

[**ExternalSecuritySolutionList**](ExternalSecuritySolutionList.md)

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

<a id="externalSecuritySolutionsListByHomeRegion"></a>
# **externalSecuritySolutionsListByHomeRegion**
> ExternalSecuritySolutionList externalSecuritySolutionsListByHomeRegion(subscriptionId, ascLocation, apiVersion)



Gets a list of external Security Solutions for the subscription and location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExternalSecuritySolutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExternalSecuritySolutionsApi apiInstance = new ExternalSecuritySolutionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    try {
      ExternalSecuritySolutionList result = apiInstance.externalSecuritySolutionsListByHomeRegion(subscriptionId, ascLocation, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExternalSecuritySolutionsApi#externalSecuritySolutionsListByHomeRegion");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |

### Return type

[**ExternalSecuritySolutionList**](ExternalSecuritySolutionList.md)

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

