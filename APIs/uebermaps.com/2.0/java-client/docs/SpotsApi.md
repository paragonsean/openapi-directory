# SpotsApi

All URIs are relative to *http://uebermaps.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mapsIdSpotsGet**](SpotsApi.md#mapsIdSpotsGet) | **GET** /maps/{id}/spots | List spots for a given map |
| [**mapsIdSpotsPost**](SpotsApi.md#mapsIdSpotsPost) | **POST** /maps/{id}/spots | Create spot |
| [**mapsMapIdSpotsIdGet**](SpotsApi.md#mapsMapIdSpotsIdGet) | **GET** /maps/{map_id}/spots/{id} | Get spot |
| [**spotsGet**](SpotsApi.md#spotsGet) | **GET** /spots | List your own spots |
| [**spotsIdDelete**](SpotsApi.md#spotsIdDelete) | **DELETE** /spots/{id} | Delete spot |
| [**spotsIdPatch**](SpotsApi.md#spotsIdPatch) | **PATCH** /spots/{id} | Update spot |


<a id="mapsIdSpotsGet"></a>
# **mapsIdSpotsGet**
> List&lt;Spot&gt; mapsIdSpotsGet(id, order)

List spots for a given map

List spots for a given map.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    SpotsApi apiInstance = new SpotsApi(defaultClient);
    Integer id = 56; // Integer | Id of map
    String order = "created_at_asc"; // String | Order of spots
    try {
      List<Spot> result = apiInstance.mapsIdSpotsGet(id, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpotsApi#mapsIdSpotsGet");
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
| **order** | **String**| Order of spots | [optional] [enum: created_at_asc, created_at_desc, updated_at_asc, updated_at_desc, title_asc, title_desc] |

### Return type

[**List&lt;Spot&gt;**](Spot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains list of spots. |  -  |

<a id="mapsIdSpotsPost"></a>
# **mapsIdSpotsPost**
> Spot mapsIdSpotsPost(id, spot)

Create spot

Create spot. Wrap parameters in [spot]. To add a spot picture pass a base64 encoded string to [spot][picture].

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    SpotsApi apiInstance = new SpotsApi(defaultClient);
    Integer id = 56; // Integer | Id of map
    SpotEditable spot = new SpotEditable(); // SpotEditable | spot attributes
    try {
      Spot result = apiInstance.mapsIdSpotsPost(id, spot);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpotsApi#mapsIdSpotsPost");
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
| **spot** | [**SpotEditable**](SpotEditable.md)| spot attributes | |

### Return type

[**Spot**](Spot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains spot data |  -  |

<a id="mapsMapIdSpotsIdGet"></a>
# **mapsMapIdSpotsIdGet**
> Spot mapsMapIdSpotsIdGet(id, mapId)

Get spot

Get basic information about a spot

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    SpotsApi apiInstance = new SpotsApi(defaultClient);
    Integer id = 56; // Integer | Id of spot
    Integer mapId = 56; // Integer | Id of map
    try {
      Spot result = apiInstance.mapsMapIdSpotsIdGet(id, mapId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpotsApi#mapsMapIdSpotsIdGet");
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
| **id** | **Integer**| Id of spot | |
| **mapId** | **Integer**| Id of map | |

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
| **200** | Contains spot data |  -  |

<a id="spotsGet"></a>
# **spotsGet**
> List&lt;Spot&gt; spotsGet(order)

List your own spots

List your own spots.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    SpotsApi apiInstance = new SpotsApi(defaultClient);
    String order = "created_at_asc"; // String | Order of spots
    try {
      List<Spot> result = apiInstance.spotsGet(order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpotsApi#spotsGet");
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
| **order** | **String**| Order of spots | [optional] [enum: created_at_asc, created_at_desc, updated_at_asc, updated_at_desc, title_asc, title_desc] |

### Return type

[**List&lt;Spot&gt;**](Spot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains list of spots. |  -  |

<a id="spotsIdDelete"></a>
# **spotsIdDelete**
> Spot spotsIdDelete(id)

Delete spot

Delete spot.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    SpotsApi apiInstance = new SpotsApi(defaultClient);
    Integer id = 56; // Integer | spot id
    try {
      Spot result = apiInstance.spotsIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpotsApi#spotsIdDelete");
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
| **id** | **Integer**| spot id | |

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
| **200** | Contains deleted spot. |  -  |

<a id="spotsIdPatch"></a>
# **spotsIdPatch**
> Spot spotsIdPatch(id, spot)

Update spot

Update spot. Wrap parameters in [spot]. To update the spot picture pass a base64 encoded string to [spot][picture].

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    SpotsApi apiInstance = new SpotsApi(defaultClient);
    Integer id = 56; // Integer | spot id
    SpotEditable spot = new SpotEditable(); // SpotEditable | spot attributes
    try {
      Spot result = apiInstance.spotsIdPatch(id, spot);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpotsApi#spotsIdPatch");
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
| **id** | **Integer**| spot id | |
| **spot** | [**SpotEditable**](SpotEditable.md)| spot attributes | [optional] |

### Return type

[**Spot**](Spot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains spot data |  -  |

