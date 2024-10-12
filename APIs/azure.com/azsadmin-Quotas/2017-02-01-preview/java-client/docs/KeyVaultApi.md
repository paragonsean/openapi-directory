# KeyVaultApi

All URIs are relative to *https://management.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quotasList**](KeyVaultApi.md#quotasList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.KeyVault.Admin/locations/{location}/quotas |  |


<a id="quotasList"></a>
# **quotasList**
> QuotaList quotasList(subscriptionId, location, apiVersion)



Get a list of all quota objects for KeyVault at a location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeyVaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    KeyVaultApi apiInstance = new KeyVaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | The location of the quota.
    String apiVersion = "2017-02-01-preview"; // String | Client Api Version.
    try {
      QuotaList result = apiInstance.quotasList(subscriptionId, location, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyVaultApi#quotasList");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | |
| **location** | **String**| The location of the quota. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2017-02-01-preview] |

### Return type

[**QuotaList**](QuotaList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

