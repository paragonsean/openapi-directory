# OutletsApi

All URIs are relative to *http://timetableapi.ptv.vic.gov.au*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**outletsGetAllOutlets**](OutletsApi.md#outletsGetAllOutlets) | **GET** /v3/outlets | List all ticket outlets |
| [**outletsGetOutletsByGeolocation**](OutletsApi.md#outletsGetOutletsByGeolocation) | **GET** /v3/outlets/location/{latitude},{longitude} | List ticket outlets near a specific location |


<a id="outletsGetAllOutlets"></a>
# **outletsGetAllOutlets**
> V3OutletResponse outletsGetAllOutlets(maxResults, token, devid, signature)

List all ticket outlets

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OutletsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://timetableapi.ptv.vic.gov.au");

    OutletsApi apiInstance = new OutletsApi(defaultClient);
    Integer maxResults = 56; // Integer | Maximum number of results returned (default = 30)
    String token = "token_example"; // String | Please ignore
    String devid = "devid_example"; // String | Your developer id
    String signature = "signature_example"; // String | Authentication signature for request
    try {
      V3OutletResponse result = apiInstance.outletsGetAllOutlets(maxResults, token, devid, signature);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OutletsApi#outletsGetAllOutlets");
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
| **maxResults** | **Integer**| Maximum number of results returned (default &#x3D; 30) | [optional] |
| **token** | **String**| Please ignore | [optional] |
| **devid** | **String**| Your developer id | [optional] |
| **signature** | **String**| Authentication signature for request | [optional] |

### Return type

[**V3OutletResponse**](V3OutletResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ticket outlets. |  -  |
| **400** | Invalid Request |  -  |
| **403** | Access Denied |  -  |

<a id="outletsGetOutletsByGeolocation"></a>
# **outletsGetOutletsByGeolocation**
> V3OutletGeolocationResponse outletsGetOutletsByGeolocation(latitude, longitude, maxDistance, maxResults, token, devid, signature)

List ticket outlets near a specific location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OutletsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://timetableapi.ptv.vic.gov.au");

    OutletsApi apiInstance = new OutletsApi(defaultClient);
    Float latitude = 3.4F; // Float | Geographic coordinate of latitude
    Float longitude = 3.4F; // Float | Geographic coordinate of longitude
    Double maxDistance = 3.4D; // Double | Filter by maximum distance (in metres) from location specified via latitude and longitude parameters (default = 300)
    Integer maxResults = 56; // Integer | Maximum number of results returned (default = 30)
    String token = "token_example"; // String | Please ignore
    String devid = "devid_example"; // String | Your developer id
    String signature = "signature_example"; // String | Authentication signature for request
    try {
      V3OutletGeolocationResponse result = apiInstance.outletsGetOutletsByGeolocation(latitude, longitude, maxDistance, maxResults, token, devid, signature);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OutletsApi#outletsGetOutletsByGeolocation");
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
| **latitude** | **Float**| Geographic coordinate of latitude | |
| **longitude** | **Float**| Geographic coordinate of longitude | |
| **maxDistance** | **Double**| Filter by maximum distance (in metres) from location specified via latitude and longitude parameters (default &#x3D; 300) | [optional] |
| **maxResults** | **Integer**| Maximum number of results returned (default &#x3D; 30) | [optional] |
| **token** | **String**| Please ignore | [optional] |
| **devid** | **String**| Your developer id | [optional] |
| **signature** | **String**| Authentication signature for request | [optional] |

### Return type

[**V3OutletGeolocationResponse**](V3OutletGeolocationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ticket outlets near the specified location. |  -  |
| **400** | Invalid Request |  -  |
| **403** | Access Denied |  -  |

