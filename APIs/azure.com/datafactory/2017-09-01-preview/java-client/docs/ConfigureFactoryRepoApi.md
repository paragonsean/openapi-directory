# ConfigureFactoryRepoApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**factoriesConfigureFactoryRepo**](ConfigureFactoryRepoApi.md#factoriesConfigureFactoryRepo) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DataFactory/locations/{locationId}/configureFactoryRepo |  |


<a id="factoriesConfigureFactoryRepo"></a>
# **factoriesConfigureFactoryRepo**
> Factory factoriesConfigureFactoryRepo(subscriptionId, locationId, apiVersion, factoryRepoUpdate)



Updates a factory&#39;s repo information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigureFactoryRepoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConfigureFactoryRepoApi apiInstance = new ConfigureFactoryRepoApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String locationId = "locationId_example"; // String | The location identifier.
    String apiVersion = "apiVersion_example"; // String | The API version.
    FactoryRepoUpdate factoryRepoUpdate = new FactoryRepoUpdate(); // FactoryRepoUpdate | Update factory repo request definition.
    try {
      Factory result = apiInstance.factoriesConfigureFactoryRepo(subscriptionId, locationId, apiVersion, factoryRepoUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigureFactoryRepoApi#factoriesConfigureFactoryRepo");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **locationId** | **String**| The location identifier. | |
| **apiVersion** | **String**| The API version. | |
| **factoryRepoUpdate** | [**FactoryRepoUpdate**](FactoryRepoUpdate.md)| Update factory repo request definition. | |

### Return type

[**Factory**](Factory.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

