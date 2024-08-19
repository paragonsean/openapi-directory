# StreamApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**streamGetChannel**](StreamApi.md#streamGetChannel) | **GET** /streams/{webId}/channel | Opens a channel that will send messages about any value changes for the specified stream. |
| [**streamGetEnd**](StreamApi.md#streamGetEnd) | **GET** /streams/{webId}/end | Returns the end-of-stream value of the stream. |
| [**streamGetInterpolated**](StreamApi.md#streamGetInterpolated) | **GET** /streams/{webId}/interpolated | Retrieves interpolated values over the specified time range at the specified sampling interval. |
| [**streamGetInterpolatedAtTimes**](StreamApi.md#streamGetInterpolatedAtTimes) | **GET** /streams/{webId}/interpolatedattimes | Retrieves interpolated values over the specified time range at the specified sampling interval. |
| [**streamGetPlot**](StreamApi.md#streamGetPlot) | **GET** /streams/{webId}/plot | Retrieves values over the specified time range suitable for plotting over the number of intervals (typically represents pixels). |
| [**streamGetRecorded**](StreamApi.md#streamGetRecorded) | **GET** /streams/{webId}/recorded | Returns a list of compressed values for the requested time range from the source provider. |
| [**streamGetRecordedAtTime**](StreamApi.md#streamGetRecordedAtTime) | **GET** /streams/{webId}/recordedattime | Returns a single recorded value based on the passed time and retrieval mode from the stream. |
| [**streamGetRecordedAtTimes**](StreamApi.md#streamGetRecordedAtTimes) | **GET** /streams/{webId}/recordedattimes | Retrieves recorded values at the specified times. |
| [**streamGetSummary**](StreamApi.md#streamGetSummary) | **GET** /streams/{webId}/summary | Returns a summary over the specified time range for the stream. |
| [**streamGetValue**](StreamApi.md#streamGetValue) | **GET** /streams/{webId}/value | Returns the value of the stream at the specified time. By default, this is usually the current value. |
| [**streamRegisterStreamUpdate**](StreamApi.md#streamRegisterStreamUpdate) | **POST** /streams/{webId}/updates | Register for stream updates |
| [**streamRetrieveStreamUpdate**](StreamApi.md#streamRetrieveStreamUpdate) | **GET** /streams/updates/{marker} | Receive stream updates |
| [**streamUpdateValue**](StreamApi.md#streamUpdateValue) | **POST** /streams/{webId}/value | Updates a value for the specified stream. |
| [**streamUpdateValues**](StreamApi.md#streamUpdateValues) | **POST** /streams/{webId}/recorded | Updates multiple values for the specified stream. |


<a id="streamGetChannel"></a>
# **streamGetChannel**
> streamGetChannel(webId, heartbeatRate, includeInitialValues, webIdType)

Opens a channel that will send messages about any value changes for the specified stream.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamApi apiInstance = new StreamApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the stream.
    Integer heartbeatRate = 56; // Integer | HeartbeatRate is an integer multiple of the Polling Interval. It specifies the rate at which a client will receive an empty message if there are no data updates. It can be used to check that the connection is still alive. Zero/negative values correspond to no heartbeat. By default, no empty messages will be sent to the user.
    Boolean includeInitialValues = true; // Boolean | Specified if the channel should send a message with the current value of the stream after the connection is opened. The default is 'false'.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.streamGetChannel(webId, heartbeatRate, includeInitialValues, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamApi#streamGetChannel");
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
| **webId** | **String**| The ID of the stream. | |
| **heartbeatRate** | **Integer**| HeartbeatRate is an integer multiple of the Polling Interval. It specifies the rate at which a client will receive an empty message if there are no data updates. It can be used to check that the connection is still alive. Zero/negative values correspond to no heartbeat. By default, no empty messages will be sent to the user. | [optional] |
| **includeInitialValues** | **Boolean**| Specified if the channel should send a message with the current value of the stream after the connection is opened. The default is &#39;false&#39;. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **101** | Switches to the Web Socket protocol. |  -  |

<a id="streamGetEnd"></a>
# **streamGetEnd**
> TimedValue streamGetEnd(webId, desiredUnits, selectedFields)

Returns the end-of-stream value of the stream.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamApi apiInstance = new StreamApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the stream.
    String desiredUnits = "desiredUnits_example"; // String | The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute's default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    try {
      TimedValue result = apiInstance.streamGetEnd(webId, desiredUnits, selectedFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamApi#streamGetEnd");
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
| **webId** | **String**| The ID of the stream. | |
| **desiredUnits** | **String**| The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute&#39;s default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |

### Return type

[**TimedValue**](TimedValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The value at the specified time value. |  -  |

<a id="streamGetInterpolated"></a>
# **streamGetInterpolated**
> TimedValues streamGetInterpolated(webId, desiredUnits, endTime, filterExpression, includeFilteredValues, interval, selectedFields, startTime, syncTime, syncTimeBoundaryType, timeZone)

Retrieves interpolated values over the specified time range at the specified sampling interval.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamApi apiInstance = new StreamApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the stream.
    String desiredUnits = "desiredUnits_example"; // String | The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute's default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure.
    String endTime = "endTime_example"; // String | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    String filterExpression = "filterExpression_example"; // String | An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering.
    Boolean includeFilteredValues = true; // Boolean | Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted.
    String interval = "interval_example"; // String | The sampling interval, in AFTimeSpan format.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String startTime = "startTime_example"; // String | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set.
    String syncTime = "syncTime_example"; // String | An optional start time anchor, in AFTime format. When specified, interpolated data retrieval will use the sync time as the origin for calculating the interval times.
    String syncTimeBoundaryType = "syncTimeBoundaryType_example"; // String | An optional string specifying the boundary type to use when applying a syncTime. The allowed values are 'Inside' and 'Outside'. The default is 'Inside'.
    String timeZone = "timeZone_example"; // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    try {
      TimedValues result = apiInstance.streamGetInterpolated(webId, desiredUnits, endTime, filterExpression, includeFilteredValues, interval, selectedFields, startTime, syncTime, syncTimeBoundaryType, timeZone);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamApi#streamGetInterpolated");
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
| **webId** | **String**| The ID of the stream. | |
| **desiredUnits** | **String**| The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute&#39;s default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure. | [optional] |
| **endTime** | **String**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] |
| **filterExpression** | **String**| An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering. | [optional] |
| **includeFilteredValues** | **Boolean**| Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted. | [optional] |
| **interval** | **String**| The sampling interval, in AFTimeSpan format. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **startTime** | **String**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] |
| **syncTime** | **String**| An optional start time anchor, in AFTime format. When specified, interpolated data retrieval will use the sync time as the origin for calculating the interval times. | [optional] |
| **syncTimeBoundaryType** | **String**| An optional string specifying the boundary type to use when applying a syncTime. The allowed values are &#39;Inside&#39; and &#39;Outside&#39;. The default is &#39;Inside&#39;. | [optional] |
| **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] |

### Return type

[**TimedValues**](TimedValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The values that meet the specified conditions. |  -  |
| **400** | The request was malformed. |  -  |
| **409** | The data reference does not support this method, or the supplied filter expression is unsupported, or the desired units of measure are incompatible. |  -  |

<a id="streamGetInterpolatedAtTimes"></a>
# **streamGetInterpolatedAtTimes**
> TimedValues streamGetInterpolatedAtTimes(webId, time, desiredUnits, filterExpression, includeFilteredValues, selectedFields, sortOrder, timeZone)

Retrieves interpolated values over the specified time range at the specified sampling interval.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamApi apiInstance = new StreamApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the stream.
    List<String> time = Arrays.asList(); // List<String> | The timestamp at which to retrieve an interpolated value. Multiple timestamps may be specified with multiple instances of the parameter.
    String desiredUnits = "desiredUnits_example"; // String | The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute's default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure.
    String filterExpression = "filterExpression_example"; // String | An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering.
    Boolean includeFilteredValues = true; // Boolean | Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'.
    String timeZone = "timeZone_example"; // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    try {
      TimedValues result = apiInstance.streamGetInterpolatedAtTimes(webId, time, desiredUnits, filterExpression, includeFilteredValues, selectedFields, sortOrder, timeZone);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamApi#streamGetInterpolatedAtTimes");
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
| **webId** | **String**| The ID of the stream. | |
| **time** | [**List&lt;String&gt;**](String.md)| The timestamp at which to retrieve an interpolated value. Multiple timestamps may be specified with multiple instances of the parameter. | |
| **desiredUnits** | **String**| The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute&#39;s default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure. | [optional] |
| **filterExpression** | **String**| An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering. | [optional] |
| **includeFilteredValues** | **Boolean**| Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] |
| **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] |

### Return type

[**TimedValues**](TimedValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The values that meet the specified conditions. |  -  |
| **400** | The request was malformed. |  -  |
| **409** | The data reference does not support this method, or the supplied filter expression is unsupported, or the desired units of measure are incompatible. |  -  |

<a id="streamGetPlot"></a>
# **streamGetPlot**
> TimedValues streamGetPlot(webId, desiredUnits, endTime, intervals, selectedFields, startTime, timeZone)

Retrieves values over the specified time range suitable for plotting over the number of intervals (typically represents pixels).

For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state). Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamApi apiInstance = new StreamApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the stream.
    String desiredUnits = "desiredUnits_example"; // String | The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute's default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure.
    String endTime = "endTime_example"; // String | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    Integer intervals = 56; // Integer | The number of intervals to plot over. Typically, this would be the number of horizontal pixels in the trend. The default is '24'. For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state).
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String startTime = "startTime_example"; // String | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set.
    String timeZone = "timeZone_example"; // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    try {
      TimedValues result = apiInstance.streamGetPlot(webId, desiredUnits, endTime, intervals, selectedFields, startTime, timeZone);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamApi#streamGetPlot");
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
| **webId** | **String**| The ID of the stream. | |
| **desiredUnits** | **String**| The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute&#39;s default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure. | [optional] |
| **endTime** | **String**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] |
| **intervals** | **Integer**| The number of intervals to plot over. Typically, this would be the number of horizontal pixels in the trend. The default is &#39;24&#39;. For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state). | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **startTime** | **String**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] |
| **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] |

### Return type

[**TimedValues**](TimedValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The values that meet the specified conditions |  -  |
| **400** | The request was malformed. |  -  |
| **409** | The data reference does not support this method, or the desired units of measure are incompatible. |  -  |

<a id="streamGetRecorded"></a>
# **streamGetRecorded**
> ExtendedTimedValues streamGetRecorded(webId, associations, boundaryType, desiredUnits, endTime, filterExpression, includeFilteredValues, maxCount, selectedFields, startTime, timeZone)

Returns a list of compressed values for the requested time range from the source provider.

Returned times are affected by the specified boundary type. If no values are found for the time range and conditions specified then the HTTP response will be success, with a body containing an empty array of Items. When specifying true for the includeFilteredValues parameter, consecutive filtered events are not returned. The first value that would be filtered out is returned with its time and the enumeration value \&quot;Filtered\&quot;. The next value in the collection will be the next compressed value in the specified direction that passes the filter criteria - if any. When both boundaryType and a filterExpression are specified, the events returned for the boundary condition specified are passed through the filter. If the includeFilteredValues parameter is true, the boundary values will be reported at the proper timestamps with the enumeration value \&quot;Filtered\&quot; when the filter conditions are not met at the boundary time. If the includeFilteredValues parameter is false for this case, no event is returned for the boundary time. Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.   If only recorded values with annotations are desired, the filterExpression parameter should include the filter IsSet(&#39;.&#39;, \&quot;a\&quot;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamApi apiInstance = new StreamApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the stream.
    String associations = "associations_example"; // String | Associated values to return in the response, separated by semicolons (;). This call supports Annotations to return events with annotation values. If this parameter is not specified, annotation values are not returned.
    String boundaryType = "boundaryType_example"; // String | An optional value that determines how the times and values of the returned end points are determined. The default is 'Inside'.
    String desiredUnits = "desiredUnits_example"; // String | The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute's default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure.
    String endTime = "endTime_example"; // String | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    String filterExpression = "filterExpression_example"; // String | An optional string containing a filter expression. Expression variables are relative to the data point. Use '.' to reference the containing attribute. The default is no filtering.
    Boolean includeFilteredValues = true; // Boolean | Specify 'true' to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a 'Filtered' enumeration value with bad status. Repeated consecutive failures are omitted.
    Integer maxCount = 56; // Integer | The maximum number of values to be returned. The default is 1000.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String startTime = "startTime_example"; // String | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set.
    String timeZone = "timeZone_example"; // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    try {
      ExtendedTimedValues result = apiInstance.streamGetRecorded(webId, associations, boundaryType, desiredUnits, endTime, filterExpression, includeFilteredValues, maxCount, selectedFields, startTime, timeZone);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamApi#streamGetRecorded");
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
| **webId** | **String**| The ID of the stream. | |
| **associations** | **String**| Associated values to return in the response, separated by semicolons (;). This call supports Annotations to return events with annotation values. If this parameter is not specified, annotation values are not returned. | [optional] |
| **boundaryType** | **String**| An optional value that determines how the times and values of the returned end points are determined. The default is &#39;Inside&#39;. | [optional] |
| **desiredUnits** | **String**| The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute&#39;s default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure. | [optional] |
| **endTime** | **String**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] |
| **filterExpression** | **String**| An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. The default is no filtering. | [optional] |
| **includeFilteredValues** | **Boolean**| Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted. | [optional] |
| **maxCount** | **Integer**| The maximum number of values to be returned. The default is 1000. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **startTime** | **String**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] |
| **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] |

### Return type

[**ExtendedTimedValues**](ExtendedTimedValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The values that meet the specified conditions. |  -  |
| **400** | The request was malformed. |  -  |
| **409** | The data reference does not support the method, or the supplied filter expression is unsupported, or the desired units of measure are incompatible, or an unsupported association was specified. |  -  |

<a id="streamGetRecordedAtTime"></a>
# **streamGetRecordedAtTime**
> ExtendedTimedValue streamGetRecordedAtTime(webId, time, associations, desiredUnits, retrievalMode, selectedFields, timeZone)

Returns a single recorded value based on the passed time and retrieval mode from the stream.

If only recorded values with annotations are desired, the filterExpression parameter should include the filter IsSet(&#39;.&#39;, \&quot;a\&quot;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamApi apiInstance = new StreamApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the stream.
    String time = "time_example"; // String | The timestamp at which the value is desired.
    String associations = "associations_example"; // String | Associated values to return in the response, separated by semicolons (;). This call supports Annotations to return events with annotation values. If this parameter is not specified, annotation values are not returned.
    String desiredUnits = "desiredUnits_example"; // String | The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute's default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure.
    String retrievalMode = "retrievalMode_example"; // String | An optional value that determines the value to return when a value doesn't exist at the exact time specified. The default is 'Auto'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String timeZone = "timeZone_example"; // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    try {
      ExtendedTimedValue result = apiInstance.streamGetRecordedAtTime(webId, time, associations, desiredUnits, retrievalMode, selectedFields, timeZone);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamApi#streamGetRecordedAtTime");
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
| **webId** | **String**| The ID of the stream. | |
| **time** | **String**| The timestamp at which the value is desired. | |
| **associations** | **String**| Associated values to return in the response, separated by semicolons (;). This call supports Annotations to return events with annotation values. If this parameter is not specified, annotation values are not returned. | [optional] |
| **desiredUnits** | **String**| The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute&#39;s default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure. | [optional] |
| **retrievalMode** | **String**| An optional value that determines the value to return when a value doesn&#39;t exist at the exact time specified. The default is &#39;Auto&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] |

### Return type

[**ExtendedTimedValue**](ExtendedTimedValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The value that meet the specified conditions. |  -  |
| **400** | The request was malformed. |  -  |
| **409** | The data reference does not support the method, or the desired units of measure are incompatible. |  -  |

<a id="streamGetRecordedAtTimes"></a>
# **streamGetRecordedAtTimes**
> ExtendedTimedValues streamGetRecordedAtTimes(webId, time, associations, desiredUnits, retrievalMode, selectedFields, sortOrder, timeZone)

Retrieves recorded values at the specified times.

Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.   If only recorded values with annotations are desired, the filterExpression parameter should include the filter IsSet(&#39;.&#39;, \&quot;a\&quot;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamApi apiInstance = new StreamApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the stream.
    List<String> time = Arrays.asList(); // List<String> | The timestamp at which to retrieve a recorded value. Multiple timestamps may be specified with multiple instances of the parameter.
    String associations = "associations_example"; // String | Associated values to return in the response, separated by semicolons (;). This call supports Annotations to return events with annotation values. If this parameter is not specified, annotation values are not returned.
    String desiredUnits = "desiredUnits_example"; // String | The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute's default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure.
    String retrievalMode = "retrievalMode_example"; // String | An optional value that determines the value to return when a value doesn't exist at the exact time specified. The default is 'Auto'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String sortOrder = "sortOrder_example"; // String | The order that the returned collection is sorted. The default is 'Ascending'.
    String timeZone = "timeZone_example"; // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    try {
      ExtendedTimedValues result = apiInstance.streamGetRecordedAtTimes(webId, time, associations, desiredUnits, retrievalMode, selectedFields, sortOrder, timeZone);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamApi#streamGetRecordedAtTimes");
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
| **webId** | **String**| The ID of the stream. | |
| **time** | [**List&lt;String&gt;**](String.md)| The timestamp at which to retrieve a recorded value. Multiple timestamps may be specified with multiple instances of the parameter. | |
| **associations** | **String**| Associated values to return in the response, separated by semicolons (;). This call supports Annotations to return events with annotation values. If this parameter is not specified, annotation values are not returned. | [optional] |
| **desiredUnits** | **String**| The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute&#39;s default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure. | [optional] |
| **retrievalMode** | **String**| An optional value that determines the value to return when a value doesn&#39;t exist at the exact time specified. The default is &#39;Auto&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] |
| **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] |

### Return type

[**ExtendedTimedValues**](ExtendedTimedValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The values that meet the specified conditions. |  -  |
| **400** | The request was malformed. |  -  |
| **409** | The data reference does not support this method, or the desired units of measure are incompatible. |  -  |

<a id="streamGetSummary"></a>
# **streamGetSummary**
> ItemsSummaryValue streamGetSummary(webId, calculationBasis, endTime, filterExpression, sampleInterval, sampleType, selectedFields, startTime, summaryDuration, summaryType, timeType, timeZone)

Returns a summary over the specified time range for the stream.

Count is the only summary type supported on non-numeric streams. Requesting a summary for any other type will generate an error. Time-weighted totals are computed by integrating the rate tag values over the requested time range. If some of the data are bad in the time range, the calculated total is divided by the fraction of the time period for which there are good values. This approach is equivalent to assuming that during the period of bad data, the tag takes on the average values for the entire calculation time range. The PercentGood summary may be used to determine if the calculation results are suitable for the application&#39;s purposes. For time-weighted totals, if the time unit rate of the stream cannot be determined, then the value will be totaled assuming a unit of \&quot;per day\&quot; and no unit of measure will be assigned to the value. If the measured time component of the tag is not based on a day, the user of the data must convert the totalized value to the correct units.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamApi apiInstance = new StreamApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the stream.
    String calculationBasis = "calculationBasis_example"; // String | Specifies the method of evaluating the data over the time range. The default is 'TimeWeighted'.
    String endTime = "endTime_example"; // String | An optional end time. The default is '*' for element attributes and points. For event frame attributes, the default is the event frame's end time, or '*' if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    String filterExpression = "filterExpression_example"; // String | A string containing a filter expression. Expression variables are relative to the attribute. Use '.' to reference the containing attribute.
    String sampleInterval = "sampleInterval_example"; // String | When the sampleType is Interval, sampleInterval specifies how often the filter expression is evaluated when computing the summary for an interval.
    String sampleType = "sampleType_example"; // String | Defines the evaluation of an expression over a time range. The default is 'ExpressionRecordedValues'.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String startTime = "startTime_example"; // String | An optional start time. The default is '*-1d' for element attributes and points. For event frame attributes, the default is the event frame's start time, or '*-1d' if that is not set.
    String summaryDuration = "summaryDuration_example"; // String | The duration of each summary interval. If specified in hours, minutes, seconds, or milliseconds, the summary durations will be evenly spaced UTC time intervals. Longer interval types are interpreted using wall clock rules and are time zone dependent.
    List<String> summaryType = Arrays.asList(); // List<String> | Specifies the kinds of summaries to produce over the range. The default is 'Total'. Multiple summary types may be specified by using multiple instances of summaryType.
    String timeType = "timeType_example"; // String | Specifies how to calculate the timestamp for each interval. The default is 'Auto'.
    String timeZone = "timeZone_example"; // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    try {
      ItemsSummaryValue result = apiInstance.streamGetSummary(webId, calculationBasis, endTime, filterExpression, sampleInterval, sampleType, selectedFields, startTime, summaryDuration, summaryType, timeType, timeZone);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamApi#streamGetSummary");
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
| **webId** | **String**| The ID of the stream. | |
| **calculationBasis** | **String**| Specifies the method of evaluating the data over the time range. The default is &#39;TimeWeighted&#39;. | [optional] |
| **endTime** | **String**| An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order. | [optional] |
| **filterExpression** | **String**| A string containing a filter expression. Expression variables are relative to the attribute. Use &#39;.&#39; to reference the containing attribute. | [optional] |
| **sampleInterval** | **String**| When the sampleType is Interval, sampleInterval specifies how often the filter expression is evaluated when computing the summary for an interval. | [optional] |
| **sampleType** | **String**| Defines the evaluation of an expression over a time range. The default is &#39;ExpressionRecordedValues&#39;. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **startTime** | **String**| An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set. | [optional] |
| **summaryDuration** | **String**| The duration of each summary interval. If specified in hours, minutes, seconds, or milliseconds, the summary durations will be evenly spaced UTC time intervals. Longer interval types are interpreted using wall clock rules and are time zone dependent. | [optional] |
| **summaryType** | [**List&lt;String&gt;**](String.md)| Specifies the kinds of summaries to produce over the range. The default is &#39;Total&#39;. Multiple summary types may be specified by using multiple instances of summaryType. | [optional] |
| **timeType** | **String**| Specifies how to calculate the timestamp for each interval. The default is &#39;Auto&#39;. | [optional] |
| **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] |

### Return type

[**ItemsSummaryValue**](ItemsSummaryValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The summaries that meet the specified conditions. |  -  |
| **409** | The data reference does not support this method. |  -  |

<a id="streamGetValue"></a>
# **streamGetValue**
> TimedValue streamGetValue(webId, desiredUnits, selectedFields, time, timeZone)

Returns the value of the stream at the specified time. By default, this is usually the current value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamApi apiInstance = new StreamApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the stream.
    String desiredUnits = "desiredUnits_example"; // String | The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute's default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String time = "time_example"; // String | An optional time. The default time context is determined from the owning object - for example, the time range of the event frame or transfer which holds this attribute. Otherwise, the implementation of the Data Reference determines the meaning of no context. For Points or simply configured PI Point Data References, this means the snapshot value of the PI Point on the Data Server.
    String timeZone = "timeZone_example"; // String | The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    try {
      TimedValue result = apiInstance.streamGetValue(webId, desiredUnits, selectedFields, time, timeZone);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamApi#streamGetValue");
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
| **webId** | **String**| The ID of the stream. | |
| **desiredUnits** | **String**| The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute&#39;s default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **time** | **String**| An optional time. The default time context is determined from the owning object - for example, the time range of the event frame or transfer which holds this attribute. Otherwise, the implementation of the Data Reference determines the meaning of no context. For Points or simply configured PI Point Data References, this means the snapshot value of the PI Point on the Data Server. | [optional] |
| **timeZone** | **String**| The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used. | [optional] |

### Return type

[**TimedValue**](TimedValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The value at the specified time value. |  -  |
| **409** | The data reference does not support the method, or the desired units of measure are incompatible. |  -  |

<a id="streamRegisterStreamUpdate"></a>
# **streamRegisterStreamUpdate**
> StreamUpdatesRegister streamRegisterStreamUpdate(webId, selectedFields, webIdType)

Register for stream updates

The supplied webId will register for stream updates. For a 201 or 204 response, the returned location header will contain the url for retrieving the next set of stream updates.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamApi apiInstance = new StreamApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the stream.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      StreamUpdatesRegister result = apiInstance.streamRegisterStreamUpdate(webId, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamApi#streamRegisterStreamUpdate");
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
| **webId** | **String**| The ID of the stream. | |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**StreamUpdatesRegister**](StreamUpdatesRegister.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful registration |  -  |
| **400** | Invalid webId |  -  |
| **409** | WebId represents a static attribute |  -  |

<a id="streamRetrieveStreamUpdate"></a>
# **streamRetrieveStreamUpdate**
> StreamUpdatesRetrieve streamRetrieveStreamUpdate(marker, desiredUnits, selectedFields, webIdType)

Receive stream updates

The supplied marker will identify the set of stream updates to retrieve. For a 200 response, the returned location header will contain the url for retrieving the stream updates.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamApi apiInstance = new StreamApi(defaultClient);
    String marker = "marker_example"; // String | Identifier of stream source and current position
    String desiredUnits = "desiredUnits_example"; // String | The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute's default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure.
    String selectedFields = "selectedFields_example"; // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      StreamUpdatesRetrieve result = apiInstance.streamRetrieveStreamUpdate(marker, desiredUnits, selectedFields, webIdType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamApi#streamRetrieveStreamUpdate");
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
| **marker** | **String**| Identifier of stream source and current position | |
| **desiredUnits** | **String**| The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute&#39;s default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure. | [optional] |
| **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

[**StreamUpdatesRetrieve**](StreamUpdatesRetrieve.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The stream updates have been successfully retrieved |  -  |
| **404** | Cache not found |  -  |
| **409** | Invalid marker supplied |  -  |

<a id="streamUpdateValue"></a>
# **streamUpdateValue**
> streamUpdateValue(webId, value, bufferOption, updateOption, webIdType)

Updates a value for the specified stream.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamApi apiInstance = new StreamApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the stream.
    TimedValue value = new TimedValue(); // TimedValue | The value to add or update.
    String bufferOption = "bufferOption_example"; // String | The desired AFBufferOption. The default is 'BufferIfPossible'.
    String updateOption = "updateOption_example"; // String | The desired AFUpdateOption. The default is 'Replace'. This parameter is ignored if the attribute is a configuration item.
    String webIdType = "webIdType_example"; // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
    try {
      apiInstance.streamUpdateValue(webId, value, bufferOption, updateOption, webIdType);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamApi#streamUpdateValue");
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
| **webId** | **String**| The ID of the stream. | |
| **value** | [**TimedValue**](TimedValue.md)| The value to add or update. | |
| **bufferOption** | **String**| The desired AFBufferOption. The default is &#39;BufferIfPossible&#39;. | [optional] |
| **updateOption** | **String**| The desired AFUpdateOption. The default is &#39;Replace&#39;. This parameter is ignored if the attribute is a configuration item. | [optional] |
| **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The value was accepted for a potential buffered update. The response&#39;s Location header is a link that can be used to examine the result. |  -  |
| **204** | The update operation was successfully applied. The response&#39;s Location header is a link that can be used to examine the result. |  -  |
| **400** | The request was malformed. |  -  |
| **409** | The attribute or data reference does not support this operation, or the specified units are incompatible. |  -  |

<a id="streamUpdateValues"></a>
# **streamUpdateValues**
> ItemsSubstatus streamUpdateValues(webId, values, bufferOption, updateOption)

Updates multiple values for the specified stream.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    StreamApi apiInstance = new StreamApi(defaultClient);
    String webId = "webId_example"; // String | The ID of the stream.
    List<TimedValue> values = Arrays.asList(); // List<TimedValue> | The values to add or update.
    String bufferOption = "bufferOption_example"; // String | The desired AFBufferOption. The default is 'BufferIfPossible'.
    String updateOption = "updateOption_example"; // String | The desired AFUpdateOption. The default is 'Replace'.
    try {
      ItemsSubstatus result = apiInstance.streamUpdateValues(webId, values, bufferOption, updateOption);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamApi#streamUpdateValues");
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
| **webId** | **String**| The ID of the stream. | |
| **values** | [**List&lt;TimedValue&gt;**](TimedValue.md)| The values to add or update. | |
| **bufferOption** | **String**| The desired AFBufferOption. The default is &#39;BufferIfPossible&#39;. | [optional] |
| **updateOption** | **String**| The desired AFUpdateOption. The default is &#39;Replace&#39;. | [optional] |

### Return type

[**ItemsSubstatus**](ItemsSubstatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | All updates executed successfully. |  -  |
| **207** | The operation was a partial success. The response body contains substatuses and errors in the same order as the supplied values. |  -  |
| **409** | The data reference does not support this operation. |  -  |

