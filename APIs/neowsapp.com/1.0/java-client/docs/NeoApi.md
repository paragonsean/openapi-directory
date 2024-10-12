# NeoApi

All URIs are relative to *http://www.neowsapp.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**browseNearEarthObjects**](NeoApi.md#browseNearEarthObjects) | **GET** /rest/v1/neo/browse | Browse the Near Earth Objects service |
| [**retrieveNearEarthObjectById**](NeoApi.md#retrieveNearEarthObjectById) | **GET** /rest/v1/neo/{asteroid_id} | Find Near Earth Objects by id |


<a id="browseNearEarthObjects"></a>
# **browseNearEarthObjects**
> NearEarthObject browseNearEarthObjects(page, size)

Browse the Near Earth Objects service

Retieve a paginated list of Near Earth Objects

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NeoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.neowsapp.com");

    NeoApi apiInstance = new NeoApi(defaultClient);
    Integer page = 0; // Integer | page
    Integer size = 20; // Integer | size
    try {
      NearEarthObject result = apiInstance.browseNearEarthObjects(page, size);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NeoApi#browseNearEarthObjects");
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
| **page** | **Integer**| page | [optional] [default to 0] |
| **size** | **Integer**| size | [optional] [default to 20] |

### Return type

[**NearEarthObject**](NearEarthObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="retrieveNearEarthObjectById"></a>
# **retrieveNearEarthObjectById**
> NearEarthObject retrieveNearEarthObjectById(asteroidId)

Find Near Earth Objects by id

Retrieve a Near Earth Objects with a given id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NeoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.neowsapp.com");

    NeoApi apiInstance = new NeoApi(defaultClient);
    String asteroidId = "asteroidId_example"; // String | ID of Near Earth Object - (ex: 3729835)
    try {
      NearEarthObject result = apiInstance.retrieveNearEarthObjectById(asteroidId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NeoApi#retrieveNearEarthObjectById");
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
| **asteroidId** | **String**| ID of Near Earth Object - (ex: 3729835) | |

### Return type

[**NearEarthObject**](NearEarthObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

