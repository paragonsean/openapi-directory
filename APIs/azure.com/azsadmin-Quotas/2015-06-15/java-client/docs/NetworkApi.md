# NetworkApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quotasCreateOrUpdate**](NetworkApi.md#quotasCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Network.Admin/locations/{location}/quotas/{resourceName} |  |
| [**quotasDelete**](NetworkApi.md#quotasDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Network.Admin/locations/{location}/quotas/{resourceName} |  |


<a id="quotasCreateOrUpdate"></a>
# **quotasCreateOrUpdate**
> Quota quotasCreateOrUpdate(subscriptionId, location, resourceName, apiVersion, quota)



Create or update a quota.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkApi apiInstance = new NetworkApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | Location of the resource.
    String resourceName = "resourceName_example"; // String | Name of the resource.
    String apiVersion = "2015-06-15"; // String | Client API Version.
    Quota quota = new Quota(); // Quota | New network quota to create.
    try {
      Quota result = apiInstance.quotasCreateOrUpdate(subscriptionId, location, resourceName, apiVersion, quota);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkApi#quotasCreateOrUpdate");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **location** | **String**| Location of the resource. | |
| **resourceName** | **String**| Name of the resource. | |
| **apiVersion** | **String**| Client API Version. | [default to 2015-06-15] |
| **quota** | [**Quota**](Quota.md)| New network quota to create. | |

### Return type

[**Quota**](Quota.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |

<a id="quotasDelete"></a>
# **quotasDelete**
> quotasDelete(subscriptionId, location, resourceName, apiVersion)



Delete a quota by name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkApi apiInstance = new NetworkApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | Location of the resource.
    String resourceName = "resourceName_example"; // String | Name of the resource.
    String apiVersion = "2015-06-15"; // String | Client API Version.
    try {
      apiInstance.quotasDelete(subscriptionId, location, resourceName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkApi#quotasDelete");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **location** | **String**| Location of the resource. | |
| **resourceName** | **String**| Name of the resource. | |
| **apiVersion** | **String**| Client API Version. | [default to 2015-06-15] |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **204** | No Content |  -  |

