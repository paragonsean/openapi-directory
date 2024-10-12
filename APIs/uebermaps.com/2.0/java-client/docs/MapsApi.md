# MapsApi

All URIs are relative to *http://uebermaps.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mapsGet**](MapsApi.md#mapsGet) | **GET** /maps | List your own maps |
| [**mapsIdDelete**](MapsApi.md#mapsIdDelete) | **DELETE** /maps/{id} | Delete map |
| [**mapsIdGet**](MapsApi.md#mapsIdGet) | **GET** /maps/{id} | Get map |
| [**mapsIdPatch**](MapsApi.md#mapsIdPatch) | **PATCH** /maps/{id} | Update map |
| [**mapsPost**](MapsApi.md#mapsPost) | **POST** /maps | Create map |
| [**usersUserIdMapsGet**](MapsApi.md#usersUserIdMapsGet) | **GET** /users/{user_id}/maps | List maps for a given user |


<a id="mapsGet"></a>
# **mapsGet**
> List&lt;Map&gt; mapsGet()

List your own maps

List your own maps.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MapsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    MapsApi apiInstance = new MapsApi(defaultClient);
    try {
      List<Map> result = apiInstance.mapsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MapsApi#mapsGet");
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

<a id="mapsIdDelete"></a>
# **mapsIdDelete**
> Map mapsIdDelete(id)

Delete map

Delete map.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MapsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    MapsApi apiInstance = new MapsApi(defaultClient);
    Integer id = 56; // Integer | map id
    try {
      Map result = apiInstance.mapsIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MapsApi#mapsIdDelete");
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
| **id** | **Integer**| map id | |

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
| **200** | Contains deleted map. |  -  |

<a id="mapsIdGet"></a>
# **mapsIdGet**
> MapWithRelation mapsIdGet(id)

Get map

Get basic information about a map

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MapsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    MapsApi apiInstance = new MapsApi(defaultClient);
    Integer id = 56; // Integer | Id of map
    try {
      MapWithRelation result = apiInstance.mapsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MapsApi#mapsIdGet");
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
| **id** | **Integer**| Id of map | |

### Return type

[**MapWithRelation**](MapWithRelation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains map data, map settings and your relation to this map |  -  |

<a id="mapsIdPatch"></a>
# **mapsIdPatch**
> Map mapsIdPatch(id, map)

Update map

Update map. Wrap map parameters in [map]. To update the map header picture pass a base64 encoded string to [map][picture].

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MapsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    MapsApi apiInstance = new MapsApi(defaultClient);
    Integer id = 56; // Integer | map id
    MapEditable map = new MapEditable(); // MapEditable | map settings attributes
    try {
      Map result = apiInstance.mapsIdPatch(id, map);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MapsApi#mapsIdPatch");
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
| **id** | **Integer**| map id | |
| **map** | [**MapEditable**](MapEditable.md)| map settings attributes | [optional] |

### Return type

[**Map**](Map.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains map data, map settings and your relation to this map |  -  |

<a id="mapsPost"></a>
# **mapsPost**
> Map mapsPost(map)

Create map

Create map. Wrap map parameters in [map]. To add a map header picture pass a base64 encoded string to [map][picture].

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MapsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    MapsApi apiInstance = new MapsApi(defaultClient);
    MapEditable map = new MapEditable(); // MapEditable | map attributes
    try {
      Map result = apiInstance.mapsPost(map);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MapsApi#mapsPost");
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
| **map** | [**MapEditable**](MapEditable.md)| map attributes | [optional] |

### Return type

[**Map**](Map.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains map data, map settings and your relation to this map |  -  |

<a id="usersUserIdMapsGet"></a>
# **usersUserIdMapsGet**
> List&lt;Map&gt; usersUserIdMapsGet(userId)

List maps for a given user

List maps for a given user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MapsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    MapsApi apiInstance = new MapsApi(defaultClient);
    Integer userId = 56; // Integer | Id of user
    try {
      List<Map> result = apiInstance.usersUserIdMapsGet(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MapsApi#usersUserIdMapsGet");
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
| **userId** | **Integer**| Id of user | |

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

