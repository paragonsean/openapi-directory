# ConfigurationsApi

All URIs are relative to *http://api.edrv.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getConfiguration**](ConfigurationsApi.md#getConfiguration) | **GET** /v1/configurations/{id} |  |
| [**getConfigurations**](ConfigurationsApi.md#getConfigurations) | **GET** /v1/configurations |  |
| [**postConfigurations**](ConfigurationsApi.md#postConfigurations) | **POST** /v1/configurations |  |


<a id="getConfiguration"></a>
# **getConfiguration**
> getConfiguration(id)



Get one Configuration data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ConfigurationsApi apiInstance = new ConfigurationsApi(defaultClient);
    String id = "id_example"; // String | ID of Configuration that needs to be fetched
    try {
      apiInstance.getConfiguration(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationsApi#getConfiguration");
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
| **id** | **String**| ID of Configuration that needs to be fetched | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getConfigurations"></a>
# **getConfigurations**
> getConfigurations(paginateLimit, paginatePage, paginateEnabled, sortBy, sortOrder, createdAt$gte, createdAt$lte, updatedAt$gte, updatedAt$lte)



Get Configurations data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ConfigurationsApi apiInstance = new ConfigurationsApi(defaultClient);
    Integer paginateLimit = 20; // Integer | Number of results per page
    String paginatePage = "paginatePage_example"; // String | The queried page index
    Boolean paginateEnabled = true; // Boolean | Enable pagination
    String sortBy = "createdAt"; // String | Sort data by this key
    String sortOrder = "desc"; // String | asc to sort ascending (default is desc - descending)
    OffsetDateTime createdAt$gte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    OffsetDateTime createdAt$lte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    OffsetDateTime updatedAt$gte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    OffsetDateTime updatedAt$lte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    try {
      apiInstance.getConfigurations(paginateLimit, paginatePage, paginateEnabled, sortBy, sortOrder, createdAt$gte, createdAt$lte, updatedAt$gte, updatedAt$lte);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationsApi#getConfigurations");
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
| **paginateLimit** | **Integer**| Number of results per page | [optional] [default to 20] |
| **paginatePage** | **String**| The queried page index | [optional] |
| **paginateEnabled** | **Boolean**| Enable pagination | [optional] [default to true] |
| **sortBy** | **String**| Sort data by this key | [optional] [default to createdAt] |
| **sortOrder** | **String**| asc to sort ascending (default is desc - descending) | [optional] [default to desc] [enum: desc, asc] |
| **createdAt$gte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **createdAt$lte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **updatedAt$gte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **updatedAt$lte** | **OffsetDateTime**| Date as ISO String | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="postConfigurations"></a>
# **postConfigurations**
> PatchChargeStation200Response postConfigurations(postConfigurationsRequest)



Create connector with parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ConfigurationsApi apiInstance = new ConfigurationsApi(defaultClient);
    PostConfigurationsRequest postConfigurationsRequest = new PostConfigurationsRequest(); // PostConfigurationsRequest | Include Configuration properties to create here
    try {
      PatchChargeStation200Response result = apiInstance.postConfigurations(postConfigurationsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationsApi#postConfigurations");
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
| **postConfigurationsRequest** | [**PostConfigurationsRequest**](PostConfigurationsRequest.md)| Include Configuration properties to create here | |

### Return type

[**PatchChargeStation200Response**](PatchChargeStation200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | A successful response |  -  |
| **400** | A failure response |  -  |

