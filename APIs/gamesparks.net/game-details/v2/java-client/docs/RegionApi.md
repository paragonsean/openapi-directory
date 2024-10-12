# RegionApi

All URIs are relative to *http://config2.gamesparks.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getGameRegionOptionsUsingGET**](RegionApi.md#getGameRegionOptionsUsingGET) | **GET** /restv2/game/{gameApiKey}/regions | getGameRegionOptions |
| [**getRegionOptionsUsingGET**](RegionApi.md#getRegionOptionsUsingGET) | **GET** /restv2/game/regions | getRegionOptions |
| [**setGameRegionUsingPOST**](RegionApi.md#setGameRegionUsingPOST) | **POST** /restv2/game/{gameApiKey}/region/{regionCode} | setGameRegion |


<a id="getGameRegionOptionsUsingGET"></a>
# **getGameRegionOptionsUsingGET**
> GameRegionOptionsDTO getGameRegionOptionsUsingGET(gameApiKey)

getGameRegionOptions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    RegionApi apiInstance = new RegionApi(defaultClient);
    String gameApiKey = "gameApiKey_example"; // String | gameApiKey
    try {
      GameRegionOptionsDTO result = apiInstance.getGameRegionOptionsUsingGET(gameApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegionApi#getGameRegionOptionsUsingGET");
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
| **gameApiKey** | **String**| gameApiKey | |

### Return type

[**GameRegionOptionsDTO**](GameRegionOptionsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="getRegionOptionsUsingGET"></a>
# **getRegionOptionsUsingGET**
> GameRegionOptionsDTO getRegionOptionsUsingGET()

getRegionOptions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    RegionApi apiInstance = new RegionApi(defaultClient);
    try {
      GameRegionOptionsDTO result = apiInstance.getRegionOptionsUsingGET();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegionApi#getRegionOptionsUsingGET");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GameRegionOptionsDTO**](GameRegionOptionsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="setGameRegionUsingPOST"></a>
# **setGameRegionUsingPOST**
> RegionResult setGameRegionUsingPOST(gameApiKey, regionCode)

setGameRegion

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    RegionApi apiInstance = new RegionApi(defaultClient);
    String gameApiKey = "gameApiKey_example"; // String | gameApiKey
    String regionCode = "regionCode_example"; // String | regionCode
    try {
      RegionResult result = apiInstance.setGameRegionUsingPOST(gameApiKey, regionCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegionApi#setGameRegionUsingPOST");
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
| **gameApiKey** | **String**| gameApiKey | |
| **regionCode** | **String**| regionCode | |

### Return type

[**RegionResult**](RegionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

