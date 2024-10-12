# AreasApi

All URIs are relative to *https://webtris.highwaysengland.co.uk/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**areasGet**](AreasApi.md#areasGet) | **GET** /v{version}/areas | Returns list of areas |
| [**vversionAreasAreaIdsGet**](AreasApi.md#vversionAreasAreaIdsGet) | **GET** /v{version}/areas/{area_Ids} | Returns details of selected area |


<a id="areasGet"></a>
# **areasGet**
> AreaResponse areasGet(version)

Returns list of areas

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AreasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://webtris.highwaysengland.co.uk/api");

    AreasApi apiInstance = new AreasApi(defaultClient);
    String version = "version_example"; // String | 
    try {
      AreaResponse result = apiInstance.areasGet(version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AreasApi#areasGet");
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
| **version** | **String**|  | |

### Return type

[**AreaResponse**](AreaResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Bad request |  -  |
| **500** | Internal Server Error |  -  |

<a id="vversionAreasAreaIdsGet"></a>
# **vversionAreasAreaIdsGet**
> AreaResponse vversionAreasAreaIdsGet(areaIds, version)

Returns details of selected area

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AreasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://webtris.highwaysengland.co.uk/api");

    AreasApi apiInstance = new AreasApi(defaultClient);
    String areaIds = "areaIds_example"; // String | 
    String version = "version_example"; // String | 
    try {
      AreaResponse result = apiInstance.vversionAreasAreaIdsGet(areaIds, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AreasApi#vversionAreasAreaIdsGet");
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
| **areaIds** | **String**|  | |
| **version** | **String**|  | |

### Return type

[**AreaResponse**](AreaResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Bad request |  -  |
| **500** | Internal Server Error |  -  |

