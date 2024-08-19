# CheckNameAvailabilityApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**nameAvailabilityCheckNameAvailability**](CheckNameAvailabilityApi.md#nameAvailabilityCheckNameAvailability) | **POST** /providers/Microsoft.Cdn/checkNameAvailability | Check the availability of a resource name without creating the resource. This is needed for resources where name is globally unique, such as a CDN endpoint. |


<a id="nameAvailabilityCheckNameAvailability"></a>
# **nameAvailabilityCheckNameAvailability**
> CheckNameAvailabilityOutput nameAvailabilityCheckNameAvailability(apiVersion, checkNameAvailabilityInput)

Check the availability of a resource name without creating the resource. This is needed for resources where name is globally unique, such as a CDN endpoint.

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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    CheckNameAvailabilityInput checkNameAvailabilityInput = new CheckNameAvailabilityInput(); // CheckNameAvailabilityInput | Input to check.
    try {
      CheckNameAvailabilityOutput result = apiInstance.nameAvailabilityCheckNameAvailability(apiVersion, checkNameAvailabilityInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CheckNameAvailabilityApi#nameAvailabilityCheckNameAvailability");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |
| **checkNameAvailabilityInput** | [**CheckNameAvailabilityInput**](CheckNameAvailabilityInput.md)| Input to check. | |

### Return type

[**CheckNameAvailabilityOutput**](CheckNameAvailabilityOutput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

