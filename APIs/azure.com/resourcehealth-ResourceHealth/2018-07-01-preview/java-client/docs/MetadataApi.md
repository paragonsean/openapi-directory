# MetadataApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**metadataGet**](MetadataApi.md#metadataGet) | **GET** /providers/Microsoft.ResourceHealth/metadata/{name} | Gets the metadata entity. |
| [**metadataList**](MetadataApi.md#metadataList) | **GET** /providers/Microsoft.ResourceHealth/metadata | Gets the list of metadata entities. |


<a id="metadataGet"></a>
# **metadataGet**
> MetadataEntity metadataGet(name, apiVersion)

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
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      MetadataEntity result = apiInstance.metadataGet(name, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#metadataGet");
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
| **apiVersion** | **String**| Client Api Version. | |

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

<a id="metadataList"></a>
# **metadataList**
> MetadataEntityListResult metadataList(apiVersion)

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
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      MetadataEntityListResult result = apiInstance.metadataList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#metadataList");
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
| **apiVersion** | **String**| Client Api Version. | |

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

