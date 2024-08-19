# PlatformApi

All URIs are relative to *https://api-2445581398133.apicast.io:443/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPlatformCollection**](PlatformApi.md#getPlatformCollection) | **GET** /platform/list | GET for platform |
| [**getPlatformEntity**](PlatformApi.md#getPlatformEntity) | **GET** /platform/{type} | GET for platform |


<a id="getPlatformCollection"></a>
# **getPlatformCollection**
> List&lt;PlatformEntity&gt; getPlatformCollection(X_API2CRM_USER_KEY, pageSize, page, fields, sort)

GET for platform

Returns all platforms from the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlatformApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    PlatformApi apiInstance = new PlatformApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | API2CRM user key
    Integer pageSize = 56; // Integer | Amount of results (default: 25)
    Integer page = 56; // Integer | Page to show (default: 1)
    String fields = "fields_example"; // String | Comma-separated list of fields to include in the response
    String sort = "sort_example"; // String | Specifies ascending or descending sort on existing fields
    try {
      List<PlatformEntity> result = apiInstance.getPlatformCollection(X_API2CRM_USER_KEY, pageSize, page, fields, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlatformApi#getPlatformCollection");
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
| **X_API2CRM_USER_KEY** | **String**| API2CRM user key | [default to e2a6379ab878ae7e58119d4ec842bf9c] |
| **pageSize** | **Integer**| Amount of results (default: 25) | [optional] |
| **page** | **Integer**| Page to show (default: 1) | [optional] |
| **fields** | **String**| Comma-separated list of fields to include in the response | [optional] |
| **sort** | **String**| Specifies ascending or descending sort on existing fields | [optional] |

### Return type

[**List&lt;PlatformEntity&gt;**](PlatformEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not Found |  -  |

<a id="getPlatformEntity"></a>
# **getPlatformEntity**
> PlatformEntity getPlatformEntity(X_API2CRM_USER_KEY, type, fields)

GET for platform

Return platform information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlatformApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    PlatformApi apiInstance = new PlatformApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | API2CRM user key
    String type = "type_example"; // String | Platform type
    String fields = "fields_example"; // String | Comma-separated list of fields to include in the response
    try {
      PlatformEntity result = apiInstance.getPlatformEntity(X_API2CRM_USER_KEY, type, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlatformApi#getPlatformEntity");
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
| **X_API2CRM_USER_KEY** | **String**| API2CRM user key | [default to e2a6379ab878ae7e58119d4ec842bf9c] |
| **type** | **String**| Platform type | |
| **fields** | **String**| Comma-separated list of fields to include in the response | [optional] |

### Return type

[**PlatformEntity**](PlatformEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not Found |  -  |

