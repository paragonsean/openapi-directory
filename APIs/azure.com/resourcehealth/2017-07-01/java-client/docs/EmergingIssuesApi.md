# EmergingIssuesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**emergingIssuesGet**](EmergingIssuesApi.md#emergingIssuesGet) | **GET** /providers/Microsoft.ResourceHealth/emergingIssues/{issueName} |  |
| [**emergingIssuesList**](EmergingIssuesApi.md#emergingIssuesList) | **GET** /providers/Microsoft.ResourceHealth/emergingIssues |  |


<a id="emergingIssuesGet"></a>
# **emergingIssuesGet**
> EmergingIssuesGetResult emergingIssuesGet(issueName, apiVersion)



Gets Azure services&#39; emerging issues.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmergingIssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EmergingIssuesApi apiInstance = new EmergingIssuesApi(defaultClient);
    String issueName = "default"; // String | The name of the emerging issue.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      EmergingIssuesGetResult result = apiInstance.emergingIssuesGet(issueName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmergingIssuesApi#emergingIssuesGet");
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
| **issueName** | **String**| The name of the emerging issue. | [enum: default] |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**EmergingIssuesGetResult**](EmergingIssuesGetResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The body contains properties of azure emerging issues, which includes a list of status banner and status active events. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="emergingIssuesList"></a>
# **emergingIssuesList**
> EmergingIssueListResult emergingIssuesList(apiVersion)



Lists Azure services&#39; emerging issues.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmergingIssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EmergingIssuesApi apiInstance = new EmergingIssuesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      EmergingIssueListResult result = apiInstance.emergingIssuesList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmergingIssuesApi#emergingIssuesList");
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
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**EmergingIssueListResult**](EmergingIssueListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The body contains a list of azure emerging issues. |  -  |
| **0** | DefaultErrorResponse |  -  |

