# ProviderOperationsMetadataApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**providerOperationsMetadataGet**](ProviderOperationsMetadataApi.md#providerOperationsMetadataGet) | **GET** /providers/Microsoft.Authorization/providerOperations/{resourceProviderNamespace} |  |
| [**providerOperationsMetadataList**](ProviderOperationsMetadataApi.md#providerOperationsMetadataList) | **GET** /providers/Microsoft.Authorization/providerOperations |  |


<a id="providerOperationsMetadataGet"></a>
# **providerOperationsMetadataGet**
> ProviderOperationsMetadata providerOperationsMetadataGet(resourceProviderNamespace, apiVersion, $expand)



Gets provider operations metadata for the specified resource provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProviderOperationsMetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProviderOperationsMetadataApi apiInstance = new ProviderOperationsMetadataApi(defaultClient);
    String resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String $expand = "resourceTypes"; // String | Specifies whether to expand the values.
    try {
      ProviderOperationsMetadata result = apiInstance.providerOperationsMetadataGet(resourceProviderNamespace, apiVersion, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProviderOperationsMetadataApi#providerOperationsMetadataGet");
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
| **resourceProviderNamespace** | **String**| The namespace of the resource provider. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **$expand** | **String**| Specifies whether to expand the values. | [optional] [default to resourceTypes] |

### Return type

[**ProviderOperationsMetadata**](ProviderOperationsMetadata.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns the operations metadata. |  -  |

<a id="providerOperationsMetadataList"></a>
# **providerOperationsMetadataList**
> ProviderOperationsMetadataListResult providerOperationsMetadataList(apiVersion, $expand)



Gets provider operations metadata for all resource providers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProviderOperationsMetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProviderOperationsMetadataApi apiInstance = new ProviderOperationsMetadataApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String $expand = "resourceTypes"; // String | Specifies whether to expand the values.
    try {
      ProviderOperationsMetadataListResult result = apiInstance.providerOperationsMetadataList(apiVersion, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProviderOperationsMetadataApi#providerOperationsMetadataList");
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
| **apiVersion** | **String**| The API version to use for this operation. | |
| **$expand** | **String**| Specifies whether to expand the values. | [optional] [default to resourceTypes] |

### Return type

[**ProviderOperationsMetadataListResult**](ProviderOperationsMetadataListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of the operations metadata. |  -  |

