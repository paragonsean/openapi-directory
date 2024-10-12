# SearchApi

All URIs are relative to *http://uebermaps.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mapsSearchGet**](SearchApi.md#mapsSearchGet) | **GET** /maps/search | Search maps |
| [**spotsSearchGet**](SearchApi.md#spotsSearchGet) | **GET** /spots/search | Search spots |
| [**usersSearchGet**](SearchApi.md#usersSearchGet) | **GET** /users/search | Search users |


<a id="mapsSearchGet"></a>
# **mapsSearchGet**
> Map mapsSearchGet(q, d, lat, lon)

Search maps

Search maps

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String q = "q_example"; // String | Query
    Integer d = 56; // Integer | Distance. Diameter of search radius in meter (default: 2000 meter)
    BigDecimal lat = new BigDecimal(78); // BigDecimal | Latitude for search radius (default distance: 2000 meter)
    BigDecimal lon = new BigDecimal(78); // BigDecimal | Longitude for search radius (default distance: 2000 meter)
    try {
      Map result = apiInstance.mapsSearchGet(q, d, lat, lon);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#mapsSearchGet");
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
| **q** | **String**| Query | [optional] |
| **d** | **Integer**| Distance. Diameter of search radius in meter (default: 2000 meter) | [optional] |
| **lat** | **BigDecimal**| Latitude for search radius (default distance: 2000 meter) | [optional] |
| **lon** | **BigDecimal**| Longitude for search radius (default distance: 2000 meter) | [optional] |

### Return type

[**Map**](Map.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains map data. |  -  |

<a id="spotsSearchGet"></a>
# **spotsSearchGet**
> Spot spotsSearchGet(q, d, lat, lon)

Search spots

Search spots

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String q = "q_example"; // String | Query
    Integer d = 56; // Integer | Distance. Diameter of search radius in meter (default: 2000 meter)
    BigDecimal lat = new BigDecimal(78); // BigDecimal | Latitude for search radius (2 km)
    BigDecimal lon = new BigDecimal(78); // BigDecimal | Longitude for search radius (2 km)
    try {
      Spot result = apiInstance.spotsSearchGet(q, d, lat, lon);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#spotsSearchGet");
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
| **q** | **String**| Query | [optional] |
| **d** | **Integer**| Distance. Diameter of search radius in meter (default: 2000 meter) | [optional] |
| **lat** | **BigDecimal**| Latitude for search radius (2 km) | [optional] |
| **lon** | **BigDecimal**| Longitude for search radius (2 km) | [optional] |

### Return type

[**Spot**](Spot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains spot data. |  -  |

<a id="usersSearchGet"></a>
# **usersSearchGet**
> User usersSearchGet(q)

Search users

Search users

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String q = "q_example"; // String | Query
    try {
      User result = apiInstance.usersSearchGet(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#usersSearchGet");
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
| **q** | **String**| Query | [optional] |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains users data. |  -  |

