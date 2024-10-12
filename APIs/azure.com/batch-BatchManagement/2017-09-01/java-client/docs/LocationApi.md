# LocationApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**locationGetQuotas**](LocationApi.md#locationGetQuotas) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Batch/locations/{locationName}/quotas |  |


<a id="locationGetQuotas"></a>
# **locationGetQuotas**
> BatchLocationQuota locationGetQuotas(locationName, apiVersion, subscriptionId)



Gets the Batch service quotas for the specified subscription at the given location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LocationApi apiInstance = new LocationApi(defaultClient);
    String locationName = "locationName_example"; // String | The region for which to retrieve Batch service quotas.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    try {
      BatchLocationQuota result = apiInstance.locationGetQuotas(locationName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationApi#locationGetQuotas");
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
| **locationName** | **String**| The region for which to retrieve Batch service quotas. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |

### Return type

[**BatchLocationQuota**](BatchLocationQuota.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful. The response contains the Batch service quotas for the subscription in the specified location. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

