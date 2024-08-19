# SoftwarePlanApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**softwarePlanRegister**](SoftwarePlanApi.md#softwarePlanRegister) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.SoftwarePlan/register |  |


<a id="softwarePlanRegister"></a>
# **softwarePlanRegister**
> softwarePlanRegister(subscriptionId, apiVersion)



Register to Microsoft.SoftwarePlan resource provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SoftwarePlanApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SoftwarePlanApi apiInstance = new SoftwarePlanApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String apiVersion = "apiVersion_example"; // String | The api-version to be used by the service
    try {
      apiInstance.softwarePlanRegister(subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling SoftwarePlanApi#softwarePlanRegister");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **apiVersion** | **String**| The api-version to be used by the service | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | OK - Microsoft.SoftwarePlan is registered |  -  |
| **0** | Error response describing why the operation failed. |  -  |

