# ProblemClassificationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**problemClassificationsGet**](ProblemClassificationsApi.md#problemClassificationsGet) | **GET** /providers/Microsoft.Support/services/{serviceName}/problemClassifications/{problemClassificationName} |  |
| [**problemClassificationsList**](ProblemClassificationsApi.md#problemClassificationsList) | **GET** /providers/Microsoft.Support/services/{serviceName}/problemClassifications |  |


<a id="problemClassificationsGet"></a>
# **problemClassificationsGet**
> ProblemClassification problemClassificationsGet(serviceName, problemClassificationName, apiVersion)



Gets the details of a specific problem classification for a specific Azure service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProblemClassificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProblemClassificationsApi apiInstance = new ProblemClassificationsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | Name of Azure service available for support.
    String problemClassificationName = "problemClassificationName_example"; // String | Name of problem classification.
    String apiVersion = "apiVersion_example"; // String | Api version
    try {
      ProblemClassification result = apiInstance.problemClassificationsGet(serviceName, problemClassificationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProblemClassificationsApi#problemClassificationsGet");
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
| **serviceName** | **String**| Name of Azure service available for support. | |
| **problemClassificationName** | **String**| Name of problem classification. | |
| **apiVersion** | **String**| Api version | |

### Return type

[**ProblemClassification**](ProblemClassification.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved problem classification details. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="problemClassificationsList"></a>
# **problemClassificationsList**
> ProblemClassificationsListResult problemClassificationsList(serviceName, apiVersion)



Lists all the problem classifications (categories) available for a specific Azure service.&lt;br/&gt;&lt;br/&gt; Always use the service and problem classifications obtained programmatically. This practice ensures that you always have the most recent set of service and problem classification Ids.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProblemClassificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProblemClassificationsApi apiInstance = new ProblemClassificationsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | Name of Azure service for which the problem classifications need to be retrieved.
    String apiVersion = "apiVersion_example"; // String | Api version
    try {
      ProblemClassificationsListResult result = apiInstance.problemClassificationsList(serviceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProblemClassificationsApi#problemClassificationsList");
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
| **serviceName** | **String**| Name of Azure service for which the problem classifications need to be retrieved. | |
| **apiVersion** | **String**| Api version | |

### Return type

[**ProblemClassificationsListResult**](ProblemClassificationsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved list of problem classifications for the specified Azure service. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

