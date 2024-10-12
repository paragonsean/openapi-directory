# AreasApi

All URIs are relative to *https://api.deutschebahn.com/flinkster-api-ng/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getArea**](AreasApi.md#getArea) | **GET** /areas/{areaUID} | Get area by UID. |
| [**listAreas**](AreasApi.md#listAreas) | **GET** /areas | List Areas by Criteria. |


<a id="getArea"></a>
# **getArea**
> AreaJO getArea(areaUID, expand)

Get area by UID.

Search for a specific area by UID.

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
    defaultClient.setBasePath("https://api.deutschebahn.com/flinkster-api-ng/v1");

    AreasApi apiInstance = new AreasApi(defaultClient);
    String areaUID = "areaUID_example"; // String | The Area UID 
    String expand = "expand_example"; // String | Expand Provider
    try {
      AreaJO result = apiInstance.getArea(areaUID, expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AreasApi#getArea");
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
| **areaUID** | **String**| The Area UID  | |
| **expand** | **String**| Expand Provider | [optional] |

### Return type

[**AreaJO**](AreaJO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Forbidden If provider is not allowed to display this area. |  -  |
| **404** | Not Found If no area was found for the given UID. |  -  |

<a id="listAreas"></a>
# **listAreas**
> AreaJO listAreas(lat, lon, radius, offset, limit, expand, type, provider, providernetwork)

List Areas by Criteria.

Search for areas (locations of rental objects) by criteria.

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
    defaultClient.setBasePath("https://api.deutschebahn.com/flinkster-api-ng/v1");

    AreasApi apiInstance = new AreasApi(defaultClient);
    Double lat = 3.4D; // Double | 
    Double lon = 3.4D; // Double | 
    Integer radius = 56; // Integer | 
    Integer offset = 56; // Integer | 
    Integer limit = 56; // Integer | 
    String expand = "expand_example"; // String | 
    String type = "type_example"; // String | 
    String provider = "provider_example"; // String | 
    String providernetwork = "providernetwork_example"; // String | 
    try {
      AreaJO result = apiInstance.listAreas(lat, lon, radius, offset, limit, expand, type, provider, providernetwork);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AreasApi#listAreas");
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
| **lat** | **Double**|  | [optional] |
| **lon** | **Double**|  | [optional] |
| **radius** | **Integer**|  | [optional] |
| **offset** | **Integer**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **expand** | **String**|  | [optional] |
| **type** | **String**|  | [optional] |
| **provider** | **String**|  | [optional] |
| **providernetwork** | **String**|  | [optional] |

### Return type

[**AreaJO**](AreaJO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Forbidden If provider is not allowed to display this area. |  -  |
| **404** | Not Found If no area was found for the given UID. |  -  |

