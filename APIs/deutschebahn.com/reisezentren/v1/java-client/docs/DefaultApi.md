# DefaultApi

All URIs are relative to *https://api.deutschebahn.com/reisezentren/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reisezentrenGet**](DefaultApi.md#reisezentrenGet) | **GET** /reisezentren | Get all station infos |
| [**reisezentrenIdGet**](DefaultApi.md#reisezentrenIdGet) | **GET** /reisezentren/{id} | Get information about a specific station |
| [**reisezentrenLocLatLonDistGet**](DefaultApi.md#reisezentrenLocLatLonDistGet) | **GET** /reisezentren/loc/{lat}/{lon}/{dist} | Get stations in a given radius |
| [**reisezentrenLocLatLonGet**](DefaultApi.md#reisezentrenLocLatLonGet) | **GET** /reisezentren/loc/{lat}/{lon} | Get information about a station near a location |


<a id="reisezentrenGet"></a>
# **reisezentrenGet**
> List&lt;TravelCenter&gt; reisezentrenGet(name)

Get all station infos

Get all station infos

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.deutschebahn.com/reisezentren/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | A station name or part of it
    try {
      List<TravelCenter> result = apiInstance.reisezentrenGet(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#reisezentrenGet");
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
| **name** | **String**| A station name or part of it | [optional] |

### Return type

[**List&lt;TravelCenter&gt;**](TravelCenter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List has been created |  -  |
| **404** | No travel centers could be found matching the given name |  -  |
| **416** | Filtering required - specify a name fragment of at least 3 characters |  -  |

<a id="reisezentrenIdGet"></a>
# **reisezentrenIdGet**
> TravelCenter reisezentrenIdGet(id)

Get information about a specific station

Get information about a specific station

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.deutschebahn.com/reisezentren/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Station id
    try {
      TravelCenter result = apiInstance.reisezentrenIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#reisezentrenIdGet");
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
| **id** | **String**| Station id | |

### Return type

[**TravelCenter**](TravelCenter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The travel center was found |  -  |
| **404** | No travel center found |  -  |

<a id="reisezentrenLocLatLonDistGet"></a>
# **reisezentrenLocLatLonDistGet**
> TravelCenter reisezentrenLocLatLonDistGet(lat, lon, dist)

Get stations in a given radius

Get stations in a given radius

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.deutschebahn.com/reisezentren/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Float lat = 3.4F; // Float | Latitude
    Float lon = 3.4F; // Float | Longitude
    Float dist = 3.4F; // Float | Radius
    try {
      TravelCenter result = apiInstance.reisezentrenLocLatLonDistGet(lat, lon, dist);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#reisezentrenLocLatLonDistGet");
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
| **lat** | **Float**| Latitude | |
| **lon** | **Float**| Longitude | |
| **dist** | **Float**| Radius | |

### Return type

[**TravelCenter**](TravelCenter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A station was found |  -  |

<a id="reisezentrenLocLatLonGet"></a>
# **reisezentrenLocLatLonGet**
> TravelCenter reisezentrenLocLatLonGet(lat, lon)

Get information about a station near a location

Get information about a station near a location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.deutschebahn.com/reisezentren/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Float lat = 3.4F; // Float | Latitude
    Float lon = 3.4F; // Float | Longitude
    try {
      TravelCenter result = apiInstance.reisezentrenLocLatLonGet(lat, lon);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#reisezentrenLocLatLonGet");
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
| **lat** | **Float**| Latitude | |
| **lon** | **Float**| Longitude | |

### Return type

[**TravelCenter**](TravelCenter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A station was found |  -  |

