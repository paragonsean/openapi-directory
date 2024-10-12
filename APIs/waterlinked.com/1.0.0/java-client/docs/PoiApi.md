# PoiApi

All URIs are relative to *http://demo.waterlinked.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**poiCreate**](PoiApi.md#poiCreate) | **POST** /api/v1/poi/ | Create poi |
| [**poiDelete**](PoiApi.md#poiDelete) | **DELETE** /api/v1/poi/{ID} | Delete poi |
| [**poiList**](PoiApi.md#poiList) | **GET** /api/v1/poi/ | List poi |
| [**poiShow**](PoiApi.md#poiShow) | **GET** /api/v1/poi/{ID} | Show poi |
| [**poiUpdate**](PoiApi.md#poiUpdate) | **PATCH** /api/v1/poi/{ID} | Update poi |


<a id="poiCreate"></a>
# **poiCreate**
> poiCreate(payload)

Create poi

Create a new POI

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    PoiApi apiInstance = new PoiApi(defaultClient);
    CreatePoiPayload payload = new CreatePoiPayload(); // CreatePoiPayload | A list of all POI
    try {
      apiInstance.poiCreate(payload);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoiApi#poiCreate");
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
| **payload** | [**CreatePoiPayload**](CreatePoiPayload.md)| A list of all POI | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.goa.error

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Resource created |  * Location - href to created resource <br>  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |

<a id="poiDelete"></a>
# **poiDelete**
> poiDelete(ID)

Delete poi

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    PoiApi apiInstance = new PoiApi(defaultClient);
    Integer ID = 56; // Integer | 
    try {
      apiInstance.poiDelete(ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoiApi#poiDelete");
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
| **ID** | **Integer**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.goa.error

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="poiList"></a>
# **poiList**
> List&lt;WaterlinkedPoi&gt; poiList()

List poi

List all points of interest

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    PoiApi apiInstance = new PoiApi(defaultClient);
    try {
      List<WaterlinkedPoi> result = apiInstance.poiList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoiApi#poiList");
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

[**List&lt;WaterlinkedPoi&gt;**](WaterlinkedPoi.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.waterlinked.poi+json; type=collection

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return list of all POIs |  -  |
| **404** | Not Found |  -  |

<a id="poiShow"></a>
# **poiShow**
> WaterlinkedPoi poiShow(ID)

Show poi

Get a POI

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    PoiApi apiInstance = new PoiApi(defaultClient);
    Integer ID = 56; // Integer | 
    try {
      WaterlinkedPoi result = apiInstance.poiShow(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoiApi#poiShow");
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
| **ID** | **Integer**|  | |

### Return type

[**WaterlinkedPoi**](WaterlinkedPoi.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.waterlinked.poi+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not Found |  -  |

<a id="poiUpdate"></a>
# **poiUpdate**
> poiUpdate(ID, payload)

Update poi

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PoiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    PoiApi apiInstance = new PoiApi(defaultClient);
    Integer ID = 56; // Integer | 
    UpdatePoiPayload payload = new UpdatePoiPayload(); // UpdatePoiPayload | A list of all POI
    try {
      apiInstance.poiUpdate(ID, payload);
    } catch (ApiException e) {
      System.err.println("Exception when calling PoiApi#poiUpdate");
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
| **ID** | **Integer**|  | |
| **payload** | [**UpdatePoiPayload**](UpdatePoiPayload.md)| A list of all POI | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.goa.error

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

