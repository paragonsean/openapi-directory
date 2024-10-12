# DefaultApi

All URIs are relative to *http://www.ticketmaster.com/publish/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**patchAttraction**](DefaultApi.md#patchAttraction) | **PATCH** /publish/v2/attractions/{id} | Publish a patch on an attraction |
| [**patchEvent**](DefaultApi.md#patchEvent) | **PATCH** /publish/v2/events/{id} | Publish a patch on an event |
| [**patchVenue**](DefaultApi.md#patchVenue) | **PATCH** /publish/v2/venues/{id} | Publish a patch on a venue |
| [**publishAttraction**](DefaultApi.md#publishAttraction) | **POST** /publish/v2/attractions | Publish an attractions |
| [**publishAttractionVideos**](DefaultApi.md#publishAttractionVideos) | **POST** /publish/v2/attractions/{id}/videos | Publish a video on an attraction |
| [**publishEntitlements**](DefaultApi.md#publishEntitlements) | **POST** /publish/v2/entitlements | Publish entitlements on an entity |
| [**publishEvent**](DefaultApi.md#publishEvent) | **POST** /publish/v2/events | Publish an event |
| [**publishEventVideos**](DefaultApi.md#publishEventVideos) | **POST** /publish/v2/events/{id}/videos | Publish a video on an event |
| [**publishExtension**](DefaultApi.md#publishExtension) | **POST** /publish/v2/extensions | Publish extension on an entity |
| [**publishVenue**](DefaultApi.md#publishVenue) | **POST** /publish/v2/venues | Publish a venue |


<a id="patchAttraction"></a>
# **patchAttraction**
> IngestionResult patchAttraction(id, tmPSCorrelationId, augmentationData)

Publish a patch on an attraction

Since 1.0.0

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
    defaultClient.setBasePath("http://www.ticketmaster.com/publish/v2");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the attraction the patch will be applied
    String tmPSCorrelationId = ""; // String | Unique correlation id to be able to trace the request in our system
    AugmentationData augmentationData = new AugmentationData(); // AugmentationData | Patch to apply
    try {
      IngestionResult result = apiInstance.patchAttraction(id, tmPSCorrelationId, augmentationData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#patchAttraction");
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
| **id** | **String**| ID of the attraction the patch will be applied | |
| **tmPSCorrelationId** | **String**| Unique correlation id to be able to trace the request in our system | [default to ] |
| **augmentationData** | [**AugmentationData**](AugmentationData.md)| Patch to apply | |

### Return type

[**IngestionResult**](IngestionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="patchEvent"></a>
# **patchEvent**
> IngestionResult patchEvent(id, tmPSCorrelationId, augmentationData)

Publish a patch on an event

Since 1.0.0

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
    defaultClient.setBasePath("http://www.ticketmaster.com/publish/v2");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the event the patch will be applied
    String tmPSCorrelationId = ""; // String | Unique correlation id to be able to trace the request in our system
    AugmentationData augmentationData = new AugmentationData(); // AugmentationData | Patch to apply
    try {
      IngestionResult result = apiInstance.patchEvent(id, tmPSCorrelationId, augmentationData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#patchEvent");
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
| **id** | **String**| ID of the event the patch will be applied | |
| **tmPSCorrelationId** | **String**| Unique correlation id to be able to trace the request in our system | [default to ] |
| **augmentationData** | [**AugmentationData**](AugmentationData.md)| Patch to apply | |

### Return type

[**IngestionResult**](IngestionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="patchVenue"></a>
# **patchVenue**
> IngestionResult patchVenue(id, tmPSCorrelationId, augmentationData)

Publish a patch on a venue

Since 1.0.0

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
    defaultClient.setBasePath("http://www.ticketmaster.com/publish/v2");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the venue the patch will be applied
    String tmPSCorrelationId = ""; // String | Unique correlation id to be able to trace the request in our system
    AugmentationData augmentationData = new AugmentationData(); // AugmentationData | Patch to apply
    try {
      IngestionResult result = apiInstance.patchVenue(id, tmPSCorrelationId, augmentationData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#patchVenue");
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
| **id** | **String**| ID of the venue the patch will be applied | |
| **tmPSCorrelationId** | **String**| Unique correlation id to be able to trace the request in our system | [default to ] |
| **augmentationData** | [**AugmentationData**](AugmentationData.md)| Patch to apply | |

### Return type

[**IngestionResult**](IngestionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="publishAttraction"></a>
# **publishAttraction**
> IngestionResult publishAttraction(tmPSCorrelationId, attraction)

Publish an attractions

Since 1.0.0

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
    defaultClient.setBasePath("http://www.ticketmaster.com/publish/v2");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String tmPSCorrelationId = ""; // String | Unique correlation id to be able to trace the request in our system
    Attraction attraction = new Attraction(); // Attraction | Attraction
    try {
      IngestionResult result = apiInstance.publishAttraction(tmPSCorrelationId, attraction);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#publishAttraction");
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
| **tmPSCorrelationId** | **String**| Unique correlation id to be able to trace the request in our system | [default to ] |
| **attraction** | [**Attraction**](Attraction.md)| Attraction | |

### Return type

[**IngestionResult**](IngestionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="publishAttractionVideos"></a>
# **publishAttractionVideos**
> IngestionResult publishAttractionVideos(id, tmPSCorrelationId, video)

Publish a video on an attraction

Since 1.0.0

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
    defaultClient.setBasePath("http://www.ticketmaster.com/publish/v2");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the attraction the video is linked to
    String tmPSCorrelationId = ""; // String | Unique correlation id to be able to trace the request in our system
    Video video = new Video(); // Video | Video data
    try {
      IngestionResult result = apiInstance.publishAttractionVideos(id, tmPSCorrelationId, video);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#publishAttractionVideos");
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
| **id** | **String**| ID of the attraction the video is linked to | |
| **tmPSCorrelationId** | **String**| Unique correlation id to be able to trace the request in our system | [default to ] |
| **video** | [**Video**](Video.md)| Video data | |

### Return type

[**IngestionResult**](IngestionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="publishEntitlements"></a>
# **publishEntitlements**
> IngestionResult publishEntitlements(tmPSCorrelationId, entitlement)

Publish entitlements on an entity

Since 2.0.0

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
    defaultClient.setBasePath("http://www.ticketmaster.com/publish/v2");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String tmPSCorrelationId = ""; // String | Unique correlation id to be able to trace the request in our system
    Entitlement entitlement = new Entitlement(); // Entitlement | Entitlements information to add to the entity
    try {
      IngestionResult result = apiInstance.publishEntitlements(tmPSCorrelationId, entitlement);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#publishEntitlements");
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
| **tmPSCorrelationId** | **String**| Unique correlation id to be able to trace the request in our system | [default to ] |
| **entitlement** | [**Entitlement**](Entitlement.md)| Entitlements information to add to the entity | |

### Return type

[**IngestionResult**](IngestionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="publishEvent"></a>
# **publishEvent**
> IngestionResult publishEvent(tmPSCorrelationId, event)

Publish an event

Since 1.0.0

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
    defaultClient.setBasePath("http://www.ticketmaster.com/publish/v2");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String tmPSCorrelationId = ""; // String | Unique correlation id to be able to trace the request in our system
    Event event = new Event(); // Event | Event
    try {
      IngestionResult result = apiInstance.publishEvent(tmPSCorrelationId, event);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#publishEvent");
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
| **tmPSCorrelationId** | **String**| Unique correlation id to be able to trace the request in our system | [default to ] |
| **event** | [**Event**](Event.md)| Event | |

### Return type

[**IngestionResult**](IngestionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="publishEventVideos"></a>
# **publishEventVideos**
> IngestionResult publishEventVideos(id, tmPSCorrelationId, video)

Publish a video on an event

Since 1.0.0

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
    defaultClient.setBasePath("http://www.ticketmaster.com/publish/v2");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | ID of the event the video is linked to
    String tmPSCorrelationId = ""; // String | Unique correlation id to be able to trace the request in our system
    Video video = new Video(); // Video | Video data
    try {
      IngestionResult result = apiInstance.publishEventVideos(id, tmPSCorrelationId, video);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#publishEventVideos");
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
| **id** | **String**| ID of the event the video is linked to | |
| **tmPSCorrelationId** | **String**| Unique correlation id to be able to trace the request in our system | [default to ] |
| **video** | [**Video**](Video.md)| Video data | |

### Return type

[**IngestionResult**](IngestionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="publishExtension"></a>
# **publishExtension**
> IngestionResult publishExtension(tmPSCorrelationId, extensionData)

Publish extension on an entity

Since 1.0.0

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
    defaultClient.setBasePath("http://www.ticketmaster.com/publish/v2");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String tmPSCorrelationId = ""; // String | Unique correlation id to be able to trace the request in our system
    ExtensionData extensionData = new ExtensionData(); // ExtensionData | Extension information to add to the entity
    try {
      IngestionResult result = apiInstance.publishExtension(tmPSCorrelationId, extensionData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#publishExtension");
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
| **tmPSCorrelationId** | **String**| Unique correlation id to be able to trace the request in our system | [default to ] |
| **extensionData** | [**ExtensionData**](ExtensionData.md)| Extension information to add to the entity | |

### Return type

[**IngestionResult**](IngestionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="publishVenue"></a>
# **publishVenue**
> IngestionResult publishVenue(tmPSCorrelationId, venue)

Publish a venue

Since 1.0.0

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
    defaultClient.setBasePath("http://www.ticketmaster.com/publish/v2");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String tmPSCorrelationId = ""; // String | Unique correlation id to be able to trace the request in our system
    Venue venue = new Venue(); // Venue | Venue
    try {
      IngestionResult result = apiInstance.publishVenue(tmPSCorrelationId, venue);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#publishVenue");
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
| **tmPSCorrelationId** | **String**| Unique correlation id to be able to trace the request in our system | [default to ] |
| **venue** | [**Venue**](Venue.md)| Venue | |

### Return type

[**IngestionResult**](IngestionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

