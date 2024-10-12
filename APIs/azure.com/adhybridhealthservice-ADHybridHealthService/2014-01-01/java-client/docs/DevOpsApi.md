# DevOpsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reportsGetDevOps**](DevOpsApi.md#reportsGetDevOps) | **GET** /providers/Microsoft.ADHybridHealthService/reports/DevOps/IsDevOps |  |


<a id="reportsGetDevOps"></a>
# **reportsGetDevOps**
> Result reportsGetDevOps(apiVersion)



Checks if the user is enabled for Dev Ops access.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevOpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DevOpsApi apiInstance = new DevOpsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      Result result = apiInstance.reportsGetDevOps(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevOpsApi#reportsGetDevOps");
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
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

[**Result**](Result.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Indicates if the user is Dev Ops or not. |  -  |

