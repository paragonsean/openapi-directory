# CheckNameAvailabilityWithSubscriptionApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkNameAvailabilityWithSubscription**](CheckNameAvailabilityWithSubscriptionApi.md#checkNameAvailabilityWithSubscription) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Cdn/checkNameAvailability |  |


<a id="checkNameAvailabilityWithSubscription"></a>
# **checkNameAvailabilityWithSubscription**
> CheckNameAvailabilityOutput checkNameAvailabilityWithSubscription(subscriptionId, apiVersion, checkNameAvailabilityInput)



Check the availability of a resource name. This is needed for resources where name is globally unique, such as a CDN endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CheckNameAvailabilityWithSubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CheckNameAvailabilityWithSubscriptionApi apiInstance = new CheckNameAvailabilityWithSubscriptionApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    CheckNameAvailabilityInput checkNameAvailabilityInput = new CheckNameAvailabilityInput(); // CheckNameAvailabilityInput | Input to check.
    try {
      CheckNameAvailabilityOutput result = apiInstance.checkNameAvailabilityWithSubscription(subscriptionId, apiVersion, checkNameAvailabilityInput);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CheckNameAvailabilityWithSubscriptionApi#checkNameAvailabilityWithSubscription");
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
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |
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
| **200** | OK. The request has succeeded. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

