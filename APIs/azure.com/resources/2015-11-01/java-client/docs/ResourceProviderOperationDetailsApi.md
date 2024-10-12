# ResourceProviderOperationDetailsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resourceProviderOperationDetailsList**](ResourceProviderOperationDetailsApi.md#resourceProviderOperationDetailsList) | **GET** /providers/{resourceProviderNamespace}/operations |  |


<a id="resourceProviderOperationDetailsList"></a>
# **resourceProviderOperationDetailsList**
> ResourceProviderOperationDetailListResult resourceProviderOperationDetailsList(resourceProviderNamespace, apiVersion)



Gets a list of resource providers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceProviderOperationDetailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceProviderOperationDetailsApi apiInstance = new ResourceProviderOperationDetailsApi(defaultClient);
    String resourceProviderNamespace = "resourceProviderNamespace_example"; // String | Resource identity.
    String apiVersion = "apiVersion_example"; // String | 
    try {
      ResourceProviderOperationDetailListResult result = apiInstance.resourceProviderOperationDetailsList(resourceProviderNamespace, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceProviderOperationDetailsApi#resourceProviderOperationDetailsList");
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
| **resourceProviderNamespace** | **String**| Resource identity. | |
| **apiVersion** | **String**|  | |

### Return type

[**ResourceProviderOperationDetailListResult**](ResourceProviderOperationDetailListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **204** |  |  -  |

