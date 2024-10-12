# RespotsApi

All URIs are relative to *http://uebermaps.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mapsIdRespotsGet**](RespotsApi.md#mapsIdRespotsGet) | **GET** /maps/{id}/respots | List respots of a map |
| [**mapsMapIdSpotsSpotIdRespotDelete**](RespotsApi.md#mapsMapIdSpotsSpotIdRespotDelete) | **DELETE** /maps/{map_id}/spots/{spot_id}/respot | Delete respot from map by spot id |
| [**respotMapsGet**](RespotsApi.md#respotMapsGet) | **GET** /respot_maps | List maps that user can respot to |
| [**respotsIdDelete**](RespotsApi.md#respotsIdDelete) | **DELETE** /respots/{id} | Delete respot |
| [**respotsIdGet**](RespotsApi.md#respotsIdGet) | **GET** /respots/{id} | Get respot |
| [**spotsIdRespotsPost**](RespotsApi.md#spotsIdRespotsPost) | **POST** /spots/{id}/respots | Respot a spot onto a map |


<a id="mapsIdRespotsGet"></a>
# **mapsIdRespotsGet**
> List&lt;Respot&gt; mapsIdRespotsGet(id)

List respots of a map

List respots of a map.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RespotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    RespotsApi apiInstance = new RespotsApi(defaultClient);
    Integer id = 56; // Integer | Map Id
    try {
      List<Respot> result = apiInstance.mapsIdRespotsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RespotsApi#mapsIdRespotsGet");
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
| **id** | **Integer**| Map Id | |

### Return type

[**List&lt;Respot&gt;**](Respot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains list of respots. |  -  |

<a id="mapsMapIdSpotsSpotIdRespotDelete"></a>
# **mapsMapIdSpotsSpotIdRespotDelete**
> Respot mapsMapIdSpotsSpotIdRespotDelete(mapId, spotId)

Delete respot from map by spot id

Delete respot from map by spot id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RespotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    RespotsApi apiInstance = new RespotsApi(defaultClient);
    Integer mapId = 56; // Integer | Map Id
    Integer spotId = 56; // Integer | Spot Id
    try {
      Respot result = apiInstance.mapsMapIdSpotsSpotIdRespotDelete(mapId, spotId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RespotsApi#mapsMapIdSpotsSpotIdRespotDelete");
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
| **mapId** | **Integer**| Map Id | |
| **spotId** | **Integer**| Spot Id | |

### Return type

[**Respot**](Respot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains deleted respot. |  -  |

<a id="respotMapsGet"></a>
# **respotMapsGet**
> List&lt;Map&gt; respotMapsGet()

List maps that user can respot to

List maps that user can respot to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RespotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    RespotsApi apiInstance = new RespotsApi(defaultClient);
    try {
      List<Map> result = apiInstance.respotMapsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RespotsApi#respotMapsGet");
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

[**List&lt;Map&gt;**](Map.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains list of maps. |  -  |

<a id="respotsIdDelete"></a>
# **respotsIdDelete**
> Respot respotsIdDelete(id)

Delete respot

Delete respot.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RespotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    RespotsApi apiInstance = new RespotsApi(defaultClient);
    Integer id = 56; // Integer | Respot Id
    try {
      Respot result = apiInstance.respotsIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RespotsApi#respotsIdDelete");
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
| **id** | **Integer**| Respot Id | |

### Return type

[**Respot**](Respot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains deleted respot. |  -  |

<a id="respotsIdGet"></a>
# **respotsIdGet**
> Respot respotsIdGet(id)

Get respot

Get basic information about a respot

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RespotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    RespotsApi apiInstance = new RespotsApi(defaultClient);
    Integer id = 56; // Integer | Id of respot
    try {
      Respot result = apiInstance.respotsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RespotsApi#respotsIdGet");
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
| **id** | **Integer**| Id of respot | |

### Return type

[**Respot**](Respot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains respot data. |  -  |

<a id="spotsIdRespotsPost"></a>
# **spotsIdRespotsPost**
> Respot spotsIdRespotsPost(id, mapId)

Respot a spot onto a map

Respot a spot onto a map.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RespotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    RespotsApi apiInstance = new RespotsApi(defaultClient);
    Integer id = 56; // Integer | Spot Id
    BigDecimal mapId = new BigDecimal(78); // BigDecimal | Map Id
    try {
      Respot result = apiInstance.spotsIdRespotsPost(id, mapId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RespotsApi#spotsIdRespotsPost");
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
| **id** | **Integer**| Spot Id | |
| **mapId** | **BigDecimal**| Map Id | |

### Return type

[**Respot**](Respot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains respot data. |  -  |

