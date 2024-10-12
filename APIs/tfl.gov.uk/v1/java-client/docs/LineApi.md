# LineApi

All URIs are relative to *https://api.digital.tfl.gov.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lineArrivals**](LineApi.md#lineArrivals) | **GET** /Line/{ids}/Arrivals/{stopPointId} | Get the list of arrival predictions for given line ids based at the given stop |
| [**lineDisruption**](LineApi.md#lineDisruption) | **GET** /Line/{ids}/Disruption | Get disruptions for the given line ids |
| [**lineDisruptionByMode**](LineApi.md#lineDisruptionByMode) | **GET** /Line/Mode/{modes}/Disruption | Get disruptions for all lines of the given modes. |
| [**lineGet**](LineApi.md#lineGet) | **GET** /Line/{ids} | Gets lines that match the specified line ids. |
| [**lineGetByMode**](LineApi.md#lineGetByMode) | **GET** /Line/Mode/{modes} | Gets lines that serve the given modes. |
| [**lineLineRoutesByIds**](LineApi.md#lineLineRoutesByIds) | **GET** /Line/{ids}/Route | Get all valid routes for given line ids, including the name and id of the originating and terminating stops for each route. |
| [**lineMetaDisruptionCategories**](LineApi.md#lineMetaDisruptionCategories) | **GET** /Line/Meta/DisruptionCategories | Gets a list of valid disruption categories |
| [**lineMetaModes**](LineApi.md#lineMetaModes) | **GET** /Line/Meta/Modes | Gets a list of valid modes |
| [**lineMetaServiceTypes**](LineApi.md#lineMetaServiceTypes) | **GET** /Line/Meta/ServiceTypes | Gets a list of valid ServiceTypes to filter on |
| [**lineMetaSeverity**](LineApi.md#lineMetaSeverity) | **GET** /Line/Meta/Severity | Gets a list of valid severity codes |
| [**lineRoute**](LineApi.md#lineRoute) | **GET** /Line/Route | Get all valid routes for all lines, including the name and id of the originating and terminating stops for each route. |
| [**lineRouteByMode**](LineApi.md#lineRouteByMode) | **GET** /Line/Mode/{modes}/Route | Gets all lines and their valid routes for given modes, including the name and id of the originating and terminating stops for each route |
| [**lineRouteSequence**](LineApi.md#lineRouteSequence) | **GET** /Line/{id}/Route/Sequence/{direction} | Gets all valid routes for given line id, including the sequence of stops on each route. |
| [**lineSearch**](LineApi.md#lineSearch) | **GET** /Line/Search/{query} | Search for lines or routes matching the query string |
| [**lineStatus**](LineApi.md#lineStatus) | **GET** /Line/{ids}/Status/{StartDate}/to/{EndDate} | Gets the line status for given line ids during the provided dates e.g Minor Delays |
| [**lineStatusByIds**](LineApi.md#lineStatusByIds) | **GET** /Line/{ids}/Status | Gets the line status of for given line ids e.g Minor Delays |
| [**lineStatusByMode**](LineApi.md#lineStatusByMode) | **GET** /Line/Mode/{modes}/Status | Gets the line status of for all lines for the given modes |
| [**lineStatusBySeverity**](LineApi.md#lineStatusBySeverity) | **GET** /Line/Status/{severity} | Gets the line status for all lines with a given severity              A list of valid severity codes can be obtained from a call to Line/Meta/Severity |
| [**lineStopPoints**](LineApi.md#lineStopPoints) | **GET** /Line/{id}/StopPoints | Gets a list of the stations that serve the given line id |
| [**lineTimetable**](LineApi.md#lineTimetable) | **GET** /Line/{id}/Timetable/{fromStopPointId} | Gets the timetable for a specified station on the give line |
| [**lineTimetableTo**](LineApi.md#lineTimetableTo) | **GET** /Line/{id}/Timetable/{fromStopPointId}/to/{toStopPointId} | Gets the timetable for a specified station on the give line with specified destination |


<a id="lineArrivals"></a>
# **lineArrivals**
> List&lt;TflApiPresentationEntitiesPrediction&gt; lineArrivals(ids, stopPointId, direction, destinationStationId)

Get the list of arrival predictions for given line ids based at the given stop

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    LineApi apiInstance = new LineApi(defaultClient);
    List<String> ids = Arrays.asList(); // List<String> | A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids.
    String stopPointId = "stopPointId_example"; // String | Optional. Id of stop to get arrival predictions for (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name)
    String direction = "inbound"; // String | Optional. The direction of travel. Can be inbound or outbound or all. If left blank, and destinationStopId is set, will default to all
    String destinationStationId = "destinationStationId_example"; // String | Optional. Id of destination stop
    try {
      List<TflApiPresentationEntitiesPrediction> result = apiInstance.lineArrivals(ids, stopPointId, direction, destinationStationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LineApi#lineArrivals");
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
| **ids** | [**List&lt;String&gt;**](String.md)| A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids. | |
| **stopPointId** | **String**| Optional. Id of stop to get arrival predictions for (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name) | |
| **direction** | **String**| Optional. The direction of travel. Can be inbound or outbound or all. If left blank, and destinationStopId is set, will default to all | [optional] [enum: inbound, outbound, all] |
| **destinationStationId** | **String**| Optional. Id of destination stop | [optional] |

### Return type

[**List&lt;TflApiPresentationEntitiesPrediction&gt;**](TflApiPresentationEntitiesPrediction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="lineDisruption"></a>
# **lineDisruption**
> List&lt;TflApiPresentationEntitiesDisruption&gt; lineDisruption(ids)

Get disruptions for the given line ids

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    LineApi apiInstance = new LineApi(defaultClient);
    List<String> ids = Arrays.asList(); // List<String> | A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids.
    try {
      List<TflApiPresentationEntitiesDisruption> result = apiInstance.lineDisruption(ids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LineApi#lineDisruption");
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
| **ids** | [**List&lt;String&gt;**](String.md)| A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids. | |

### Return type

[**List&lt;TflApiPresentationEntitiesDisruption&gt;**](TflApiPresentationEntitiesDisruption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="lineDisruptionByMode"></a>
# **lineDisruptionByMode**
> List&lt;TflApiPresentationEntitiesDisruption&gt; lineDisruptionByMode(modes)

Get disruptions for all lines of the given modes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    LineApi apiInstance = new LineApi(defaultClient);
    List<String> modes = Arrays.asList(); // List<String> | A comma-separated list of modes e.g. tube,dlr
    try {
      List<TflApiPresentationEntitiesDisruption> result = apiInstance.lineDisruptionByMode(modes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LineApi#lineDisruptionByMode");
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
| **modes** | [**List&lt;String&gt;**](String.md)| A comma-separated list of modes e.g. tube,dlr | |

### Return type

[**List&lt;TflApiPresentationEntitiesDisruption&gt;**](TflApiPresentationEntitiesDisruption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="lineGet"></a>
# **lineGet**
> List&lt;TflApiPresentationEntitiesLine&gt; lineGet(ids)

Gets lines that match the specified line ids.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    LineApi apiInstance = new LineApi(defaultClient);
    List<String> ids = Arrays.asList(); // List<String> | A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids.
    try {
      List<TflApiPresentationEntitiesLine> result = apiInstance.lineGet(ids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LineApi#lineGet");
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
| **ids** | [**List&lt;String&gt;**](String.md)| A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids. | |

### Return type

[**List&lt;TflApiPresentationEntitiesLine&gt;**](TflApiPresentationEntitiesLine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="lineGetByMode"></a>
# **lineGetByMode**
> List&lt;TflApiPresentationEntitiesLine&gt; lineGetByMode(modes)

Gets lines that serve the given modes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    LineApi apiInstance = new LineApi(defaultClient);
    List<String> modes = Arrays.asList(); // List<String> | A comma-separated list of modes e.g. tube,dlr
    try {
      List<TflApiPresentationEntitiesLine> result = apiInstance.lineGetByMode(modes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LineApi#lineGetByMode");
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
| **modes** | [**List&lt;String&gt;**](String.md)| A comma-separated list of modes e.g. tube,dlr | |

### Return type

[**List&lt;TflApiPresentationEntitiesLine&gt;**](TflApiPresentationEntitiesLine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="lineLineRoutesByIds"></a>
# **lineLineRoutesByIds**
> List&lt;TflApiPresentationEntitiesLine&gt; lineLineRoutesByIds(ids, serviceTypes)

Get all valid routes for given line ids, including the name and id of the originating and terminating stops for each route.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    LineApi apiInstance = new LineApi(defaultClient);
    List<String> ids = Arrays.asList(); // List<String> | A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids.
    List<String> serviceTypes = Arrays.asList(); // List<String> | A comma seperated list of service types to filter on. Supported values: Regular, Night. Defaulted to 'Regular' if not specified
    try {
      List<TflApiPresentationEntitiesLine> result = apiInstance.lineLineRoutesByIds(ids, serviceTypes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LineApi#lineLineRoutesByIds");
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
| **ids** | [**List&lt;String&gt;**](String.md)| A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids. | |
| **serviceTypes** | [**List&lt;String&gt;**](String.md)| A comma seperated list of service types to filter on. Supported values: Regular, Night. Defaulted to &#39;Regular&#39; if not specified | [optional] [enum: Regular, Night] |

### Return type

[**List&lt;TflApiPresentationEntitiesLine&gt;**](TflApiPresentationEntitiesLine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="lineMetaDisruptionCategories"></a>
# **lineMetaDisruptionCategories**
> List&lt;String&gt; lineMetaDisruptionCategories()

Gets a list of valid disruption categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    LineApi apiInstance = new LineApi(defaultClient);
    try {
      List<String> result = apiInstance.lineMetaDisruptionCategories();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LineApi#lineMetaDisruptionCategories");
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

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="lineMetaModes"></a>
# **lineMetaModes**
> List&lt;TflApiPresentationEntitiesMode&gt; lineMetaModes()

Gets a list of valid modes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    LineApi apiInstance = new LineApi(defaultClient);
    try {
      List<TflApiPresentationEntitiesMode> result = apiInstance.lineMetaModes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LineApi#lineMetaModes");
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

[**List&lt;TflApiPresentationEntitiesMode&gt;**](TflApiPresentationEntitiesMode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="lineMetaServiceTypes"></a>
# **lineMetaServiceTypes**
> List&lt;String&gt; lineMetaServiceTypes()

Gets a list of valid ServiceTypes to filter on

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    LineApi apiInstance = new LineApi(defaultClient);
    try {
      List<String> result = apiInstance.lineMetaServiceTypes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LineApi#lineMetaServiceTypes");
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

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="lineMetaSeverity"></a>
# **lineMetaSeverity**
> List&lt;TflApiPresentationEntitiesStatusSeverity&gt; lineMetaSeverity()

Gets a list of valid severity codes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    LineApi apiInstance = new LineApi(defaultClient);
    try {
      List<TflApiPresentationEntitiesStatusSeverity> result = apiInstance.lineMetaSeverity();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LineApi#lineMetaSeverity");
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

[**List&lt;TflApiPresentationEntitiesStatusSeverity&gt;**](TflApiPresentationEntitiesStatusSeverity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="lineRoute"></a>
# **lineRoute**
> List&lt;TflApiPresentationEntitiesLine&gt; lineRoute(serviceTypes)

Get all valid routes for all lines, including the name and id of the originating and terminating stops for each route.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    LineApi apiInstance = new LineApi(defaultClient);
    List<String> serviceTypes = Arrays.asList(); // List<String> | A comma seperated list of service types to filter on. Supported values: Regular, Night. Defaulted to 'Regular' if not specified
    try {
      List<TflApiPresentationEntitiesLine> result = apiInstance.lineRoute(serviceTypes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LineApi#lineRoute");
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
| **serviceTypes** | [**List&lt;String&gt;**](String.md)| A comma seperated list of service types to filter on. Supported values: Regular, Night. Defaulted to &#39;Regular&#39; if not specified | [optional] [enum: Regular, Night] |

### Return type

[**List&lt;TflApiPresentationEntitiesLine&gt;**](TflApiPresentationEntitiesLine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="lineRouteByMode"></a>
# **lineRouteByMode**
> List&lt;TflApiPresentationEntitiesLine&gt; lineRouteByMode(modes, serviceTypes)

Gets all lines and their valid routes for given modes, including the name and id of the originating and terminating stops for each route

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    LineApi apiInstance = new LineApi(defaultClient);
    List<String> modes = Arrays.asList(); // List<String> | A comma-separated list of modes e.g. tube,dlr
    List<String> serviceTypes = Arrays.asList(); // List<String> | A comma seperated list of service types to filter on. Supported values: Regular, Night. Defaulted to 'Regular' if not specified
    try {
      List<TflApiPresentationEntitiesLine> result = apiInstance.lineRouteByMode(modes, serviceTypes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LineApi#lineRouteByMode");
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
| **modes** | [**List&lt;String&gt;**](String.md)| A comma-separated list of modes e.g. tube,dlr | |
| **serviceTypes** | [**List&lt;String&gt;**](String.md)| A comma seperated list of service types to filter on. Supported values: Regular, Night. Defaulted to &#39;Regular&#39; if not specified | [optional] [enum: Regular, Night] |

### Return type

[**List&lt;TflApiPresentationEntitiesLine&gt;**](TflApiPresentationEntitiesLine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="lineRouteSequence"></a>
# **lineRouteSequence**
> TflApiPresentationEntitiesRouteSequence lineRouteSequence(id, direction, serviceTypes, excludeCrowding)

Gets all valid routes for given line id, including the sequence of stops on each route.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    LineApi apiInstance = new LineApi(defaultClient);
    String id = "id_example"; // String | A single line id e.g. victoria
    String direction = "inbound"; // String | The direction of travel. Can be inbound or outbound.
    List<String> serviceTypes = Arrays.asList(); // List<String> | A comma seperated list of service types to filter on. Supported values: Regular, Night. Defaulted to 'Regular' if not specified
    Boolean excludeCrowding = true; // Boolean | That excludes crowding from line disruptions. Can be true or false.
    try {
      TflApiPresentationEntitiesRouteSequence result = apiInstance.lineRouteSequence(id, direction, serviceTypes, excludeCrowding);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LineApi#lineRouteSequence");
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
| **id** | **String**| A single line id e.g. victoria | |
| **direction** | **String**| The direction of travel. Can be inbound or outbound. | [enum: inbound, outbound, all] |
| **serviceTypes** | [**List&lt;String&gt;**](String.md)| A comma seperated list of service types to filter on. Supported values: Regular, Night. Defaulted to &#39;Regular&#39; if not specified | [optional] [enum: Regular, Night] |
| **excludeCrowding** | **Boolean**| That excludes crowding from line disruptions. Can be true or false. | [optional] |

### Return type

[**TflApiPresentationEntitiesRouteSequence**](TflApiPresentationEntitiesRouteSequence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="lineSearch"></a>
# **lineSearch**
> TflApiPresentationEntitiesRouteSearchResponse lineSearch(query, modes, serviceTypes)

Search for lines or routes matching the query string

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    LineApi apiInstance = new LineApi(defaultClient);
    String query = "query_example"; // String | Search term e.g victoria
    List<String> modes = Arrays.asList(); // List<String> | Optionally filter by the specified modes
    List<String> serviceTypes = Arrays.asList(); // List<String> | A comma seperated list of service types to filter on. Supported values: Regular, Night. Defaulted to 'Regular' if not specified
    try {
      TflApiPresentationEntitiesRouteSearchResponse result = apiInstance.lineSearch(query, modes, serviceTypes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LineApi#lineSearch");
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
| **query** | **String**| Search term e.g victoria | |
| **modes** | [**List&lt;String&gt;**](String.md)| Optionally filter by the specified modes | [optional] |
| **serviceTypes** | [**List&lt;String&gt;**](String.md)| A comma seperated list of service types to filter on. Supported values: Regular, Night. Defaulted to &#39;Regular&#39; if not specified | [optional] [enum: Regular, Night] |

### Return type

[**TflApiPresentationEntitiesRouteSearchResponse**](TflApiPresentationEntitiesRouteSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="lineStatus"></a>
# **lineStatus**
> List&lt;TflApiPresentationEntitiesLine&gt; lineStatus(ids, startDate, endDate, startDate2, endDate2, detail, dateRangeStartDate, dateRangeEndDate)

Gets the line status for given line ids during the provided dates e.g Minor Delays

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    LineApi apiInstance = new LineApi(defaultClient);
    List<String> ids = Arrays.asList(); // List<String> | A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids.
    String startDate = "startDate_example"; // String | 
    String endDate = "endDate_example"; // String | 
    String startDate2 = "startDate_example"; // String | Automatically added
    String endDate2 = "endDate_example"; // String | Automatically added
    Boolean detail = true; // Boolean | Include details of the disruptions that are causing the line status including the affected stops and routes
    OffsetDateTime dateRangeStartDate = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime dateRangeEndDate = OffsetDateTime.now(); // OffsetDateTime | 
    try {
      List<TflApiPresentationEntitiesLine> result = apiInstance.lineStatus(ids, startDate, endDate, startDate2, endDate2, detail, dateRangeStartDate, dateRangeEndDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LineApi#lineStatus");
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
| **ids** | [**List&lt;String&gt;**](String.md)| A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids. | |
| **startDate** | **String**|  | |
| **endDate** | **String**|  | |
| **startDate2** | **String**| Automatically added | |
| **endDate2** | **String**| Automatically added | |
| **detail** | **Boolean**| Include details of the disruptions that are causing the line status including the affected stops and routes | [optional] |
| **dateRangeStartDate** | **OffsetDateTime**|  | [optional] |
| **dateRangeEndDate** | **OffsetDateTime**|  | [optional] |

### Return type

[**List&lt;TflApiPresentationEntitiesLine&gt;**](TflApiPresentationEntitiesLine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="lineStatusByIds"></a>
# **lineStatusByIds**
> List&lt;TflApiPresentationEntitiesLine&gt; lineStatusByIds(ids, detail)

Gets the line status of for given line ids e.g Minor Delays

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    LineApi apiInstance = new LineApi(defaultClient);
    List<String> ids = Arrays.asList(); // List<String> | A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids.
    Boolean detail = true; // Boolean | Include details of the disruptions that are causing the line status including the affected stops and routes
    try {
      List<TflApiPresentationEntitiesLine> result = apiInstance.lineStatusByIds(ids, detail);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LineApi#lineStatusByIds");
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
| **ids** | [**List&lt;String&gt;**](String.md)| A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids. | |
| **detail** | **Boolean**| Include details of the disruptions that are causing the line status including the affected stops and routes | [optional] |

### Return type

[**List&lt;TflApiPresentationEntitiesLine&gt;**](TflApiPresentationEntitiesLine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="lineStatusByMode"></a>
# **lineStatusByMode**
> List&lt;TflApiPresentationEntitiesLine&gt; lineStatusByMode(modes, detail, severityLevel)

Gets the line status of for all lines for the given modes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    LineApi apiInstance = new LineApi(defaultClient);
    List<String> modes = Arrays.asList(); // List<String> | A comma-separated list of modes to filter by. e.g. tube,dlr
    Boolean detail = true; // Boolean | Include details of the disruptions that are causing the line status including the affected stops and routes
    String severityLevel = "severityLevel_example"; // String | If specified, ensures that only those line status(es) are returned within the lines that have disruptions with the matching severity level.
    try {
      List<TflApiPresentationEntitiesLine> result = apiInstance.lineStatusByMode(modes, detail, severityLevel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LineApi#lineStatusByMode");
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
| **modes** | [**List&lt;String&gt;**](String.md)| A comma-separated list of modes to filter by. e.g. tube,dlr | |
| **detail** | **Boolean**| Include details of the disruptions that are causing the line status including the affected stops and routes | [optional] |
| **severityLevel** | **String**| If specified, ensures that only those line status(es) are returned within the lines that have disruptions with the matching severity level. | [optional] |

### Return type

[**List&lt;TflApiPresentationEntitiesLine&gt;**](TflApiPresentationEntitiesLine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="lineStatusBySeverity"></a>
# **lineStatusBySeverity**
> List&lt;TflApiPresentationEntitiesLine&gt; lineStatusBySeverity(severity)

Gets the line status for all lines with a given severity              A list of valid severity codes can be obtained from a call to Line/Meta/Severity

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    LineApi apiInstance = new LineApi(defaultClient);
    Integer severity = 56; // Integer | The level of severity (eg: a number from 0 to 14)
    try {
      List<TflApiPresentationEntitiesLine> result = apiInstance.lineStatusBySeverity(severity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LineApi#lineStatusBySeverity");
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
| **severity** | **Integer**| The level of severity (eg: a number from 0 to 14) | |

### Return type

[**List&lt;TflApiPresentationEntitiesLine&gt;**](TflApiPresentationEntitiesLine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="lineStopPoints"></a>
# **lineStopPoints**
> List&lt;TflApiPresentationEntitiesStopPoint&gt; lineStopPoints(id, tflOperatedNationalRailStationsOnly)

Gets a list of the stations that serve the given line id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    LineApi apiInstance = new LineApi(defaultClient);
    String id = "id_example"; // String | A single line id e.g. victoria
    Boolean tflOperatedNationalRailStationsOnly = true; // Boolean | If the national-rail line is requested, this flag will filter the national rail stations so that only those operated by TfL are returned
    try {
      List<TflApiPresentationEntitiesStopPoint> result = apiInstance.lineStopPoints(id, tflOperatedNationalRailStationsOnly);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LineApi#lineStopPoints");
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
| **id** | **String**| A single line id e.g. victoria | |
| **tflOperatedNationalRailStationsOnly** | **Boolean**| If the national-rail line is requested, this flag will filter the national rail stations so that only those operated by TfL are returned | [optional] |

### Return type

[**List&lt;TflApiPresentationEntitiesStopPoint&gt;**](TflApiPresentationEntitiesStopPoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="lineTimetable"></a>
# **lineTimetable**
> TflApiPresentationEntitiesTimetableResponse lineTimetable(fromStopPointId, id)

Gets the timetable for a specified station on the give line

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    LineApi apiInstance = new LineApi(defaultClient);
    String fromStopPointId = "fromStopPointId_example"; // String | The originating station's stop point id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name)
    String id = "id_example"; // String | A single line id e.g. victoria
    try {
      TflApiPresentationEntitiesTimetableResponse result = apiInstance.lineTimetable(fromStopPointId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LineApi#lineTimetable");
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
| **fromStopPointId** | **String**| The originating station&#39;s stop point id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name) | |
| **id** | **String**| A single line id e.g. victoria | |

### Return type

[**TflApiPresentationEntitiesTimetableResponse**](TflApiPresentationEntitiesTimetableResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="lineTimetableTo"></a>
# **lineTimetableTo**
> TflApiPresentationEntitiesTimetableResponse lineTimetableTo(fromStopPointId, id, toStopPointId)

Gets the timetable for a specified station on the give line with specified destination

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    LineApi apiInstance = new LineApi(defaultClient);
    String fromStopPointId = "fromStopPointId_example"; // String | The originating station's stop point id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name)
    String id = "id_example"; // String | A single line id e.g. victoria
    String toStopPointId = "toStopPointId_example"; // String | The destination stations's Naptan code
    try {
      TflApiPresentationEntitiesTimetableResponse result = apiInstance.lineTimetableTo(fromStopPointId, id, toStopPointId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LineApi#lineTimetableTo");
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
| **fromStopPointId** | **String**| The originating station&#39;s stop point id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name) | |
| **id** | **String**| A single line id e.g. victoria | |
| **toStopPointId** | **String**| The destination stations&#39;s Naptan code | |

### Return type

[**TflApiPresentationEntitiesTimetableResponse**](TflApiPresentationEntitiesTimetableResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

