# MetadataApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**recommendationMetadataGet**](MetadataApi.md#recommendationMetadataGet) | **GET** /providers/Microsoft.Advisor/metadata/{name} | Gets the metadata entity. |
| [**recommendationMetadataList**](MetadataApi.md#recommendationMetadataList) | **GET** /providers/Microsoft.Advisor/metadata | Gets the list of metadata entities. |


<a id="recommendationMetadataGet"></a>
# **recommendationMetadataGet**
> MetadataEntity recommendationMetadataGet(name, apiVersion)

Gets the metadata entity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    String name = "name_example"; // String | Name of metadata entity.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      MetadataEntity result = apiInstance.recommendationMetadataGet(name, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#recommendationMetadataGet");
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
| **name** | **String**| Name of metadata entity. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

[**MetadataEntity**](MetadataEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Successfully retrieved metadata entities |  -  |
| **404** | Client sent unknown metadata name |  -  |

<a id="recommendationMetadataList"></a>
# **recommendationMetadataList**
> MetadataEntityListResult recommendationMetadataList(apiVersion)

Gets the list of metadata entities.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      MetadataEntityListResult result = apiInstance.recommendationMetadataList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#recommendationMetadataList");
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
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

[**MetadataEntityListResult**](MetadataEntityListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Successfully retrieved metadata entities |  -  |

