# CheckNameAvailabilityApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkNameAvailability**](CheckNameAvailabilityApi.md#checkNameAvailability) | **POST** /providers/Microsoft.Management/checkNameAvailability |  |


<a id="checkNameAvailability"></a>
# **checkNameAvailability**
> CheckNameAvailabilityResult checkNameAvailability(apiVersion, checkNameAvailabilityRequest)



Checks if the specified management group name is valid and unique

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CheckNameAvailabilityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CheckNameAvailabilityApi apiInstance = new CheckNameAvailabilityApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-01-01-preview.
    CheckNameAvailabilityRequest checkNameAvailabilityRequest = new CheckNameAvailabilityRequest(); // CheckNameAvailabilityRequest | Management group name availability check parameters.
    try {
      CheckNameAvailabilityResult result = apiInstance.checkNameAvailability(apiVersion, checkNameAvailabilityRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CheckNameAvailabilityApi#checkNameAvailability");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-01-01-preview. | |
| **checkNameAvailabilityRequest** | [**CheckNameAvailabilityRequest**](CheckNameAvailabilityRequest.md)| Management group name availability check parameters. | |

### Return type

[**CheckNameAvailabilityResult**](CheckNameAvailabilityResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

