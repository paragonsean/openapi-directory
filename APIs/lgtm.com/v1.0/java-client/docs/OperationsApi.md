# OperationsApi

All URIs are relative to *https://lgtm.com/api/v1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOperation**](OperationsApi.md#getOperation) | **GET** /operations/{operation-id} | Get operation status |


<a id="getOperation"></a>
# **getOperation**
> Operation getOperation(operationId)

Get operation status

Track progress of a long-running operation using the operations identifier returned when you  created the operation. For example, by triggering the analysis of a commit, or the code review of a patch. For both LGTM.com and LGTM Enterprise, you must include an access token with the &#x60;operations:read&#x60; scope. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://lgtm.com/api/v1.0");
    
    // Configure HTTP bearer authorization: access-token
    HttpBearerAuth access-token = (HttpBearerAuth) defaultClient.getAuthentication("access-token");
    access-token.setBearerToken("BEARER TOKEN");

    OperationsApi apiInstance = new OperationsApi(defaultClient);
    Long operationId = 56L; // Long | The operation identifier returned on creating the task.
    try {
      Operation result = apiInstance.getOperation(operationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationsApi#getOperation");
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
| **operationId** | **Long**| The operation identifier returned on creating the task. | |

### Return type

[**Operation**](Operation.md)

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. Requested data returned. |  -  |

